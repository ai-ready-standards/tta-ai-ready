# 5종 시범 표준 — AI 레디 패키지

본 디렉토리는 본 사업의 5종 시범 표준 AI 레디 패키지를 담습니다. 각 표준은 **Application Profile (AP)** 1.0.0 형식으로 발행되며, 6개 하위 디렉토리 구조를 따릅니다.

## 표준 목록

| ID | 표준번호 | 표준명 | 도메인 | 상태 |
| --- | --- | --- | --- | --- |
| [P-01](./P-01-research-data/) | TTAK.KO-10.0976 | 연구데이터 관리 및 공유를 위한 메타데이터 | 과학기술 연구 | :material-check-circle: AP 1.0.0 발행 |
| [P-02](./P-02-public-data/) | (1단계 확정 예정) | 공공데이터 메타데이터 기술 규칙 | 공공데이터 | :material-clock-outline: 8월 착수 |
| [P-03](./P-03-tagging-labeling/) | TTAK.KO-10.1343-Part2 | 비정형 데이터 태깅·라벨링 | AI 학습데이터 | :material-clock-outline: 9월 착수 |
| [P-04](./P-04-agriculture/) | TTAK.KO-10.1533 | 농업 AI 학습 데이터 메타데이터 | 농업 AI | :material-clock-outline: 9월 착수 |
| [P-05](./P-05-steel-manufacturing/) | TTAK.KO-10.1571 | 철강산업 제조업 데이터 메타데이터 | 철강 제조 | :material-clock-outline: 9월 착수 |

## 각 패키지의 6개 디렉토리 구조

P-01에 정착된 표준 구조:

```
P-XX-domain/
├── 1_document/         AP 명세 문서 (TTA-XXXX-AP.md)
├── 2_schema/           JSON-LD context + SHACL shapes
├── 3_code/             Python Pydantic 모델 + 테스트
├── 4_validator/        pySHACL 래퍼 검증 도구
├── 5_examples/         실제 도메인 JSON-LD 예시
└── 6_changelog/        버전 lock + 결정 사항
```

## 7개 구성요소 적용 (제안서 2.4절)

각 AP는 7개 구성요소를 다음 방식으로 적용합니다:

| # | 구성요소 | 구현 |
| --- | --- | --- |
| 1 | 시맨틱 (전환) | JSON-LD context — 외부 어휘 매핑 |
| 2 | 데이터 모델 (전환) | SHACL `sh:in` + cardinality |
| 3 | 신태틱 (전환) | JSON-LD `@context` |
| 4 | 운영 시맨틱 (신규) | (ML 학습 데이터 표준에서만 활성) |
| 5 | 출처·계보 (신규) | PROV-O 조건부 매핑 |
| 6 | 품질 프로파일 (신규) | DQV Boolean Activation Slot |
| 7 | 접근·사용 제약 (신규) | dcterms:accessRights / dcterms:license |

## 글로벌 어휘 정합성

| 어휘 | 사용처 | 인벤토리 |
| --- | --- | --- |
| DCMI Terms | 모든 표준 (기본) | [inventory/dcterms.csv](../inventory/dcterms.csv) |
| DCAT v3 | P-01, P-02 | [inventory/dcat-v3.csv](../inventory/dcat-v3.csv) |
| DataCite | P-01 (식별자) | [inventory/datacite.csv](../inventory/datacite.csv) |
| re3data | P-01 (Repository) | [inventory/re3data.csv](../inventory/re3data.csv) |
| Schema.org | P-01, P-02, P-03 | [inventory/schema-org.csv](../inventory/schema-org.csv) |
| MLCommons Croissant | P-03, P-04 | [inventory/croissant.csv](../inventory/croissant.csv) |
| ISO/IEC 5259 / DQV | P-04, P-05 | [inventory/dqv.csv](../inventory/dqv.csv) |
| W3C PROV-O | P-01, P-05 | [inventory/prov-o.csv](../inventory/prov-o.csv) |
| ISO 코드 | 모든 | [inventory/iso-codes.csv](../inventory/iso-codes.csv) |

전체 인벤토리(478행 통합): [inventory/master_inventory.csv](../inventory/master_inventory.csv)

## 매핑 작업 흐름

1. **Phase A**: 표준 본문 추출 → [tta-standards/0976/elements.csv](../tta-standards/0976/elements.csv)
2. **Phase A.5**: 누락 어휘 보강 → [reports/phase_a5_summary.md](../reports/phase_a5_summary.md)
3. **Phase B**: 매핑 매트릭스 작성 → [mappings/tta-0976_x_components.csv](../mappings/tta-0976_x_components.csv)
4. **Phase C**: AP 패키지 작성 → 본 디렉토리
5. **Phase D-1**: 자기 검증 → [reports/phase_d1_verification.md](../reports/phase_d1_verification.md)
