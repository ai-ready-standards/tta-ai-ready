# 매핑 매트릭스 — TTA × 7구성요소

본 매트릭스는 TTAK.KO-10.0976의 93개 요소가 **7개 AI 레디 구성요소**(c1~c7)에 어떻게 매핑되는지를 한 눈에 보여줍니다.

## 매트릭스 (93행 × 16컬럼)

[:material-download: tta-0976_x_components.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_x_components.csv){ .md-button .md-button--primary }

### 16개 컬럼

| # | 컬럼 | 내용 |
| --- | --- | --- |
| 1 | `tta_inventory_id` | TTA-0976-001 ~ 327 |
| 2 | `tta_element_name_ko` | 한글 요소명 |
| 3 | `tta_layer` | repository / collection / dataset / file |
| 4 | `tta_cardinality` | M / R / O |
| 5 | **`c1_semantic`** | 시맨틱 매핑 (IRI) |
| 6 | **`c2_data_model`** | SHACL 제약 |
| 7 | **`c3_syntactic`** | JSON-LD 표현 |
| 8 | **`c4_operational_semantic`** | ML 운영 시맨틱 (P-01은 NA 일관 처리) |
| 9 | **`c5_provenance`** | PROV-O 매핑 |
| 10 | **`c6_quality`** | DQV 매핑 |
| 11 | **`c7_access_constraint`** | 접근·사용 제약 |
| 12 | `mapping_priority` | primary / secondary / loose / none |
| 13 | `mapping_confidence` | high / medium / low |
| 14 | `conflict_notes` | 매핑 충돌 사항 |
| 15 | `decision_basis` | 결정 근거 |
| 16 | `reviewer_notes` | 검토 노트 |

## 통제어 매핑 (117행)

[:material-download: tta-0976_enumerations_mapping.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_enumerations_mapping.csv){ .md-button }

24개 통제어 카테고리의 117개 enum 값 각각이 어느 외부 어휘에서 유래하는지 추적.

## 검토용 표본 (46행)

[:material-download: tta-0976_review_sample.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_review_sample.csv){ .md-button }

전체 매핑 검수에 시간이 부족할 때 핵심 항목만 검토할 수 있도록 추출한 표본.

## 매핑 통계 (Phase B)

### 등급 분포

| 등급 | 매트릭스 (93) | 통제어 (117) |
| --- | --- | --- |
| **primary** | 82 (88.2%) | 111 (94.9%) |
| secondary | 11 (11.8%) | 4 (3.4%) |
| loose | 0 | 0 |
| none | 0 | 2 (1.7%) |

### 신뢰도 분포 (매트릭스)

| 신뢰도 | 개수 | 비율 |
| --- | --- | --- |
| high | 76 | 81.7% |
| medium | 17 | 18.3% |
| low | 0 | 0% |

### 종합 매핑 가능률

| 영역 | 총 항목 | 성공 | 비율 |
| --- | --- | --- | --- |
| 메타데이터 매트릭스 | 93 | 93 | **100.0%** |
| 통제어 | 117 | 115 | 98.3% |
| **종합** | **210** | **208** | **★ 99.0%** |

매핑 부재 2건:
- **UCI** (한국 보편적 콘텐츠 식별자) — 글로벌 어휘 부재
- **'other' FileType** — DCMI Type Vocabulary 외 폴백 값

→ 글로벌 어휘 보유 가능 항목은 **100% 매핑 완료**.

## 7개 구성요소 채움 현황

| 구성요소 | 활성 행 / 93 | 비율 | 비고 |
| --- | --- | --- | --- |
| c1 시맨틱 | 93 | 100% | 모든 행에 매핑 결정 |
| c2 데이터 모델 | 93 | 100% | SHACL 제약 작성 |
| c3 신태틱 | 93 | 100% | JSON-LD 매핑 |
| **c4 운영 시맨틱** | 0 | 0% | **본 표준은 일반 연구데이터** — Decision-3 일관 적용 |
| c5 출처·계보 | 6 | 6% | Date+DateType 조건부 + ResponsibilityType |
| **c6 품질** | 1 | 1% | **★ Decision-Q4 (Boolean Activation Slot)** |
| c7 접근·사용 제약 | 13 | 14% | AccessType + AccessRestriction + Rights + License |

## 매핑 충돌 분석

상세 충돌 + 결정 과정: [reports/tta-0976_mapping_conflicts.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/tta-0976_mapping_conflicts.md) (459행 보고서)
