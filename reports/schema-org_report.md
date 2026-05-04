# Schema.org 표준 인벤토리 추출 리포트

- 추출 일자: 2026-05-03
- 출처: Schema.org current vocabulary — https://schema.org/
- 명세 캐시: `D:\ARD\sources\schema-org.jsonld` (canonical JSON-LD vocabulary, 약 1.5MB)
- 출력: `D:\ARD\inventory\schema-org.csv` (133개 행)

## 추출 항목 수

| term_type | 개수 |
|---|---|
| Class | 16 |
| Property | 117 |
| Enumeration | 0 |
| **합계** | **133** |

Schema.org는 600+ 클래스와 1300+ 속성을 가진 거대 어휘이므로, 프로젝트 컨텍스트의 추출 범위 원칙("AI Ready Data와 직접 관련된 타입/속성만")에 따라 데이터셋 메타데이터에 직접 관련된 항목만 선별 추출함.

## 포함된 16개 클래스

**핵심 데이터셋 타입 (6개):** Dataset, DataCatalog, DataDownload, DataFeed, DataFeedItem, MediaObject (DataDownload의 부모)

**상속 체인을 위한 상위 타입 (2개):** CreativeWork, Thing — Dataset/DataCatalog가 상속하는 속성들의 출처

**행위자 타입 (2개):** Person, Organization

**공간 타입 (1개):** Place

**연락처·주소 타입 (2개):** PostalAddress, ContactPoint

**값·분류 타입 (3개):** PropertyValue, DefinedTerm, DefinedTermSet (마지막 2개는 [BORDERLINE])

## 포함된 117개 속성 (출처 클래스별)

| 출처 클래스 | 속성 개수 | 주요 속성 |
|---|---|---|
| Thing | 11 | name, description, identifier, url, sameAs, alternateName, image, additionalType, disambiguatingDescription, mainEntityOfPage, subjectOf |
| CreativeWork | 41 | author, citation, conditionsOfAccess, contentLocation, contributor, copyrightHolder/Notice/Year, countryOfOrigin, creator, creditText, dateCreated, dateModified, datePublished, encoding, encodingFormat, funder, funding, hasPart, inLanguage, isBasedOn, isPartOf, keywords, license, locationCreated, maintainer, producer, provider, publisher, sdDatePublished, sdLicense, sdPublisher, sourceOrganization, spatial, spatialCoverage, temporal, temporalCoverage, usageInfo, version, about, abstract |
| Dataset | 6 | distribution, includedInDataCatalog, issn, measurementMethod, measurementTechnique, variableMeasured |
| DataCatalog | 1 | dataset |
| DataFeed | 1 | dataFeedElement |
| DataFeedItem | 2 | item, dateDeleted |
| MediaObject | 9 | contentUrl, contentSize, sha256, uploadDate, height, width, duration, bitrate, embedUrl |
| Person | 10 | givenName, familyName, jobTitle, worksFor, affiliation, birthDate, gender, knowsAbout, knowsLanguage, alumniOf |
| Organization | 7 | founder, foundingDate, legalName, logo, memberOf, parentOrganization, department |
| Place | 4 | geo, latitude, longitude, hasMap |
| PostalAddress | 5 | streetAddress, addressLocality, addressRegion, postalCode, addressCountry |
| ContactPoint | 4 | contactType, availableLanguage, hoursAvailable, productSupported |
| 다중 도메인 (사람·조직·장소·연락처) | 4 | address, email, telephone, faxNumber, contactPoint, areaServed |
| PropertyValue | 7 | value, propertyID, unitCode, unitText, maxValue, minValue, valueReference |
| DefinedTerm/Set | 3 | termCode, inDefinedTermSet, hasDefinedTerm |

## concept_tag 분포

| concept_tag | 개수 |
|---|---|
| uncategorized | 35 |
| actor.contact | 13 |
| identification.identifier | 6 |
| spatial.location | 6 |
| temporal.creation | 5 |
| actor.creator | 7 |
| actor.contributor | 7 |
| structure.dataset | 7 |
| distribution.url | 8 |
| identification.keyword | 5 |
| identification.title | 3 |
| identification.description | 4 |
| spatial.coverage | 4 |
| rights.access | 4 |
| temporal.coverage | 3 |
| structure.recordset | 3 |
| quality.general | 3 |
| temporal.modification | 2 |
| rights.license | 2 |
| actor.publisher | 2 |
| distribution.size | 1 |
| distribution.media_type | 1 |

`uncategorized` 35개의 주요 구성:
- 구조적 상위 클래스 (Thing, CreativeWork, Person, Organization, MediaObject) 5개
- 미디어 객체 정량 속성 (height, width, bitrate, sha256, value 등) 8개
- 조직·사람 비-연락처 속성 (memberOf, parentOrganization, department, alumniOf, knowsAbout, knowsLanguage, birthDate, gender) 8개
- 단위·값 (unitCode, unitText, maxValue, minValue, valueReference) 5개
- 기타 (additionalType, image, mainEntityOfPage, subjectOf, version, logo, inLanguage, about 등) 9개

`actor.contact` 13개가 가장 많은 의미 태그인 점은 Person/Organization/Place/ContactPoint/PostalAddress가 모두 포함되어 있기 때문.

## 플래그 표시 항목

| 플래그 | 개수 | 항목 |
|---|---|---|
| [CHECK] | 0 | (모든 정의 JSON-LD에서 직접 검증) |
| [BORDERLINE] | 5 | DefinedTerm, DefinedTermSet, termCode, inDefinedTermSet, hasDefinedTerm (모두 pending.schema.org 영역) |
| [TRUNCATED] | 2 | PropertyValue, value (정의가 길어 핵심만 발췌) |
| [TRANSLATION] | 0 | 없음 |

### [BORDERLINE] 상세

DefinedTerm, DefinedTermSet 및 그들의 3개 속성은 spec에서 `schema:isPartOf <https://pending.schema.org>`로 표시되어 있어 프로젝트 컨텍스트의 제외 기준("pending 영역의 실험적 타입")에 해당. 그러나 user가 명시적으로 "필수 추가" 목록에 포함시켰으므로 인벤토리에 포함하되 [BORDERLINE] 표시. 후속 결정에서 제외 시 INV-1015, INV-1016, INV-1131, INV-1132, INV-1133 일괄 삭제 가능.

### [TRUNCATED] 상세

- **PropertyValue (INV-1014)**: 원문에 `\n\n` 줄바꿈으로 구분된 추가 사용 지침이 있음. 본 인벤토리는 핵심 정의 + 사용 지침 첫 줄까지 포함하고 줄바꿈을 공백으로 치환.
- **value (INV-1124)**: 원문에 사용 가능 데이터 타입에 대한 상세 가이드라인이 있음. 본 인벤토리는 핵심 type-value 정보만 발췌.

## 추출 원칙

### 포함

- **핵심 데이터셋 클래스 6종**: Dataset/DataCatalog/DataDownload/DataFeed/DataFeedItem/MediaObject. 사용자 요청 모두 반영.
- **상속용 상위 클래스 2종**: CreativeWork (Dataset 부모), Thing (모든 클래스 최상위). 상속 속성의 출처를 명시하기 위해 클래스 자체를 포함.
- **행위자·장소·연락처 8종**: Person, Organization, Place, PostalAddress, ContactPoint. 데이터셋 메타데이터의 actor·spatial 영역.
- **값·분류 3종**: PropertyValue (variableMeasured 대상), DefinedTerm/DefinedTermSet (keywords·theme).
- **117개 속성**: 데이터셋 메타데이터에 직접 관련된 속성. CreativeWork의 ~80개 속성 중 actor/temporal/rights/structure/distribution/spatial 관련 41개만 추출. Schema.org가 정의한 전체 ~1300개 속성 중 ~9% 선별.

### 제외

- **Schema.org 도메인 특화 타입**: Recipe, Movie, Event, Product, Book, Course, Article, MusicRecording, VideoObject 등. 사용자 요청에 따른 명시적 제외.
- **CreativeWork 비-데이터셋 속성** (~40개 제외): accessibilityFeature, accessibilityHazard, accessibilitySummary, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accountablePerson, acquireLicensePage, aggregateRating, alternativeHeadline, archivedAt, assesses, associatedMedia, audience, audio, award, character, comment, commentCount, contentRating, contentReferenceTime, correction, creativeWorkStatus, digitalSourceType, discussionUrl, displayLocation, editEIDR, editor, educationalAlignment, educationalLevel, educationalUse, exampleOfWork, expires, genre, headline, interactionStatistic, interactivityType, interpretedAsClaim, isAccessibleForFree, isFamilyFriendly, learningResourceType, mainEntity, material, materialExtent, mentions, offers, pattern, position, publication, publisherImprint, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, size, sponsor, teaches, text, thumbnail, thumbnailUrl, timeRequired, translationOfWork, translator, typicalAgeRange, video, wordCount, workExample, workTranslation. 모두 데이터셋 메타데이터와 직접 무관.
- **pending.schema.org 영역**: DefinedTerm/DefinedTermSet 외에는 모두 제외 (사용자 명시적 제외 기준).
- **deprecated 속성**: schema:supersededBy로 폐기된 속성들 (catalog, includedDataCatalog 등 옛 이름) 제외.

### 경계 사례 처리 정책

사용자 지침: "어떤 속성이 포함 대상인지 모호하면 일단 포함시키고 notes 컬럼에 [BORDERLINE]을 표기" — 본 인벤토리에서 [BORDERLINE]은 pending.schema.org 명시 케이스 5개에만 적용. 다른 경계 속성(image, additionalType, version 등)은 dataset 메타데이터 통례적 사용을 인정하여 포함하되 [BORDERLINE] 미표시.

## 정의 출처 충실도

모든 133개 행의 definition은 `D:\ARD\sources\schema-org.jsonld`의 `rdfs:comment` 필드에서 직접 추출. WebFetch 결과는 검증·교차 확인 용도로만 사용.

**HTML 엔티티 변환 정책:**
- `&#x2014;` (em-dash) → `—` (Unicode em-dash) 변환 (예: ContactPoint 정의)
- `&#x000A;` 줄바꿈은 공백으로 치환 (CSV 호환성)
- markdown wiki-link `[[Term]]`은 원문 보존
- 외부 링크 `[text](url)`도 원문 보존

## cardinality 일괄 처리

Schema.org는 cardinality를 명시하지 않음 (도메인/range는 inclusive — `domainIncludes`/`rangeIncludes` 사용으로 다중 가능). 모든 133개 행 cardinality는 `unspecified`.

## equivalent_terms 사전 채움

Schema.org가 `owl:equivalentClass` 또는 `owl:equivalentProperty`로 명시한 매핑을 사전 기재 + 명백한 cross-vocabulary 매핑 추가:

**owl:equivalentClass 명시 (10건):**
- schema:Dataset → dcat:Dataset, dctype:Dataset, void:Dataset
- schema:DataCatalog → dcat:Catalog
- schema:DataDownload → dcat:Distribution
- schema:Person → foaf:Person
- schema:Organization → gs1:Organization, fibo-fnd-org-org:Organization
- schema:Place → cmns-loc:Location
- schema:PostalAddress → gs1:PostalAddress, unece:TradeAddress, fibo-fnd-plc-adr:PostalAddress, cmns-loc:Address
- schema:ContactPoint → gs1:ContactPoint, fibo-fnd-org-org:ContactPoint, vcard:VCard

**owl:equivalentProperty 명시 (다수):** description, identifier, name, creator, publisher, contributor, sameAs/url, image, dateCreated, license, address, telephone, email, distribution 등 다수가 dct:/dcat:/foaf:/gs1: 등과 동등 명시.

**확장 매핑 (4개 표준 cross-reference, 본 작업 대상):**
- schema:Dataset → croissant:Dataset (extends, not equivalent)
- schema:dateCreated → prov:generatedAtTime
- schema:isBasedOn → prov:wasDerivedFrom
- schema:creator → prov:Creator
- schema:publisher → prov:Publisher
- schema:copyrightHolder → prov:RightsHolder, dcterms:rightsHolder
- 외 다수 (master_inventory에서 양방향 보강 예정)

## 다음 단계 권장 검토 사항

1. **DefinedTerm/DefinedTermSet 5개 [BORDERLINE] 처리 확정**: pending.schema.org이지만 사용자 명시 요청. 유지/제거 결정.
2. **`uncategorized` 35개 재검토**: Person/Organization의 birthDate, gender, jobTitle, worksFor는 actor.* 의 어느 하위로 분류 가능한지 검토. (현재 actor.creator로 분류한 것들과의 일관성 점검)
3. **수치·단위 속성 (PropertyValue/QuantitativeValue)의 태그 보완**: value, unitCode, unitText, maxValue, minValue 등이 모두 uncategorized. `quality.general` 또는 새 `measurement.value` 태그 도입 검토.
4. **Croissant이 의미 변경한 schema:distribution**: notes에 표시했으나 master_inventory에서 별도 cross-reference 필요. (Croissant ↔ Schema.org 통합 행에서 명시)
5. **Schema.org의 schema:image, schema:additionalType, schema:mainEntityOfPage 등 메타-구조 속성**: AI Ready Data 표현에 직접 쓰이지 않으나 다른 표준 매핑을 위해 포함. 통합 단계에서 actually 사용되지 않으면 master_inventory에서 제외 검토.
