# TTAK.KO-10.0976 요소 매핑표

본 표는 TTA 표준의 79개 요소(컬렉션 12 + 데이터셋 15 + 파일 19 + 리포지토리 21, 그리고 하위 요소 변형) 전체를 JSON-LD 어휘와 SHACL 제약에 1:1 매핑한다.

**범례**:
- 유형: Property / SEP(Syntax Encoding Property) / Class / CVP(Controlled Vocabulary Property)
- M/R/O: Mandatory / Recommended / Optional

**공통 네임스페이스**:
- `tta:` `https://standards.tta.or.kr/ai-ready/research-data/v1#` (본 사업 잠정 IRI)
- `dcat:` `http://www.w3.org/ns/dcat#`
- `dct:` `http://purl.org/dc/terms/`
- `dcmitype:` `http://purl.org/dc/dcmitype/`
- `prov:` `http://www.w3.org/ns/prov#`
- `schema:` `https://schema.org/`
- `skos:` `http://www.w3.org/2004/02/skos/core#`

---

## 6.2 컬렉션 메타데이터 (C1~C12)

| TTA ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | Collection | Class | O | `Collection` | `dcat:Catalog` (+ `dcmitype:Collection`) | 최상위 클래스 |
| C2 | Identifier | Property | M | `identifier` | `dct:identifier` | 식별자 |
| C2.1 | IdentifierType | CVP | M | `identifierType` | `tta:identifierType` | 통제어: IdentifierType |
| C3 | Title | Property | M | `title` | `dct:title` | `@language` 권고 |
| C3.1 | TitleType | CVP | O | `titleType` | `tta:titleType` | 통제어: TitleType |
| C4 | Date | SEP | R | `date` | `dct:date` | ISO 8601 (YYYY-MM-DD) |
| C4.1 | DateType | CVP | M | `dateType` | `tta:dateType` | 통제어: CollectionDateType |
| C5 | Description | Property | R | `description` | `dct:description` | — |
| C6 | Subject | Class | R | `subject` | `dct:subject` | 객체로 SubjectScheme/ID/Name 포함 |
| C6.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` | 예: DFG |
| C6.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` | 코드값 |
| C6.3 | SubjectName | Property | M | `subjectName` | `skos:prefLabel` | 명칭 |
| C7 | Creator | Property | R | `creator` | `dct:creator` | 사람·조직 IRI 권고 |
| C8 | Contact | Property | R | `contact` | `tta:contact` | 이메일·전화·웹주소 |
| C9 | Rights | Property | R | `rights` | `dct:rights` | — |
| C10 | Keyword | Property | O | `keyword` | `dcat:keyword` | 자유 키워드 |
| C11 | AccessType | CVP | O | `accessType` | `tta:accessType` | 통제어: CollectionAccessType |
| C12 | AccessRestriction | CVP | O | `accessRestriction` | `tta:accessRestriction` | 통제어: CollectionAccessRestrictionType |

## 6.3 데이터셋 메타데이터 (D1~D15)

| TTA ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | Dataset | Class | O | `Dataset` | `dcat:Dataset` | 최상위 클래스 |
| D2 | Identifier | Property | M | `identifier` | `dct:identifier` | DOI 권고 |
| D2.1 | IdentifierType | CVP | M | `identifierType` | `tta:identifierType` | 통제어: IdentifierType |
| D3 | Title | Property | M | `title` | `dct:title` | — |
| D3.1 | TitleType | CVP | O | `titleType` | `tta:titleType` | — |
| D4 | Creator | Property | M | `creator` | `dct:creator` | — |
| D5 | Publisher | Property | M | `publisher` | `dct:publisher` | — |
| D6 | PublicationYear | SEP | M | `publicationYear` | `dct:issued` | YYYY (xsd:gYear) |
| D7 | Date | SEP | R | `date` | `dct:date` | YYYY-MM-DD |
| D7.1 | DateType | CVP | M | `dateType` | `tta:dateType` | 통제어: DatasetDateType |
| D8 | Description | Property | R | `description` | `dct:description` | — |
| D9 | Subject | Class | R | `subject` | `dct:subject` | — |
| D9.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` | — |
| D9.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` | — |
| D9.3 | SubjectName | Property | M | `subjectName` | `skos:prefLabel` | — |
| D10 | Contributor | Property | R | `contributor` | `dct:contributor` | — |
| D10.1 | ContributorType | CVP | M | `contributorType` | `tta:contributorType` | 통제어: ContributorType |
| D11 | Contact | Property | R | `contact` | `tta:contact` | — |
| D12 | Rights | Property | R | `rights` | `dct:rights` | — |
| D13 | Keyword | Property | O | `keyword` | `dcat:keyword` | — |
| D14 | AccessType | CVP | O | `accessType` | `tta:accessType` | — |
| D15 | AccessRestriction | CVP | O | `accessRestriction` | `tta:accessRestriction` | — |

## 6.4 파일 메타데이터 (F1~F19)

| TTA ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | File | Class | O | `File` | `dcat:Distribution` (+ `schema:DataDownload`) | 최상위 클래스 |
| F2 | Identifier | Property | M | `identifier` | `dct:identifier` | — |
| F2.1 | IdentifierType | CVP | M | `identifierType` | `tta:identifierType` | — |
| F3 | Title | Property | M | `title` | `dct:title` | — |
| F3.1 | TitleType | CVP | O | `titleType` | `tta:titleType` | — |
| F4 | Creator | Property | M | `creator` | `dct:creator` | — |
| F5 | Publisher | Property | M | `publisher` | `dct:publisher` | — |
| F6 | PublicationYear | SEP | M | `publicationYear` | `dct:issued` | — |
| F7 | Contributor | Property | R | `contributor` | `dct:contributor` | — |
| F7.1 | ContributorType | CVP | M | `contributorType` | `tta:contributorType` | — |
| F8 | Date | SEP | R | `date` | `dct:date` | — |
| F8.1 | DateType | CVP | M | `dateType` | `tta:dateType` | 통제어: FileDateType (=DatasetDateType) |
| F9 | Description | Property | R | `description` | `dct:description` | — |
| F10 | Subject | Class | R | `subject` | `dct:subject` | — |
| F10.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` | — |
| F10.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` | — |
| F10.3 | SubjectName | Property | M | `subjectName` | `skos:prefLabel` | — |
| F11 | Contact | Property | R | `contact` | `tta:contact` | — |
| F12 | Rights | Property | R | `rights` | `dct:rights` | — |
| F13 | Keyword | Property | O | `keyword` | `dcat:keyword` | — |
| F14 | AccessType | CVP | O | `accessType` | `tta:accessType` | — |
| F15 | AccessRestriction | CVP | O | `accessRestriction` | `tta:accessRestriction` | — |
| F16 | Coverage | SEP | O | `coverage` | `dct:coverage` | W3CDTF + 지역 |
| F17 | Type | CVP | O | `type` | `dct:type` | 통제어: FileType (DCMI) |
| F18 | Format | Property | O | `format` | `dct:format` | 확장자명 |
| F19 | Size | Property | O | `size` | `dcat:byteSize` | 단위 없는 숫자 |
| F19.1 | Unit | CVP | O | `sizeUnit` | `tta:sizeUnit` | 통제어: FileSizeUnitType |

## 7. 리포지토리 메타데이터 (R1~R21)

| TTA ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Repository | Class | O | `Repository` | `dcat:DataService` | 최상위 클래스 |
| R2 | RepositoryUrl | Property | M | `repositoryUrl` | `dcat:endpointURL` | — |
| R3 | Identifier | Property | M | `identifier` | `dct:identifier` | re3data·OpenDOAR·ROAR |
| R3.1 | IdentifierType | CVP | M | `identifierType` | `tta:identifierType` | — |
| R4 | RepositoryName | Property | M | `repositoryName` | `dct:title` | — |
| R4.1 | RepositoryNameType | CVP | O | `repositoryNameType` | `tta:titleType` | TitleType 통제어 재사용 |
| R5 | Type | CVP | M | `type` | `dct:type` | 통제어: RepositoryType |
| R6 | RepositoryLanguage | CVP | M | `repositoryLanguage` | `dct:language` | ISO-639-3 |
| R7 | Subject | Class | M | `subject` | `dct:subject` | — |
| R7.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` | — |
| R7.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` | — |
| R7.3 | SubjectName | Property | M | `subjectName` | `skos:prefLabel` | — |
| R8 | InstitutionName | Property | M | `institutionName` | `schema:legalName` | — |
| R9 | InstitutionCountry | CVP | M | `institutionCountry` | `schema:addressCountry` | ISO 3166-1 alpha-3 |
| R10 | DatabaseAccessType | CVP | M | `databaseAccessType` | `tta:databaseAccessType` | 통제어: DatabaseAccessType |
| R11 | DataAccessType | CVP | M | `dataAccessType` | `tta:dataAccessType` | 통제어: DatasetAccessType 재사용 |
| R12 | DataLicenseName | Property | M | `dataLicenseName` | `tta:dataLicenseName` | 자유 형식 (예: CC-BY-4.0) |
| R13 | DataLicenseUrl | Property | M | `dataLicenseUrl` | `dct:license` | URI (예: CC license URL) |
| R14 | DataUpload | CVP | M | `dataUpload` | `tta:dataUpload` | 통제어: DataUploadType |
| R15 | Versioning | CVP | M | `versioning` | `tta:versioning` | yes/no/unknown |
| R16 | EnhancedPublication | CVP | M | `enhancedPublication` | `tta:enhancedPublication` | yes/no/unknown |
| R17 | QualityManagement | CVP | M | `qualityManagement` | `tta:qualityManagement` | yes/no/unknown |
| R18 | Description | Property | R | `description` | `dct:description` | — |
| R19 | ResponsibilityType | CVP | O | `responsibilityType` | `tta:responsibilityType` | 통제어: ResponsibilityType |
| R20 | InstitutionContact | Property | O | `institutionContact` | `schema:contactPoint` | — |
| R21 | RepositoryContact | Property | O | `repositoryContact` | `tta:repositoryContact` | — |

---

## 통제어 (CVP) 14종

`shapes/`의 `sh:in` 제약에 인라인되어 있다. Phase B에서 SKOS Concept Scheme으로 분리 예정.

| 통제어 명 | 값 |
| --- | --- |
| CollectionAccessRestrictionType | `feeRequired`, `registration`, `institutional membership`, `non-registration`, `free`, `other` |
| CollectionAccessType | `open`, `embargoed`, `restricted`, `closed` |
| CollectionDateType | `Created`, `Updated`, `Deleted` |
| ContributorType | `ContactPerson`, `DataCollector`, `DataCurator`, `DataManager`, `Distributor`, `Editor`, `Funder`, `HostingInstitution`, `Producer`, `ProjectLeader`, `ProjectManager`, `ProjectMember`, `RegistrationAgency`, `RegistrationAuthority`, `RelatedPerson`, `Researcher`, `ResearchGroup`, `RightsHolder`, `Sponsor`, `Supervisor`, `WorkPackageLeader`, `Other` |
| DatabaseAccessType | `open`, `restricted`, `closed` |
| DatasetDateType | `Accepted`, `Available`, `Copyrighted`, `Collected`, `Created`, `Issued`, `Submitted`, `Updated`, `Valid` |
| DataUploadType | `open`, `restricted`, `closed` |
| EnhancedPublication | `yes`, `no`, `unknown` |
| FileSizeUnitType | `Byte`, `Mega Byte`, `Giga Byte`, `Tera Byte` |
| FileType (DCMI) | `Event`, `Image`, `InteractiveResource`, `MovingImage`, `PhysicalObject`, `Service`, `Software`, `Sound`, `StillImage`, `Text`, `other` |
| IdentifierType | `ARK`, `arXiv`, `bibcode`, `DOI`, `EAN13`, `EISSN`, `Handle`, `ISBN`, `ISSN`, `ISTC`, `LISSN`, `LSID`, `PMID`, `PURL`, `UPC`, `URL`, `URN`, `URI`, `UCI` |
| QualityManagement | `yes`, `no`, `unknown` |
| RepositoryType | `disciplinary`, `governmental`, `institutional`, `multidisciplinary`, `project-related`, `other` |
| ResponsibilityType | `funding`, `general`, `main`, `sponsoring`, `technical`, `other` |
| TitleType | `AlternativeTitle`, `Subtitle`, `TranslatedTitle`, `other` |
| Versioning | `yes`, `no`, `unknown` |
