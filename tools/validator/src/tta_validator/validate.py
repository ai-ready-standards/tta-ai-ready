"""SHACL 검증 핵심 로직."""

from __future__ import annotations

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


def _load_data_graph(jsonld_path: Path) -> rdflib.Graph:
    """JSON-LD 파일을 rdflib Graph로 로드. 상대 @context를 절대 경로로 해석."""
    graph = rdflib.Graph()
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
    data_graph = _load_data_graph(jsonld_path)
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
