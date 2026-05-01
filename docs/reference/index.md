# 스키마 레퍼런스

본 섹션은 P-01(TTAK.KO-10.0976)의 79개 메타데이터 요소와 14종 통제어의 상세 정의입니다. 다른 4종 표준(P-02~P-05)도 정식 착수 후 동일한 형태로 추가됩니다.

## 4개 클래스

| 클래스 | 요소 ID | 요소 수 | 매핑 |
| --- | --- | --- | --- |
| [Collection](collection.md) | C1 ~ C12 | 18 | `dcat:Catalog` |
| [Dataset](dataset.md) | D1 ~ D15 | 22 | `dcat:Dataset` |
| [File](file.md) | F1 ~ F19 | 27 | `dcat:Distribution` |
| [Repository](repository.md) | R1 ~ R21 | 24 | `dcat:DataService` |

## M/R/O 등급

| 등급 | SHACL severity | 의미 |
| --- | --- | --- |
| **M** (Mandatory) | `sh:Violation` | 필수. CI 실패 |
| **R** (Recommended) | `sh:Warning` | 권고. 경고 표시 |
| **O** (Optional) | `sh:Info` | 선택. 정보성 |

## 요소 유형

| 유형 | 의미 |
| --- | --- |
| Property | 일반적인 값을 갖는 요소 |
| SEP (Syntax Encoding Property) | 일정한 형식을 갖는 요소 (예: ISO 8601 날짜) |
| Class | 기술 대상 자원을 의미하는 요소 |
| CVP (Controlled Vocabulary Property) | 통제어 중 하나를 값으로 갖는 요소 |

## 통제어

[14종 통제어 페이지](vocabularies.md)에서 모든 허용 값을 확인할 수 있습니다.

## JSON-LD Context

[`schema/context.jsonld`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/schema/context.jsonld)에서 모든 매핑이 통합되어 있습니다.
