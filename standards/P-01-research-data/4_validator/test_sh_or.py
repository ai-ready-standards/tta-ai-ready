"""Issue-001 완화: pySHACL `sh:or` 패턴 지원 단위 테스트.

본 테스트는 Phase C 시작 시 즉시 실행하여 sh:or 처리 가능 여부 확인.
미지원 시 SHACL shapes를 분리하거나 Pydantic fallback으로 검증.
"""
import sys
from pathlib import Path

try:
    from pyshacl import validate as pyshacl_validate
except ImportError:
    print("✗ pyshacl 미설치. 'pip install pyshacl' 실행 필요.")
    sys.exit(1)


# 테스트 SHACL shape — Coverage dual-purpose (시간 OR 공간)
SHACL_SHAPE = """
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.com/> .

ex:CoverageShape a sh:NodeShape ;
    sh:targetClass ex:File ;
    sh:property [
        sh:path dcterms:coverage ;
        sh:or (
            [ sh:datatype xsd:string ]
            [ sh:datatype xsd:dateTime ]
            [ sh:datatype xsd:date ]
            [ sh:nodeKind sh:IRI ]
        ) ;
        sh:maxCount 1 ;
    ] .
"""

# 테스트 데이터 1: 시간 형식 (xsd:date)
DATA_1 = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.com/> .

ex:file1 a ex:File ;
    dcterms:coverage "2026-05-04"^^xsd:date .
"""

# 테스트 데이터 2: 공간 형식 (자유 텍스트)
DATA_2 = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.com/> .

ex:file2 a ex:File ;
    dcterms:coverage "서울시" .
"""

# 테스트 데이터 3: IRI 형식
DATA_3 = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.com/> .

ex:file3 a ex:File ;
    dcterms:coverage <https://example.com/place/seoul> .
"""

# 테스트 데이터 4: 잘못된 형식 (Boolean — 거부되어야 함)
DATA_4 = """
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ex: <https://example.com/> .

ex:file4 a ex:File ;
    dcterms:coverage "true"^^xsd:boolean .
"""


def test_sh_or(data_ttl: str, expected_conforms: bool, label: str) -> bool:
    """단일 sh:or 시나리오 테스트."""
    try:
        conforms, _, _ = pyshacl_validate(
            data_graph=data_ttl,
            shacl_graph=SHACL_SHAPE,
            data_graph_format="turtle",
            shacl_graph_format="turtle",
            inference="rdfs",
        )
        status = "✓" if conforms == expected_conforms else "✗"
        print(f"  {status} {label}: conforms={conforms} (expected {expected_conforms})")
        return conforms == expected_conforms
    except Exception as e:
        print(f"  ✗ {label}: ERROR - {e}")
        return False


def main():
    print("=" * 60)
    print("Issue-001: pySHACL sh:or 패턴 지원 검증")
    print("=" * 60)
    print()

    results = [
        test_sh_or(DATA_1, True, "Test 1 (xsd:date) → conforms 기대"),
        test_sh_or(DATA_2, True, "Test 2 (xsd:string) → conforms 기대"),
        test_sh_or(DATA_3, True, "Test 3 (IRI) → conforms 기대"),
        test_sh_or(DATA_4, False, "Test 4 (xsd:boolean) → 거부 기대"),
    ]

    print()
    passed = sum(results)
    total = len(results)
    print(f"=" * 60)
    if passed == total:
        print(f"✓ pySHACL sh:or 완전 지원 확인 ({passed}/{total})")
        print("  Coverage dual-purpose 패턴이 정상 작동합니다.")
        print("  → shapes.shacl.ttl을 그대로 사용 가능. fallback 불필요.")
    else:
        print(f"✗ pySHACL sh:or 부분 지원 ({passed}/{total})")
        print("  Issue-001 완화 필요:")
        print("  1. shapes.shacl.ttl에서 sh:or 분기를 두 NodeShape으로 분리")
        print("  2. 또는 4_validator/validate.py --fallback-pydantic 사용")
        sys.exit(1)


if __name__ == "__main__":
    main()
