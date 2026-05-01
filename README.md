# TTA AI-Ready Standards Repository

> AI 레디(AI-Ready) 표준 생태계 조성을 위한 표준화 전략 수립 용역 — 공개 미러
>
> 본 저장소는 한국정보통신기술협회(TTA) 발주 사업의 산출물(JSON-LD 스키마, SHACL 검증 파일, 참조 구현 코드, 예시 데이터셋, 매뉴얼)을 공개·배포하기 위한 GitHub 미러입니다. 마스터 저장소는 TTA 내부망의 GitLab Enterprise이며, 본 저장소는 자동 검증·승인을 거친 패키지만 동기화됩니다.

## 사업 개요

| 항목 | 내용 |
| --- | --- |
| 사업명 | AI 레디(AI-Ready) 표준 생태계 조성을 위한 표준화 전략 수립 용역 |
| 발주처 | 한국정보통신기술협회(TTA) |
| 사업기간 | 2026년 5월 ~ 2026년 12월 15일 |
| 핵심 산출물 | 프레임워크 정의서 · 리포지토리 설계서 · 표준화 지침 개정(안) · 파일럿 5종 · 매뉴얼 3종 · 설명회 1회 |

## 저장소 구조

```
standards/        # PG606 소관 5종 파일럿 표준의 AI 레디 패키지
  P-01-research-data/        # 연구데이터 메타데이터 (DataCite, DCAT v3)
  P-02-public-data/          # 공공데이터 메타데이터 (DCAT v3, CC)
  P-03-tagging-labeling/     # 비정형 데이터 태깅·라벨링 (Croissant RAI, DUO)
  P-04-agriculture/          # 농업 AI 학습 데이터 (Croissant, ISO 5259)
  P-05-steel-manufacturing/  # 철강 제조 데이터 (IEC 62264, PROV-O)
profiles/         # 4개 목적별 프로파일 (ML / RAG / KG / Statistics)
tools/            # 공통 검증 CLI (pySHACL 기반)
docs/             # 프레임워크 정의서·리포지토리 설계서·매뉴얼 3종
.github/workflows/ # CI: SHACL · JSON-LD · pytest · 예시 로딩
```

각 파일럿 디렉토리는 `schema/`(JSON-LD 스키마), `shapes/`(SHACL 검증 규칙), `examples/`(예시 데이터셋) 하위 구조를 가집니다.

## 빠른 시작

```bash
# 검증 도구 설치 (예정)
pip install tta-ai-ready-validator

# 파일럿 표준 검증
tta-validator standards/P-01-research-data/examples/sample-01.jsonld
```

## 국제 표준 어휘

본 저장소의 모든 패키지는 다음 글로벌 어휘와 정합성을 가지도록 설계됩니다.

- [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/) — 데이터셋 메타데이터
- [W3C SHACL](https://www.w3.org/TR/shacl/) — 데이터 검증
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) — 출처·계보
- [MLCommons Croissant 1.0](https://mlcommons.org/croissant/) — ML 데이터셋
- [ISO/IEC 5259](https://www.iso.org/standard/81088.html) — 데이터 품질
- [DUO (Data Use Ontology)](https://github.com/EBISPOT/DUO) — 사용 제약

## 기여 및 거버넌스

- 기여 절차: [CONTRIBUTING.md](./CONTRIBUTING.md)
- 코드 소유자: [CODEOWNERS](./CODEOWNERS)
- 라이선스: [Apache License 2.0](./LICENSE)

## 문의

본 사업 관련 문의는 TTA PG606 소관 부서 또는 사업 수행사로 연락 주시기 바랍니다.
