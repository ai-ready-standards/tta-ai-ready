# PROV-O 표준 인벤토리 추출 리포트

- 추출 일자: 2026-05-03
- 출처: W3C PROV-O Recommendation (2013-04-30) — https://www.w3.org/TR/prov-o/
- 명세 캐시: `D:\ARD\sources\prov-o.ttl` (canonical PROV namespace .ttl, 약 113KB)
- 출력: `D:\ARD\inventory\prov-o.csv` (89개 행)

## 추출 항목 수

| term_type | PROV-O proper | PROV-DC 확장 | 합계 |
|---|---|---|---|
| Class | 30 | 9 | 39 |
| Property | 50 | 0 | 50 |
| Enumeration | 0 | 0 | 0 |
| **합계** | **80** | **9** | **89** |

PROV-O proper 30개 클래스: Starting-point 3개 (Entity, Activity, Agent), Expanded 8개 (Bundle, Collection, EmptyCollection, Plan, Person, SoftwareAgent, Organization, Location), Qualified 19개 (Influence + 3 sub-influence + InstantaneousEvent + Generation/Usage/Communication/Start/End/Invalidation + Derivation/Quotation/Revision/PrimarySource + Attribution/Association/Delegation + Role).

PROV-O proper 50개 속성: Starting-point 9개 (object 7개 + datatype 2개), Expanded 16개 (object 13개 + datatype 3개), Qualified 25개 (qualified* 14개 + entity/activity/agent/influencer 4개 + had* 5개 + atTime 1개 + qualifiedInfluence 1개).

## concept_tag 분포

PROV-O는 본질적으로 프로비넌스/파생 어휘이므로, 24개 분류 태그 중 `provenance.*`와 `uncategorized`가 다수를 차지함.

| concept_tag | 개수 |
|---|---|
| uncategorized | 41 |
| provenance.derivation | 13 |
| provenance.activity | 14 |
| actor.creator | 3 |
| actor.contributor | 3 |
| structure.recordset | 3 |
| temporal.coverage | 3 |
| provenance.source | 2 |
| spatial.location | 2 |
| temporal.creation | 2 |
| structure.dataset | 1 |
| actor.publisher | 1 |
| rights.license | 1 |
| rights.access | 1 |

`uncategorized`가 많은 이유: PROV-O의 qualified 메커니즘(qualifiedAssociation, hadActivity 등)과 추상 구조 클래스(Plan, Role, InstantaneousEvent)는 24개 태그 어디에도 정확히 매핑되지 않음. 통합 단계에서 PROV-O 전용 보조 태그(예: `provenance.qualifier`) 추가 여부 검토 필요.

## 플래그 표시 항목

| 플래그 | 개수 | 항목 |
|---|---|---|
| [CHECK] | 13 | EntityInfluence, ActivityInfluence, AgentInfluence (Q), wasGeneratedBy, hadPrimarySource, wasInvalidatedBy (P), hadMember, generated, invalidated, influenced (P), entity, activity, agent (P) |
| [BORDERLINE] | 9 | PROV-DC 9개 클래스 (Create, Modify, Publish, Contribute, RightsAssignment, Creator, Publisher, Contributor, RightsHolder) |
| [TRUNCATED] | 3 | PrimarySource, Attribution, Delegation (정의가 다중 문단; 핵심 문단만 발췌) |
| [TRANSLATION] | 0 | 없음 |

### [CHECK] 상세

PROV-O 온톨로지(.ttl)에 `:definition` 또는 `rdfs:comment`가 명시되지 않은 13개 항목. 다음 두 그룹으로 분류:

**그룹 A — 구조 클래스 (정의 자체가 부재):** EntityInfluence, ActivityInfluence, AgentInfluence는 `:definition`도 `rdfs:comment`도 없음. `rdfs:subClassOf prov:Influence`만 선언. 정의 칸은 클래스 계층 구조에 기반한 자연어 표현으로 채움 ("Influence where the influencer is an Entity." 등).

**그룹 B — 속성 (대응 클래스의 정의 차용):** wasGeneratedBy, hadPrimarySource, wasInvalidatedBy는 `:definition`/`rdfs:comment`가 없으나 PROV-O는 명시적으로 대응 qualified 클래스 (Generation, PrimarySource, Invalidation)와 의미를 공유한다고 봄 (`:qualifiedForm` 주석 참조). 정의 칸은 대응 클래스의 `:definition`을 그대로 복사. 같은 패턴으로 generated, invalidated, influenced, hadMember는 `:sharesDefinitionWith` 주석을 따라 차용. entity/activity/agent는 `:editorialNote`만 가지므로 그것을 정의 칸에 사용.

### [BORDERLINE] 상세

PROV-DC 9개 클래스(Create, Modify, Publish, Contribute, RightsAssignment, Creator, Publisher, Contributor, RightsHolder)는 엄밀히 PROV-O 표준이 아닌 W3C Note(PROV-DC)의 일부지만, prov: 네임스페이스 .ttl에 함께 포함되어 있고 데이터셋 메타데이터(creator/publisher/license 등)와 직접 대응되어 포함함. notes 컬럼에 "PROV-DC extension class" 명시. 후속 검수에서 제외 결정 시 inventory_id INV-4081–INV-4089 일괄 삭제하면 됨.

## 포함/제외 결정 주요 사례

### 포함 (포함 결정 사유)

- **PROV-O proper 클래스 30개 전체**: Starting/Expanded/Qualified 3계층 모두 포함. 데이터셋 프로비넌스 표현은 qualified 메커니즘이 핵심이므로 Generation/Usage/Attribution 같은 한정 클래스가 필수.
- **`atTime`, `generatedAtTime`, `invalidatedAtTime` 등 시간 datatype 속성**: AI Ready Data의 temporal 메타데이터에 직접 매핑됨.
- **`Location`, `atLocation`**: spatial.location 매핑됨.
- **PROV-DC 9개**: 위 [BORDERLINE] 참조.

### 제외 (제외 결정 사유)

- **PROV-DICTIONARY 확장** (Dictionary, EmptyDictionary, KeyEntityPair, Insertion, Removal, derivedByInsertionFrom, derivedByRemovalFrom, hadDictionaryMember, qualifiedInsertion, qualifiedRemoval, insertedKeyEntityPair, pairKey, pairEntity, removedKey, dictionary): 사전형 자료 구조 확장으로 데이터셋 메타데이터에 일반적으로 사용되지 않음. .ttl 파일 line 2174 이후에 정의되어 있으나 PROV-O proper가 아님.
- **PROV-AQ 확장** (ServiceDescription, DirectQueryService, has_anchor, has_provenance, has_query_service, describesService, pingback, provenanceUriTemplate): 프로비넌스 데이터의 접근/조회 엔드포인트 표현용으로 인벤토리 자체 메타데이터와는 거리가 멂.
- **`qualifiedForm`** annotation property: 메타-구조 주석(예: prov:wasGeneratedBy prov:qualifiedForm prov:Generation .)이며 데이터셋 기술과 무관.
- **`hadDelegate`, `wasUsedBy`, `wasMemberOf` 등 inverse 별칭**: .ttl의 `:inverse "..."` annotation으로만 선언되고 owl:ObjectProperty로 정의되지 않음. 별도 IRI 없음.

## 공식 명세 원문 인용 정책

- `:definition` 주석이 있는 항목 → 원문 그대로 인용 (PrimarySource/Attribution/Delegation는 다중 문단이라 핵심 문단만; notes에 [TRUNCATED] 표시)
- `:definition` 없고 `rdfs:comment`만 있는 항목 → rdfs:comment를 그대로 인용 (notes에 "Source: rdfs:comment" 표시)
- 둘 다 없는 항목 → 위 [CHECK] 그룹 B 정책 (qualified form 차용 + [CHECK] 표시), 또는 :editorialNote 차용

## cardinality 일괄 처리

PROV-O는 OWL 온톨로지로서 owl:FunctionalProperty/owl:InverseFunctionalProperty를 일부 사용하지 않고, 명시적인 카디널리티 제약(owl:cardinality, owl:maxCardinality 등)도 PROV-O proper에서 거의 선언하지 않음. 따라서 모든 89개 행의 cardinality 칸은 `unspecified`로 일괄 처리.

## equivalent_terms 사전 채움

다음 항목만 자명한 매핑을 사전 기재함 (다른 표준 인벤토리 작업이 진행되지 않았으므로 보수적):

- prov:Person → foaf:Person, schema:Person
- prov:Organization → foaf:Organization, schema:Organization
- prov:generatedAtTime → schema:dateCreated, dcterms:created
- prov:Creator → schema:creator, dcterms:creator
- prov:Publisher → schema:publisher, dcterms:publisher
- prov:Contributor → schema:contributor, dcterms:contributor
- prov:RightsHolder → dcterms:rightsHolder

나머지 86개 행의 equivalent_terms는 빈 칸. 통합 단계(`master_inventory.csv` 작성 시)에 양방향으로 보강할 예정.

## 다음 단계 권장 검토 사항

1. **PROV-DC 포함 여부 최종 확정**: 9개 [BORDERLINE] 항목을 master_inventory에 유지할지, 별도 카탈로그로 분리할지 결정 필요.
2. **concept_tag 보완**: PROV-O qualified 메커니즘 특화 태그(예: `provenance.qualifier`) 추가 여부.
3. **InstantaneousEvent, Plan, Role의 분류**: 현재 uncategorized이나 데이터셋 메타데이터 관점에서 별도 태그 필요성 검토.
4. **`atTime` vs `startedAtTime`/`endedAtTime`/`generatedAtTime`/`invalidatedAtTime`의 temporal 태그 일관성**: 현재 startedAtTime/generatedAtTime을 `temporal.creation`, 나머지를 `temporal.coverage`로 분리했으나 재고 가능.
