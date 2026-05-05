# TTA AI-Ready Standards Repository

> AI 레디(AI-Ready) 표준 생태계 조성을 위한 표준화 전략 수립 용역 — 공개 미러
>
> 한국정보통신기술협회(TTA) 발주 사업의 산출물(JSON-LD 스키마, SHACL 검증 파일, 참조 구현 코드, 예시 데이터셋, 매뉴얼)을 공개·배포하는 GitHub 저장소입니다.

## 🌐 공개 사이트

**👉 [ai-ready-standards.github.io/tta-ai-ready](https://ai-ready-standards.github.io/tta-ai-ready/)**

대부분의 사용자는 위 사이트에서 시작하는 것이 편합니다. 본 README는 개발자·기여자용입니다.

## 사업 개요

| 항목 | 내용 |
| --- | --- |
| 사업명 | AI 레디(AI-Ready) 표준 생태계 조성을 위한 표준화 전략 수립 용역 |
| 발주처 | 한국정보통신기술협회(TTA) |
| 사업기간 | 2026년 5월 ~ 2026년 12월 15일 |
| 시범 표준 | P-01 ~ P-05 (5종, 모두 PG606 소관) |
| 핵심 산출물 | 프레임워크 정의서 · 리포지토리 설계서 · 표준화 지침 개정(안) · 파일럿 5종 · 매뉴얼 3종 · 설명회 1회 |

## 저장소 구조

```
catalog.jsonld         # 5종 표준의 DCAT v3 카탈로그 (기계 판독용)
mkdocs.yml             # 공개 사이트 설정
docs/                  # 공개 사이트 콘텐츠 (Markdown)
standards/             # 5종 시범 표준의 AI 레디 패키지
  P-01-research-data/  # JSON-LD 스키마 + SHACL shapes + 예시
  P-02-public-data/
  P-03-tagging-labeling/
  P-04-agriculture/
  P-05-steel-manufacturing/
profiles/              # 4개 목적별 프로파일 (ML/RAG/KG/통계)
tools/validator/       # tta-validator CLI (pySHACL 기반)
.github/workflows/     # CI · GitHub Pages 배포 · PyPI 배포
.devcontainer/         # GitHub Codespaces 검증 환경
```

## 빠른 시작

### 검증 도구

```bash
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
python3.11 -m venv venv && source venv/bin/activate
pip install -e tools/validator/
tta-validator standards/P-01-research-data/5_examples/
```

### 사이트 로컬 미리보기

```bash
pip install mkdocs-material
mkdocs serve
# http://127.0.0.1:8000
```

### Codespaces (브라우저)

[`Open in Codespaces`](https://codespaces.new/ai-ready-standards/tta-ai-ready?quickstart=1) 클릭 → 1~2분 후 즉시 사용 가능.

## 국제 표준 어휘

본 저장소의 모든 패키지는 다음 글로벌 어휘와 정합성을 가지도록 설계됩니다.

- [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/)
- [W3C SHACL](https://www.w3.org/TR/shacl/)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [MLCommons Croissant 1.0](https://mlcommons.org/croissant/)
- [DataCite Metadata Schema 4.5](https://schema.datacite.org/)
- [ISO/IEC 5259](https://www.iso.org/standard/81088.html)
- [DUO (Data Use Ontology)](https://github.com/EBISPOT/DUO)

## 기여 및 거버넌스

- 기여 절차: [CONTRIBUTING.md](./CONTRIBUTING.md)
- 코드 소유자: [CODEOWNERS](./CODEOWNERS)
- 라이선스: [Apache License 2.0](./LICENSE)

## 운영 모델

- **마스터 저장소**: TTA 내부망 GitLab Enterprise (개발·심의·승인)
- **공개 미러**: 본 GitHub 저장소 (자동 검증·승인 통과한 패키지만 동기화)
- **자동 배포**: main 브랜치 push 시 GitHub Pages 자동 갱신

## 문의

본 사업 관련 문의는 TTA PG606 소관 부서 또는 사업 수행사로 연락 주시기 바랍니다.
