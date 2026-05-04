# 4_validator — pySHACL Validator

TTA-0976 SHACL shapes로 JSON-LD 데이터 검증.

## 설치

```bash
pip install pyshacl  # 0.25+ 권장
```

## 사용법

### 기본 검증

```bash
python validate.py ../5_examples/kisti_dataon.jsonld
```

기대 출력 (검증 통과 시):
```
TTA-0976 SHACL Validator v1.0.0
Data: ../5_examples/kisti_dataon.jsonld
Shapes: ../2_schema/shapes.shacl.ttl

✓ Conforms: True
  데이터가 모든 SHACL shape 제약을 통과했습니다.
```

### 상세 출력 (위반 사항 표시)

```bash
python validate.py --verbose data.jsonld
```

### Issue-001 fallback (Pydantic 검증)

pySHACL이 sh:or 패턴을 완전 지원하지 못하는 경우:

```bash
python validate.py --fallback-pydantic data.jsonld
```

## Issue-001 사전 검증

Phase C 첫 작업: sh:or 패턴 지원 단위 테스트 실행.

```bash
python test_sh_or.py
```

기대 출력:
```
============================================================
Issue-001: pySHACL sh:or 패턴 지원 검증
============================================================

  ✓ Test 1 (xsd:date) → conforms 기대: conforms=True (expected True)
  ✓ Test 2 (xsd:string) → conforms 기대: conforms=True (expected True)
  ✓ Test 3 (IRI) → conforms 기대: conforms=True (expected True)
  ✓ Test 4 (xsd:boolean) → 거부 기대: conforms=False (expected False)

============================================================
✓ pySHACL sh:or 완전 지원 확인 (4/4)
  Coverage dual-purpose 패턴이 정상 작동합니다.
  → shapes.shacl.ttl을 그대로 사용 가능. fallback 불필요.
```

만약 일부 실패 시: shapes.shacl.ttl을 분리하거나 fallback 사용.

## 종료 코드

- `0`: Conforms (검증 통과)
- `1`: Non-conforms 또는 오류

CI/CD 파이프라인에 직접 통합 가능.

## 작동 원리

본 검증기는 다음을 수행:

1. JSON-LD 파일 로드 + RDF 트리플로 변환
2. `2_schema/shapes.shacl.ttl` 로드
3. pySHACL로 SHACL Core + 일부 Advanced Features 검증
4. 결과 포맷팅 (한국어 메시지)

검증되는 항목:
- 4 NodeShape (Repository/Collection/Dataset/File)
- 2 보조 Shape (SubjectShape SKOS, QualityActivationShape)
- 1 조건부 Shape (ProvenanceConditionalShape)
- ~85 PropertyShape (sh:minCount/maxCount/datatype/in/pattern/or)
