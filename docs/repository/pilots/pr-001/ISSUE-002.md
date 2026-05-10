# [Infra] glossary ⑤ 섹션 통합표 재구성 + schema.org 추가

> **라벨**: `documentation`, `vocabulary`, `framework`
> **유형**: 용어집 정정 (PR-001이 노출한 갭 H 보정)
> **연동 PR**: PR-002 (본 이슈와 동시 등록)

## 1. 문제

PR-001이 신규 외부 어휘로 schema.org를 도입(`mappings/aird-datatype-to-schemaorg.ttl`)했으나 `docs/glossary.md` ⑤ 섹션이 동시 갱신되지 않아 다음 두 문제가 노출됨:

- **schema.org 누락**: 어떤 하위표에도 등재되지 않음
- **분류 혼동**: ⑤ 섹션이 4개 하위표로 분리되어 있고 첫 표가 "W3C 표준 어휘" 라벨 — 외부 어휘를 찾을 때 W3C 발행이 아닌 어휘(Croissant, schema.org 등)가 어디에 위치하는지 직관적이지 않음. 검토 중 "Croissant이 빠져있고 schema.org도 빠져있는 것 같다"는 오인 보고가 실제 발생

## 2. 제안

### 2.1 표 통합

⑤ 섹션의 4개 하위표 중 어휘·표준 두 표(표 1 "W3C 표준 어휘" + 표 2 "메타데이터 표준 (외부 기관)")를 단일 통합표로 합치고 **발행 기관** 컬럼을 신설. W3C 발행 여부는 컬럼으로 식별. 표 3(형식·언어), 표 4(표준화 기관)은 어휘가 아니므로 분리 유지.

### 2.2 schema.org 추가

통합표에 schema.org 행을 추가. 발행 기관: schema.org Community Group (Google·Microsoft·Yahoo·Yandex 공동 출범).

### 2.3 표준화 기관 표 보강

기존 표 4(표준화 기관)에 통합표에서 등장하는 발행 기관 중 누락된 5개 추가: schema.org Community Group, DCMI, DDI Alliance, SDMX Consortium, EBI/EBISPOT.

## 3. 영향 범위 (연동 PR-002가 전달하는 변경)

- 수정: `docs/glossary.md` (⑤ 섹션 — 표 1·2 통합 + schema.org 추가 + 표 4 보강)

## 4. 7-구성요소 관계

본 변경은 **c1 시맨틱**(외부 어휘 인벤토리) 의 보조 자료 정정. 시맨틱 본문 변경 아님.

## 5. IPR 확약

- [x] 발행 기관 정보는 공개 사실 인용
- [x] 외부 어휘 본문은 인용·캐시만 함

## 6. 검토 요청 대상 (CODEOWNERS)

| 영역 | 변경 | 필요 승인 |
| --- | --- | --- |
| `/docs/` | glossary 수정 | (영역 owner 미명시 → 기본 @tta-pm) — **갭 D 관련** |

## 7. 후속 과제 (본 PR 범위 외)

1. **CI 자동 검증 신설**: `mappings/`·`vocabularies/cached/MANIFEST.json` 의 prefix 사용 어휘가 glossary에 모두 등재되었는지 검증하는 도구 (`tta-verify-glossary` 또는 기존 `tta-verify-mappings` 확장)
2. **PR 템플릿 체크리스트 갱신**: "신규 외부 어휘 도입 시 glossary ⑤ 섹션 갱신 필수" 항목 추가
3. **CONTRIBUTING.md 갱신**: 외부 어휘 신규 채택 거버넌스 명시

## 8. PG606 절차상 위치

본 변경은 PR-001 머지 후 발견된 **용어집 동기화 누락**(갭 H) 의 시뮬레이션 후속 처리입니다. 갭 H의 본질은 "외부 어휘 도입과 용어집 갱신이 절차상 강제 연동되어 있지 않음"이며, 본 PR-002는 갭 H 보정의 1차 구현입니다. 거버넌스 규칙 자체의 정비(§7 후속 과제)는 추가 PR 또는 표준화 지침 개정안에서 다룹니다.

상세 단계 매핑·갭 분석은 [`WORKFLOW_LOG.md`](./WORKFLOW_LOG.md) §2 갭 H 참조.
