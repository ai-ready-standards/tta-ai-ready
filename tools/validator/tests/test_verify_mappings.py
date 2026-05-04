"""tta_validator.verify_mappings 단위 테스트."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tta_validator.verify_mappings import (
    EXCLUDED_PREFIXES,
    _extract_from_jsonld_context,
    _extract_from_turtle,
    _extract_jsonld_prefix_map,
    load_manifest,
    merge_usages,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
CACHE_DIR = REPO_ROOT / "vocabularies" / "cached"


# ────────────────────────────────────────────────────────────────────────
# Fixtures
# ────────────────────────────────────────────────────────────────────────

@pytest.fixture
def sample_jsonld(tmp_path):
    """테스트용 JSON-LD context 파일 생성."""
    p = tmp_path / "context.jsonld"
    p.write_text(json.dumps({
        "@context": {
            "tta": "https://standards.tta.or.kr/test#",
            "dcat": "http://www.w3.org/ns/dcat#",
            "dcterms": "http://purl.org/dc/terms/",
            "Dataset": "dcat:Dataset",
            "title": "dcterms:title",
            "BadOne": "dcat:NonExistentTerm",
        }
    }))
    return p


@pytest.fixture
def sample_ttl(tmp_path):
    """테스트용 SHACL Turtle 파일 생성."""
    p = tmp_path / "shapes.ttl"
    p.write_text("""
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix tta:  <https://standards.tta.or.kr/test#> .

tta:DatasetShape a sh:NodeShape ;
    sh:targetClass dcat:Dataset ;
    sh:property [ sh:path dct:title ; sh:minCount 1 ] .
""")
    return p


# ────────────────────────────────────────────────────────────────────────
# Manifest loading
# ────────────────────────────────────────────────────────────────────────

def test_manifest_loads():
    specs = load_manifest(CACHE_DIR)
    assert len(specs) >= 11
    prefixes = {s.prefix for s in specs}
    # 필수 어휘들이 모두 있어야 함
    for required in ["dcat", "dct", "prov", "sh", "skos", "schema", "dqv"]:
        assert required in prefixes, f"Missing vocabulary: {required}"


def test_manifest_files_exist():
    specs = load_manifest(CACHE_DIR)
    for s in specs:
        assert s.file.is_file(), f"Vocab file missing: {s.file}"


def test_excluded_prefixes_includes_self():
    """우리 자체 namespace는 검증 제외되어야 함."""
    assert "tta" in EXCLUDED_PREFIXES
    assert "ttaap" in EXCLUDED_PREFIXES
    assert "tta0976" in EXCLUDED_PREFIXES
    assert "re3data" in EXCLUDED_PREFIXES  # XSD 기반, RDF 미발행


# ────────────────────────────────────────────────────────────────────────
# JSON-LD context extraction
# ────────────────────────────────────────────────────────────────────────

def test_extract_jsonld_prefix_map(sample_jsonld):
    pmap = _extract_jsonld_prefix_map(sample_jsonld)
    assert pmap["dcat"] == "http://www.w3.org/ns/dcat#"
    assert pmap["dcterms"] == "http://purl.org/dc/terms/"


def test_extract_iris_from_jsonld(sample_jsonld):
    pmap = _extract_jsonld_prefix_map(sample_jsonld)
    usages = _extract_from_jsonld_context(sample_jsonld, pmap)
    iris = {u.iri for u in usages}
    assert "http://www.w3.org/ns/dcat#Dataset" in iris
    assert "http://purl.org/dc/terms/title" in iris
    assert "http://www.w3.org/ns/dcat#NonExistentTerm" in iris


# ────────────────────────────────────────────────────────────────────────
# Turtle extraction
# ────────────────────────────────────────────────────────────────────────

def test_extract_iris_from_turtle(sample_ttl):
    pmap, usages = _extract_from_turtle(sample_ttl)
    assert pmap["dcat"] == "http://www.w3.org/ns/dcat#"
    iris = {u.iri for u in usages}
    assert "http://www.w3.org/ns/dcat#Dataset" in iris
    assert "http://purl.org/dc/terms/title" in iris


# ────────────────────────────────────────────────────────────────────────
# Usage merging
# ────────────────────────────────────────────────────────────────────────

def test_merge_usages_dedups():
    from tta_validator.verify_mappings import IRIUsage
    usages = [
        IRIUsage(iri="http://example.org/x", prefix="ex", sources=["a.json:1"]),
        IRIUsage(iri="http://example.org/x", prefix="ex", sources=["b.ttl:5"]),
        IRIUsage(iri="http://example.org/y", prefix="ex", sources=["c.json:2"]),
    ]
    merged = merge_usages(usages)
    assert len(merged) == 2
    x_entry = next(u for u in merged if u.iri == "http://example.org/x")
    assert sorted(x_entry.sources) == ["a.json:1", "b.ttl:5"]


# ────────────────────────────────────────────────────────────────────────
# End-to-end verification
# ────────────────────────────────────────────────────────────────────────

def test_verify_e2e_passes_for_repo():
    """본 저장소 자체의 매핑이 100% 통과해야 함 (회귀 방지)."""
    from tta_validator.verify_mappings import verify
    result = verify(REPO_ROOT)
    assert result.passed, (
        f"Verify failed: {len(result.failed)} IRIs missing.\n"
        + "\n".join(f"  - {u.iri}" for u in result.failed[:10])
    )
    assert result.verified > 0, "Should verify at least some IRIs"
