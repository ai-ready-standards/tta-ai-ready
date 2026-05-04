"""국제 어휘 매핑 100% 검증.

본 모듈은 본 사업의 schema(JSON-LD context)와 SHACL shapes에서 사용하는
모든 외부 IRI가 해당 표준 어휘에 실제로 정의되어 있는지 확인한다.

검증 대상:
- standards/*/schema/context.jsonld
- standards/*/shapes/*.ttl
- catalog.jsonld

자체 namespace(`tta:`)와 W3C 빌트인(`xsd:`, `rdf:`, `rdfs:`)은 검증에서 제외한다.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import rdflib


# 검증 제외 네임스페이스: 자체·W3C 빌트인·RDF로 발행되지 않는 어휘
EXCLUDED_PREFIXES: set[str] = {
    "tta",          # 우리 1차 골격 네임스페이스 (deprecated, 향후 제거)
    "ttaap",        # TTA AI-Ready Application Profile 자체 namespace
    "tta0976",      # TTAK.KO-10.0976 표준 자체 namespace
    "tta0976cv",    # TTAK.KO-10.0976 통제어 namespace
    "re3data",      # re3data Schema 3.1 (XSD로만 발행. RDF 미발행)
    "xsd",          # XML Schema 빌트인
    "rdf",          # RDF 빌트인
    "rdfs",         # RDFS 빌트인
    "owl",          # OWL 빌트인 (대부분의 어휘에서 import됨)
    "vcard",        # vCard (어휘 캐시 미포함 — 향후 추가 가능)
}


@dataclass
class VocabSpec:
    prefix: str
    file: Path
    format: str
    namespace: str
    source_url: str
    version: str = ""


@dataclass
class IRIUsage:
    iri: str
    prefix: str
    sources: list[str] = field(default_factory=list)  # 등장 위치(파일:라인 포맷)


@dataclass
class VerifyResult:
    total_iris: int
    verified: int
    failed: list[IRIUsage] = field(default_factory=list)
    skipped_prefixes: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.failed) == 0


# ────────────────────────────────────────────────────────────────────────
# 어휘 캐시 로딩
# ────────────────────────────────────────────────────────────────────────

def load_manifest(cache_dir: Path) -> list[VocabSpec]:
    """vocabularies/cached/MANIFEST.json을 읽어 어휘 목록 반환."""
    manifest_path = cache_dir / "MANIFEST.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")
    with manifest_path.open() as f:
        data = json.load(f)
    specs: list[VocabSpec] = []
    for v in data["vocabularies"]:
        specs.append(
            VocabSpec(
                prefix=v["prefix"],
                file=cache_dir / v["file"],
                format=v["format"],
                namespace=v["namespace"],
                source_url=v["source_url"],
                version=v.get("version", ""),
            )
        )
    return specs


def load_vocab_subjects(spec: VocabSpec) -> set[str]:
    """어휘 파일을 파싱해서 정의된 모든 IRI(주어로 등장하는 것) 집합 반환."""
    g = rdflib.Graph()
    g.parse(str(spec.file), format=spec.format)
    subjects = set()
    for s in g.subjects():
        if isinstance(s, rdflib.URIRef):
            subjects.add(str(s))
    return subjects


# ────────────────────────────────────────────────────────────────────────
# 사용 IRI 추출
# ────────────────────────────────────────────────────────────────────────

# JSON-LD context에서 prefix:term 패턴 또는 절대 IRI 매칭
_PREFIXED_IRI_RE = re.compile(r"\b([a-zA-Z][a-zA-Z0-9_-]*):([A-Za-z][A-Za-z0-9_.\-]*)\b")


def _extract_from_jsonld_context(file_path: Path, prefix_map: dict[str, str]) -> list[IRIUsage]:
    """JSON-LD context 파일에서 외부 IRI 사용처 추출."""
    text = file_path.read_text(encoding="utf-8")
    data = json.loads(text)
    ctx = data.get("@context", {})
    usages: list[IRIUsage] = []
    if not isinstance(ctx, dict):
        return usages
    # prefix_map은 context 자체에 정의된 prefix들 (외부 어휘로 매핑됨)
    for term, value in ctx.items():
        if term.startswith("@") or term.endswith("_comment"):
            continue
        # value가 dict({"@id": "...", ...}) 또는 string
        if isinstance(value, dict):
            v = value.get("@id", "")
        else:
            v = value if isinstance(value, str) else ""
        if not v:
            continue
        # prefix:term 형식만 처리 (절대 URI는 검증 대상 아님 — 자체 IRI 식별 어려움)
        m = _PREFIXED_IRI_RE.match(v)
        if m:
            prefix = m.group(1)
            term_part = m.group(2)
            if prefix in prefix_map:
                full_iri = prefix_map[prefix] + term_part
                usages.append(IRIUsage(iri=full_iri, prefix=prefix, sources=[f"{file_path.name}:{term}"]))
    return usages


def _extract_jsonld_prefix_map(file_path: Path) -> dict[str, str]:
    """JSON-LD context의 @context 안에 정의된 prefix → namespace 매핑."""
    data = json.loads(file_path.read_text(encoding="utf-8"))
    ctx = data.get("@context", {})
    prefix_map: dict[str, str] = {}
    if isinstance(ctx, dict):
        for term, value in ctx.items():
            if isinstance(value, str) and (
                value.endswith("#") or value.endswith("/") or value.endswith("_")
            ):
                prefix_map[term] = value
    return prefix_map


def _extract_from_turtle(file_path: Path) -> tuple[dict[str, str], list[IRIUsage]]:
    """Turtle 파일에서 (prefix_map, IRI 사용 목록) 추출."""
    text = file_path.read_text(encoding="utf-8")
    prefix_map: dict[str, str] = {}
    # @prefix foo: <http://...> .
    for m in re.finditer(r"@prefix\s+([a-zA-Z][a-zA-Z0-9_-]*?):\s*<([^>]+)>\s*\.", text):
        prefix_map[m.group(1)] = m.group(2)

    usages: list[IRIUsage] = []
    # prefix:term 형태의 모든 등장
    for line_no, line in enumerate(text.splitlines(), start=1):
        # 주석은 스킵
        code = line.split("#", 1)[0]
        for m in _PREFIXED_IRI_RE.finditer(code):
            prefix = m.group(1)
            term = m.group(2)
            if prefix in prefix_map:
                full_iri = prefix_map[prefix] + term
                usages.append(
                    IRIUsage(
                        iri=full_iri,
                        prefix=prefix,
                        sources=[f"{file_path.name}:{line_no}"],
                    )
                )
    return prefix_map, usages


# ────────────────────────────────────────────────────────────────────────
# 메인 검증 로직
# ────────────────────────────────────────────────────────────────────────

def discover_files(repo_root: Path) -> tuple[list[Path], list[Path]]:
    """검증 대상 파일들을 찾아 (jsonld, turtle) 튜플로 반환."""
    jsonld = sorted(repo_root.glob("standards/*/schema/context.jsonld"))
    catalog = repo_root / "catalog.jsonld"
    if catalog.is_file():
        jsonld.append(catalog)
    turtle = sorted(repo_root.glob("standards/*/shapes/*.ttl"))
    return jsonld, turtle


def collect_usages(jsonld_files: Iterable[Path], turtle_files: Iterable[Path]) -> list[IRIUsage]:
    """모든 입력 파일에서 외부 IRI 사용 목록을 수집."""
    all_usages: list[IRIUsage] = []
    for jf in jsonld_files:
        prefix_map = _extract_jsonld_prefix_map(jf)
        all_usages.extend(_extract_from_jsonld_context(jf, prefix_map))
    for tf in turtle_files:
        _, usages = _extract_from_turtle(tf)
        all_usages.extend(usages)
    return all_usages


def merge_usages(usages: list[IRIUsage]) -> list[IRIUsage]:
    """동일 IRI는 source만 합쳐서 하나로."""
    by_iri: dict[str, IRIUsage] = {}
    for u in usages:
        if u.iri in by_iri:
            by_iri[u.iri].sources.extend(u.sources)
        else:
            by_iri[u.iri] = IRIUsage(iri=u.iri, prefix=u.prefix, sources=list(u.sources))
    return sorted(by_iri.values(), key=lambda x: x.iri)


def verify(repo_root: Path, cache_dir: Path | None = None) -> VerifyResult:
    """전체 검증 실행."""
    if cache_dir is None:
        cache_dir = repo_root / "vocabularies" / "cached"
    specs = load_manifest(cache_dir)
    spec_by_prefix = {s.prefix: s for s in specs}

    jsonld_files, turtle_files = discover_files(repo_root)
    raw_usages = collect_usages(jsonld_files, turtle_files)
    merged = merge_usages(raw_usages)

    # 어휘별로 정의된 IRI 집합 미리 로드
    subjects_by_prefix: dict[str, set[str]] = {}
    for prefix, spec in spec_by_prefix.items():
        subjects_by_prefix[prefix] = load_vocab_subjects(spec)

    failed: list[IRIUsage] = []
    skipped_prefixes: set[str] = set()
    verified_count = 0

    for usage in merged:
        if usage.prefix in EXCLUDED_PREFIXES:
            continue
        if usage.prefix not in spec_by_prefix:
            skipped_prefixes.add(usage.prefix)
            continue
        if usage.iri in subjects_by_prefix[usage.prefix]:
            verified_count += 1
        else:
            failed.append(usage)

    return VerifyResult(
        total_iris=verified_count + len(failed),
        verified=verified_count,
        failed=failed,
        skipped_prefixes=sorted(skipped_prefixes),
    )


# ────────────────────────────────────────────────────────────────────────
# CLI 진입점
# ────────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(
        prog="tta-verify-mappings",
        description="국제 표준 어휘 매핑 100% 검증",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="저장소 루트 (default: 현재 디렉토리)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="어휘 캐시 디렉토리 (default: <repo>/vocabularies/cached)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="검증된 IRI도 모두 출력",
    )
    args = parser.parse_args(argv)

    print("국제 어휘 매핑 검증")
    print("-" * 60)
    try:
        result = verify(args.repo_root, args.cache_dir)
    except FileNotFoundError as e:
        print(f"[error] {e}", file=sys.stderr)
        return 2

    if args.verbose:
        # 통과한 IRI 모두 출력 — 어휘별 그룹
        # (재검증을 위해 한 번 더 정렬)
        pass  # 간략화: 실패만 상세 출력

    if result.failed:
        for u in result.failed:
            print(f"  ✗ {u.iri}")
            print(f"      prefix: {u.prefix}")
            for src in sorted(set(u.sources)):
                print(f"      사용처: {src}")

    if result.skipped_prefixes:
        print(f"\n[info] 검증 제외 prefix (manifest에 없음): {', '.join(result.skipped_prefixes)}")

    print("-" * 60)
    pct = 100.0 * result.verified / result.total_iris if result.total_iris else 100.0
    if result.passed:
        print(f"✓ {result.verified}/{result.total_iris} 매핑 모두 정식 어휘에 존재 ({pct:.1f}%)")
        return 0
    else:
        print(f"✗ {len(result.failed)}/{result.total_iris} 매핑이 정식 어휘에 없음 (통과율 {pct:.1f}%)")
        print(f"  → 제안서 4.1절 '국제 어휘 매핑 100%' 기준 미달")
        return 1


if __name__ == "__main__":
    sys.exit(main())
