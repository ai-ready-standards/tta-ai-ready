# [Infra] 프로파일 분류를 다축(구조×목적)으로 정정 + AI Ready Data 자체 어휘 도입

> **라벨**: `enhancement`, `vocabulary`, `framework`
> **유형**: 어휘/인프라 개선 (특정 P-XX 표준이 아닌 프레임워크 운영 어휘)
> **연동 PR**: 파일럿 PR-001 (본 이슈와 동시 등록)

## 1. 문제

현재 [`profiles/README.md`](https://github.com/ai-ready-standards/tta-ai-ready/blob/feat/pilot-pr-001-multiaxis/profiles/README.md) 는 ML / RAG / KG / 통계 4종을 모두 "목적별 프로파일"로 분류하고 있습니다. 그러나 이 4종은 카테고리가 혼합되어 있습니다.

| 항목 | 본질 | 현 분류 |
| --- | --- | --- |
| ML | 사용 **목적** (학습 파이프라인) | "목적별" ✅ |
| RAG | 사용 **목적** (검색 증강 생성) | "목적별" ✅ |
| KG | 데이터 **구조** (그래프) | "목적별" ❌ |
| 통계 | 데이터 **구조** (표 형식) + 목적 | "목적별" ❌ |

이 혼합은 다음 문제를 야기합니다:

- 한 데이터셋이 "표 형식 × ML 학습용 × 통계 분석용" 처럼 다중 분류를 가질 때 단일 축에 강제로 끼워맞춰야 함
- 새 데이터 구조(예: 시계열, 멀티모달)를 추가할 때 "목적별 프로파일" 명목을 위반
- 외부 표준(DCAT, schema.org)이 이미 두 축을 분리해 다루므로 매핑 시 어색함

## 2. 제안

### 2.1 다축 분리

데이터셋 적용 맥락을 두 직교 슬롯으로 표현:

| 축 | 술어 | 카디널리티 | 어휘 |
| --- | --- | --- | --- |
| **구조축** | `dct:type` | 1 (필수) | aird-datatype (신규) |
| **목적축** | `aird:intendedUse` | 0..n (다중) | aird-intendeduse (신규) |

### 2.2 자체 어휘 신설 (SKOS Concept Scheme)

외부 어휘로 ML/RAG/KG/통계 등을 1:1 매칭할 적합 어휘가 부재하므로, AI Ready Data 자체 어휘를 신설하고 외부 표준에는 SKOS 매핑 술어로 정합성을 명시.

- `vocabularies/aird/aird-datatype.ttl` — 6개 Concept (tabular, graph, text, image, multimodal, time-series)
- `vocabularies/aird/aird-intendeduse.ttl` — 5개 Concept (ml-training, rag-corpus, knowledge-base, statistical-analysis, general)

### 2.3 외부 매핑

- `mappings/aird-datatype-to-schemaorg.ttl` — schema.org 매핑 (1차)
- `mappings/aird-datatype-to-croissant.ttl` — Croissant RecordSet 매핑 (후속)
- `mappings/aird-intendeduse-to-*.ttl` — 향후 외부 표준 발견 시 추가

### 2.4 조건부 규칙 매핑

기존 단일 축 가정의 4개 프로파일은 목적축 값과 1:1 대응:

| 프로파일 | 트리거 |
| --- | --- |
| `profiles/ml/` | `intendedUse ⊇ {ml-training}` |
| `profiles/rag/` | `intendedUse ⊇ {rag-corpus}` |
| `profiles/kg/` | `dct:type = graph` (구조축으로 이동) |
| `profiles/statistics/` | `intendedUse ⊇ {statistical-analysis}` 또는 `dct:type = tabular` |

## 3. 영향 범위 (연동 PR-001이 전달하는 변경)

- 신규: `vocabularies/aird/` 디렉토리 + 어휘 파일 2종 + README
- 신규: `mappings/aird-datatype-to-schemaorg.ttl`
- 수정: `vocabularies/README.md` (외부 캐시 + 자체 어휘 두 종 표기)
- 수정: `profiles/README.md` (다축 분류 설명)

## 4. 7-구성요소 관계

본 변경은 **c1 시맨틱** (어휘 신설) 과 **c2 데이터 모델** (분류 슬롯 구조) 에 해당. c4-c7 외부 표준 매핑에는 영향 없음.

## 5. IPR 확약

- [x] 제안자가 본 자료의 권리를 보유하며 Apache License 2.0 적용에 동의
- [x] 제3자 권리 침해 없음
- [x] 외부 표준 매핑은 매핑 술어(skos:closeMatch 등)로 표현하며 외부 표준 본문은 인용·캐시만 함

## 6. 검토 요청 대상 (CODEOWNERS)

| 영역 | 변경 | 필요 승인 |
| --- | --- | --- |
| `/profiles/` | README 수정 | @tta-pm @tta-standards-lead @tta-tech-lead |
| `/vocabularies/` | 신규 어휘 + README 수정 | @tta-pm (영역 owner 미명시 → 기본) |
| `/mappings/` | 신규 매핑 파일 | (CODEOWNERS 미정 → 기본 @tta-pm, **CODEOWNERS 갱신 후속 과제**) |

## 7. 후속 과제 (본 PR 범위 외)

1. **이슈 템플릿 신설**: 어휘/인프라 변경용 (`vocabulary-or-infra-change.md`)
2. **CODEOWNERS 갱신**: `/mappings/`, `/vocabularies/aird/` 영역 명시
3. **Croissant 매핑**: `aird-datatype-to-croissant.ttl` 작성
4. **이슈 템플릿 본문 수정**: `proposal-new-standard.md` 의 "5. 적용 프로파일 후보" 항목을 다축 체크박스로 갱신
5. **URI 정책 확정**: `aird-*` 어휘 베이스 URI 정식화 (현재는 사이트 URL 가정)

## 8. PG606 절차상 위치 — 본 이슈가 노출하는 거버넌스 갭

본 변경은 표준 제·개정 11단계 중 어느 단계에도 정확히 매핑되지 않으며, GitHub-운영 가능성 검증을 위한 **파일럿 PR-001** 의 시연 사례입니다.

기존 이슈 템플릿 2종(`proposal-new-standard.md`, `standard-task.md`) 은 모두 표준 단위(P-XX) 변경을 가정하므로, 본 이슈처럼 어휘·매핑·CODEOWNERS·CI 등 운영 인프라를 다루는 변경에 정확히 부합하는 템플릿이 없습니다. 이 자체가 "어휘/인프라 변경" 전용 템플릿 신설의 근거 사례입니다 (§7 후속 과제 1번).

상세 단계 매핑·갭 분석은 [`WORKFLOW_LOG.md`](./WORKFLOW_LOG.md) 참조.
