# P-04 — 농업 AI 학습 데이터 (AI 레디 패키지)

> 🚧 **Placeholder** — 본 패키지는 아직 작성되지 않았습니다. WBS C-8에 따라 **2026년 9월 착수, 11월 중순 완료** 예정입니다. 본 디렉토리의 6개 하위 폴더는 [프레임워크 정의서](../../docs/framework/index.md)의 6-패키지 구조에 따라 사전에 생성된 빈 골격입니다.

## 대상 표준

| 항목 | 내용 |
| --- | --- |
| 표준번호 | **TTAK.KO-10.1533** |
| 표준명 | 농업 분야 인공지능 학습 데이터 플랫폼 관리를 위한 메타데이터 스키마 |
| 제정일 | 2024-12 |
| 소관 | TTA · PG606 |
| AP 버전 | (미발행) |

## 국제 연계 어휘

- [MLCommons Croissant 1.0](https://mlcommons.org/croissant/) — ML 데이터셋 메타데이터
- [ISO/IEC 5259](https://www.iso.org/standard/81088.html) — 데이터 품질

## 6 패키지 구성 (예정)

본 디렉토리는 [프레임워크 정의서 Part III](../../docs/framework/index.md)의 6-패키지 표준 구조를 따릅니다.

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| `1_document/` | AP 명세 문서 | 🚧 |
| `2_schema/` | JSON-LD context + SHACL shapes (농업 특화 어휘 포함) | 🚧 |
| `3_code/` | Python Pydantic + ML 호환 로더 | 🚧 |
| `4_validator/` | pySHACL 래퍼 + 영상·센서 결측률 자동 검사 | 🚧 |
| `5_examples/` | 작물 유형·생육 단계·촬영 조건별 예시 | 🚧 |
| `6_changelog/` | 어휘 버전 lock + 결정 추적 | 🚧 |

## 농업 특화 어휘

- 작물 유형 (Crop type)
- 생육 단계 (Growth stage)
- 촬영 조건 (Capture conditions)
- 센서 메타데이터

## 핵심 차별점 (예정)

- 영상·센서 결측률 SHACL 자동 검사
- ISO/IEC 5259 품질 차원 차용
- Croissant + ISO 5259 결합

## c4 + c6 활성

본 표준은 **ML 학습 데이터 + 품질 차원이 핵심**이므로 c4 운영 시맨틱과 c6 품질 프로파일 **모두 활성**됩니다.

## 일정

WBS C-8 (수행계획서 2.3절). **정식 착수: 2026년 9월**.

본 작업은 [기존 표준 전환 매뉴얼](../../docs/manuals/migration-guide.md)의 Phase A → A.5 → B → C → D 흐름을 따릅니다.
