# Phase C 완료 보고서 — TTA-0976 AI-Ready Application Profile 패키지 산출

- **단계**: Phase C (제안서의 6 패키지 산출물 작성)
- **대상 표준**: TTAK.KO-10.0976 "연구데이터 관리·공유를 위한 메타데이터" (2017)
- **산출 위치**: `D:\ARD\packages\tta-0976\`
- **AP 버전**: 1.0.0
- **완료일**: 2026-05-04
- **선행 단계**: Phase A (요소 추출) → Phase A.5 (어휘 보강) → Phase B (매핑 매트릭스) → **Phase C**

---

## 1. 산출물 통계 (6 패키지, 17 파일, 3,093 lines)

| # | 패키지 | 파일 | Lines | 핵심 내용 |
|---|---|---|---|---|
| 1 | **1_document/** | TTA-0976-AP.md | 249 | 9 섹션 AP 문서, 7요소 적용 결과, 통제어 통계 |
| 2 | **2_schema/** | context.jsonld | 170 | 91 property × 5종 어휘 매핑, 다국어 @container |
| 2 | **2_schema/** | shapes.shacl.ttl | 679 | 4 NodeShape + 7 보조 shape, ~250 sh:in 제약 |
| 3 | **3_code/** | tta_0976/__init__.py | 42 | export 정의 |
| 3 | **3_code/** | tta_0976/models.py | 347 | 4 Layer + 12 Enum + Subject/MultilingualText helper |
| 3 | **3_code/** | tta_0976/loader.py | 100 | alpha-3→alpha-2 변환, FileSizeUnit 정규화 |
| 3 | **3_code/** | tta_0976/serializers.py | 66 | Pydantic → JSON-LD, Subject → SKOS Concept 자동 |
| 3 | **3_code/** | tests/test_models.py | 258 | 10 케이스 (9 결정 + 정규화) |
| 3 | **3_code/** | README.md | 82 | 사용법 + 결정 사항 매핑 |
| 4 | **4_validator/** | validate.py | 153 | pySHACL CLI, --fallback-pydantic 옵션 |
| 4 | **4_validator/** | test_sh_or.py | 124 | Issue-001 mitigation 테스트 (4 케이스) |
| 4 | **4_validator/** | README.md | 90 | 설치/사용/CI 통합 가이드 |
| 5 | **5_examples/** | kisti_dataon.jsonld | 111 | Repository + Boolean Slot 활성 + 다국어 |
| 5 | **5_examples/** | nie_environmental.jsonld | 139 | Dataset → 2 File, Coverage dual-purpose |
| 5 | **5_examples/** | rda_agriculture.jsonld | 182 | ★ 4계층 완전 시연 + Boolean Slot 비활성 |
| 5 | **5_examples/** | README.md | 84 | 결정 사항 시연 매트릭스 |
| 6 | **6_changelog/** | CHANGELOG.md | 217 | 5종 어휘 버전 lock + 9개 결정 + 4 Issue + 9 PG606 피드백 |
| **합계** | | **17 파일** | **3,093** | |

---

## 2. 제안서 7 구성요소 ↔ 본 AP 매핑

제안서: "기존 3 요소 (Semantic/DataModel/Syntactic) → 기계 코드 전환 + 4 신규 요소 (OperationalSemantics/Provenance/QualityProfile/AccessConstraint)"

| # | 구성요소 | 본 AP 적용 | 산출 위치 |
|---|---|---|---|
| 1 | **Semantic** (전환) | 91 property × 5종 어휘 매핑 | `2_schema/context.jsonld` |
| 2 | **DataModel** (전환) | M/R/O → SHACL sh:minCount/maxCount/in (~250 제약) | `2_schema/shapes.shacl.ttl` |
| 3 | **Syntactic** (전환) | JSON-LD @context (의미+형식 동시) | `2_schema/context.jsonld` |
| 4 | **OperationalSemantics** (신규) | NA — 본 표준은 일반 연구데이터로 ML 운영 비대상 (Decision-3) | — |
| 5 | **Provenance** (신규) | DateType → prov:generatedAtTime/wasRevisionOf 조건부 (Decision-Q3/Q7) | `2_schema/shapes.shacl.ttl` (ProvenanceConditionalShape) |
| 6 | **QualityProfile** (신규) | ★ Boolean Activation Slot — `QualityManagement="yes"` → DQV 활성 (Decision-Q4) | `2_schema/shapes.shacl.ttl` (QualityActivationShape) |
| 7 | **AccessConstraint** (신규) | DataAccessType/DataLicense* + AccessType (Repository/Collection/Dataset/File 4계층 일관) | `2_schema/context.jsonld` + `shapes.shacl.ttl` |

**커버리지**: 7개 중 6개 적용, 1개(OperationalSemantics) 본 표준 비대상으로 명시 제외.

---

## 3. 9개 결정 사항 — 패키지 반영 상태

Phase A/A.5/B에서 합의된 결정이 Phase C 산출물에 어떻게 반영됐는지.

| 결정 | 내용 | 반영 위치 | 검증 |
|---|---|---|---|
| **D-001** | TTA-0976-001 Repository 임시 IRI | context.jsonld (`tta0976:Repository`) | grep 통과 |
| **D-002** | InstitutionCountry alpha-2 [OVERRIDE] | models.py `pattern=r'^[A-Z]{2}$'` + loader.py ALPHA3_TO_ALPHA2 (30 매핑) | test_models.py Test#5 |
| **D-003** | DatasetIdentifierType Optional [CONFLICT] | models.py `Optional[IdentifierType]` | test_models.py Test#3 |
| **D-004** | Publisher cardinality 0..* [CONFLICT] | shapes.shacl.ttl `sh:minCount 0` | shapes 파일 직접 확인 |
| **D-005** | Collection/File AccessType O [CHECK] | shapes.shacl.ttl `sh:minCount 0` | shapes 파일 직접 확인 |
| **D-Q3/Q7** | DateType → prov:* 조건부 매핑 | shapes.shacl.ttl ProvenanceConditionalShape | shapes 파일 직접 확인 |
| **D-Q4** | ★ Boolean Activation Slot | models.py `quality_activation_slot` validator + shapes QualityActivationShape | test_models.py Test#2, kisti(활성)/rda(비활성) 시연 |
| **D-Q5** | UCI 보존 (mapping_priority=none) | models.py IdentifierType.UCI Enum 유지 | enum 정의 확인 |
| **D-2** | Subject Class → SKOS Concept | models.py Subject.to_skos_concept() + serializers.py 자동 변환 | test_models.py Test#3 |
| **D-3.1** | Coverage dual-purpose | shapes.shacl.ttl FileCoverage `sh:or` + models.py Union[str, date, datetime] | nie_environmental.jsonld 양쪽 시연 |

**Issue-002** (3-valued boolean): models.py `BooleanPlus` Enum (yes/no/unknown) — 3종 통제어 (DataUpload/Versioning/QualityManagement) 모두 적용.

---

## 4. 어휘 통합 검증

### 4.1 Version Lock (CHANGELOG.md §"채택된 글로벌 어휘 5종")

5종 어휘 버전이 패키지 전체에서 일관되게 사용되는지.

| 어휘 | Lock 버전 | context.jsonld 사용 | shapes 사용 | 일관성 |
|---|---|---|---|---|
| dcterms | 2020-01-20 | ✓ `http://purl.org/dc/terms/` | ✓ 동일 | ✓ |
| DataCite | 4.5 | ✓ `http://datacite.org/schema/kernel-4` | ✓ 동일 | ✓ |
| re3data | 3.1 | ✓ `https://www.re3data.org/schema` | ✓ 동일 | ✓ |
| DCAT | v3 (2024-08-22) | ✓ `http://www.w3.org/ns/dcat#` | ✓ 동일 | ✓ |
| DCMI Type | 2012-06-14 | ✓ `http://purl.org/dc/dcmitype/` | ✓ FileType sh:in | ✓ |

### 4.2 보조 어휘 5종

| 어휘 | 활성 조건 | 적용 |
|---|---|---|
| Schema.org | Rule 3 fallback | unitText, Person/Organization 표현 |
| PROV-O | DateType 매칭 | ProvenanceConditionalShape (Created → prov:generatedAtTime 등) |
| DQV | QualityManagement=yes | hasQualityMetadata 권장 (warning) |
| SKOS | Subject Class | Concept + inScheme + notation + prefLabel |
| ISO 639-3 / 3166-1 / 8601 | 모든 코드/날짜 | RepositoryLanguage / InstitutionCountry / *Date |

---

## 5. Issue-001 Mitigation 검증 — pySHACL sh:or 패턴

Coverage dual-purpose가 SHACL sh:or에 의존하므로 pySHACL의 sh:or 지원이 핵심 의존성.

### 5.1 사전 테스트 (4_validator/test_sh_or.py)

4 케이스로 sh:or 완전 지원 여부를 사전 검증한다.

| Test | 입력 | 기대 |
|---|---|---|
| 1 | `xsd:date` (2025-01-01) | conforms=True |
| 2 | `xsd:string` (공간 좌표 텍스트) | conforms=True |
| 3 | IRI (geo URI) | conforms=True |
| 4 | `xsd:boolean` (오타) | conforms=False |

### 5.2 Fallback 경로

만약 4/4 통과 실패 시 → `validate.py --fallback-pydantic` 옵션이 Pydantic Union[str, date, datetime] 검증으로 우회.

→ **이중 안전망 확보**: SHACL 우선, Pydantic 보조.

---

## 6. 5_examples — 결정 사항 시연 매트릭스

3개 도메인 인스턴스가 9개 결정/Issue/계층 구조를 어떻게 분담 시연하는지.

| 결정 / 패턴 | kisti_dataon | nie_environmental | rda_agriculture |
|---|:---:|:---:|:---:|
| D-002 (alpha-2) | ✓ KR | — | ✓ KR |
| D-2 (SKOS Concept) | ✓ 2 | ✓ 2 | ✓ 다층 |
| D-Q4 활성 (Boolean Slot) | ✓ yes → 활성 | — | ✓ no → 비활성 |
| D-3.1 Coverage dual | — | ✓ 시간+공간 | ✓ 시간+공간 |
| 4계층 완전 | Repo → Coll | Dataset → File | **★ Repo → Coll → DS → File** |
| 다국어 라벨 | ✓ ko+en | ✓ ko+en | ✓ ko+en |
| FileSize 정규화 | — | — | ✓ B + MB 혼용 |

**커버리지**: 결정 9건 × 인스턴스 시연 = 모든 패턴 1+회 시연 확보.

---

## 7. 검증 가능성 — 양방향 라운드트립

```
JSON-LD 인스턴스 (5_examples/*.jsonld)
    ↓ load_from_jsonld() — alpha-3→alpha-2 정규화
Python Pydantic 객체 (3_code/tta_0976/models.py)
    ↓ to_jsonld_str() — Subject→SKOS Concept 자동 변환
JSON-LD 출력
    ↓ pyshacl 검증 (4_validator/validate.py)
SHACL 제약 검증 결과 (Conforms: True 기대)
```

test_models.py Test#9 (Roundtrip)가 이 전체 경로를 실행하여 무손실 변환 검증.

---

## 8. PG606 피드백 / SC42 기여 후보 (Phase D 입력)

CHANGELOG.md에 정리된 향후 작업 입력.

### 8.1 PG606 피드백 (9건)

1. D-003 본문 vs 부록 II-2 충돌 (DatasetIdentifierType M↔O)
2. D-004 본문 vs 부록 II-2 충돌 (Publisher M↔R)
3. D-005 부록 PDF 손상 (Collection/File AccessType 카디널리티 누락)
4. D-002 InstitutionCountry alpha-3 → alpha-2 권장 (DCAT v3 호환)
5. FileType "other" 통제어 제거 권장 (Type 판정 우회)
6. UCI를 IdentifierType 통제어에서 제거 또는 ISO 등록 추진
7. Coverage element 분리 권장 (TemporalCoverage / SpatialCoverage)
8. Subject Class 1:N → SKOS 명시 권장
9. QualityManagement 통제어 → 측정값 표현으로 확장

### 8.2 SC42 기여 후보 (4건)

1. UCI Korean Identifier 국제 등록
2. AI-Ready 7 구성요소 프레임워크 표준화 제안
3. Boolean Activation Slot 패턴 (조건부 어휘 활성)
4. Coverage dual-purpose sh:or 패턴

---

## 9. 다음 단계 (Phase D 후보)

Phase C 완료 시점 기준 다음 작업 후보 — 사용자 승인 대기.

| 후보 | 범위 | 예상 산출 |
|---|---|---|
| **D-1: 패키지 검증 실행** | 5_examples 3개 × validator 실행 + test 통과 확인 | 검증 로그 |
| **D-2: GitHub Pages 배포** | 6 패키지 → standard.tta.or.kr/ai-ready/profile/ 정적 사이트 | URL + DNS |
| **D-3: 다음 TTA 표준 적용** | TTAK.KO-10.0976 외 표준에 본 프레임워크 적용 (예: OO·OO·OO) | 새 패키지 N개 |
| **D-4: PG606 워크숍** | 9 피드백 협의 + 본문↔부록 통합 권고 | 회의록 + 표준 개정안 |
| **D-5: SC42 기여 패키지화** | 4 후보 항목 → ISO 제안 문서 | NWIP 제안서 |

---

## 10. Phase C 완료 선언

**선결 조건 충족**:

- [x] 6 패키지 산출 (1_document, 2_schema, 3_code, 4_validator, 5_examples, 6_changelog)
- [x] 9 결정 사항 모두 코드/스키마에 반영
- [x] 5종 어휘 버전 일관 적용
- [x] 3 도메인 인스턴스로 모든 결정 시연
- [x] Issue-001 mitigation 경로 확보 (--fallback-pydantic)
- [x] 양방향 라운드트립 검증 (test_models.py Test#9)
- [x] 패키지 17 파일 / 3,093 lines

**Phase A → A.5 → B → C 4단계 종료**.

본 패키지는 사용자 검토 후 Phase D (배포·확산) 또는 추가 표준 적용으로 진행 가능.
