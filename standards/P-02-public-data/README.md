# P-02 — 공공데이터 메타데이터 (AI 레디 패키지)

> 🚧 **Placeholder** — 본 패키지는 아직 작성되지 않았습니다. WBS C-6에 따라 **2026년 8월 착수, 11월 중순 완료** 예정입니다. 본 디렉토리의 6개 하위 폴더는 [프레임워크 정의서](../../docs/framework/index.md)의 6-패키지 구조에 따라 사전에 생성된 빈 골격입니다.

## 대상 표준

| 항목 | 내용 |
| --- | --- |
| 표준번호 | (1단계 확정 예정) |
| 표준명 | 공공데이터 메타데이터 기술 규칙 |
| 소관 | TTA · PG606 |
| 연계 | 행안부 공공데이터포털 (공통표준용어 9,027개, 표준 데이터셋 250종) |
| AP 버전 | (미발행) |

## 국제 연계 어휘

- [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/) — 카탈로그·데이터셋 표현
- [Creative Commons URI](https://creativecommons.org/licenses/) — 라이선스 기계 판독

## 6 패키지 구성 (예정)

본 디렉토리는 [프레임워크 정의서 Part III](../../docs/framework/index.md)의 6-패키지 표준 구조를 따릅니다.

| 디렉토리 | 내용 | 상태 |
| --- | --- | --- |
| `1_document/` | AP 명세 문서 (`TTA-XXXX-AP.md`) | 🚧 |
| `2_schema/` | JSON-LD context + SHACL shapes | 🚧 |
| `3_code/` | Python Pydantic 모델 + 단위 테스트 | 🚧 |
| `4_validator/` | pySHACL 래퍼 검증 도구 | 🚧 |
| `5_examples/` | 공공데이터포털 실데이터 예시 3종 | 🚧 |
| `6_changelog/` | 어휘 버전 lock + 결정 추적 | 🚧 |

## 핵심 차별점 (예정)

- DCAT v3 매핑으로 글로벌 카탈로그 도구 직접 호환
- CC 라이선스 URI 기반 사용 제약의 기계 판독화
- 품질 프로파일(완전성·적시성·정확성)의 ISO/IEC 5259 차원 매핑

## 일정

WBS C-6 (수행계획서 2.3절). **정식 착수: 2026년 8월**.

본 작업은 [기존 표준 전환 매뉴얼](../../docs/manuals/migration-guide.md)의 Phase A → A.5 → B → C → D 흐름을 따릅니다.
