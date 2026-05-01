# P-01 — 연구데이터 메타데이터 (AI 레디 패키지)

## 대상 표준

- **표준번호**: TTAK.KO-10.0976
- **표준명**: 연구데이터 관리 및 공유를 위한 메타데이터
- **제정**: 2017-03-30 (TTA · PG606)
- **본 수행사 직접 개발 표준** — 본 사업의 첫 번째 파일럿이자 가장 이상적인 조건의 파일럿

## 표준 구조

본 표준은 **컬렉션 → 데이터셋 → 파일** 3계층의 자원 관리 단위와 이를 보관·서비스하는 **리포지토리** 1단위, 총 4종 클래스를 정의한다 (요소 79개, 통제어 14종).

| 클래스 | 표준 ID 범위 | 요소 수 | M/R/O |
| --- | --- | --- | --- |
| Collection (컬렉션) | C1 ~ C12 | 18 | M:5 / R:8 / O:5 |
| Dataset (데이터셋) | D1 ~ D15 | 22 | M:9 / R:8 / O:5 |
| File (파일) | F1 ~ F19 | 27 | M:8 / R:8 / O:11 |
| Repository (리포지토리) | R1 ~ R21 | 24 | M:16 / R:3 / O:5 |

상세 매핑은 [`MAPPINGS.md`](./MAPPINGS.md), 7개 구성요소 모델은 [`PROFILE.md`](./PROFILE.md) 참조.

## 패키지 구성

```
P-01-research-data/
├── README.md         (본 문서)
├── PROFILE.md        7개 구성요소 + AI 레디화 설계 원칙
├── MAPPINGS.md       TTA 요소 → JSON-LD/SHACL 매핑표
├── schema/
│   └── context.jsonld    JSON-LD 1.1 @context (어휘 매핑)
├── shapes/
│   ├── collection.ttl    컬렉션 SHACL (C1~C12)
│   ├── dataset.ttl       데이터셋 SHACL (D1~D15)
│   ├── file.ttl          파일 SHACL (F1~F19)
│   └── repository.ttl    리포지토리 SHACL (R1~R21)
└── examples/
    ├── README.md
    ├── valid/            유효 예시 4종
    └── invalid/          음성 테스트 1종
```

## 국제 어휘 매핑

| TTA 클래스 | DCAT v3 | DataCite | Dublin Core |
| --- | --- | --- | --- |
| Collection | `dcat:Catalog` | — | `dcmitype:Collection` |
| Dataset | `dcat:Dataset` | DataCite Schema 4.5 | `dcmitype:Dataset` |
| File | `dcat:Distribution` | — | — |
| Repository | `dcat:DataService` | — | — |

## 빠른 검증

```bash
# 의존성 설치 (venv 권장)
pip install pyshacl rdflib

# 단일 파일 검증
python -m tta_validator standards/P-01-research-data/examples/valid/dataset-minimal.jsonld

# 전체 예시 일괄 검증
python -m tta_validator standards/P-01-research-data/examples/
```

## 7개 구성요소 적용 현황 (Phase A 기준)

| # | 구성요소 | Phase A | Phase B (TODO) |
| --- | --- | --- | --- |
| 1 | 의미 정의 (semantic) | ✅ TTA 표준 본문 직접 매핑 | — |
| 2 | 구조 정의 (JSON-LD) | ✅ context.jsonld | TTL/RDF 직렬화 형식 추가 |
| 3 | 코드값 정의 (controlled vocabularies) | ✅ SHACL `sh:in` 인라인 | SKOS Concept Scheme 분리 |
| 4 | 검증 규칙 (SHACL) | ✅ M/R/O 등급별 4개 shape | 음성 테스트 케이스 확장 |
| 5 | 출처·계보 (PROV-O) | 🟡 dataset-complete 예시에서 시연 | 파일럿 데이터셋 PROV 시나리오 |
| 6 | 사용 제약 (DUO/CC) | 🟡 dct:license URI + DUO 어휘 컨텍스트 | DUO permission code 매핑표 |
| 7 | 품질 프로파일 (ISO 5259) | ⏳ Phase B | 완전성·적시성·정확성 측정 정의 |

## WBS 일정

C-5 (수행계획서 2.3절). 정식 착수는 2026년 8월. 본 골격은 사전 탐색용 PR이다.
