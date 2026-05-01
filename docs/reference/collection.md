# Collection (C1~C12)

컬렉션은 데이터셋의 **논리적 그룹**(프로젝트·부서·연구과제 등)을 표현하는 메타데이터입니다. 18개 요소(C1~C12 + 하위 변형)로 구성됩니다.

## DCAT 매핑

`Collection` → `dcat:Catalog` + `dcmitype:Collection`

## 요소 일람

| ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI |
| --- | --- | --- | --- | --- | --- |
| C1 | Collection | Class | O | `Collection` | `dcat:Catalog` |
| **C2** | **Identifier** | Property | **M** | `identifier` | `dct:identifier` |
| **C2.1** | **IdentifierType** | CVP | **M** | `identifierType` | `tta:identifierType` |
| **C3** | **Title** | Property | **M** | `title` | `dct:title` |
| C3.1 | TitleType | CVP | O | `titleType` | `tta:titleType` |
| C4 | Date | SEP | R | `date` | `dct:date` |
| C4.1 | DateType | CVP | M | `dateType` | `tta:dateType` |
| C5 | Description | Property | R | `description` | `dct:description` |
| C6 | Subject | Class | R | `subject` | `dct:subject` |
| C6.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` |
| C6.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` |
| C6.3 | SubjectName | Property | M | `subjectName` | `skos:prefLabel` |
| C7 | Creator | Property | R | `creator` | `dct:creator` |
| C8 | Contact | Property | R | `contact` | `tta:contact` |
| C9 | Rights | Property | R | `rights` | `dct:rights` |
| C10 | Keyword | Property | O | `keyword` | `dcat:keyword` |
| C11 | AccessType | CVP | O | `accessType` | `tta:accessType` |
| C12 | AccessRestriction | CVP | O | `accessRestriction` | `tta:accessRestriction` |

## 필수(M) 요소만 채운 최소 예시

```json
{
  "@context": "https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/schema/context.jsonld",
  "type": "Collection",
  "identifier": "https://example.org/collection/my-research",
  "identifierType": "URI",
  "title": {"en": "My Research Collection"}
}
```

[:material-download: collection-minimal.jsonld](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/examples/valid/collection-minimal.jsonld){ .md-button }

## 통제어

본 클래스에서 사용되는 통제어:

- `IdentifierType` (C2.1) — DOI, Handle, URI, UCI 등 19종
- `TitleType` (C3.1) — AlternativeTitle, Subtitle, TranslatedTitle, other
- `CollectionDateType` (C4.1) — Created, Updated, Deleted
- `CollectionAccessType` (C11) — open, embargoed, restricted, closed
- `CollectionAccessRestrictionType` (C12) — feeRequired, registration, free 등 6종

전체 값 목록은 [통제어 페이지](vocabularies.md)에서 확인하세요.

## SHACL Shape

[:material-file-code: collection.ttl 보기](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/shapes/collection.ttl)
