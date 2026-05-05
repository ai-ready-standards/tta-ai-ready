# tta-validator

TTA AI 레디 표준 적합성 자동 검증 CLI. pySHACL 기반.

본 도구는 **저장소 전체에서 사용되는 범용 검증 CLI**이며, 표준별 전용 검증기(`standards/P-XX-domain/4_validator/validate.py`)와 별개로 동작합니다.

## 두 명령

| 명령 | 용도 |
| --- | --- |
| `tta-validator` | JSON-LD 인스턴스를 SHACL shapes로 검증 (M/R/O 등급별 출력) |
| `tta-verify-mappings` | JSON-LD context와 SHACL shapes의 모든 IRI가 정식 어휘에 존재하는지 검증 |

## 검증 단계 (`tta-validator`)

| # | 단계 | 도구 |
| --- | --- | --- |
| 1 | JSON-LD 1.1 파싱 | rdflib |
| 2 | SHACL 적합성 (M 위반 시 실패) | pySHACL |
| 3 | M/R/O 등급별 결과 분류 | tta-validator |

## 설치

```bash
# venv 권장 (pyld는 Python 3.10+ 필요)
python3.11 -m venv venv
source venv/bin/activate
pip install -e tools/validator/[dev]
```

## `tta-validator` 사용

### 단일 파일

```bash
tta-validator standards/P-01-research-data/5_examples/kisti_dataon.jsonld
```

### 디렉토리 일괄

```bash
tta-validator standards/P-01-research-data/5_examples/
```

### 다른 표준의 shapes 사용

`--shapes-dir`로 명시. 기본값은 P-01의 `2_schema/`.

```bash
tta-validator <files> --shapes-dir standards/P-04-agriculture/2_schema
```

### CI 모드

`--ci`: M(Mandatory) 위반이 1건 이상이면 exit code 1.

```bash
tta-validator standards/P-01-research-data/5_examples/ --ci
```

### 상세 출력

`-v`: 위반·경고·정보 메시지 전체 출력.

## 통과 기준

- **M (Mandatory) 위반 = 0**: CI 통과
- **R (Recommended) 경고**: CI는 통과, 리포트에 표시
- **O (Optional) 정보**: 통계 수집

## `tta-verify-mappings` 사용

JSON-LD context와 SHACL shapes에서 사용한 외부 IRI가 정식 어휘(DCAT, DCMI Terms, PROV-O 등 12종)에 정의되어 있는지 확인.

```bash
tta-verify-mappings
```

```
국제 어휘 매핑 검증
------------------------------------------------------------
✓ 75/75 매핑 모두 정식 어휘에 존재 (100.0%)
```

## 로컬 빠른 검증 예시

```bash
$ tta-validator standards/P-01-research-data/5_examples/
검증 대상: 3개 파일 / shapes: standards/P-01-research-data/2_schema
------------------------------------------------------------
  ✓ kisti_dataon.jsonld           (M:0 R:0 O:0)
  ✓ nie_environmental.jsonld     (M:0 R:0 O:0)
  ✓ rda_agriculture.jsonld       (M:0 R:0 O:0)
------------------------------------------------------------
합계: 3개 / 위반(M)=0  경고(R)=0  정보(O)=0
```

## 단위 테스트

```bash
pytest tools/validator/tests/
```
