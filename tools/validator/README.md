# tta-validator

TTA AI 레디 표준 적합성 자동 검증 CLI. pySHACL 기반.

## 검증 단계

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
pip install -e tools/validator/
```

## 사용

### 단일 파일

```bash
tta-validator standards/P-01-research-data/examples/valid/dataset-minimal.jsonld
```

### 디렉토리 일괄

```bash
tta-validator standards/P-01-research-data/examples/valid/
```

### 다른 표준의 shapes 사용

```bash
tta-validator <files> --shapes-dir standards/P-02-public-data/shapes
```

### CI 모드

`--ci`: M(Mandatory) 위반이 1건 이상이면 exit code 1.

```bash
tta-validator standards/P-01-research-data/examples/valid/ --ci
```

### 음성 테스트

`--expect-fail`: 의도된 오류 케이스. M 위반이 0건이면 exit code 1.

```bash
tta-validator standards/P-01-research-data/examples/invalid/ --expect-fail
```

### 상세 출력

`-v`: 위반·경고·정보 메시지 전체 출력.

## 통과 기준

- **M (Mandatory) 위반 = 0**: CI 통과
- **R (Recommended) 경고**: CI는 통과, 리포트에 표시
- **O (Optional) 정보**: 통계 수집

## 로컬 빠른 검증 예시

```bash
$ tta-validator standards/P-01-research-data/examples/valid/
검증 대상: 4개 파일 / shapes: standards/P-01-research-data/shapes
------------------------------------------------------------
  ✓ collection-minimal.jsonld         (M:0 R:4 O:0)
  ✓ dataset-complete-kisti.jsonld    (M:0 R:0 O:0)
  ✓ dataset-minimal.jsonld           (M:0 R:3 O:0)
  ✓ repository-narda.jsonld          (M:0 R:0 O:0)
------------------------------------------------------------
합계: 4개 / 위반(M)=0  경고(R)=7  정보(O)=0
```
