# 인벤토리 — 11종 국제 어휘 + TTA 표준 통합

본 인벤토리는 본 사업의 매핑 작업의 **출발점이 되는 데이터셋**입니다. Phase A → A.5에서 작성·확장되었습니다.

## 마스터 인벤토리 (478행)

[:material-download: master_inventory.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/master_inventory.csv){ .md-button .md-button--primary }

478행 × 17컬럼:

| 컬럼 | 내용 |
| --- | --- |
| inventory_id | INV-XXXX (어휘별 ID 범위) |
| standard | DCAT v3 / Schema.org / DataCite / re3data 등 |
| version | 어휘 버전 |
| term_type | Class / Property / Datatype |
| term_name | 영문 용어명 |
| iri | 절대 IRI |
| prefix_local | dcat:Dataset 등 |
| **concept_tag** | 주제 분류 (28개 태그) |
| **equivalent_terms** | 동등·유사 어휘 |
| definition | 영문 정의 |
| definition_ko | 한글 번역 |
| source_url | 정식 출처 |

## 어휘별 인벤토리 (11개)

| 어휘 | 행 수 | inventory_id 범위 |
| --- | --- | --- |
| [Schema.org](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/schema-org.csv) | 134 | INV-1xxx |
| [PROV-O](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/prov-o.csv) | 83 | INV-2xxx |
| [DCAT v3](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/dcat-v3.csv) | 53 | INV-3xxx |
| [Croissant](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/croissant.csv) | 46 | INV-4xxx |
| [DCMI Terms](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/dcterms.csv) | 26 | INV-5xxx |
| [DQV](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/dqv.csv) | 22 | INV-5xxx |
| [DataCite](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/datacite.csv) | 51 | INV-6001~6050 |
| [re3data](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/re3data.csv) | 54 | INV-6101~6153 |
| [DCMI Type](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/dcmi-type.csv) | 13 | INV-6201~6212 |
| [ISO 코드](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/iso-codes.csv) | 7 | INV-6301~6306 |

## TTA 표준 추출

[`tta-standards/0976/`](https://github.com/ai-ready-standards/tta-ai-ready/tree/main/tta-standards/0976) — TTAK.KO-10.0976에서 직접 추출.

| 파일 | 행 수 |
| --- | --- |
| [elements.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/elements.csv) | 93 (Repository 26 + Collection 18 + Dataset 22 + File 27) |
| [enumerations.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/enumerations.csv) | 117 (24 카테고리) |
| [extraction_report.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/extraction_report.md) | 추출 과정 |

## 28개 concept_tag

마스터 인벤토리의 행을 의미적으로 분류하는 태그입니다.

| 카테고리 | 태그 |
| --- | --- |
| identification | identifier · title · description · keyword |
| actor | creator · publisher · contributor · contact |
| temporal | creation · coverage · modification |
| spatial | coverage · location |
| rights | license · access · attribution |
| structure | dataset · recordset · field |
| distribution | url · media_type · size |
| quality | general · accuracy · bias · completeness |
| provenance | derivation · activity · agent |

이 태그를 통해 서로 다른 어휘 간의 동등 관계를 자동 식별합니다.
