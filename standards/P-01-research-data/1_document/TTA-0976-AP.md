# TTAK.KO-10.0976 AI-Ready Application Profile

- **표준**: TTAK.KO-10.0976 — 연구데이터 관리·공유를 위한 메타데이터
- **AP 버전**: 1.0.0
- **AP 발행일**: 2026-05-04
- **TTA 표준 발행**: 2017.03.30 (제1판), TTA PG606
- **TTA-AP namespace**: `https://standard.tta.or.kr/ai-ready/profile#` (`ttaap:`)
- **TTA 원본 namespace**: `https://standard.tta.or.kr/0976#` (`tta0976:`)

---

## 1. 개요

본 Application Profile (AP)은 한국정보통신기술협회(TTA) 표준 TTAK.KO-10.0976 "연구데이터 관리·공유를 위한 메타데이터" (2017)를 글로벌 표준 어휘에 매핑하여 **AI 시스템이 직접 임포트·검증·활용 가능한 패키지** 형태로 제공한다.

### 1.1 본 AP의 목적

1. **TTA 표준의 의미를 글로벌 어휘로 표현** — DCMI/DataCite/re3data/DCAT/Schema.org 5종 어휘 통합
2. **기계 판독 가능 스키마 제공** — JSON-LD context + SHACL shapes
3. **즉시 실행 가능한 코드** — Python Pydantic 모델 + pySHACL 검증
4. **국제 호환성** — 글로벌 데이터 카탈로그(re3data/DataCite)에 등록 가능한 형태

### 1.2 본 AP의 6 패키지 산출물

```
D:\ARD\packages\tta-0976\
├── 1_document\         ← 본 문서
├── 2_schema\
│   ├── context.jsonld  (170 lines, 91개 property 매핑)
│   └── shapes.shacl.ttl (679 lines, 4계층 NodeShapes + 7개 보조 shape)
├── 3_code\             (Python Pydantic 패키지)
├── 4_validator\        (pySHACL 래퍼 CLI)
├── 5_examples\         (3개 도메인 JSON-LD 인스턴스)
└── 6_changelog\
    └── CHANGELOG.md    (217 lines, 5종 어휘 버전 lock + 9개 결정)
```

---

## 2. 7개 구성요소 적용 결과

본 AP는 제안서의 "7개 스키마 구성요소 + 6개 패키지 요소" 프레임워크에 따라 작성되었다.

| # | 구성요소 | 본 AP 적용 결과 | 적용 패키지 |
|---|---|---|---|
| 1 | **시맨틱** (전환) | 91개 property를 5종 어휘(dcterms/datacite/re3data/dcat/schema)에 매핑 | 2_schema/context.jsonld |
| 2 | **데이터 모델** (전환) | M/R/O 카디널리티 → SHACL sh:minCount/maxCount + sh:in 통제어 제약 ~250개 | 2_schema/shapes.shacl.ttl |
| 3 | **신태틱** (전환) | JSON-LD @context로 표현 형식 + 의미 동시 처리 | 2_schema/context.jsonld |
| 4 | **운영 시맨틱** (신규) | **NA (general research data standard, not ML-specific)** — Decision-3 | — |
| 5 | **출처·계보** (신규) | Date+DateType → prov:generatedAtTime/wasRevisionOf/invalidatedAtTime 조건부 매핑 (Decision-Q3/Q7) | 2_schema/shapes.shacl.ttl (ProvenanceConditionalShape) |
| 6 | **품질 프로파일** (신규) | **★ Boolean Activation Slot** — re3data:qualityManagement="yes" 시 dqv:hasQualityMetadata 활성 (Decision-Q4) | 2_schema/shapes.shacl.ttl (QualityActivationShape) |
| 7 | **접근·사용 제약** (신규) | AccessType/AccessRestriction/Rights/License 13건 매핑 + dcterms:accessRights/license | 2_schema/shapes.shacl.ttl (각 계층 c7 영역) |

→ **본 표준은 일반 연구데이터 표준이라 #4 (운영 시맨틱)는 NA**. ML 학습 데이터 표준 (예: 차후 TTA-XXXX) 작업 시 #4 활성화.

---

## 3. 4계층 구조 매핑

| TTA 4계층 | TTA inventory_id 범위 | 항목 수 | DCMI/DCAT 매핑 | 핵심 ttaap: 클래스 |
|---|---|---|---|---|
| **Repository** | TTA-0976-001 ~ 026 | 26 | dcat:Catalog (loose, 4계층 차이) | `ttaap:Repository` |
| **Collection** | TTA-0976-101 ~ 118 | 18 | dctype:Collection | `dctype:Collection` |
| **Dataset** | TTA-0976-201 ~ 222 | 22 | dcat:Dataset (equivalentClass) | `dcat:Dataset` |
| **File** | TTA-0976-301 ~ 327 | 27 | dcat:Distribution | `dcat:Distribution` |
| **합계** | — | **93** | — | — |

### 3.1 4계층 구조와 DCAT 3계층의 매핑

DCAT v3는 Catalog/Dataset/Distribution 3계층. TTA의 4계층은 한국 연구데이터 생태계의 특수성(부서/연구과제 단위 그룹화) 반영.

```
TTA 4계층:        Repository ─ Collection ─ Dataset ─ File
                      │            │           │         │
                      ↓            ↓           ↓         ↓
DCAT 3계층:       Catalog ─ ─ ─ (없음) ─ ─ ─ Dataset ─ Distribution
                  (loose)                  (equiv)   (loose)
```

본 AP는 다음 매핑으로 4↔3계층 격차 해소:
- `ttaap:Repository` ⊆ `dcat:Catalog` (subClassOf)
- `ttaap:hasCollection` 관계로 Collection 계층 명시
- `ttaap:Collection` = `dctype:Collection` (DCMI Type)
- `ttaap:Dataset` = `dcat:Dataset` (equivalentClass)
- `ttaap:File` ≈ `dcat:Distribution` (loose, File은 raw data, Distribution은 access form)

---

## 4. 통제어 (Controlled Vocabularies)

본 표준은 24개 통제어 카테고리를 정의 (총 117개 enum 값).

| 카테고리 | 값 개수 | 출처 | sh:in 적용 위치 |
|---|---|---|---|
| ContributorType | 22 | DataCite contributorType | DatasetShape, FileShape |
| IdentifierType | 19+1(UCI) | DataCite relatedIdentifierType + 한국 UCI | 4개 계층 IdentifierType |
| FileType | 11+1('other') | DCMI Type Vocabulary + TTA 'other' | FileShape Type |
| DatasetDateType | 9 | DataCite dateType | Dataset/File DateType |
| AccessRestriction | 6 | re3data dataAccessRestriction | 3개 계층 |
| RepositoryType | 6 | re3data type | RepositoryShape |
| ResponsibilityType | 6 | re3data responsibilityType | RepositoryShape |
| AccessType | 4 | re3data dataAccessType | 4개 계층 |
| FileSizeUnitType | 4 | (Rule 3) schema:unitText | FileShape |
| TitleType | 4 | DataCite titleType | 4개 계층 |
| CollectionDateType | 3 | (subset of DataCite) | CollectionShape |
| DatabaseAccessType | 3 | re3data databaseAccessType | RepositoryShape |
| DataUploadType | 3 | re3data dataUploadType | RepositoryShape |
| EnhancedPublication | 3 | re3data | RepositoryShape |
| QualityManagement | 3 | re3data + ★ Boolean Slot trigger | RepositoryShape |
| Versioning | 3 | re3data | RepositoryShape |
| (5 aliases + 1 SubjectScheme + 2 open vocabs) | — | — | — |

**완전 매핑 비율**: 115/117 = 98.3% (none 2건은 UCI 한국 표준 + 'other' FileType).

---

## 5. 핵심 매핑 결정 9건

| Decision | 항목 | 결정 |
|---|---|---|
| 001 | Repository tta_iri | 임시 IRI 부여, TTA 공식 발급 시 갱신 |
| 002 | InstitutionCountry | [OVERRIDE] alpha-3 → alpha-2 (DCAT v3 호환) |
| 003 | D2.1 IdentifierType | [CONFLICT] 본문 M / 부록 O — 부록 우선 |
| 004 | D5 Publisher | [CONFLICT] 본문 M / 부록 R — 부록 우선 |
| 005 | D14 AccessType | [CHECK] PDF 손상 — O 추정 |
| Q3 | PROV-O 보조 매핑 | Date+DateType 조건부 활성 |
| Q4 | DQV 활성화 | ★ Boolean Activation Slot (QualityManagement="yes") |
| Q5 | 통제어 매핑 단위 | 값 단위 매핑 (117 enum 모두) |
| Q7 | Repository PROV | Decision-Q3와 일관 적용 |

전체 결정 사항과 근거: `6_changelog/CHANGELOG.md` 또는 `D:\ARD\reports\tta-0976_mapping_conflicts.md` 참조.

---

## 6. 사용 가이드

### 6.1 JSON-LD 인스턴스 작성

`2_schema/context.jsonld`를 참조하여 TTA-AP 형식 데이터 작성:

```json
{
  "@context": "https://standard.tta.or.kr/ai-ready/profile/context.jsonld",
  "@type": "Repository",
  "@id": "https://kisti.re.kr/repository/dataon",
  "RepositoryUrl": "https://dataon.kisti.re.kr",
  "RepositoryIdentifier": "10.5072/REP-001",
  "RepositoryIdentifierType": "DOI",
  "RepositoryName": {"ko": "DataON", "en": "DataON"},
  "RepositoryType": "institutional",
  "RepositoryLanguage": "kor",
  "InstitutionCountry": "KR",
  "DatabaseAccessType": "open",
  "DataAccessType": "open",
  "DataLicenseName": "Creative Commons Attribution 4.0 International",
  "DataLicenseUrl": "http://creativecommons.org/licenses/by/4.0/",
  "DataUpload": "restricted",
  "Versioning": "yes",
  "EnhancedPublication": "no",
  "QualityManagement": "yes",
  "hasQualityMetadata": {
    "@type": "dqv:QualityMetadata",
    "//": "★ Boolean Activation Slot 활성 — Decision-Q4"
  }
}
```

3개 완전 예시: `5_examples/` 디렉토리 참조.

### 6.2 SHACL 검증

```bash
cd D:\ARD\packages\tta-0976\
python 4_validator/validate.py 5_examples/kisti_dataon.jsonld
```

기대 출력:
```
✓ Conforms: True
✓ 93/93 properties validated
✓ 117/117 enum values validated
```

### 6.3 Python 코드로 사용

```python
from tta_0976 import Repository, Dataset, File
from tta_0976.loader import load_from_jsonld

# JSON-LD 파일 로드
repo = load_from_jsonld('5_examples/kisti_dataon.jsonld')

# 타입 검증된 객체 사용
print(repo.RepositoryName.ko)  # "DataON"
print(repo.QualityManagement)  # "yes"
print(repo.DataLicenseUrl)     # HttpUrl typed

# JSON-LD로 출력
import json
print(json.dumps(repo.to_jsonld(), ensure_ascii=False, indent=2))
```

자세한 사용법: `3_code/README.md` 참조.

---

## 7. 알려진 제약 사항

본 AP 1.0.0의 알려진 제약은 `6_changelog/CHANGELOG.md`의 Known Issues 섹션 참조:

- **Issue-001**: pySHACL `sh:or` 패턴 (Coverage dual-purpose) 지원 검증 필요
- **Issue-002**: 3-valued boolean (yes/no/unknown) 표현
- **Issue-003**: UCI (한국 콘텐츠 식별체계) 글로벌 어휘 부재 → SC42 기여 후보
- **Issue-004**: TTA FileType 'other' DCMI 부재 → PG606 'other' 제거 권고

---

## 8. 후속 작업 권장

본 AP를 활용한 다음 작업 가능:

1. **TTA AI Ready Standard 인증**: 본 AP를 TTA에 제출하여 AI Ready Standard 인증 획득
2. **re3data 등록**: 한국 연구 리포지터리를 re3data에 본 AP 형식으로 등록
3. **DataCite metadata 출력**: DOI 발급 시 본 AP를 DataCite Schema 4.5로 자동 변환
4. **ML 데이터셋 표준 확장**: 본 AP를 기반으로 #4 (운영 시맨틱) 활성화한 ML 학습 데이터 표준 작성

---

## 9. 참조

### 9.1 TTA 표준 원본
- TTAK.KO-10.0976 (2017.03.30, 제1판), 한국정보통신기술협회 PG606

### 9.2 채택된 글로벌 어휘 (CHANGELOG.md 참조)
- DCMI Metadata Terms 2020-01-20
- DataCite Metadata Schema v4.5 (2024)
- re3data Schema v3.1
- DCAT v3 (W3C Rec 2024-08-22)
- DCMI Type Vocabulary 2012-06-14

### 9.3 TTA AI-Ready 프레임워크 제안서
- "TTA AI-Ready Data 표준 인벤토리 작성" 프로젝트 (2026-05)
- 7개 스키마 구성요소 + 6개 패키지 요소 정의

### 9.4 작업 산출물 위치
- 인벤토리: `D:\ARD\inventory\` (master_inventory.csv 477행)
- 매핑: `D:\ARD\mappings\` (매트릭스 93 + 통제어 117)
- 리포트: `D:\ARD\reports\` (Phase A/A.5/B/C 종합)
- 본 패키지: `D:\ARD\packages\tta-0976\`
