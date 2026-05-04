# Croissant 표준 인벤토리 추출 리포트

- 추출 일자: 2026-05-03
- 출처: MLCommons Croissant 1.0 Specification — https://docs.mlcommons.org/croissant/docs/croissant-spec.html
- 명세 캐시: `D:\ARD\sources\croissant-spec.md` (markdown source from GitHub raw, 약 76KB)
- 출력: `D:\ARD\inventory\croissant.csv` (45개 행)

## 추출 항목 수

| term_type | cr: 네임스페이스 |
|---|---|
| Class | 12 |
| Property | 30 |
| Enumeration | 3 |
| **합계** | **45** |

Class 12개: FileObject, FileSet, RecordSet, Field, DataSource, Extract, Transform, Format, BoundingBox, SegmentationMask, Split, Label.
Enumeration 3개: TrainingSplit, ValidationSplit, TestSplit (cr:Split의 인스턴스).
Property 30개: JSON-LD context (Appendix 1) 정의 27개 + 명세 본문에만 정의된 3개(containedIn, excludes, equivalentProperty).

Croissant 네임스페이스는 `http://mlcommons.org/croissant/`이며 `cr:` 약식 표기 사용.

## concept_tag 분포

Croissant는 ML 데이터셋 구조 어휘로 `structure.*` 비중이 가장 큼. 그러나 ML 특화 시맨틱 타입(BoundingBox, SegmentationMask, Split, Label)과 변환 메커니즘(Transform 관련) 다수가 24개 태그에 매핑되지 않아 `uncategorized`도 큼.

| concept_tag | 개수 |
|---|---|
| uncategorized | 17 |
| structure.field | 12 |
| distribution.url | 6 |
| structure.recordset | 5 |
| distribution.media_type | 2 |
| identification.identifier | 2 |
| structure.dataset | 1 |

`uncategorized` 17개 주요 구성:
- ML 시맨틱 타입 6개: BoundingBox, SegmentationMask, Split, TrainingSplit, ValidationSplit, TestSplit, Label
- Transform 메커니즘 4개: Transform 클래스, regex, replace, separator
- 메커니즘성 클래스/속성 7개: Extract, equivalentProperty, isLiveDataset, md5, path, transform, recordSet

통합 단계에서 ML 특화 보조 태그(예: `ml.split`, `ml.label`, `ml.bounding_box`) 추가 여부 검토 필요.

## 플래그 표시 항목

| 플래그 | 개수 | 항목 |
|---|---|---|
| [CHECK] | 12 | Split, TrainingSplit, ValidationSplit, TestSplit (정의 부재), containedIn/excludes/equivalentProperty (JSON-LD ctx 누락), md5/path/replace (정의 부재), separator (terminology 불일치), recordSet (dual-domain) |
| [BORDERLINE] | 0 | 없음 |
| [TRUNCATED] | 0 | 없음 (정의 모두 단일/소수 문장) |
| [TRANSLATION] | 0 | 없음 |

### [CHECK] 상세

**그룹 A — JSON-LD context와 spec body 불일치 (3건):** Croissant Appendix 1 JSON-LD context는 27개 property를 cr: namespace로 alias하나, spec body는 추가로 `containedIn`, `excludes`, `equivalentProperty`를 FileObject/FileSet/Field의 클래스 정의 표에서 명시함 (즉 Croissant 어휘에 속함이 명백). 그러나 JSON-LD context에 alias가 없어 `@vocab` 기본값(schema.org)으로 해석될 위험. 본 인벤토리는 spec body 우선 → cr:containedIn, cr:excludes, cr:equivalentProperty로 처리.

**그룹 B — JSON-LD context에만 등장 (3건):** `cr:md5`, `cr:path`, `cr:replace`는 JSON-LD context Appendix에는 alias가 있으나 spec body에 정의·설명이 전혀 없음. 인벤토리에는 포함하되:
- cr:md5 → sc:sha256과 유추하여 정의 합성 + [CHECK]
- cr:path → 정의 칸을 "(No definition provided in specification body)"로 두고 [CHECK]
- cr:replace → Transform 맥락에서 정의 합성 + [CHECK]

**그룹 C — Split 클래스 + 3개 인스턴스 (4건):** cr:Split 자체는 spec section intro 한 문장만 있어 형식적 클래스 정의가 없음. cr:TrainingSplit/ValidationSplit/TestSplit은 spec 본문에서 example 데이터 값으로만 등장 (별도 설명 없음). enumeration term_type으로 처리하고 정의는 ML 일반 용어로 합성 + [CHECK].

**그룹 D — Transform 용어 불일치 (1건):** spec body의 Transform 목록은 "delimiter" 사용하지만 JSON-LD context는 "separator" → "cr:separator"로 alias. 본 인벤토리는 JSON-LD context 우선 (cr:separator) + [CHECK].

**그룹 E — recordSet dual-domain (1건):** DataSource 표(line 1009)는 `recordSet`이 DataSource → RecordSet (Reference, ONE)로 정의됨. 동일 alias `recordSet`이 데이터셋 수준에서도 사용되어 sc:Dataset → cr:RecordSet (MANY)으로 작동하는 것이 spec 사례에서 확인됨. 그러나 spec은 두 용도를 명시적으로 구분하지 않음 → 본 인벤토리는 DataSource 도메인만 표기 + [CHECK].

## 포함/제외 결정 주요 사례

### 포함

- **JSON-LD context의 27개 cr: alias**: Appendix 1에 명시되어 cr: namespace 소속 명백.
- **spec body에서 정의된 추가 3개** (containedIn, excludes, equivalentProperty): JSON-LD context 누락이지만 spec text가 "FileSet defines the following properties"로 명시.
- **15개 클래스 (FileObject ~ Label)**: spec section heading 또는 본문에서 정의된 모든 cr: 클래스/Enumeration.

### 제외

- **schema.org/Dataset의 modified property `distribution`**: Croissant가 의미를 변경(distribution은 FileObject/FileSet여야 함, schema.org의 DataDownload가 아님)했으나 cr: namespace term이 아님. Schema.org 인벤토리에서 처리 예정.
- **cr:RAI namespace** (Responsible AI 확장, `http://mlcommons.org/croissant/RAI/`): JSON-LD context에 존재하나 별도 namespace이며 본 spec의 핵심 어휘가 아님. 후속 결정 필요 시 별도 인벤토리.
- **schema.org 재사용 용어 (sc:name, sc:description, sc:url, sc:license, sc:creator, sc:datePublished, sc:keywords, sc:publisher, sc:version, sc:dateCreated, sc:dateModified, sc:sameAs, sc:inLanguage, sc:contentUrl, sc:contentSize, sc:encodingFormat, sc:sha256, sc:Enumeration, sc:GeoCoordinates, sc:GeoShape, sc:ImageObject, sc:Integer, sc:Float, sc:Boolean, sc:Text, sc:Date, sc:DateTime, sc:Intangible, sc:CreativeWork)**: Schema.org 인벤토리에서 별도 처리 예정.
- **dct:conformsTo**: Croissant가 dataset 수준 필수로 권장(`"dct:conformsTo": "http://mlcommons.org/croissant/1.0"`)하나 DCMI Terms 어휘. 본 인벤토리에서 제외.
- **wd:Q48277, wd:Q6581072, wd:Q6581097**: spec example의 Wikidata 식별자. 어휘가 아니라 데이터 값이므로 제외.

## Croissant가 schema.org/Dataset에 추가하거나 수정한 사항 (Dataset 수준 요약)

후속 Schema.org 인벤토리 작업과 통합 단계 결정에 필요. Croissant 1.0 spec의 "Dataset-level Information" 섹션 기준:

**필수 schema.org 속성** (Croissant Dataset이 가져야 함):
- sc:name, sc:description, sc:url, sc:license, sc:creator, sc:datePublished
- dct:conformsTo (값: `http://mlcommons.org/croissant/1.0`)

**권장 schema.org 속성:**
- sc:keywords, sc:publisher, sc:version, sc:dateCreated, sc:dateModified, sc:sameAs, sc:inLanguage

**Croissant가 수정한 schema.org 속성 (1건):**
- `sc:distribution`: schema.org/Dataset은 DataDownload를 받으나 Croissant는 FileObject 또는 FileSet 값을 요구함. notes에 명시.

**Croissant가 추가한 dataset-level 속성 (cr: namespace, 본 인벤토리 포함):**
- cr:isLiveDataset (INV-2031)
- cr:citeAs (INV-2016)
- cr:recordSet (INV-2037) — DataSource 외 Dataset 수준 사용도 spec 사례에서 관찰됨

## cardinality 표기

PROV-O/DCAT v3와 달리 Croissant spec은 각 property 표에 cardinality(ONE/MANY)를 명시함. 다음과 같이 변환:
- ONE → `0..1` (필수성은 별도이므로 0..1로 보수 처리)
- MANY → `0..*`

필수 property는 spec에 "must be specified" 등으로 별도 표시되나 본 인벤토리의 cardinality 컬럼은 multiplicity 표현이므로 0..1/0..* 위주 표기.

특수 항목:
- INV-2018 containedIn: 0..* (spec 표가 MANY)
- INV-2031 isLiveDataset: 0..1 (ONE)
- INV-2033 key: 0..* (MANY, but typically 1)
- INV-2041 replace, INV-2042 separator: spec body 정의 부재 → unspecified

## equivalent_terms 사전 채움

다음 명백한 매핑만 사전 기재:
- cr:FileObject → schema:DataDownload, schema:MediaObject
- cr:citeAs → schema:citation (다만 spec이 "different from schema.org/citation"이라 명시함 → 양방향 동등 매핑은 아니고 유사 개념)
- cr:md5 → schema:sha256 (둘 다 체크섬)

나머지 42개 행은 빈 칸. master_inventory.csv 통합 단계에서 cr:RecordSet/Field와 schema.org/Dataset의 변형 schema 표현 비교 등 보강 예정.

## 다음 단계 권장 검토 사항

1. **ML 특화 concept_tag 추가 검토**: BoundingBox/SegmentationMask/Split/Label 등 7개 시맨틱 타입이 모두 uncategorized. ML 도메인 태그(`ml.semantic_type` 또는 분리하여 `ml.split`, `ml.bounding_box`, `ml.label` 등) 추가 여부.
2. **JSON-LD context vs spec body 불일치 처리 정책 (Croissant upstream에 issue 제기 가치 있음)**: containedIn/excludes/equivalentProperty가 JSON-LD context에 없는 점은 spec의 명백한 결함으로 보임.
3. **cr:path 처리**: 정의가 없는 채로 인벤토리에 있는 것이 적절한지, 아니면 제외할지. 결정 필요.
4. **cr:RAI 확장**: Croissant Responsible AI extension의 어휘를 별도 인벤토리로 추가할지.
5. **Croissant ↔ Schema.org Dataset의 매핑 명세화**: Schema.org 인벤토리가 작성되면 sc:Dataset의 modified `distribution` 속성과 cr:distribution 사용 패턴의 차이를 master_inventory에 반영 필요.
