# 스키마 레퍼런스

본 섹션은 P-01 (TTAK.KO-10.0976) AP 1.0.0의 스키마·매핑·통제어 레퍼런스입니다. 다른 4종 표준(P-02~P-05)도 정식 착수 후 동일한 형태로 추가됩니다.

## 4계층 구조

| 클래스 | 요소 ID 범위 | 요소 수 | DCAT 매핑 |
| --- | --- | --- | --- |
| Repository | R1 ~ R21 | 26 | `dcat:Catalog` ⊃ |
| Collection | C1 ~ C12 | 18 | `dctype:Collection` |
| Dataset | D1 ~ D15 | 22 | `dcat:Dataset` ≡ |
| File | F1 ~ F19 | 27 | `dcat:Distribution` ≈ |

각 요소의 상세 매핑은 다음에서 확인하세요:

- [tta-standards/0976/elements.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/elements.csv) — TTA 본문 기반 요소 정의
- [mappings/tta-0976_x_components.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_x_components.csv) — 7구성요소 매트릭스
- [`2_schema/context.jsonld`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/2_schema/context.jsonld) — JSON-LD 매핑
- [`2_schema/shapes.shacl.ttl`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/2_schema/shapes.shacl.ttl) — SHACL 제약

## 통제어

24개 카테고리, 117개 enum 값. 전체 목록은 [tta-standards/0976/enumerations.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/enumerations.csv) 참조.

## 핵심 인벤토리·매핑 자산

| 자산 | GitHub 위치 |
| --- | --- |
| TTA 요소 추출 (93행) | [tta-standards/0976/elements.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/elements.csv) |
| TTA 통제어 (117행) | [tta-standards/0976/enumerations.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/enumerations.csv) |
| 마스터 인벤토리 (478행) | [inventory/master_inventory.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/master_inventory.csv) |
| TTA × 7구성요소 매트릭스 | [mappings/tta-0976_x_components.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_x_components.csv) |
| 통제어 매핑 | [mappings/tta-0976_enumerations_mapping.csv](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_enumerations_mapping.csv) |
| 매핑 충돌·결정 보고서 | [reports/tta-0976_mapping_conflicts.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/tta-0976_mapping_conflicts.md) |

## M/R/O 등급 → SHACL severity

| 등급 | SHACL severity | CI 처리 |
| --- | --- | --- |
| **M** (Mandatory) | `sh:Violation` | 머지 차단 |
| **R** (Recommended) | `sh:Warning` | 경고 |
| **O** (Optional) | `sh:Info` | 정보성 |

## 사용한 어휘

| Prefix | 매핑 수 | 정합성 검증 캐시 |
| --- | --- | --- |
| dcterms | 32 | [vocabularies/cached/dct.ttl](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/vocabularies/cached/dct.ttl) |
| re3data | 28 | (RDF 미발행 — 검증 제외) |
| datacite | 19 | [datacite.ttl](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/vocabularies/cached/datacite.ttl) |
| dcat | 12 | [dcat.ttl](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/vocabularies/cached/dcat.ttl) |
| schema | (선택) | [schema.ttl](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/vocabularies/cached/schema.ttl) |
| 보조: prov, dqv, skos, vcard, foaf | — | 각각 cached/에 포함 |

## JSON-LD Context

[`2_schema/context.jsonld`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/2_schema/context.jsonld) — 91개 property 매핑이 모두 통합되어 있습니다.

## SHACL Shapes

[`2_schema/shapes.shacl.ttl`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/2_schema/shapes.shacl.ttl) — 4계층 NodeShape + 7개 보조 shape (680 라인).

핵심 Shape 7종:
- `RepositoryShape`, `CollectionShape`, `DatasetShape`, `FileShape` — 4계층 본체
- `QualityActivationShape` — Boolean Slot (Decision-Q4)
- `ProvenanceConditionalShape` — PROV 조건부 (advisory)
- 보조 6종 — controlled vocabularies, multi-language, etc.
