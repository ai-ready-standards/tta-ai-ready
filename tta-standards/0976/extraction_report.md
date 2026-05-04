# TTAK.KO-10.0976 항목 추출 리포트 (Phase A)

- **표준**: TTAK.KO-10.0976 — 연구데이터 관리·공유를 위한 메타데이터
- **발행**: 2017.03.30 (제1판), TTA PG606 (메타데이터 PG)
- **추출 일자**: 2026-05-04
- **출처**: `D:\ARD\TTAK.KO-10.0976.pdf` (51 페이지)
- **명세 캐시**: `D:\ARD\sources\TTAK.KO-10.0976-utf8.txt` (UTF-8 텍스트)
- **출력**: `D:\ARD\tta-standards\0976\elements.csv` (93 행, 20 컬럼)

## 1. 추출 항목 통계

### 1.1 계층별 항목 수 (총 93개)

| 계층 | inventory_id 범위 | 행 수 | 비중 |
|---|---|---|---|
| 리포지터리 (Repository) | TTA-0976-001 ~ 026 | 26 | 28.0% |
| 컬렉션 (Collection) | TTA-0976-101 ~ 118 | 18 | 19.4% |
| 데이터셋 (Dataset) | TTA-0976-201 ~ 222 | 22 | 23.7% |
| 파일 (File) | TTA-0976-301 ~ 327 | 27 | 29.0% |
| **합계** | — | **93** | **100%** |

### 1.2 term_type 분포

| term_type | 행 수 |
|---|---|
| Class | 8 (각 계층의 최상위 + Subject 4개) |
| Property | 85 |
| Enumeration | 0 |

### 1.3 TTA 요소 유형 분포 (notes에서 파싱)

| 요소 유형 | 행 수 | 의미 |
|---|---|---|
| Property | 44 | 일반 값을 갖는 요소 |
| CVP (Controlled Vocabulary Property) | 34 | 통제어 값을 갖는 요소 |
| Class | 8 | 기술 대상 자원 요소 |
| SEP (Syntax Encoding Property) | 6 | 일정 형식의 값을 갖는 요소 (Date, Coverage, PublicationYear) |

CVP가 37%로 매우 높은 비중을 차지하는 것이 본 표준의 특징. 즉, 많은 메타데이터 값이 통제어휘에서 선택되도록 설계됨. 통제어 정의는 부록 Ⅱ-1에 21개 통제어 카테고리로 수록되어 있음.

### 1.4 cardinality 분포 (M/R/O 변환 결과)

| TTA M/R/O | 변환 cardinality | 행 수 | 비중 |
|---|---|---|---|
| M (Mandatory) | 1..1 | 39 | 41.9% |
| R (Recommended) | 0..* | 27 | 29.0% |
| O (Optional) | 0..1 | 27 | 29.0% |

필수 항목이 약 42%로 양호. 본 표준이 "최소 메타데이터" 모델보다는 "권장 풀 세트" 모델에 가까움.

### 1.5 DCMI 참조 보유 항목 비율

| 구분 | 행 수 | 비중 |
|---|---|---|
| equivalent_terms에 dcterms: 포함 | 48 | 51.6% |
| dcterms: 미포함 | 45 | 48.4% |

전체의 절반이 DCMI Dublin Core를 명시적으로 참조함. **이는 Phase B 매핑에서 약 50%의 항목이 자동 매핑 가능함을 의미** — 본 표준 매핑의 가장 큰 자산.

DCMI 미참조 45개의 주요 사유:
- CVP 항목의 통제어 자체는 DCMI에 직접 매핑되지 않음 (예: ContributorType — DataCite 통제어)
- TTA 자체 정의 항목 (Contact, Keyword 등 일부 — N/A로 명시)
- re3data.org 전용 항목 (Repository 계층 다수)

### 1.6 concept_tag 분포 (28개 태그 체계)

| concept_tag | 행 수 | 주요 항목 |
|---|---|---|
| identification.keyword | 19 | Subject + SubjectScheme/ID/Name + Keyword × 4 layers |
| rights.access | 11 | AccessType + AccessRestriction + Rights × 다층 |
| identification.identifier | 8 | Identifier + IdentifierType × 4 layers |
| identification.title | 8 | Title + TitleType × 4 layers |
| temporal.coverage | 7 | Date + DateType + Coverage |
| uncategorized | 6 | Type, RepositoryLanguage, DataUpload, Versioning, EnhancedPublication, FileType |
| actor.contributor | 5 | Contributor + ContributorType × 2 + ResponsibilityType |
| actor.contact | 5 | Contact + InstitutionContact + RepositoryContact |
| identification.description | 4 | Description × 4 layers |
| structure.dataset | 3 | Repository/Collection/Dataset 클래스 |
| actor.publisher | 3 | Publisher × 2 + InstitutionName |
| actor.creator | 3 | Creator × 3 layers |
| distribution.url | 2 | File 클래스, RepositoryUrl |
| rights.license | 2 | DataLicenseName, DataLicenseUrl |
| temporal.creation | 2 | PublicationYear × 2 |
| distribution.size | 2 | Size, Unit |
| spatial.coverage | 1 | InstitutionCountry |
| quality.general | 1 | QualityManagement |
| distribution.media_type | 1 | Format |

본 인벤토리의 28개 태그 중 19개가 사용됨. 미사용 9개 태그:
- ml.split, ml.label, ml.bounding_box, measurement.value (ML 특화 — 본 표준이 일반 연구데이터라 미사용. 정상)
- provenance.* (source/activity/derivation/qualifier 4개 — 본 표준에 출처·계보 어휘 부재. 결정 3 운영 시맨틱 NA와 일치)
- temporal.modification (Date의 DateType=Updated로 표현 가능하나 별도 명시 필드 없음)
- quality.bias/completeness/accuracy (본 표준에 품질 차원 어휘 부재)

→ **결정 3에서 합의한 "운영 시맨틱 NA" + 결함 1의 "품질 어휘 부재"가 추출 결과로 확인됨.**

## 2. 추출 결정 사례

### 2.1 [CHECK] 표시 항목 (5건)

| inventory_id | 항목 | 사유 |
|---|---|---|
| TTA-0976-001 | Repository (Class) | tta_iri 미정 — 본 표준이 자체 URN 체계를 정의하지 않음. Phase B에서 결정 |
| TTA-0976-014 | InstitutionCountry | ISO 3166-1 alpha-3 코드 사용 (예: KOR) 권장 — 본 인벤토리(schema:addressCountry)는 alpha-2 권장과 불일치 |
| TTA-0976-203 | Dataset IdentifierType | 본문은 "데이터셋을 웹에 공개·출판하기 위해 반드시 기술" (=M)이나 부록 Ⅱ-2 표는 "O" — 본 작업은 부록 우선 적용 |
| TTA-0976-207 | Dataset Publisher | 본문은 "반드시 기술" (=M)이나 부록 Ⅱ-2 표는 "R" — 본 작업은 부록 우선 적용 |
| TTA-0976-221 | Dataset AccessType | 부록 Ⅱ-2 표에서 M/R/O 컬럼 값 누락 (PDF 표 wrap 손상). Collection AccessType (O), File AccessType (O) 패턴으로 O 추정 |

### 2.2 본문 vs 부록 Ⅱ-2 상충 (2건)

D2.1 IdentifierType, D5 Publisher의 경우 본문 설명("반드시 기술")과 부록 카디널리티표가 일치하지 않음. 이는 표준 자체의 결함으로 보이며, **본 추출은 부록 Ⅱ-2의 M/R/O 표를 정본으로 적용**. Phase B/C 작업 시 SHACL 제약으로 옮길 때는 본문의 강한 권장(SHOULD)을 추가 코멘트로 처리하는 것을 권장.

### 2.3 PDF 텍스트 추출 결함 (1건)

TTA-0976-221 (Dataset AccessType)의 경우 부록 Ⅱ-2 표 라인 1819-1820에서 M/R/O 컬럼이 PDF 텍스트 추출 시 손상되어 누락됨. 패턴 추정으로 "O"를 사용했으나 PDF를 사람이 직접 확인하여 검증 권장.

### 2.4 4계층 구조 보충 항목

본 표준에 명시되지 않은 항목은 추가하지 않음. 단, prefix_local 부여 시 동일 영문 명칭(Identifier, Title 등)이 4계층에 반복 출현하므로 다음 규칙으로 구분:
- `tta0976:Repository_Identifier` (R3)
- `tta0976:Collection_Identifier` (C2)
- `tta0976:Dataset_Identifier` (D2)
- `tta0976:File_Identifier` (F2)

이 prefix 규칙은 Phase B에서 SHACL 제약 작성 시 동일 의미 요소가 계층마다 다른 카디널리티를 가지는 것을 명확히 표현하기 위함.

### 2.5 DCMI 참조 외 다른 표준 참조 발견

- **DataCite Metadata Schema**: IdentifierType, ContributorType, TitleType, DateType 등 통제어 정의의 1차 출처
- **re3data.org Schema**: Repository 계층 대부분 (RepositoryUrl/Identifier/Type/Language/Subject/Institution/AccessType/License/Versioning 등)
- **DCMI Type Vocabulary**: FileType (Image/Sound/Text 등 dctype: 어휘)
- **ISO 639-3**: RepositoryLanguage
- **ISO 3166-1 alpha-3**: InstitutionCountry
- **ISO 8601 [W3CDTF]**: 모든 Date/Coverage 필드의 값 형식

→ 이는 본 표준이 단일 표준이 아닌 **5개 글로벌 어휘의 통합 프로파일**임을 보여줌. Phase B 매핑 시 dcterms 외에 datacite·re3data 어휘 추가 도입 검토 필요.

## 3. Phase B (매핑) 사전 관찰

### 3.1 즉시 매핑 가능해 보이는 항목 (약 60%)

DCMI 직접 참조 48건 + 명백한 의미 매칭 약 8건. 다음 4개 카테고리는 1:1 매핑이 거의 자명함:

**그룹 A — DCMI Core (15요소) 직접 매핑** (약 30건):
- Identifier × 4 layers → dcterms:identifier
- Title × 4 layers → dcterms:title (Repository는 RepositoryName)
- Date × 3 layers → dcterms:date
- Description × 4 layers → dcterms:description
- Subject × 4 layers → dcterms:subject
- Creator × 3 layers → dcterms:creator
- Publisher × 2 layers (Dataset/File) → dcterms:publisher
- Format (File) → dcterms:format
- Type (File/Repository) → dcterms:type
- Coverage (File) → dcterms:coverage
- Rights × 3 layers → dcterms:rights

**그룹 B — DCAT v3 직접 매핑** (약 12건):
- File 클래스 → dcat:Distribution (또는 schema:DataDownload)
- Dataset 클래스 → dcat:Dataset
- Collection 클래스 → dcat:Catalog
- Repository 클래스 → dcat:Catalog (or 메타 catalog)
- AccessType/AccessRestriction → dcat:accessRights / dcterms:accessRights
- DataLicense* → dcterms:license
- Format → dcat:mediaType
- Size → dcat:byteSize
- RepositoryUrl → dcat:landingPage

**그룹 C — Schema.org 매핑** (약 8건):
- Keyword → schema:keywords / dcat:keyword
- Contact → schema:contactPoint / dcat:contactPoint
- InstitutionName → schema:legalName

### 3.2 매핑 어려울 것으로 예상되는 항목 (약 20%)

| 항목 | 사유 | 매핑 후보 |
|---|---|---|
| TitleType, IdentifierType, DateType, ContributorType, SubjectScheme/ID/Name 등 통제어 sub-element (약 14건) | 글로벌 어휘는 보통 단일 property로 처리하고 type을 별도 sub-property로 두지 않음 | DataCite-Property 자체 매핑, 또는 사용자 지정 sub-property로 표현 |
| RepositoryLanguage | 리포지터리 시스템 언어 ≠ 데이터셋 언어 | dcterms:language의 변형 또는 schema:inLanguage |
| DataUpload, EnhancedPublication, Versioning (re3data 전용) | 글로벌 어휘에 직접 대응 부재 | re3data: 어휘 그대로 사용 또는 vann: 메타데이터로 표현 |
| QualityManagement | DQV는 측정 컨테이너이지 단순 boolean이 아님 | dqv:hasQualityMetadata 존재 여부로 우회 표현 |
| ResponsibilityType | prov:hadRole의 약식 표현 | prov:hadRole + 제한된 enumeration |
| Coverage (시간·공간 dual-purpose) | 글로벌 어휘는 시간(temporal)과 공간(spatial)을 분리 | 매핑 시 분할 필요. 본 작업은 두 매핑 모두 equivalent_terms에 기재 |

### 3.3 본 표준 고유 개념 (글로벌 어휘에 대응 없음으로 추정)

| 항목 | 추정 | Phase B 결정 권고 |
|---|---|---|
| RepositoryNameType | 리포지터리 이름의 다언어 정렬 표현용. 글로벌 어휘에 직접 매칭 없음 | TitleType 통제어를 적용하므로 dcterms:alternative로 우회 가능 |
| FileSize Unit (KB/MB/GB/TB) | dcat:byteSize는 단일 단위(byte) 사용. 단위 분리는 본 표준 고유 | bytes로 정규화 후 dcat:byteSize 매핑 권장 |

### 3.4 Phase B로 즉시 진행 가능 판단

**판단: 즉시 진행 가능 (조건부)**

근거:
- 93개 항목 모두 20 컬럼 형식으로 깔끔히 추출됨
- DCMI 참조 비율 52%로 자동 매핑 가능 비중이 높음
- [CHECK] 5건 모두 본 표준의 결함이거나 PDF 손상이 원인이며, 매핑 진행에는 영향 없음
- 컬럼 누락 5건은 즉시 발견·수정됨 (final 93/93 정확)

**조건**:
- Phase B 시작 전 아래 "개방 질문" 4건에 대한 사전 결정 필요
- 특히 Q3 (PROV-O #5 출처·계보 적용 방식)와 Q4 (DQV #6 품질 적용 방식)는 Phase B 매핑 매트릭스 구조에 영향

## 4. 개방 질문 (Phase B 시작 전 결정 필요)

### Q1. 통제어 (Controlled Vocabulary) 자체의 인벤토리 처리

본 표준의 부록 Ⅱ-1에는 21개 통제어 카테고리(IdentifierType, TitleType, DateType, ContributorType, AccessType 등)가 정의되어 있음. 각 통제어의 가능한 값(예: "Created", "Updated", "Deleted")은 별도 항목으로 추출하지 않음.

옵션:
- (a) 통제어를 본 인벤토리에 Enumeration term_type으로 추가 (TTA-0976-401~ 별도 범위)
- (b) 통제어는 SKOS ConceptScheme으로 별도 파일에 추출
- (c) Phase C(SHACL 제약 작성) 시점에 sh:in 제약으로만 표현

권장: (a) 또는 (b) — 통제어 값 21 카테고리 × 평균 5개 값 ≈ 100여 개 추가 행. 매핑 단계에서 가치 있음.

### Q2. 다른 TTA 표준 추가 시 prefix 충돌

본 작업은 `tta0976:` namespace를 사용. 향후 TTA-1234 추가 시:
- `tta1234:Identifier`로 별도 namespace 사용 → 표준 간 동등성 표현 어려움
- `tta:Identifier_0976`처럼 한 namespace에서 표준별 suffix → 충돌 회피 어려움

권장: 표준별 별도 namespace + master mapping 매트릭스에서 동등성 명시

### Q3. PROV-O #5 (출처·계보) 적용 방식

본 표준에 출처·계보 관련 항목 없음. 본 표준의 Date+DateType (Created/Updated/Deleted) 패턴은 PROV-O의 generatedAtTime/invalidatedAtTime과 의미적으로 유사하나 1:1 매핑은 아님. Phase B에서:
- (a) Date+Created → prov:generatedAtTime, Date+Updated → prov:wasRevisionOf+atTime 등으로 분해 매핑
- (b) Date 자체는 dcterms:date로 두고, PROV-O는 별도 layer로 추가 (Phase C에서)

권장: (b) — 본 표준의 변경 없이 PROV-O를 보조 layer로 추가

### Q4. DQV #6 (품질 프로파일) 적용 방식

본 표준의 QualityManagement (yes/no/unknown)는 단순 boolean. DQV의 풍부한 측정 모델과는 거리가 멂.

옵션:
- (a) QualityManagement="yes"인 경우만 dqv:hasQualityMetadata 슬롯 활성화
- (b) DQV는 본 표준에 적용하지 않고, 차후 품질 측정값을 기록하는 별도 표준에서만 사용

권장: (a) — Phase C에서 SHACL 조건부 제약으로 표현

## 5. Phase B 작업 권고

위 통계를 바탕으로 다음 단계를 제안:

1. **Q1-Q4 결정** (사용자 측)
2. **mappings 디렉토리 생성** (`D:\ARD\mappings\tta-0976\`)
3. **매핑 매트릭스 CSV 작성** — TTA 93행 × 7개 구성요소 = 651 셀의 매핑 결정 표
4. **갭 분석 리포트** — 7개 구성요소 중 본 표준에 NA/부분/완전 매핑 비율
5. **Phase C 입력 명세서** — Phase C(패키지 산출물)에서 생성할 6개 산출물의 구체 명세

예상 소요: Q1-Q4 결정 후 Phase B 작업은 약 2-3 세션 (매트릭스 작성 + 갭 분석 + 리포트).

## 6. 산출물 위치

```
D:\ARD\tta-standards\0976\
├── elements.csv              (93 rows × 20 columns)
└── extraction_report.md      (이 파일)
```

다음 단계 산출물 예정:
```
D:\ARD\mappings\tta-0976\
├── tta-0976_x_components.csv (Phase B 출력)
└── mapping_report.md          (Phase B 출력)

D:\ARD\packages\tta-0976\
├── 1_document\               (Phase C)
├── 2_schema\                 (Phase C)
├── 3_code\                   (Phase C)
├── 4_validator\              (Phase C)
├── 5_examples\               (Phase C)
└── 6_changelog\              (Phase C)
```

## 7. Decisions Log (2026-05-04, Phase A.5 Step 1)

Phase A에서 발견된 [CHECK] 5건에 대해 사용자가 다음과 같이 결정함. elements.csv를 즉시 갱신.

### Decision-001: TTA-0976-001 Repository tta_iri 부여

- **이전 상태**: tta_iri 컬럼 빈칸, notes에 "[CHECK] tta_iri 미정 — Phase B에서 결정"
- **결정**: 임시 IRI `https://standard.tta.or.kr/0976#Repository` 부여
- **갱신 후 notes**: "임시 IRI 부여 (decision: 2026-05-04). TTA가 공식 IRI 발급 시 갱신 필요"
- **근거**: namespace 정책 결정에 따라 표준별 namespace `https://standard.tta.or.kr/{표준번호}#`을 채택. Phase B 매핑 진행을 위해 임시 IRI 즉시 부여.

### Decision-002: TTA-0976-014 InstitutionCountry alpha-2 적용

- **이전 상태**: range="xsd:string", notes에 "[CHECK] alpha-3 사용은 ISO-3166의 alpha-2 권장과 차이가 있음"
- **결정**: range 컬럼을 `"ISO 3166-1 alpha-2 (e.g., KR, US)"`로 변경, alpha-2 적용
- **갱신 후 notes**: "[OVERRIDE] 표준 원문은 alpha-3 (예: KOR) 권장이나 본 인벤토리는 DCAT v3·HTML lang·웹 호환성 위해 alpha-2 적용 (decision: 2026-05-04). 변환 함수 필요 (KOR↔KR). PG606 피드백 대상"
- **근거**: 표준 원문은 alpha-3 (예: KOR) 권장이나 DCAT v3, HTML lang, ICANN 등 글로벌 웹 표준이 모두 alpha-2 사용. 글로벌 호환성 우선. 단, Phase B 매핑 시 KOR↔KR 변환 함수 필요. PG606에 표준 개정 시 alpha-2 통일 권고.

### Decision-003: TTA-0976-203 Dataset IdentifierType 본문/부록 상충

- **이전 상태**: cardinality="0..1", notes에 "[CHECK] 본문은 'M' 표시이나 부록은 'O' — 상충"
- **결정**: 부록 Ⅱ-2 정본 우선 적용 (cardinality=0..1 유지)
- **갱신 후 notes**: "TTA M/R/O = O (부록 II-2 정본). [CONFLICT] 본문은 M (반드시 기술), 부록은 O. 부록 우선 적용 (decision: 2026-05-04). PG606 피드백 대상"
- **근거**: 부록 Ⅱ-2 "요소 리스트"는 표준의 normative 카디널리티 정의 표이므로 본문 설명("반드시 기술")과 상충 시 부록 우선. 표준 자체의 결함이며 PG606 피드백 자료로 보존.

### Decision-004: TTA-0976-207 Dataset Publisher 본문/부록 상충

- **이전 상태**: cardinality="0..*", notes에 "[CHECK] 본문은 '반드시'이나 부록은 R"
- **결정**: 부록 Ⅱ-2 정본 우선 적용 (cardinality=0..* 유지)
- **갱신 후 notes**: "TTA M/R/O = R (부록 II-2 정본). [CONFLICT] 본문은 M (반드시 기술), 부록은 R. 부록 우선 적용 (decision: 2026-05-04). 출처: DCMI dc:publisher. PG606 피드백 대상"
- **근거**: Decision-003과 동일.

### Decision-005: TTA-0976-221 Dataset AccessType PDF 손상

- **이전 상태**: cardinality="0..1", notes에 "[CHECK] 부록 II-2 표에서 M/R/O 값 누락 — 본문 맥락상 O 추정"
- **결정**: O로 추정 적용 유지 (cardinality=0..1)
- **갱신 후 notes**: "TTA M/R/O = O (추정). 요소 유형: CVP. [CHECK] 부록 II-2 PDF 표에서 M/R/O 컬럼 손상으로 누락. Collection AccessType=O, File AccessType=O 패턴 + 본문 맥락상 O 추정 (decision: 2026-05-04). PG606 확인 필요. 통제어: DatasetAccessType (re3data ID 22.1)"
- **근거**: 표준 PDF 부록 Ⅱ-2 line 1819-1820의 표 wrap이 손상되어 M/R/O 컬럼이 누락됨. Collection/File 계층의 동일 항목이 모두 O이고 본문 맥락도 O와 일치하므로 추정 적용. 다만 PG606 직접 확인 권장으로 [CHECK] 플래그는 유지.

### 처리 결과 요약

| inventory_id | 항목 | 이전 플래그 | 변경 후 플래그 | cardinality 변경 |
|---|---|---|---|---|
| TTA-0976-001 | Repository | [CHECK] | (해제) | 변경 없음 |
| TTA-0976-014 | InstitutionCountry | [CHECK] | [OVERRIDE] | 변경 없음 (range만 변경) |
| TTA-0976-203 | Dataset IdentifierType | [CHECK] | [CONFLICT] | 변경 없음 |
| TTA-0976-207 | Dataset Publisher | [CHECK] | [CONFLICT] | 변경 없음 |
| TTA-0976-221 | Dataset AccessType | [CHECK] | [CHECK] (유지) | 변경 없음 |

**플래그 분포 변화**: [CHECK] 5건 → [CHECK] 1건 + [CONFLICT] 2건 + [OVERRIDE] 1건 + (해제) 1건.

### PG606 피드백 자료 (3건)

다음 3건은 향후 표준 개정 또는 후속 표준 작성 시 고려 사항:
1. **D2.1 IdentifierType**: 본문 "반드시 기술" vs 부록 "O" — 본문/부록 일관성 확보 필요
2. **D5 Publisher**: 본문 "반드시 기술" vs 부록 "R" — 본문/부록 일관성 확보 필요
3. **InstitutionCountry alpha-3 사용**: 글로벌 웹 표준(alpha-2)과 불일치. 후속 표준에서 alpha-2로 통일 권고

### Phase A.5 진행 상태

본 Decisions Log 추가로 Phase A.5 Step 1 완료. 다음 단계 (Step 2: enumerations.csv 작성) 진행.
