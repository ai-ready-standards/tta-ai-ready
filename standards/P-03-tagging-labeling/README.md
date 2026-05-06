# P-03 — 비정형 데이터 태깅·라벨링 (AI 레디 패키지)

> 🚧 **Placeholder** — 본 패키지는 아직 작성되지 않았습니다. WBS C-7에 따라 **2026년 9월 착수, 11월 중순 완료** 예정입니다. 본 디렉토리의 6개 하위 폴더는 [프레임워크 정의서](../../docs/framework/index.md)의 6-패키지 구조에 따라 사전에 생성된 빈 골격입니다.

## 대상 표준

| 항목 | 내용 |
| --- | --- |
| 표준번호 | **TTAK.KO-10.1343-Part2** |
| 표준명 | 데이터 가공 공정 직무 구성 - 제2부 비정형 데이터 태깅 및 라벨링 |
| 소관 | TTA · PG606 |
| 연계 | NIA AI Hub (600종 AI 학습 데이터셋) |
| AP 버전 | (미발행) |

## 국제 연계 어휘

- [MLCommons Croissant 1.0 RAI Extension](https://mlcommons.org/croissant/) — 책임 있는 AI 어휘
- [DUO (Data Use Ontology)](https://github.com/EBISPOT/DUO) — 사용 제약

## 6 패키지 구성 (예정)

본 디렉토리는 [프레임워크 정의서 Part III](../../docs/framework/index.md)의 6-패키지 표준 구조를 따릅니다.

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| `1_document/` | AP 명세 문서 | 🚧 |
| `2_schema/` | JSON-LD context + SHACL shapes (Croissant RAI 연계) | 🚧 |
| `3_code/` | Python Pydantic + PyTorch DataLoader 호환 로더 | 🚧 |
| `4_validator/` | pySHACL 래퍼 + 라벨 품질 통계 검증 | 🚧 |
| `5_examples/` | NIA AI Hub 실제 시나리오 예시 3종 | 🚧 |
| `6_changelog/` | 어휘 버전 lock + 결정 추적 | 🚧 |

## 핵심 차별점 (예정)

- **PyTorch DataLoader 한 줄 로딩** — Croissant 1.0 호환
- 라벨 품질 자동 검증 — SHACL + 통계적 일관성 검사 결합
- DUO 어휘 기반 사용 제약 — 의료·민감 데이터의 사용 가능 범위를 기계화

## c4 운영 시맨틱 활성

본 표준은 **ML 학습 데이터** 표준이므로 7개 구성요소 중 **c4 운영 시맨틱이 활성**됩니다 ([용어집 c4 참조](../../docs/glossary.md)).

## 일정

WBS C-7 (수행계획서 2.3절). **정식 착수: 2026년 9월**.

본 작업은 [기존 표준 전환 매뉴얼](../../docs/manuals/migration-guide.md)의 Phase A → A.5 → B → C → D 흐름을 따릅니다.
