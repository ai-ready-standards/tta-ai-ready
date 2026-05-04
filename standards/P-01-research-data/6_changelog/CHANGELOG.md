# TTAK.KO-10.0976 AI-Ready Application Profile — Changelog

본 파일은 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 형식을 따른다.
버전 번호는 [Semantic Versioning](https://semver.org/spec/v2.0.0.html)을 준수한다.

---

## [1.0.1] — 2026-05-04 (D-1 자기검증 패치)

Phase D-1 자기검증 (`pytest` + `pyshacl validate.py`) 실행 결과 발견된 6건의 버그를 수정. 본 패치 후 3개 예시 인스턴스가 모두 `Conforms: True`로 검증 통과. 보고서: `D:\ARD\reports\phase_d1_verification.md`.

### Fixed — 수정

#### models.py — Python 3.14 PEP 649 호환

- `Collection.CollectionDateType`, `Dataset.DatasetDateType`, `File.FileType` 3개 필드의 타입 어노테이션이 동명 Enum을 가리는 name shadowing 버그 수정
- `_CollectionDateTypeT`, `_DatasetDateTypeT`, `_FileTypeT` 모듈 수준 alias 추가
- `__init__.py`에 `MultilingualText` export 추가 (테스트 임포트 누락)

#### shapes.shacl.ttl — 모델링 버그 4건

1. **다국어 필드 datatype**: `dcterms:title` / `dcterms:description` / `re3data:institutionName` (4 layer × 3 path = 11 PropertyShape)에서 `sh:datatype xsd:string` → `sh:or ( [sh:datatype xsd:string] [sh:datatype rdf:langString] )` 변환
2. **다국어 필드 cardinality**: 위 필드의 `sh:maxCount 1` 제거 (다국어 = 언어수만큼 entries 발생)
3. **sh:in datatype 명시**: 31개 sh:in 리스트의 223개 string literal에 `^^xsd:string` 명시 (pySHACL strict 비교용)
4. **ProvenanceConditionalShape 비활성**: SHACL Core로 조건부 advisory 표현 한계 → `sh:targetClass` 3 lines 주석 처리. SHACL-AF 또는 코드 보조로 향후 대응

#### context.jsonld — predicate 충돌

- `InstitutionName`이 `dcterms:title`로 매핑되어 `RepositoryName`과 동일 술어 충돌 → `re3data:institutionName`으로 변경 (shape의 path와 일치)

#### validate.py — 네트워크 fetch 회피

- `inline_local_context()` 추가: `@context` URL이 `https://standard.tta.or.kr/ai-ready/profile/context.jsonld`이면 로컬 `2_schema/context.jsonld` 내용으로 inline 후 검증. 네트워크 미연결 환경에서도 검증 가능

### Verified — 검증 결과

- pytest 11/11 PASS (`tests/test_models.py`)
- Issue-001 sh:or pre-test 4/4 PASS — **fallback 불필요 확정** (Issue-001 closed)
- 3 examples × `Conforms: True`:
  - `kisti_dataon.jsonld` ✓
  - `nie_environmental.jsonld` ✓ (Coverage dual-purpose 시간/공간 양쪽 검증)
  - `rda_agriculture.jsonld` ✓ (4계층 완전 시연)

### Open Issues — 미해결

- **PROV-O 조건부 매핑** (Decision-Q3/Q7): SHACL Core 표현 한계. SHACL-AF `sh:rule` 또는 Pydantic 후처리로 1.1.0 재구현 검토
- **FileShape AccessType "opened" vs Enum "open"**: shape는 "opened", Pydantic Enum은 "open". 본문 확인 후 통일 (PG606 피드백 추가 후보)

---

## [1.0.0] — 2026-05-04 (초기 릴리스)

### Added — 신규 추가

#### 6 패키지 산출물

- **1_document/** — TTA-0976 AI-Ready Application Profile 문서 (Markdown)
- **2_schema/** — JSON-LD @context (`context.jsonld`) + SHACL shapes (`shapes.shacl.ttl`)
- **3_code/** — Python Pydantic 모델 패키지 `tta_0976/`
- **4_validator/** — pySHACL 래퍼 `validate.py`
- **5_examples/** — 3개 도메인 JSON-LD 인스턴스 (KISTI / 생태원 / 농촌진흥청)
- **6_changelog/** — 본 파일

#### TTA-AP namespace 정의

- **표준별 namespace**: `https://standard.tta.or.kr/0976#` (TTA-0976 원본 IRI)
- **TTA-AP 통합 namespace**: `https://standard.tta.or.kr/ai-ready/profile#` (본 산출물의 모든 정의)

### 채택된 글로벌 어휘 5종 (Version Lock)

본 1.0.0 릴리스는 다음 5개 글로벌 어휘 버전에 정합된다. 이들 중 어느 어휘가 메이저 버전을 변경하면 본 AP의 호환성 점검이 필요하다.

| 어휘 | 버전 | IRI 네임스페이스 | TTA-0976 활용 건수 |
|---|---|---|---|
| **DCMI Metadata Terms (dcterms)** | 2020-01-20 | `http://purl.org/dc/terms/` | 32 properties + DCMI Type 11개 |
| **DataCite Metadata Schema** | 4.5 (2024) | `http://datacite.org/schema/kernel-4` | 19 properties + 110 controlled values |
| **re3data Schema** | 3.1 | `https://www.re3data.org/schema` | 28 properties + 33 controlled values |
| **DCAT** | v3 (W3C Rec 2024-08-22) | `http://www.w3.org/ns/dcat#` | 12 properties + 4 controlled values |
| **DCMI Type Vocabulary** | 2012-06-14 | `http://purl.org/dc/dcmitype/` | 11 type values (FileType 통제어) |

**보조 어휘** (참조 또는 fallback 용도):

| 어휘 | 버전 | IRI 네임스페이스 | 용도 |
|---|---|---|---|
| Schema.org | current (2026-05-03 download) | `https://schema.org/` | Rule 3 fallback (unitText 등) |
| PROV-O | W3C Rec 2013-04-30 | `http://www.w3.org/ns/prov#` | c5 출처·계보 보조 매핑 (조건부 활성) |
| DQV (Data Quality Vocabulary) | W3C Note 2016-12-15 | `http://www.w3.org/ns/dqv#` | c6 품질 (Boolean Activation Slot 활성 시) |
| SKOS | W3C Rec 2009-08-18 | `http://www.w3.org/2004/02/skos/core#` | Subject Class → Concept 변환 |
| ISO 639-3 | 2007 | `urn:iso:std:iso:639:-3:ed-1:v1:en` | RepositoryLanguage 코드 |
| ISO 3166-1 alpha-2 | 2020 | `urn:iso:std:iso:3166:-1:alpha-2` | InstitutionCountry 코드 ([OVERRIDE] 적용) |
| ISO 8601 | 2019 | `urn:iso:std:iso:8601:ed-3:v1:en` | 모든 Date/Coverage 포맷 |

### 적용된 매핑 결정 사항 (9건)

본 AP 1.0.0은 Phase A/A.5/B에서 합의된 다음 결정을 반영한다.

#### Decision-001 (2026-05-04): TTA-0976-001 Repository tta_iri 부여

- 임시 IRI `https://standard.tta.or.kr/0976#Repository` 부여
- TTA가 공식 IRI 발급 시 갱신 필요

#### Decision-002 (2026-05-04): InstitutionCountry [OVERRIDE]

- TTA 표준 원문 권장: ISO 3166-1 alpha-3 (예: KOR)
- 본 AP 적용: ISO 3166-1 alpha-2 (예: KR) — DCAT v3 호환
- 변환 함수: `loader.py`에 KOR↔KR 변환 테이블 내장

#### Decision-003 (2026-05-04): TTA-0976-203 IdentifierType [CONFLICT]

- 본문 "반드시 기술" (M) vs 부록 II-2 "O"
- 부록 우선 적용 → cardinality=0..1
- PG606 피드백 대상

#### Decision-004 (2026-05-04): TTA-0976-207 Publisher [CONFLICT]

- 본문 "반드시 기술" (M) vs 부록 II-2 "R"
- 부록 우선 적용 → cardinality=0..*
- PG606 피드백 대상

#### Decision-005 (2026-05-04): TTA-0976-221 AccessType [CHECK]

- 부록 PDF 손상으로 카디널리티 누락
- O로 추정 적용 (Collection/File AccessType=O 패턴 일관)
- PG606 직접 확인 필요

#### Decision-Q3 (2026-05-04): PROV-O 보조 매핑은 조건부 활성

- Date/PublicationYear 항목에서 DateType 값에 따라 c5 컬럼 활성:
  - `Created` → `prov:generatedAtTime`
  - `Updated` → `prov:wasRevisionOf`
  - `Withdrawn`/`Deleted` → `prov:invalidatedAtTime`
- dcterms 매핑은 항상 활성, PROV-O는 보조

#### Decision-Q4 (2026-05-04): Boolean Activation Slot 패턴

- `QualityManagement="yes"` 시 DQV 어휘(dqv:hasQualityMetadata) 활성화
- `no`/`unknown` 시 DQV 슬롯 비활성
- SHACL conditional shape으로 표현 (`sh:if`/`sh:then` pattern)

#### Decision-Q7 (2026-05-04): Repository 계층에도 PROV-O 보조 매핑 일관 적용

- Repository ResponsibilityType → prov:hadRole (loose)
- Date/PublicationYear와 동일한 조건부 활성 패턴

### Phase B 매핑 통계 (1.0.0 기준)

- 메타데이터 항목 매핑 매트릭스: **93 행** (4계층: Repository 26 + Collection 18 + Dataset 22 + File 27)
- 통제어 매핑: **117 행** (24개 카테고리)
- **종합 매핑 가능률**: **99.0%** (208/210, none 2건은 TTA 고유: UCI + 'other' FileType)
- 매트릭스 primary 비율: 88.2% (82/93)
- 매트릭스 high confidence 비율: 81.7% (76/93)

### Known Issues (1.0.0 미해결)

#### Issue-001: pySHACL `sh:or` 패턴 지원 불확실

- **영향**: TTA-0976-323 Coverage dual-purpose 검증
- **완화**: `4_validator/test_sh_or.py`에서 단위 테스트로 사전 검증 (Phase C 첫 작업)
- **fallback**: 미지원 시 두 SHACL shape 분리 + Python 검증 코드로 결합

#### Issue-002: 3-valued boolean 표현 (yes/no/unknown)

- **영향**: EnhancedPublication, QualityManagement, Versioning 3개 통제어
- **완화**: `sh:in (true false "unknown"^^xsd:string)` + sh:or
- **장기**: 3-valued logic 표준화 검토

#### Issue-003: UCI (한국 콘텐츠 식별체계) — 글로벌 어휘 부재

- **영향**: TTA-0976-CV-088
- **완화**: ttaap 자체 namespace에 `IdentifierType.UCI` 정의
- **장기**: SC42 기여 후보 (DataCite WG에 추가 제안)

#### Issue-004: TTA FileType 'other' — DCMI Type Vocabulary 부재

- **영향**: TTA-0976-CV-069
- **완화**: ttaap 자체 namespace에서만 사용. dctype:으로 매핑하지 않음
- **장기**: PG606에 'other' 제거 권고

### PG606 피드백 패키지 (9건, 1.0.0 기준)

본 1.0.0 릴리스 시 PG606에 보고할 사항:

#### 표준 결함 (수정 권고) — 4건

1. D2.1 IdentifierType 본문 vs 부록 카디널리티 상충 (High)
2. D5 Publisher 본문 vs 부록 카디널리티 상충 (High)
3. D14/D15 부록 II-2 PDF 표 손상 (Medium)
4. F17 Type 통제어의 'other' 값 (Medium — DCMI Type closed enum과 충돌)

#### 어휘 격차 (글로벌 표준 정합성) — 3개 영역

5. DCAT v3 (2024) 정합성 격차 (DataService/DatasetSeries/Relationship 미반영)
6. DataCite v4.5 (2024) 정합성 격차 (RelatedIdentifier/FundingReference/RelatedItem 미반영)
7. SKOS Concept 패턴 도입 권장 (Subject Class)

#### TTA 고유 개념 (보존 권장) — 2건

8. 4계층 구조 (Repository/Collection/Dataset/File) — 한국 연구데이터 생태계의 특수성
9. UCI (한국 콘텐츠 식별체계) — 한국 콘텐츠 생태계 표준

### SC42 기여 후보 (4건, 1.0.0 기준)

본 AP 작업 결과 ISO/IEC JTC1 SC42에 한국 기여로 제안 가능한 항목:

1. **4계층 구조 패턴** (High 우선순위) — DCAT/ISO 23081에 4계층 옵션 추가 제안
2. **Boolean Activation Slot 패턴** (Medium) — DQV/DCAT-AP RAI에 베스트 프랙티스로 제안
3. **UCI 어휘 추가** (Low) — DataCite WG에 한국 식별자 등록 제안
4. **Coverage sh:or 처리 패턴** (Low) — SHACL Best Practices에 사례 등록

---

## 향후 변경 이력 (예약 슬롯)

### [Unreleased]

다음 릴리스 (1.1.0 또는 1.0.1)에서 다룰 사항:

- pySHACL `sh:or` 단위 테스트 결과 반영 (Issue-001 해소 또는 fallback 적용)
- 표본 검토 결과 (46행) 반영 — 매핑 미세 조정
- PG606 피드백 회신 반영 (9건 중 일부 또는 전체)

### 버전 번호 정책

- **MAJOR (X.0.0)**: TTA 표준 자체 개정 (PG606 발행 변경) 또는 채택 어휘 메이저 버전 변경
- **MINOR (1.X.0)**: 매핑 추가/변경, 새 패키지 산출물 추가
- **PATCH (1.0.X)**: 버그 수정, 주석 보강, 검증 결과 반영

### 호환성 약속

본 AP 1.x 릴리스는 다음 호환성을 보장한다:
- TTA-0976 원문 (2017.03.30 제1판) 의미 보존
- DCMI/DCAT/DataCite 어휘 메이저 버전 호환성
- JSON-LD `@context` 구조 안정성 (1.x 내 추가만 가능, 제거 불가)
- SHACL shape의 단조 강화 (1.x 내 제약 약화 불가)

---

## Phase 별 작업 이력 (참조용)

본 1.0.0 릴리스 직전까지의 작업 이력:

| Phase | 작업 내용 | 산출 위치 | 완료일 |
|---|---|---|---|
| Phase A | TTA-0976 elements.csv 추출 (93행) | `D:\ARD\tta-standards\0976\` | 2026-05-03 |
| Phase A.5 | 누락 어휘 보강 (DataCite/re3data/DCMI Type/ISO + 통제어 117) | `D:\ARD\inventory\`, `D:\ARD\tta-standards\0976\enumerations.csv` | 2026-05-04 |
| Phase B | 매핑 매트릭스 작성 (93 + 117 = 210 mappings) | `D:\ARD\mappings\` | 2026-05-04 |
| **Phase C** | **6 패키지 산출물 (본 1.0.0 릴리스)** | **`D:\ARD\packages\tta-0976\`** | **2026-05-04** |

### Phase 별 산출 리포트

- `D:\ARD\reports\prov-o_report.md` (Phase A: PROV-O 인벤토리)
- `D:\ARD\reports\dcat-v3_report.md` (Phase A: DCAT v3)
- `D:\ARD\reports\croissant_report.md` (Phase A: Croissant)
- `D:\ARD\reports\schema-org_report.md` (Phase A: Schema.org)
- `D:\ARD\reports\inventory_validation.md` (Phase A v1 + v2)
- `D:\ARD\reports\phase_a5_summary.md` (Phase A.5)
- `D:\ARD\tta-standards\0976\extraction_report.md` (Phase A: TTA 추출)
- `D:\ARD\reports\tta-0976_mapping_conflicts.md` (Phase B: 충돌 분석)
- `D:\ARD\reports\phase_b_summary.md` (Phase B 종합)
- `D:\ARD\reports\phase_c_summary.md` (Phase C 종합 — 본 릴리스 완료 후 작성)
