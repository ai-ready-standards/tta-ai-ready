# tta-validator

TTA AI 레디 표준 적합성 자동 검증 CLI 도구.

## 검증 대상

| # | 검증 항목 | 도구 |
| --- | --- | --- |
| 1 | RDF 문법 | rdflib |
| 2 | SHACL 적합성 | pySHACL |
| 3 | JSON-LD `@context` 유효성 | pyld |
| 4 | Python 단위 테스트 | pytest |
| 5 | 예시 데이터셋 로딩 | mlcroissant, pandas |

## 사용 (예정)

```bash
# 설치
pip install tta-ai-ready-validator

# 단일 파일 검증
tta-validator examples/sample-01.jsonld

# 디렉토리 일괄 검증
tta-validator standards/P-01-research-data/

# CI 모드 (실패 시 exit 1)
tta-validator --ci standards/
```

## 개발

WBS C-10. `pyproject.toml`은 1단계 인프라 구축 완료 후 추가됩니다.
