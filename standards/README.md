# 파일럿 5종 표준 (PG606 소관)

본 사업에서 AI 레디화하는 5종 파일럿 표준입니다. 모두 PG606 소관 메타데이터 표준으로 통일하여 TC 간 조율 부담을 최소화하면서 도메인 다양성을 확보합니다.

| ID | 도메인 | 대상 표준 | 국제 연계 | 상태 |
| --- | --- | --- | --- | --- |
| [P-01](./P-01-research-data/) | 과학기술 연구 | 연구데이터 관리 및 공유를 위한 메타데이터 (2017) | DataCite, DCAT v3 | 🚧 착수 예정 |
| [P-02](./P-02-public-data/) | 공공데이터 | 공공데이터 메타데이터 기술 규칙 | DCAT v3, CC | 🚧 착수 예정 |
| [P-03](./P-03-tagging-labeling/) | AI 학습데이터 | 비정형 데이터 태깅·라벨링 (TTAK.KO-10.1343-Part2) | Croissant RAI, DUO | 🚧 착수 예정 |
| [P-04](./P-04-agriculture/) | 농업 AI | 농업 AI 학습 데이터 플랫폼 메타데이터 (TTAK.KO-10.1533, 2024) | Croissant, ISO 5259 | 🚧 착수 예정 |
| [P-05](./P-05-steel-manufacturing/) | 철강 제조 | 철강산업 제조업 데이터 공유 메타데이터 (TTAK.KO-10.1571, 2025) | IEC 62264, PROV-O | 🚧 착수 예정 |

## 각 파일럿의 표준 디렉토리 구조

```
P-XX-<domain>/
├── README.md          # 표준 개요·범위·국제 연계
├── schema/            # JSON-LD 1.1 스키마 (@context, 클래스/속성 정의)
├── shapes/            # SHACL 검증 규칙 (.ttl)
└── examples/          # 실행 가능한 예시 데이터셋 (3종 이상)
```

## 7개 스키마 구성요소

각 파일럿은 다음 7개 구성요소를 갖추도록 설계됩니다 (전환 3 + 신규 4).

전환 3개:
1. 의미 정의 (semantic definitions) — 기존 표준 자산
2. 구조 정의 (structural schema) — JSON-LD 변환
3. 코드값 정의 (controlled vocabularies) — URI 기반

신규 4개:
4. 검증 규칙 (SHACL shapes)
5. 출처·계보 (PROV-O)
6. 사용 제약 (DUO/CC URI)
7. 품질 프로파일 (ISO 5259 차원)

자세한 정의는 [`docs/framework/`](../docs/framework/) 참조.
