"""SHACL 검증 핵심 로직."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import rdflib
from pyshacl import validate as pyshacl_validate


@dataclass
class ValidationResult:
    path: Path
    conforms: bool
    violations: int
    warnings: int
    infos: int
    text: str


def _inline_local_context(jsonld_path: Path, shapes_dir: Path) -> str:
    """JSON-LD의 @context가 원격 URL이면 shapes_dir/context.jsonld로 치환.

    네트워크 fetch 실패 회피용. ARD의 inline_local_context()와 동일 로직.
    """
    with jsonld_path.open(encoding="utf-8") as f:
        doc = json.load(f)
    ctx_value = doc.get("@context")
    if isinstance(ctx_value, str) and ctx_value.startswith(("http://", "https://")):
        local_ctx = shapes_dir / "context.jsonld"
        if local_ctx.is_file():
            with local_ctx.open(encoding="utf-8") as f:
                local_doc = json.load(f)
            doc["@context"] = local_doc.get("@context", local_doc)
    return json.dumps(doc, ensure_ascii=False)


def _load_data_graph(jsonld_path: Path, shapes_dir: Path | None = None) -> rdflib.Graph:
    """JSON-LD 파일을 rdflib Graph로 로드. @context URL은 로컬 context.jsonld로 치환."""
    graph = rdflib.Graph()
    if shapes_dir is not None and (shapes_dir / "context.jsonld").is_file():
        # 원격 @context를 로컬로 치환
        data_str = _inline_local_context(jsonld_path, shapes_dir)
        graph.parse(data=data_str, format="json-ld", base=jsonld_path.absolute().as_uri())
    else:
        graph.parse(str(jsonld_path), format="json-ld", base=jsonld_path.absolute().as_uri())
    return graph


def _load_shapes(shapes_dir: Path) -> rdflib.Graph:
    """디렉토리 내의 모든 *.ttl을 합쳐 SHACL shapes graph로 로드."""
    shapes = rdflib.Graph()
    ttls = sorted(shapes_dir.glob("*.ttl"))
    if not ttls:
        raise FileNotFoundError(f"No .ttl files found in {shapes_dir}")
    for ttl in ttls:
        if ttl.name.startswith("_"):
            continue
        shapes.parse(str(ttl), format="turtle")
    return shapes


def _count_severities(results_graph: rdflib.Graph) -> tuple[int, int, int]:
    """결과 graph에서 Violation/Warning/Info 개수 집계."""
    sh = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    violations = 0
    warnings = 0
    infos = 0
    for _s, _p, severity in results_graph.triples((None, sh.resultSeverity, None)):
        if severity == sh.Violation:
            violations += 1
        elif severity == sh.Warning:
            warnings += 1
        elif severity == sh.Info:
            infos += 1
    return violations, warnings, infos


def validate_file(
    jsonld_path: Path,
    shapes_dir: Path,
) -> ValidationResult:
    """단일 JSON-LD 파일을 SHACL shapes로 검증."""
    data_graph = _load_data_graph(jsonld_path, shapes_dir)
    shapes_graph = _load_shapes(shapes_dir)

    conforms, results_graph, results_text = pyshacl_validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        debug=False,
        meta_shacl=False,
        advanced=False,
    )
    v, w, i = _count_severities(results_graph)
    return ValidationResult(
        path=jsonld_path,
        conforms=conforms,
        violations=v,
        warnings=w,
        infos=i,
        text=results_text,
    )


def discover_files(paths: list[Path]) -> list[Path]:
    """경로 인자에서 *.jsonld 파일을 평탄화하여 모음."""
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files.extend(sorted(p.rglob("*.jsonld")))
        elif p.suffix == ".jsonld":
            files.append(p)
    return files
