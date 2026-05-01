# Repository (R1~R21)

리포지토리는 연구데이터를 **수집·저장·관리·서비스하는 시스템**의 메타데이터입니다. 24개 요소로 구성되며, **필수(M) 요소가 16개로 가장 엄격한** 클래스입니다.

## DCAT 매핑

`Repository` → `dcat:DataService`

DCAT v3에서 데이터 서비스를 표현하는 정식 클래스입니다.

## 요소 일람

| ID | 요소명 | 유형 | M/R/O | JSON-LD 키 |
| --- | --- | --- | --- | --- |
| R1 | Repository | Class | O | `Repository` |
| **R2** | **RepositoryUrl** | Property | **M** | `repositoryUrl` |
| **R3** | **Identifier** | Property | **M** | `identifier` |
| **R3.1** | **IdentifierType** | CVP | **M** | `identifierType` |
| **R4** | **RepositoryName** | Property | **M** | `repositoryName` |
| R4.1 | RepositoryNameType | CVP | O | `repositoryNameType` |
| **R5** | **Type** | CVP | **M** | `type` |
| **R6** | **RepositoryLanguage** | CVP | **M** | `repositoryLanguage` |
| **R7** | **Subject** | Class | **M** | `subject` |
| R7.1 | SubjectScheme | CVP | R | `subjectScheme` |
| R7.2 | SubjectID | Property | R | `subjectId` |
| **R7.3** | **SubjectName** | Property | **M** | `subjectName` |
| **R8** | **InstitutionName** | Property | **M** | `institutionName` |
| **R9** | **InstitutionCountry** | CVP | **M** | `institutionCountry` |
| **R10** | **DatabaseAccessType** | CVP | **M** | `databaseAccessType` |
| **R11** | **DataAccessType** | CVP | **M** | `dataAccessType` |
| **R12** | **DataLicenseName** | Property | **M** | `dataLicenseName` |
| **R13** | **DataLicenseUrl** | Property | **M** | `dataLicenseUrl` |
| **R14** | **DataUpload** | CVP | **M** | `dataUpload` |
| **R15** | **Versioning** | CVP | **M** | `versioning` |
| **R16** | **EnhancedPublication** | CVP | **M** | `enhancedPublication` |
| **R17** | **QualityManagement** | CVP | **M** | `qualityManagement` |
| R18 | Description | Property | R | `description` |
| R19 | ResponsibilityType | CVP | O | `responsibilityType` |
| R20 | InstitutionContact | Property | O | `institutionContact` |
| R21 | RepositoryContact | Property | O | `repositoryContact` |

## 식별자 정책

R3 Identifier는 **국제 리포지토리 레지스트리 등록 식별자** 사용을 권고합니다.

- [re3data.org](https://www.re3data.org/) — 연구 데이터 리포지토리 레지스트리
- [OpenDOAR](https://v2.sherpa.ac.uk/opendoar/) — 오픈 액세스 레지스트리
- [ROAR](http://roar.eprints.org/) — 오픈 리포지토리 레지스트리

## 국가 코드

R9 InstitutionCountry는 **ISO 3166-1 alpha-3 코드** (예: `KOR`, `USA`)를 사용합니다. SHACL 정규식으로 자동 검증됩니다.

## 라이선스 표현

- **R12 DataLicenseName** — 자유 형식 (예: `Creative Commons Attribution 4.0 International`)
- **R13 DataLicenseUrl** — 라이선스 URL (예: `https://creativecommons.org/licenses/by/4.0/`)

R13은 `dct:license` IRI로 매핑되어 자동 검증 시 IRI 형식을 강제합니다.

## 운영 메타데이터

본 클래스의 특징은 운영 정보(R14~R17)를 통제어로 표현한다는 점입니다.

- `R14 DataUpload` — 데이터 제출 유형: open / restricted / closed
- `R15 Versioning` — 버전 관리 지원: yes / no / unknown
- `R16 EnhancedPublication` — 출판물 상호참조: yes / no / unknown
- `R17 QualityManagement` — 품질관리: yes / no / unknown

→ 이 4개 요소가 모두 통제어이므로 리포지토리 비교·검색이 자동화됩니다.

## 예시

[:material-download: repository-narda.jsonld](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/examples/valid/repository-narda.jsonld){ .md-button .md-button--primary }

KISTI NARDA(국가연구데이터 리포지토리) 시나리오로 모든 16개 M 요소가 채워져 있습니다.

## SHACL Shape

[:material-file-code: repository.ttl 보기](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/shapes/repository.ttl)
