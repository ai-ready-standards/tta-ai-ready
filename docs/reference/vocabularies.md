# 통제어 14종

본 표준의 부록 II-1에 정의된 14종 통제어 전체 값입니다. 모든 값은 SHACL `sh:in` 제약으로 검증됩니다.

## CollectionAccessType / DatasetAccessType / FileAccessType

리포지토리 접근 유형. 본 통제어는 `re3data.org`의 `dataAccessType`을 참조합니다.

| 값 | 의미 |
| --- | --- |
| `open` | 공개 — 누구나 접근 가능 |
| `embargoed` | 이용 지연 |
| `restricted` | 제한 공개 |
| `closed` | 비공개 |

사용 위치: C11, D14, F14

## CollectionAccessRestrictionType / DatasetAccessRestrictionType / FileAccessRestrictionType

접근 제한 유형. 본 통제어는 `re3data.org`의 `dataAccessRestriction`을 참조합니다.

| 값 | 의미 |
| --- | --- |
| `feeRequired` | 유료 |
| `registration` | 가입 필요 |
| `institutional membership` | 기관 회원제 |
| `non-registration` | 가입 불필요 |
| `free` | 무료 |
| `other` | 기타 |

사용 위치: C12, D15, F15

## CollectionDateType

컬렉션 이벤트 날짜 유형.

| 값 | 의미 |
| --- | --- |
| `Created` | 생성 |
| `Updated` | 갱신 |
| `Deleted` | 삭제 |

사용 위치: C4.1

## DatasetDateType / FileDateType

데이터셋·파일 이벤트 날짜 유형. DataCite의 `dateType`을 참조합니다.

| 값 | 의미 |
| --- | --- |
| `Accepted` | 수락 |
| `Available` | 이용 가능 |
| `Copyrighted` | 저작권 등록 |
| `Collected` | 수집 |
| `Created` | 생성 |
| `Issued` | 공개 |
| `Submitted` | 제출 |
| `Updated` | 갱신 |
| `Valid` | 유효 |

사용 위치: D7.1, F8.1

## ContributorType

기여자 유형. DataCite의 `contributorType`을 참조합니다.

`ContactPerson`, `DataCollector`, `DataCurator`, `DataManager`, `Distributor`, `Editor`, `Funder`, `HostingInstitution`, `Producer`, `ProjectLeader`, `ProjectManager`, `ProjectMember`, `RegistrationAgency`, `RegistrationAuthority`, `RelatedPerson`, `Researcher`, `ResearchGroup`, `RightsHolder`, `Sponsor`, `Supervisor`, `WorkPackageLeader`, `Other`

사용 위치: D10.1, F7.1

## DatabaseAccessType

리포지토리 데이터베이스 접근 유형.

| 값 | 의미 |
| --- | --- |
| `open` | 공개 |
| `restricted` | 제한 |
| `closed` | 비공개 |

사용 위치: R10

## DataUploadType

리포지토리 데이터 제출 유형.

| 값 | 의미 |
| --- | --- |
| `open` | 누구나 제출 가능 |
| `restricted` | 제한된 사용자만 |
| `closed` | 운영 기관 내부만 |

사용 위치: R14

## EnhancedPublication / QualityManagement / Versioning

운영 정책 yes/no/unknown 통제어.

| 값 | 의미 |
| --- | --- |
| `yes` | 지원 |
| `no` | 미지원 |
| `unknown` | 알 수 없음 |

사용 위치: R15, R16, R17

## FileType

파일 유형. DCMI의 Type 어휘를 참조합니다.

`Event`, `Image`, `InteractiveResource`, `MovingImage`, `PhysicalObject`, `Service`, `Software`, `Sound`, `StillImage`, `Text`, `other`

사용 위치: F17

## FileSizeUnitType

파일 크기 단위.

`Byte`, `Mega Byte`, `Giga Byte`, `Tera Byte`

사용 위치: F19.1

## IdentifierType

식별자 유형. DataCite의 `relatedIdentifierType`을 참조합니다.

`ARK`, `arXiv`, `bibcode`, `DOI`, `EAN13`, `EISSN`, `Handle`, `ISBN`, `ISSN`, `ISTC`, `LISSN`, `LSID`, `PMID`, `PURL`, `UPC`, `URL`, `URN`, `URI`, `UCI`

사용 위치: C2.1, D2.1, F2.1, R3.1

## RepositoryType

리포지토리 유형. `re3data.org`의 `type`을 참조합니다.

| 값 | 의미 |
| --- | --- |
| `disciplinary` | 분야별 |
| `governmental` | 정부 |
| `institutional` | 기관 |
| `multidisciplinary` | 다분야 |
| `project-related` | 프로젝트 관련 |
| `other` | 기타 |

사용 위치: R5

## ResponsibilityType

기관 책임 유형.

`funding`, `general`, `main`, `sponsoring`, `technical`, `other`

사용 위치: R19

## TitleType

제목 유형. DataCite를 참조합니다.

| 값 | 의미 |
| --- | --- |
| `AlternativeTitle` | 대체 제목 |
| `Subtitle` | 부제목 |
| `TranslatedTitle` | 번역 제목 |
| `other` | 기타 |

사용 위치: C3.1, D3.1, F3.1, R4.1

## SubjectScheme

주제 분류 체계. 본 표준에서는 `DFG`(Deutsche Forschungsgemeinschaft)만 예시로 제시되며, 다른 분류 체계 추가 사용 가능합니다.

사용 위치: C6.1, D9.1, F10.1, R7.1

---

## Phase B 예정

본 통제어 14종은 Phase B에서 [SKOS Concept Scheme](https://www.w3.org/TR/skos-reference/)으로 분리되어 IRI 기반 참조가 가능해질 예정입니다. 그 후에는 `tta:dateType "Created"` 대신 `tta:dateType <https://standards.tta.or.kr/cv/CollectionDateType/Created>`처럼 표현됩니다.
