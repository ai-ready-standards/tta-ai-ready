# 보고서 — Phase A ~ D-1

본 사업의 매핑 작업은 4단계 Phase로 진행됩니다. 각 Phase 종료 시 작성된 보고서가 여기에 모아져 있습니다.

## Phase별 보고서

| Phase | 단계 | 보고서 | 라인 수 |
| --- | --- | --- | --- |
| **A.5** | 누락 어휘 4종 보강 | [phase_a5_summary.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/phase_a5_summary.md) | ~13KB |
| **B** | 매핑 매트릭스 작성 | [phase_b_summary.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/phase_b_summary.md) | ~21KB |
| **C** | AP 패키지 작성 | [phase_c_summary.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/phase_c_summary.md) | ~11KB |
| **D-1** | 자기 검증 | [phase_d1_verification.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/phase_d1_verification.md) | ~7.5KB |

## 어휘별 분석 보고서

각 외부 어휘를 본 사업 관점에서 분석한 보고서.

| 어휘 | 보고서 |
| --- | --- |
| DCAT v3 | [dcat-v3_report.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/dcat-v3_report.md) |
| MLCommons Croissant | [croissant_report.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/croissant_report.md) |
| W3C PROV-O | [prov-o_report.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/prov-o_report.md) |
| Schema.org | [schema-org_report.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/schema-org_report.md) |

## 매핑 충돌 분석

| 보고서 | 내용 |
| --- | --- |
| [tta-0976_mapping_conflicts.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/tta-0976_mapping_conflicts.md) | 459행. 카디널리티·의미·구조 충돌 정밀 추적 + 9건 결정 |
| [inventory_validation.md](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/inventory_validation.md) | 인벤토리 품질 검증 |

## Phase D-1 자기 검증 결과

| 검증 항목 | 결과 | 비고 |
| --- | --- | --- |
| pytest (test_models.py) | **11/11 PASS** | Pydantic 모델 결정 사항 9건 + 정규화 |
| Issue-001 sh:or 사전 테스트 | **4/4 PASS** | pySHACL sh:or 완전 지원 확인 |
| KISTI DataON 인스턴스 | :material-check: Conforms | Repository + Boolean Slot 활성 + 다국어 |
| NIE 환경 인스턴스 | :material-check: Conforms | Dataset + Coverage dual-purpose |
| RDA 농업 인스턴스 | :material-check: Conforms | 4계층 완전 시연 + Boolean Slot 비활성 |

→ **모든 산출물이 자기 일관성 확인** (Phase D-1 종합 결과)

## Phase D-1에서 발견·수정한 버그 6건

| # | 영역 | 버그 | 수정 |
| --- | --- | --- | --- |
| 1 | models.py | Python 3.14 PEP 649 호환 (name shadowing) | 3개 type alias 추가 |
| 2 | shapes.shacl.ttl | 다국어 필드에 `xsd:string` 강제 | `sh:or (xsd:string ‖ rdf:langString)` |
| 3 | shapes.shacl.ttl | 다국어 필드 `sh:maxCount 1` | maxCount 제거 |
| 4 | shapes.shacl.ttl | sh:in 항목 datatype 미선언 | 31개 list × 평균 7개 항목에 `^^xsd:string` |
| 5 | shapes.shacl.ttl | ProvenanceConditionalShape 강제 | sh:targetClass 주석 처리 (advisory only) |
| 6 | context.jsonld | InstitutionName predicate 충돌 | `re3data:institutionName`으로 변경 |

## 다음 단계 (D-2 이후)

| 단계 | 범위 | 우선순위 |
| --- | --- | --- |
| D-2 | ProvenanceConditionalShape SHACL-AF 재구현 | 중 |
| D-3 | 다른 TTA 표준에 본 프레임워크 적용 | 높음 (확장성 검증) |
| D-4 | 배포 준비 (git tag v1.0.0, DOI 등록) | 중 (PG606 협의 후) |
| D-5 | PG606 워크숍 (9건 피드백) | 높음 (표준 개정 트리거) |
