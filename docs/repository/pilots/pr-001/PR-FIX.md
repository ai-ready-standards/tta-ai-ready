# PR-001-fix: schema.org 매핑 술어 보정 (broadMatch / narrowMatch)

> 본 PR-FIX 본문은 `.github/PULL_REQUEST_TEMPLATE.md` 형식을 따릅니다.
> **선행 PR**: PR-001 (이미 머지됨, 시뮬레이션상)
> **변경 규모**: 단일 파일 5라인

## 요약

PR-001에서 도입된 `aird-datatype-to-schemaorg.ttl` 의 매핑 술어를 SKOS 의미론에 맞게 보정합니다. `closeMatch` 일부를 `broadMatch` 로, `relatedMatch` 일부를 `narrowMatch` 로 교체합니다.

## 관련 WBS / 이슈

- 선행 PR: PR-001 ([`PR.md`](./PR.md))
- 관련 이슈: 본 보정은 PR-001 머지 직후 발견된 SKOS 의미론 오류로, 별도 신규 이슈 없이 핫픽스 형태로 등록 (단, 이슈 부재 자체가 갭 — WORKFLOW_LOG §2 갭 G 참조)
- WBS: PR-001 후속 보정 (정식 코드 미배정)

## 변경 파일

| 유형 | 파일 |
| --- | --- |
| 수정 | `mappings/aird-datatype-to-schemaorg.ttl` (5건 술어 교체) |

## 변경 상세

| Concept → 외부 | 변경 전 | 변경 후 | 근거 |
| --- | --- | --- | --- |
| `tabular` → `schema:Dataset` | `closeMatch` | `broadMatch` | Dataset은 모든 데이터셋의 상위 범주 |
| `graph` → `schema:Dataset` | `closeMatch` | `broadMatch` | 동상 |
| `text` → `schema:Article` | `relatedMatch` | `narrowMatch` | Article은 Text의 한 구체 형태 (Article ⊂ Text) |
| `time-series` → `schema:Dataset` | `closeMatch` | `broadMatch` | 동상 |
| `time-series` → `schema:Observation` | `relatedMatch` | `narrowMatch` | 단일 Observation은 시계열의 한 점 |

변경 없음:
- `image` → `schema:ImageObject` (closeMatch 유지 — 정확한 개념 일치)
- `multimodal` → `schema:MediaObject` (relatedMatch 유지 — 합성 관계는 hierarchical 매핑 불가)

## 4계층 품질 보증 체크리스트

- [x] **L1 작성자 셀프 체크**: SKOS 매핑 술어 정의(W3C SKOS Reference §10) 재확인 후 보정
- [ ] **L2 PM 검토**: 리뷰 대기 (@tta-pm)
- [ ] **L3 외부 전문가 검토**: 매핑 보정은 작은 변경이지만 SKOS 의미론 영역이므로 1인 검토 권장
- [ ] **L4 자동 검증**: CI 통과 대기

## 산출물 유형별 정량 기준

- [x] **SKOS Turtle 파일**: 문법 오류 0건, 매핑 술어 사용 W3C SKOS Reference 정합

## 보안 확인

- [x] 발주처 미공개 자료, 인증 키, 내부망 전용 자료 미포함

## 본 PR이 시연하는 거버넌스 갭

PR-001 머지 후 별도 PR로 분리하여 보정한 행위 자체가 다음 4가지 갭을 노출합니다 (WORKFLOW_LOG §2 갭 G 참조):

① **소규모 변경의 절차 부담** — 1라인 수정도 11단계 동일 적용?
② **PR 간 의존 관계 표현** — `Refs PR-001`, milestone, linked PRs 정책 부재
③ **회의 정족수의 한계 사례** — 술어 1건 보정도 정족수 필요?
④ **변경 이력 audit trail** — 별도 PR이 단일 PR 내 commit history보다 가독성·접근성 우수
