# DCAT v3 표준 인벤토리 추출 리포트

- 추출 일자: 2026-05-03
- 출처: W3C Data Catalog Vocabulary version 3 (DCAT 3) Recommendation, 2024-08-22 — https://www.w3.org/TR/vocab-dcat-3/
- 명세 캐시: `D:\ARD\sources\dcat-v3.ttl` (canonical DCAT 3 ontology, 약 196KB)
- 출력: `D:\ARD\inventory\dcat-v3.csv` (52개 행)

## 추출 항목 수

| term_type | dcat: 네임스페이스 |
|---|---|
| Class | 9 |
| Property | 43 |
| Enumeration | 0 |
| **합계** | **52** |

`dcat:` 네임스페이스의 모든 정의 용어를 포함함. .ttl 파일에서 `^dcat:` 패턴으로 추출한 결과 정확히 52개 매치 확인.

## concept_tag 분포

DCAT v3는 카탈로그·데이터셋·배포본 메타데이터 어휘로 24개 분류 태그 중 `structure.*`와 `distribution.*` 비중이 가장 큼. PROV-O와 달리 `uncategorized` 비율은 낮음.

| concept_tag | 개수 |
|---|---|
| uncategorized | 14 |
| structure.dataset | 13 |
| distribution.url | 9 |
| distribution.media_type | 3 |
| temporal.coverage | 3 |
| identification.keyword | 3 |
| spatial.coverage | 2 |
| provenance.derivation | 2 |
| spatial.location | 1 |
| distribution.size | 1 |
| actor.contact | 1 |

`uncategorized` 14개의 주요 구성: 추상 상위 클래스(Resource, Role, Relationship, Distribution), 시리즈 정렬 properties(first, last, prev, next, hasVersion, hasCurrentVersion, isVersionOf, hadRole, qualifiedRelation, version). 시리즈 정렬용 properties는 PROV-O의 한정 메커니즘과 유사하게 24개 태그 어디에도 매핑되지 않음.

## 플래그 표시 항목

| 플래그 | 개수 | 항목 |
|---|---|---|
| [CHECK] | 8 | accessService (no rdfs:domain), 6개 inverse-only properties, packageFormat (subPropertyOf 추정) |
| [BORDERLINE] | 0 | 없음 |
| [TRUNCATED] | 0 | 없음 (모든 정의가 단일 문장) |
| [TRANSLATION] | 0 | 없음 |

### [CHECK] 상세

**그룹 A — Inverse-only properties (정의가 부재):** DCAT v3에서 새로 도입된 6개 inverse 속성은 .ttl에서 `owl:inverseOf` 한 줄과 `rdfs:isDefinedBy`/`skos:changeNote`/`skos:scopeNote`만 갖고 자체 `skos:definition`이 없음.

| 속성 | inverse of | definition 차용 출처 |
|---|---|---|
| dcat:isDistributionOf | dcat:distribution | dcat:distribution의 skos:definition |
| dcat:isVersionOf | dcat:hasVersion | dcat:hasVersion의 skos:definition |
| dcat:inCatalog | dcat:resource | dcat:resource의 skos:definition |
| dcat:next | dcat:prev | dcat:prev의 skos:definition |
| dcat:nextVersion | dcat:previousVersion | dcat:previousVersion의 skos:definition |
| dcat:seriesMember | dcat:inSeries | dcat:inSeries의 skos:definition |

inverse-only 속성에는 모두 spec scopeNote `"This property MAY be used only in addition to its inverse, and it MUST NOT be used to replace it."`가 붙어있음 — 즉 의미는 역속성과 같다는 것이 명시되어 있어 차용이 정당함. 그래도 [CHECK] 표시 유지.

**그룹 B — accessService:** rdfs:domain이 .ttl에 선언되어 있지 않음 (rdfs:range는 dcat:DataService로 명시). spec 본문은 dcat:Distribution을 도메인으로 사용하나 온톨로지에는 형식적 제약 없음. domain 칸을 비우고 [CHECK] 표시.

**그룹 C — packageFormat subPropertyOf:** compressFormat과 유사하게 dcterms:format의 sub로 추정되나 .ttl 부분 읽기에서 확인하지 못함. notes에 [CHECK] 표시.

## 포함/제외 결정 주요 사례

### 포함

- **모든 dcat: 네임스페이스 용어 52개**: `^dcat:` 정규식 매치 기준으로 빠짐없이 포함.
- **inverse-only properties 6개**: 의미적으로 의존이 명시되어 있어 인벤토리에서 빼면 cross-reference에 구멍이 생김. 차용 정의 + [CHECK]로 처리.
- **DCAT 2/3에서 새로 추가된 속성**: notes에 "New property in DCAT 2/3" 표시.

### 제외

- **`dcat:Checksum`, `dcat:checksumValue`, `dcat:algorithm`** (WebFetch 1차 결과에 포함되었으나): .ttl을 직접 검증한 결과 dcat: 네임스페이스에 정의되지 않음. DCAT v3는 무결성 체크에 SPDX 어휘(spdx:checksum, spdx:Checksum)를 참조함. 인벤토리에서 제외.
- **`dcat:relation`** (WebFetch 1차 결과에 포함되었으나): .ttl에 정의되지 않음. WebFetch가 paraphrase 과정에서 생성한 환각으로 판단. 제외. `dcat:qualifiedRelation`은 별도 속성으로 존재하며 포함됨.
- **재사용되는 dcterms: 속성** (title, description, identifier, issued, modified, language, license, rights, accessRights, creator, publisher, conformsTo, isReferencedBy, hasPart, isPartOf, format, type, relation, temporal, spatial, accrualPeriodicity 등): DCAT v3는 데이터셋 메타데이터 표현에 이들을 강하게 권장하나 dcat: 네임스페이스가 아니므로 본 인벤토리에서 제외. 후속 단계에서 별도 DCMI Terms 인벤토리로 분리 또는 통합 단계에서 보강 결정 필요. 다음 사항 참조.
- **재사용되는 외부 어휘**: foaf: (homepage, primaryTopic, page, Document), vcard:Kind, prov:Attribution, prov:Role, prov:wasRevisionOf, skos:Concept, skos:ConceptScheme, dcterms:MediaType, dcterms:PeriodOfTime, dcterms:Location, xhv:first/last/prev — 본 인벤토리에서는 dcat:가 아니므로 제외하되 parent/domain/range 컬럼에는 prefix 그대로 표기.

## DCAT v3가 강하게 권장하는 dcterms: 속성 목록

후속 통합 단계에서 결정이 필요한 사항. DCAT v3 spec은 다음 dcterms: 속성을 normative하게 권장:

**식별·기술:**
- dcterms:title, dcterms:description, dcterms:identifier

**시간:**
- dcterms:issued (발행일), dcterms:modified (수정일), dcterms:temporal (시간 범위)

**행위자·권리:**
- dcterms:creator, dcterms:publisher, dcterms:license, dcterms:rights, dcterms:accessRights, dcterms:rightsHolder

**언어·포맷:**
- dcterms:language, dcterms:format

**관계:**
- dcterms:conformsTo, dcterms:isReferencedBy, dcterms:hasPart, dcterms:isPartOf, dcterms:relation, dcterms:replaces, dcterms:isReplacedBy, dcterms:references, dcterms:requires

**기타:**
- dcterms:accrualPeriodicity (갱신 주기), dcterms:spatial (공간 범위), dcterms:type, dcterms:subject

→ 이들은 DCAT v3 application profile의 핵심이지만 본 인벤토리에는 빠져 있음. 통합 단계에서 (a) 별도 DCMI Terms 인벤토리 추가, 또는 (b) master_inventory에 보조 행으로 포함 결정 필요.

## domain/range 처리 정책

- .ttl에서 `rdfs:domain`, `rdfs:range`가 명시된 경우 그대로 표기.
- 도메인이 `owl:unionOf`로 다중 클래스인 경우 콤마 구분 (예: hadRole의 `prov:Attribution, dcat:Relationship`).
- 일부 속성은 도메인이 명시되지 않음 (accessService, contactPoint 등). 빈 칸으로 두고 필요 시 [CHECK] 표시.
- range가 `rdfs:Literal` (느슨한 타입)인 경우 그대로 기록. spec scopeNote에 "should be typed as xsd:decimal" 등 추가 제약이 있으면 notes에 표시.

## cardinality 일괄 처리

DCAT v3 .ttl은 클래스 수준 owl:Restriction이 일부 있음 (예: CatalogRecord에 cardinality 1 on foaf:primaryTopic). 그러나 속성 자체에는 cardinality 제약이 거의 없으므로 모든 52개 행의 cardinality 칸은 `unspecified`로 일괄 처리. 클래스의 owl:Restriction은 notes에 표시.

## equivalent_terms 사전 채움

DCAT v3 → 다른 표준의 명백한 매핑만 사전 기재 (보수적):

- dcat:Catalog → schema:DataCatalog
- dcat:Dataset → schema:Dataset, croissant:Dataset
- dcat:DatasetSeries → schema:DataFeed (느슨)
- dcat:Distribution → schema:DataDownload
- dcat:Resource → prov:Entity (느슨)
- dcat:Role → prov:Role
- dcat:dataset → schema:dataset
- dcat:distribution → schema:distribution
- dcat:downloadURL → schema:contentUrl
- dcat:byteSize → schema:contentSize
- dcat:mediaType → schema:encodingFormat
- dcat:keyword → schema:keywords
- dcat:contactPoint → schema:contactPoint
- dcat:startDate → schema:startDate
- dcat:endDate → schema:endDate
- dcat:bbox → schema:GeoShape (간접)
- dcat:hadRole → prov:hadRole
- dcat:previousVersion → prov:wasRevisionOf
- dcat:version → schema:version

나머지 33개 행의 equivalent_terms는 빈 칸. master_inventory.csv에서 양방향 보강 예정.

## 다음 단계 권장 검토 사항

1. **dcterms: 재사용 속성 처리**: 위 권장 목록(약 25개)을 인벤토리에 어떻게 반영할지 결정.
2. **inverse-only properties의 정의 차용 정책**: PROV-O의 wasGeneratedBy/generated 등과 동일한 패턴이므로 통합 단계에서 일관 정책 적용.
3. **PROV-DC와의 중첩**: dcat:Role vs prov:Role, dcat:hadRole vs prov:hadRole 등 의미적으로 거의 동일한 짝의 처리. equivalent_terms로 충분한지, 아니면 별도 cross-reference 표 필요한지.
4. **DataService를 distribution.url로 분류한 결정 재검토**: 서비스 자체는 distribution이라기보다 별도 개념일 수 있음. 통합 단계에서 새 태그(예: `service.endpoint`) 추가 여부 검토.
