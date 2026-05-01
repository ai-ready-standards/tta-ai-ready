# 5종 시범 표준

본 사업으로 AI 레디화되는 5종 시범 표준은 모두 **PG606(메타데이터 프로젝트그룹) 소관**으로 통일되어 있습니다. 도메인 다양성(연구·공공·AI·농업·철강)과 국제 표준 연계 다양성(DCAT · Croissant · PROV-O · IEC 62264)을 동시에 확보하면서 TC 간 조율 부담을 최소화한 선정입니다.

## 한눈에 보기

| ID | 도메인 | 표준번호 | 제정 | 국제 어휘 | 상태 |
| --- | --- | --- | --- | --- | --- |
| [P-01](p-01.md) | 과학기술 연구 | TTAK.KO-10.0976 | 2017-03-30 | DataCite · DCAT v3 · PROV-O | :material-rocket: 1차 골격 완성 |
| [P-02](p-02.md) | 공공데이터 | (확정 예정) | — | DCAT v3 · CC | :material-clock-outline: 8월 착수 |
| [P-03](p-03.md) | AI 학습데이터 | TTAK.KO-10.1343-Part2 | — | Croissant RAI · DUO | :material-clock-outline: 9월 착수 |
| [P-04](p-04.md) | 농업 AI | TTAK.KO-10.1533 | 2024-12 | Croissant · ISO 5259 | :material-clock-outline: 9월 착수 |
| [P-05](p-05.md) | 철강 제조 | TTAK.KO-10.1571 | 2025-06 | IEC 62264 · PROV-O | :material-clock-outline: 9월 착수 |

## 도메인별 분류

=== ":material-flask: 과학기술"
    - **[P-01 연구데이터](p-01.md)** — 연구과제에서 생산되는 모든 종류의 데이터
    - 컬렉션 → 데이터셋 → 파일 → 리포지토리 4계층 구조

=== ":material-bank: 공공"
    - **[P-02 공공데이터](p-02.md)** — 행안부 공공데이터포털 250종 표준 데이터셋
    - 9,027개 공통표준용어 기반

=== ":material-robot: AI"
    - **[P-03 태깅·라벨링](p-03.md)** — NIA AI Hub 600종 데이터셋
    - 책임 있는 AI(RAI) 어휘 결합

=== ":material-leaf: 산업"
    - **[P-04 농업](p-04.md)** — 작물·생육·센서 데이터
    - **[P-05 철강](p-05.md)** — 원자재→공정→제품 추적

## 국제 어휘 연계 분류

| 국제 어휘 | 사용 표준 | 효과 |
| --- | --- | --- |
| [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/) | P-01, P-02 | Google Dataset Search 자동 색인 |
| [MLCommons Croissant 1.0](https://mlcommons.org/croissant/) | P-01, P-03, P-04 | PyTorch · TensorFlow · HuggingFace 직접 로딩 |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | P-01, P-05 | 출처·계보 자동 추적 |
| [DataCite Schema 4.5](https://schema.datacite.org/) | P-01 | DOI 등록 호환 |
| [DUO (Data Use Ontology)](https://github.com/EBISPOT/DUO) | P-03 | 사용 제약 기계화 |
| [ISO/IEC 5259](https://www.iso.org/standard/81088.html) | P-04, P-05 | 데이터 품질 차원 |
| [IEC 62264](https://webstore.iec.ch/publication/5563) | P-05 | 제조 도메인 상호운용성 |

## DCAT 카탈로그

본 카탈로그 자체는 W3C DCAT v3 형식으로 발행됩니다. AI 시스템·데이터 검색 엔진·DataHub 등 카탈로그 도구가 자동으로 5종을 발견할 수 있습니다.

[catalog.jsonld 보기 :material-download:](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/catalog.jsonld){ .md-button }

```bash
curl -L https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/catalog.jsonld
```
