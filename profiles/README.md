# 프로파일 — 다축 분류 기반 적용 가이드

각 프로파일은 동일한 7-구성요소 스키마를 특정 적용 맥락에 맞게 구성한 적용 가이드입니다. 프레임워크 정의서(B-3 산출물)에서 정식으로 정의됩니다.

## 분류 체계

데이터셋의 적용 맥락은 **두 직교 축**으로 표현합니다.

| 축 | 술어 | 카디널리티 | 어휘 |
| --- | --- | --- | --- |
| **구조축 (dataType)** | `dct:type` | 1 (필수) | [`vocabularies/aird/aird-datatype.ttl`](../vocabularies/aird/aird-datatype.ttl) |
| **목적축 (intendedUse)** | `aird:intendedUse` | 0..n (다중) | [`vocabularies/aird/aird-intendeduse.ttl`](../vocabularies/aird/aird-intendeduse.ttl) |

한 데이터셋이 "표 형식 × ML 학습용 + 통계 분석용" 처럼 두 축의 다중 값을 동시에 가질 수 있습니다.

## 조건부 규칙 (요지)

| 트리거 | 활성 규칙 |
| --- | --- |
| `intendedUse` 가 `ml-training` 포함 | c4 운영 시맨틱 규칙(Croissant 호환 feature/label/split 필드) 필수 |
| `intendedUse` 가 `rag-corpus` 포함 | chunk·embedding 메타데이터 필드 권장 |
| `dct:type` = `graph` | KG 온톨로지/스키마 URI 필드 필수 |
| `dct:type` = `tabular` 이면서 `intendedUse` 가 `statistical-analysis` 포함 | 변수 정의·표본 설계 메타데이터 권장 |

## 프로파일 구성

목적축 값별로 조건부 shape 정의 모음을 둡니다. 구조축 특수 규칙은 코어 스펙 본문에 흡수합니다.

| 프로파일 | 트리거 (목적축 값) | 핵심 어휘 |
| --- | --- | --- |
| [`ml/`](./ml/) | `ml-training` | Croissant 1.0, DCAT v3 |
| [`rag/`](./rag/) | `rag-corpus` | DCAT v3, schema.org |
| [`kg/`](./kg/) | `knowledge-base` | OWL, SKOS, PROV-O |
| [`statistics/`](./statistics/) | `statistical-analysis` | DDI, SDMX, ISO 5259 |

> **이전 버전 대비 변경**: 직전 README는 ML/RAG/KG/통계를 모두 "목적별 프로파일"로 단일 축에 분류했으나, KG·통계는 본질적으로 데이터 구조 차원이고 ML·RAG는 목적 차원으로 카테고리가 혼합되어 있었습니다. 본 개정으로 두 축이 분리되었습니다 (관련 PR 본문 참조).
