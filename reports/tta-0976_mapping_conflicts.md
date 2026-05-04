# TTAK.KO-10.0976 매핑 충돌·결함 분석 리포트

- **작성 일자**: 2026-05-04
- **작성 단계**: Phase B Step 5
- **입력 자료**:
  - `D:\ARD\mappings\tta-0976_x_components.csv` (93 행)
  - `D:\ARD\mappings\tta-0976_enumerations_mapping.csv` (117 행)
- **분석 범위**: 매핑 부재, 카디널리티 충돌, 의미 차이, Rule 3 사례, PG606 피드백, SC42 기여, 통제어 부재

---

## 섹션 1. 매핑 부재 (none) 항목 분석

총 매핑 부재: **2건** (모두 통제어 카테고리)

### 1.1 TTA-0976-CV-088 UCI (IdentifierType)

| 항목 | 내용 |
|---|---|
| tta_cv_id | TTA-0976-CV-088 |
| 원문 한국어 명칭 | UCI |
| 원문 정의 | 한국 국가표준 디지털콘텐츠식별체계 (Universal Content Identifier) |
| 사용 위치 | TTA-0976-004/103/203/303 (모든 4계층 IdentifierType 통제어) |
| 글로벌 어휘 부재 이유 | DataCite의 relatedIdentifierType 통제어(19개)에 UCI 미포함. ARK·arXiv·bibcode·DOI·EAN13·EISSN·Handle·ISBN·ISSN·ISTC·LISSN·LSID·PMID·PURL·UPC·URL·URN·URI까지 18개와 미국·국제 식별자만 포함 |
| 분류 | **한국 특화 (일반화 검토)** |
| PG606 피드백 권장 | High (DataCite에 UCI 추가 제안 가능성 검토) |
| SC42 기여 가능성 | Medium — 한국 콘텐츠 식별 인프라가 글로벌 가치를 가지나 도입 비용 고려 필요 |

**채택 후속 처리:**
- Phase C SHACL `sh:in` 제약에 UCI 포함하되 datacite-cv 외 별도 enum 정의
- TTA-AP namespace에서 `ttaap:IdentifierType.UCI` 자체 IRI 부여
- conflicts.md 본 항목을 SC42 기여 후보 (섹션 6)에 등록

### 1.2 TTA-0976-CV-069 other (FileType)

| 항목 | 내용 |
|---|---|
| tta_cv_id | TTA-0976-CV-069 |
| 원문 한국어 명칭 | 기타 (other) |
| 원문 정의 | 위 분류에 없음 (DCMI Type Vocabulary 11개 외 catchall) |
| 사용 위치 | TTA-0976-324 File Type 통제어 |
| 글로벌 어휘 부재 이유 | DCMI Type Vocabulary는 정확히 12개 표준 타입(Collection/Dataset/Event/Image/InteractiveResource/MovingImage/PhysicalObject/Service/Software/Sound/StillImage/Text)만 정의. catchall 'other' 미정의 |
| 분류 | **TTA 고유 개념 (글로벌 기여 후보 X)** — catchall 패턴은 표준 어휘 설계 철학에 반함 |
| PG606 피드백 권장 | Medium — DCMI Type Vocabulary가 의도적으로 closed enum이므로, 'other'를 두면 자동 분류 실패. **TTA 표준에서 'other' 제거 권고** 가능 |
| SC42 기여 가능성 | None |

**채택 후속 처리:**
- Phase C: 'other' 발생 시 fallback 정책 명시 (가장 가까운 dctype으로 자동 분류 또는 검증 실패)
- PG606 피드백 5.1 (표준 결함)에 등록

### 1.3 종합 평가

매트릭스 0건 + 통제어 2건 = 전체 매핑 가능 비율 **99.0%** (208/210). 매핑 부재 2건 모두:
- TTA 표준의 의도된 "확장성" 또는 "한국 특화" 결과
- Phase C 작업에 직접 영향 없음 (sh:in에서 별도 처리)
- 후속 표준 개정 또는 SC42 기여 검토 대상

---

## 섹션 2. 카디널리티 충돌 사례

총 충돌 사례: **3건** (Phase A에서 발견, Phase B에서 일관 적용)

### 2.1 TTA-0976-203 IdentifierType (D2.1) — 본문 vs 부록 상충

| 항목 | 내용 |
|---|---|
| 충돌 유형 | **TTA 내부 충돌** (본문과 부록 II-2가 일치하지 않음) |
| 본문 기술 | "데이터셋을 웹에 공개 또는 출판하기 위해 반드시 기술되어야 함" → M (Mandatory) |
| 부록 II-2 기술 | "O" (Optional) — 카디널리티 표 |
| 적용 결정 | 부록 우선 적용 (cardinality=0..1) |
| 매트릭스 행 | TTA-0976-203, conflict_notes에 [CONFLICT] 명시 |
| 결정 근거 | 부록 II-2가 normative한 카디널리티 정의 표이므로. 본문 설명은 "반드시 기술" SHOULD 권고로 해석 |
| PG606 보고 우선순위 | **High** — 표준 자체의 결함, 후속 개정 시 일관성 확보 필수 |

### 2.2 TTA-0976-207 Publisher (D5) — 본문 vs 부록 상충

| 항목 | 내용 |
|---|---|
| 충돌 유형 | **TTA 내부 충돌** |
| 본문 기술 | "데이터셋을 웹에 공개 또는 출판하기 위해 반드시 기술되어야 함" → M |
| 부록 II-2 기술 | "R" (Recommended) |
| 적용 결정 | 부록 우선 적용 (cardinality=0..*) |
| 매트릭스 행 | TTA-0976-207, conflict_notes에 [CONFLICT] 명시 |
| 결정 근거 | Decision-004와 동일 |
| PG606 보고 우선순위 | **High** — 본문/부록 일관성 확보 필수 |

### 2.3 TTA-0976-221 AccessType (D14) — PDF 손상으로 카디널리티 누락

| 항목 | 내용 |
|---|---|
| 충돌 유형 | **PDF 손상** (TTA 내부) |
| 본문 기술 | "데이터셋의 접근 또는 이용 유형" — 카디널리티 명시 없음 |
| 부록 II-2 기술 | M/R/O 컬럼이 PDF 표 wrap으로 손상되어 누락 |
| 적용 결정 | O로 추정 (cardinality=0..1) |
| 매트릭스 행 | TTA-0976-221, [CHECK] 잔존 |
| 결정 근거 | Collection AccessType=O, File AccessType=O 패턴 일관성 |
| PG606 보고 우선순위 | **Medium** — PDF 재생산 또는 원문 확인 필요 |

### 2.4 TTA-0976-014 InstitutionCountry (R9) — TTA-글로벌 충돌

| 항목 | 내용 |
|---|---|
| 충돌 유형 | **TTA-글로벌 충돌** (alpha-3 vs alpha-2) |
| TTA 원문 권장 | ISO 3166-1 alpha-3 (예: KOR) |
| 글로벌 표준 (DCAT v3, HTML, ICANN) | ISO 3166-1 alpha-2 (예: KR) |
| 적용 결정 | [OVERRIDE] alpha-2 적용. KOR↔KR 변환 함수 필요 |
| 매트릭스 행 | TTA-0976-014, [OVERRIDE] 명시 |
| 결정 근거 | Decision-002. 글로벌 호환성 우선 |
| PG606 보고 우선순위 | **Medium** — 후속 표준 개정 시 alpha-2 통일 권고 |

### 2.5 매트릭스 작성 중 추가 발견 (없음)

Step 3 매핑 작업 중 신규 카디널리티 충돌은 발견되지 않음. 위 4건이 전체.

---

## 섹션 3. 정의 차이 (semantic_diff) 사례

매트릭스/통제어에서 conflict_notes 또는 semantic_diff 컬럼에 명시된 의미 차이 사례.

### 3.1 구조적 차이 (Structural)

#### 3.1.1 TTA-0976-001 Repository ↔ dcat:Catalog (4계층 vs 3계층)

| 항목 | 내용 |
|---|---|
| 차이 본질 | **구조** — TTA는 Repository/Collection/Dataset/File 4계층, DCAT v3는 Catalog/Dataset/Distribution 3계층 |
| 자동화 영향 | SHACL 작성 시 ttaap:Repository에 dcat:Catalog 제약 import + ttaap:hasCollection 관계 추가 필요. JSON-LD context는 정상 매핑 가능 |
| Phase C 처리 권장 | **다중 매핑 방식**: ttaap:Repository ⊆ dcat:Catalog (subClassOf) + ttaap:hasCollection 관계로 4계층 명시 |

#### 3.1.2 TTA Subject Class (4계층) ↔ dcterms:subject (Property)

| 항목 | 내용 |
|---|---|
| 차이 본질 | **구조** — TTA Subject는 SubjectScheme/SubjectID/SubjectName 하위를 포함하는 Class. dcterms:subject는 단일 Property |
| 자동화 영향 | 1:N 구조 변환 필요. Phase C에서 SKOS Concept 패턴으로 변환 |
| Phase C 처리 권장 | **★ SKOS Concept 패턴 적용** (Decision-2 결과) — `dcterms:subject [a skos:Concept; skos:inScheme [...]; skos:notation [...]; skos:prefLabel [...]]`. Subject가 통제어 사용 시 ConceptScheme 정의, 자유 텍스트면 Concept만 |

#### 3.1.3 TTA-0976-323 Coverage (dual-purpose temporal+spatial)

| 항목 | 내용 |
|---|---|
| 차이 본질 | **구조** — TTA Coverage 단일 필드에 시간/공간 양쪽 값 가능. 글로벌은 dcterms:temporal과 dcterms:spatial로 분리 |
| 자동화 영향 | 검증 단계에서 값 분류 필요 |
| Phase C 처리 권장 | **★ Decision-3.1 (Pattern A) 적용**: SHACL `sh:or { sh:path dcterms:temporal sh:datatype xsd:dateTime } { sh:path dcterms:spatial sh:class dcterms:Location }`. 변환 시 자동 분류 (날짜형식 → temporal, 지역명 → spatial) 가능 |

### 3.2 범위 차이 (Scope)

#### 3.2.1 TTA-0976-013 InstitutionName ↔ dcterms:title

| 항목 | 내용 |
|---|---|
| 차이 본질 | **범위** — TTA InstitutionName은 기관 명칭, dcterms:title은 일반 자원 명칭 |
| 자동화 영향 | dcterms:title은 기관에도 적용 가능하나 schema:legalName이 의미상 더 정확 |
| Phase C 처리 권장 | **다중 표현**: ttaap:InstitutionName → dcterms:title + schema:legalName 동시 매핑. SHACL에서 sh:or 또는 두 매핑 모두 출력 |

#### 3.2.2 TTA-0976-CV-013 Deleted (CollectionDateType) ↔ schema:dateDeleted

| 항목 | 내용 |
|---|---|
| 차이 본질 | **범위** — TTA CollectionDateType (3개 값: Created/Updated/Deleted)은 DataCite DatasetDateType (9개 값: Accepted/Available/Copyrighted/.../Valid)의 부분집합. 'Deleted'는 DataCite에 없음 |
| 자동화 영향 | TTA Collection-only 값 → schema:dateDeleted (DataFeedItem property) 차용 |
| Phase C 처리 권장 | **Layer-specific 매핑**: Collection 계층은 별도 sh:in (3개 값), Dataset/File 계층은 datacite:dateType 9개 값. CV-013 Deleted → c5 prov:invalidatedAtTime 활성 |

### 3.3 의미 차이 (Semantic)

#### 3.3.1 TTA-0976-020 Versioning ↔ dcat:version

| 항목 | 내용 |
|---|---|
| 차이 본질 | **의미** — TTA Versioning은 시스템 능력 (yes/no/unknown), dcat:version은 자원의 버전 번호 (string) |
| 자동화 영향 | 매핑 안 됨. 의미 다름 |
| Phase C 처리 권장 | TTA-AP에서 `ttaap:supportsVersioning` (boolean) 별도 property 정의. dcat:version과 매핑하지 않음 |

#### 3.3.2 TTA-0976-CV-054, 093, 112 unknown 값 (3건)

| 항목 | 내용 |
|---|---|
| 차이 본질 | **의미** — TTA boolean+ (yes/no/unknown), 글로벌 xsd:boolean (true/false 2-valued) |
| 자동화 영향 | xsd:boolean으로 unknown 표현 불가 |
| Phase C 처리 권장 | 3-valued logic 또는 nullable boolean. SHACL 작성: `sh:in (true false "unknown"^^xsd:string) ; sh:or {sh:datatype xsd:boolean} {sh:hasValue "unknown"^^xsd:string}` |

### 3.4 정규화 차이 (Normalization)

#### 3.4.1 TTA-0976-CV-056~058 Mega/Giga/Tera Byte (공백)

| 항목 | 내용 |
|---|---|
| 차이 본질 | **정규화** — TTA "Mega Byte" (공백 포함) vs UN/CEFACT "MB" (공백 없음, 표준 단위 코드) |
| 자동화 영향 | Phase C 변환 시 공백 제거 + 약어화 |
| Phase C 처리 권장 | 변환 함수: "Mega Byte" → "MB", "Giga Byte" → "GB", "Tera Byte" → "TB". schema:unitText 값으로 약어 사용 |

### 3.5 종합

총 **9건의 의미 차이** 식별:
- 구조 (Structural): 3건 (4계층 차이, Subject Class, Coverage dual)
- 범위 (Scope): 2건 (InstitutionName, CollectionDateType subset)
- 의미 (Semantic): 4건 (Versioning, 3건 unknown 값)
- 정규화 (Normalization): 1건 (Mega Byte 공백)

모든 9건에 대해 Phase C 처리 방침 명문화. 자동화 가능한 변환은 변환 함수로, 수동 결정 필요한 사항은 SHACL `sh:or` 또는 별도 property로 분리.

---

## 섹션 4. Rule 3 적용 사례집

본 사례집은 Rule 3(의미 일치도) 적용 케이스를 일관 형식으로 등록하여 **향후 다른 TTA 표준 작업에서 직접 참조** 가능하도록 한다.

### Rule 3 적용 기준 (재확인)

> Rule 3은 다음 조건을 모두 만족할 때 적용:
> (1) TTA 표준이 N/A 또는 출처 부재 명시
> (2) DCMI(dcterms), DataCite, re3data에 직접 대응 어휘 부재
> (3) Schema.org 또는 다른 글로벌 어휘 중 의미상 가장 가까운 매핑 존재

### 사례집 #1 — TTA-0976-327 Unit (FileSizeUnitType)

| 항목 | 내용 |
|---|---|
| tta_inventory_id | TTA-0976-327 |
| TTA 원본 정의 | 파일 <Size> 요소의 단위를 기술함. 통제어: Byte / Mega Byte / Giga Byte / Tera Byte |
| TTA 출처 명시 | "관련 출처: N/A" (line 1222) |
| DCMI/DataCite/re3data 부재 확인 | dcterms:extent는 단일 단위(byte), DataCite size는 자유 텍스트, re3data size는 단일 값. 단위 분리 없음 |
| 채택된 매핑 | **schema:unitText** — 측정 단위를 텍스트로 표현하는 정확한 의미 |
| 매핑 신뢰도 | secondary, medium |
| 근거 | Schema.org schema:unitText는 PropertyValue/QuantitativeValue의 단위 표기용. 약어(MB/GB/TB) 또는 풀네임 모두 허용 |
| Phase C 처리 | bytes 정규화 + dcat:byteSize 호환성 확보. 또는 schema:unitText로 단위 보존 |

### 사례집 #2 — (현재까지 없음)

Step 3 + Step 4 작업 중 추가 Rule 3 사례 발견되지 않음. Step 4의 Contact 항목들(C8/D11/F11)은 표면적으로는 N/A이지만 schema:contactPoint와 dcat:contactPoint 모두 존재 → Rule 4(DCAT v3 우선)로 처리됨. Rule 3 적용 불요.

### 향후 표준에서 Rule 3 활용 가이드

다른 TTA 표준 작업 시 Rule 3 적용 후보 식별 패턴:
- **단위/측정 관련 항목**: FileSize Unit과 같은 측정 보조 정보 (schema:unitCode/unitText)
- **시각/청각 미디어 속성**: 해상도/비트레이트 등 (schema:bitrate/encodingFormat)
- **사람 메타데이터 보조**: 이름 분리/직함 등 (schema:givenName/jobTitle)

이러한 패턴 발견 시 사례집에 추가 등록.

---

## 섹션 5. PG606 피드백 패키지

PG606에 정식 보고할 수 있는 형태로 정리.

### 5.1 표준 결함 (수정 권고) — 4건

#### 5.1.1 본문 vs 부록 카디널리티 상충 (2건)

| 항목 | 본문 | 부록 II-2 | 우선순위 |
|---|---|---|---|
| D2.1 IdentifierType | "반드시 기술" (M) | O | High |
| D5 Publisher | "반드시 기술" (M) | R | High |

**권고 사항**: 차기 표준 개정 시 본문 설명과 부록 카디널리티 표를 일관 검증. 본문 "반드시 기술" 문구를 부록 정의에 정확히 동기화 (M으로 통일하거나, 본문을 "권고"로 약화).

#### 5.1.2 부록 II-2 PDF 표 손상 (1건)

| 항목 | 위치 | 우선순위 |
|---|---|---|
| D14 AccessType, D15 AccessRestriction | 부록 II-2 line 1819-1820 (PDF wrap 손상) | Medium |

**권고 사항**: PDF 원본 확인 후 정정. 다른 페이지 표도 표 wrap 점검 권장.

#### 5.1.3 FileType "other" 값의 catchall 패턴 (1건)

| 항목 | 위치 | 우선순위 |
|---|---|---|
| F17 Type 통제어 (FileType, line 1187) | 부록 II-1 통제어 | Medium |

**권고 사항**: DCMI Type Vocabulary는 정확히 12개 표준 타입만 정의 (의도적 closed enum). TTA가 'other'를 추가하면 자동 분류 실패. **표준 개정 시 'other' 제거 권고**.

### 5.2 어휘 격차 (글로벌 표준 정합성) — 3개 영역

#### 5.2.1 DCAT v3 (2024) 정합성

본 표준은 2017년 발행. DCAT v3 (2024-08-22)와 다음 격차:
- DCAT v3의 DataService/DatasetSeries/Relationship 3개 클래스 미반영
- DCAT v3의 dcat:hasVersion/previousVersion/inSeries 4계층 시리즈 표현 부재

**권고 사항**: 차기 개정 시 DCAT v3 어휘 도입 검토. 특히 DatasetSeries는 본 표준의 Collection 계층과 의미 가까움.

#### 5.2.2 DataCite v4.5 (2024) 정합성

본 표준은 DataCite의 일부 어휘만 인용 (titleType, dateType, contributorType, identifierType). 미반영:
- v4.5의 ResourceType + ResourceTypeGeneral (자원 분류)
- v4.5의 RelatedIdentifier + RelationType (자원 관계 그래프)
- v4.5의 GeoLocation 구조화 (Place/Point/Box)
- v4.5의 FundingReference (자금 정보)
- v4.5의 RelatedItem (관계된 자원)

**권고 사항**: 차기 개정 시 RelatedIdentifier/RelationType과 FundingReference 도입을 우선 검토. 연구데이터 표준에서 출처·자금 정보가 점점 중요해짐.

#### 5.2.3 SKOS Concept 패턴 도입 권장

본 표준의 Subject Class는 SKOS Concept 패턴으로 자연스럽게 표현 가능. 차기 개정 시 SKOS 어휘 명시:
- `dcterms:subject` → `skos:Concept`
- `SubjectScheme` → `skos:inScheme` (skos:ConceptScheme)
- `SubjectID` → `skos:notation`
- `SubjectName` → `skos:prefLabel`

### 5.3 TTA 고유 개념 (보존 권장) — 2건

#### 5.3.1 4계층 구조 (Repository/Collection/Dataset/File)

DCAT v3는 3계층(Catalog/Dataset/Distribution). TTA의 4계층은 한국 연구데이터 생태계의 특수성 반영 (특히 Collection 계층이 부서/연구과제 단위 그룹화를 표현).

**권고 사항**: 4계층 구조 유지. 단, dcat:Catalog와의 매핑 규칙 명문화 (Repository ⊃ Catalog ⊃ Collection... 또는 Collection ↔ dcat:DatasetSeries 등 검토).

#### 5.3.2 UCI (한국 콘텐츠 식별체계)

DataCite relatedIdentifierType에 UCI 미포함. 한국 콘텐츠 생태계의 표준 식별자.

**권고 사항**: 본 표준에서 UCI 보존. 별도 제안서로 DataCite Working Group에 UCI 등록 요청 가능 (SC42 기여 후보 — 섹션 6 참조).

### 5.4 PG606 보고 패키지 종합

| 영역 | 사례 수 | 우선순위 |
|---|---|---|
| 표준 결함 (5.1) | 4건 | High 2 + Medium 2 |
| 어휘 격차 (5.2) | 3개 영역 | Medium |
| TTA 고유 개념 보존 (5.3) | 2건 | Low (개정 시 검토) |
| **합계** | **9건** | — |

---

## 섹션 6. SC42 기여 후보

ISO/IEC JTC1 SC42에 한국 기여로 제안 가능한 항목.

### 6.1 후보 1 — UCI (Universal Content Identifier) 어휘 추가

| 항목 | 내용 |
|---|---|
| 기여 유형 | **어휘 추가** (DataCite RelatedIdentifierType에 UCI 등록) |
| 근거 데이터 | TTAK.KO-10.0976 통제어 CV-088. 한국 국가표준. 국내 다수 콘텐츠 생태계 활용 |
| 권장 채널 | DataCite Working Group → ISO/IEC SC42 SC36 (정보학) → DCAT-AP 확장 |
| 예상 호응도 | **Medium** — 한국 외 활용도 낮으나, 글로벌 식별자 다양성 가치 인정 |
| 다음 단계 | 기여 제안서 초안 작성. UCI 사용 통계 + 거버넌스 정보 첨부 |

### 6.2 후보 2 — 4계층 구조 패턴 (Repository/Collection/Dataset/File)

| 항목 | 내용 |
|---|---|
| 기여 유형 | **패턴 제안** (DCAT 또는 ISO 23081 메타데이터 표준에 4계층 옵션 추가) |
| 근거 데이터 | TTAK.KO-10.0976 + KISTI/생태원/산림과학원 등 6개 한국 연구기관 활용 사례 |
| 권장 채널 | DCAT Working Group + ISO TC46/SC11 (Archives/records management) |
| 예상 호응도 | **High** — 특히 ISO 23081의 다단계 메타데이터 모델과 잘 부합. 4계층 구조의 효용성을 데이터로 입증 가능 |
| 다음 단계 | 6개 한국 기관 활용 사례 연구 보고서 + dcat:Catalog 확장 제안 |

### 6.3 후보 3 — Boolean Activation Slot 패턴 (DQV 통합)

| 항목 | 내용 |
|---|---|
| 기여 유형 | **베스트 프랙티스 (Best Practice) 제안** |
| 근거 데이터 | Decision-Q4 결정의 결과. TTA-0976-022 QualityManagement="yes" → DQV 어휘 활성화 |
| 권장 채널 | DQV Working Group (W3C) + DCAT-AP RAI Working Group |
| 예상 호응도 | **High** — 단순 boolean 한 비트가 풍부한 어휘 entrypoint 역할을 하는 패턴은 어휘 진화 메커니즘으로 유용 |
| 다음 단계 | 패턴 명세서 작성. 다른 표준에서의 일반화 가능성 입증 |

### 6.4 후보 4 — Coverage dual-purpose의 sh:or 처리 패턴

| 항목 | 내용 |
|---|---|
| 기여 유형 | **베스트 프랙티스** (SHACL 패턴) |
| 근거 데이터 | Decision-3.1 + TTA-0976-323 Coverage 처리 |
| 권장 채널 | SHACL Best Practices Working Group (W3C) |
| 예상 호응도 | Medium — SHACL `sh:or`의 실용 사례로 유용 |
| 다음 단계 | 패턴 사례집에 등록. SHACL 커뮤니티에 공유 |

### 6.5 SC42 기여 종합

| 후보 | 기여 유형 | 호응도 | 우선순위 |
|---|---|---|---|
| 6.1 UCI 어휘 추가 | 어휘 추가 | Medium | Low (한국 외 활용도 한계) |
| 6.2 4계층 구조 패턴 | 패턴 제안 | High | **High** (가장 가치 있는 한국 기여) |
| 6.3 Boolean Activation Slot | 베스트 프랙티스 | High | Medium |
| 6.4 Coverage sh:or | 베스트 프랙티스 | Medium | Low |

**권장 우선순위**: 6.2 (4계층 구조) → 6.3 (Boolean Activation Slot) → 6.1 (UCI) → 6.4 (sh:or)

---

## 섹션 7. 통제어 매핑 부재 2건 상세 분석 (섹션 1과 별도)

섹션 1에서 일반 분석. 본 섹션은 통제어 부재만 집중 분석.

### 7.1 CV-088 UCI 상세 분석

#### 한국 연구 환경에서의 사용 사례

- KISTI 한국과학기술정보연구원: 연구데이터 식별자 체계
- 한국저작권위원회: 디지털 콘텐츠 식별
- 국립중앙도서관: 디지털 자료 식별
- 한국정보화진흥원(NIA): AI 학습 데이터 식별
- 일부 학회·기관: 연구 산출물 식별

→ 연 수십만 건의 콘텐츠가 UCI로 식별되는 인프라 존재.

#### 글로벌 표준에 추가 제안 시 예상 호응도

| 채널 | 호응도 | 사유 |
|---|---|---|
| DataCite | **Medium** | DataCite의 RelatedIdentifierType은 의도적으로 다양한 식별자를 수용. UCI 추가 가능성 높음 |
| ISO 8459 (정보의 자동화 식별) | Low | 이미 다수의 식별자 표준 존재 |
| IETF (URN namespace) | High | URN namespace 등록 가능성. urn:uci: 등 |
| W3C | Low | W3C는 일반 IRI 권장 |

#### 권장 전략

1. **단기**: 본 TTA 표준에서 UCI 보존
2. **중기**: DataCite WG에 UCI 추가 제안 (사용 통계 + 거버넌스 정보)
3. **장기**: URN namespace 등록 (urn:uci:) — IANA 등록 가능

### 7.2 CV-069 'other' (FileType) 상세 분석

#### 한국 연구 환경에서의 사용 사례

- 일반적인 사용자 자유도 보장 목적
- 분류 어려운 케이스 (예: 복합 미디어, 새 미디어 형식)
- 사용 빈도: 낮음 (대부분 11개 표준 타입 중 적합한 것 선택 가능)

#### 글로벌 표준에 추가 제안 시 예상 호응도

DCMI Type Vocabulary는 의도적으로 closed enum 12개. 'other' 추가는 표준 어휘 설계 철학과 충돌 → **호응도 None**.

#### 권장 전략

1. **TTA 표준에서 'other' 제거** (PG606 권고)
2. 부득이 'other' 유지 시: ttaap 자체 namespace에서만 사용. dctype:으로 매핑하지 않음

### 7.3 통제어 매핑 부재 종합

| CV | 사례 | 한국 사용 강도 | 글로벌 기여 가능성 |
|---|---|---|---|
| CV-088 UCI | 한국 콘텐츠 식별 | High (수십만 건) | Medium (DataCite 추가 가능) |
| CV-069 other (FileType) | 분류 catchall | Low | None (제거 권고) |

→ UCI는 SC42 기여 후보로 우선 추진. 'other'는 TTA 표준에서 제거 권고.

---

## 분석 종합

| 분석 영역 | 발견 건수 |
|---|---|
| 매핑 부재 (none) | 2 |
| 카디널리티 충돌 | 4 |
| 의미 차이 | 9 |
| Rule 3 사례집 | 1 |
| PG606 피드백 (3개 영역) | 9 |
| SC42 기여 후보 | 4 |
| 통제어 부재 (상세) | 2 |
| **총 발견 사항** | **31** |

모든 발견은 Phase C 작업 또는 후속 PG606/SC42 활동으로 명확한 행동 경로 식별됨.
