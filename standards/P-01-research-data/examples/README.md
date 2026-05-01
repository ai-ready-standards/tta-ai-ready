# P-01 예시 데이터셋

## 유효 예시 (valid/)

| 파일 | 클래스 | 설명 |
| --- | --- | --- |
| [`dataset-minimal.jsonld`](./valid/dataset-minimal.jsonld) | Dataset (D) | 모든 M(Mandatory) 요소만 포함한 최소 데이터셋 |
| [`dataset-complete-kisti.jsonld`](./valid/dataset-complete-kisti.jsonld) | Dataset (D) | KISTI NARDA 시나리오 — M+R+O + PROV-O 계보 |
| [`collection-minimal.jsonld`](./valid/collection-minimal.jsonld) | Collection (C) | 컬렉션 최소 예시 |
| [`repository-narda.jsonld`](./valid/repository-narda.jsonld) | Repository (R) | KISTI NARDA 리포지토리 메타데이터 |

## 음성 테스트 (invalid/)

검증 도구가 오류를 정확히 잡아내는지 확인하기 위한 의도적 오류 예시.

| 파일 | 의도된 오류 |
| --- | --- |
| [`dataset-missing-mandatory.jsonld`](./invalid/dataset-missing-mandatory.jsonld) | D2 Identifier, D5 Publisher 누락 — 2건의 sh:Violation 발생해야 함 |

## 검증 실행

```bash
# 유효 예시는 모두 통과해야 함
python -m tta_validator standards/P-01-research-data/examples/valid/

# 음성 테스트는 명시된 오류가 발생해야 함 (--expect-fail 모드)
python -m tta_validator standards/P-01-research-data/examples/invalid/ --expect-fail
```
