# PR: 프로파일 다축 분류 도입 + AI Ready Data 자체 어휘 (1차)

> 본 PR 본문은 `.github/PULL_REQUEST_TEMPLATE.md` 형식을 따릅니다.

## 요약

`profiles/` 의 단일 축 분류(ML/RAG/KG/통계)를 **구조축(`dct:type`) × 목적축(`aird:intendedUse`)** 다축 분류로 정정하고, 이를 표현하는 AI Ready Data 자체 SKOS 어휘 2종과 schema.org 외부 매핑 1건을 신설합니다.

## 관련 WBS / 이슈

- 관련 이슈: Closes #TBD (연동 이슈는 [`ISSUE.md`](./ISSUE.md) 참조)
- WBS: 정식 코드 미배정 — 본 PR은 "트랙 A 운영체계 파일럿 PR-001"로 식별 (WBS 코드 부여 절차 자체가 갭으로 식별됨, WORKFLOW_LOG §2 갭 F)
- 트랙 B 영향: 프레임워크 정의서 §4 (목적별 프로파일) 후속 갱신 필요

## 변경 파일

| 유형 | 파일 |
| --- | --- |
| 신규 | `vocabularies/aird/aird-datatype.ttl` |
| 신규 | `vocabularies/aird/aird-intendeduse.ttl` |
| 신규 | `vocabularies/aird/README.md` |
| 신규 | `mappings/aird-datatype-to-schemaorg.ttl` |
| 수정 | `vocabularies/README.md` |
| 수정 | `profiles/README.md` |

## 4계층 품질 보증 체크리스트

- [x] **L1 작성자 셀프 체크**: SKOS 문법 수동 검증, 외부 어휘 매핑 표 일관성 확인
- [ ] **L2 PM 검토**: 리뷰 대기 (@tta-pm)
- [ ] **L3 외부 전문가 검토**: 본 PR은 어휘 신설을 포함하므로 동료 검토 1인 이상 권장 (메타데이터 표준 전문가)
- [ ] **L4 자동 검증**: CI 통과 대기 (RDF·SHACL·예시 로딩)

## 산출물 유형별 정량 기준

해당 항목 체크:

- [ ] JSON-LD 스키마: 본 PR 변경 없음 (Turtle만 추가)
- [x] **SKOS Turtle 파일**: 문법 오류 0건 — 수동 검증 완료, CI에서 재확인 필요
- [ ] SHACL 검증 파일: 본 PR 변경 없음 (다음 PR에서 조건부 shape 추가 예정)
- [ ] Python 코드: 본 PR 변경 없음
- [x] **외부 어휘 매핑**: schema.org 매핑은 100% Concept 커버 (6/6), Croissant 매핑은 후속 PR

## 보안 확인

- [x] 발주처 미공개 자료, 인증 키, 내부망 전용 자료가 포함되지 않음
- [x] 외부 공개 가능한 산출물만 포함됨 — 본 PR은 공개 SKOS 어휘 정의

## 리뷰 요청 대상

CODEOWNERS 자동 지정 외 추가 검토 권장:

- **메타데이터 표준 전문가 1인**: SKOS 매핑 술어 선택(closeMatch vs relatedMatch)의 적정성
- **schema.org 활용 경험자 1인**: 매핑 후보 선정의 적정성

## 주의 사항 (검토자용)

1. **URI 베이스는 잠정값**: `https://ai-ready-standards.github.io/tta-ai-ready/vocab/...` — 정식 URI 정책 확정 후 일괄 갱신 필요. 본 PR은 베이스 결정 사안이 아님.
2. **이슈 템플릿 미적합**: 본 PR 관련 이슈는 기존 템플릿 2종(`proposal-new-standard.md`, `standard-task.md`) 어디에도 정확히 부합하지 않음. 후속 과제로 어휘/인프라 변경용 템플릿 신설 권고.
3. **CODEOWNERS 보강 필요**: `/mappings/`, `/vocabularies/aird/` 영역 owner가 명시되지 않아 기본 owner(@tta-pm) 단독 승인이 됨. 후속 PR에서 보강 권고.
4. **Croissant 매핑은 후속**: `aird-datatype-to-croissant.ttl` 은 별도 PR. ML 프로파일이 Croissant를 핵심 참조 모델로 채택했으므로 우선 순위 높음.

## 본 PR이 시연하는 PG606 단계

본 PR은 표준 제·개정 11단계 중 **⑦ 초안 작성 ~ ⑩ 심의** 의 GitHub 구현을 시연합니다 (제안 ①~⑥은 ISSUE.md, 공고 ⑪은 머지 후 자동 배포로 시연). 단계별 매핑 상세는 `WORKFLOW_LOG.md` 참조.
