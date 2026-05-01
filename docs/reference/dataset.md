# Dataset (D1~D15)

데이터셋은 연구데이터의 **공유·활용을 위한 파일 그룹**입니다. 22개 요소로 구성되며, **본 표준에서 가장 흔히 사용되는 클래스**입니다.

## DCAT 매핑

`Dataset` → `dcat:Dataset` (1:1)

이 매핑 덕분에 Google Dataset Search · DataHub · re3data 등에서 자동 인식됩니다.

## 요소 일람

| ID | 요소명 | 유형 | M/R/O | JSON-LD 키 | IRI |
| --- | --- | --- | --- | --- | --- |
| D1 | Dataset | Class | O | `Dataset` | `dcat:Dataset` |
| **D2** | **Identifier** | Property | **M** | `identifier` | `dct:identifier` |
| **D2.1** | **IdentifierType** | CVP | **M** | `identifierType` | `tta:identifierType` |
| **D3** | **Title** | Property | **M** | `title` | `dct:title` |
| D3.1 | TitleType | CVP | O | `titleType` | `tta:titleType` |
| **D4** | **Creator** | Property | **M** | `creator` | `dct:creator` |
| **D5** | **Publisher** | Property | **M** | `publisher` | `dct:publisher` |
| **D6** | **PublicationYear** | SEP | **M** | `publicationYear` | `dct:issued` |
| D7 | Date | SEP | R | `date` | `dct:date` |
| D7.1 | DateType | CVP | M | `dateType` | `tta:dateType` |
| D8 | Description | Property | R | `description` | `dct:description` |
| D9 | Subject | Class | R | `subject` | `dct:subject` |
| D9.1 | SubjectScheme | CVP | R | `subjectScheme` | `tta:subjectScheme` |
| D9.2 | SubjectID | Property | R | `subjectId` | `tta:subjectId` |
| **D9.3** | **SubjectName** | Property | **M** | `subjectName` | `skos:prefLabel` |
| D10 | Contributor | Property | R | `contributor` | `dct:contributor` |
| D10.1 | ContributorType | CVP | M | `contributorType` | `tta:contributorType` |
| D11 | Contact | Property | R | `contact` | `tta:contact` |
| D12 | Rights | Property | R | `rights` | `dct:rights` |
| D13 | Keyword | Property | O | `keyword` | `dcat:keyword` |
| D14 | AccessType | CVP | O | `accessType` | `tta:accessType` |
| D15 | AccessRestriction | CVP | O | `accessRestriction` | `tta:accessRestriction` |

## 필수(M) 요소만 채운 최소 예시

```json
{
  "@context": "https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/schema/context.jsonld",
  "id": "https://doi.org/10.7488/ds/example-001",
  "type": "Dataset",

  "identifier": "https://doi.org/10.7488/ds/example-001",
  "identifierType": "DOI",
  "title": {"en": "Minimal Example Dataset"},
  "creator": {"type": "Person", "name": "Suntae Kim"},
  "publisher": {"type": "Organization", "name": "KISTI"},
  "publicationYear": "2026"
}
```

[:material-download: dataset-minimal.jsonld](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/examples/valid/dataset-minimal.jsonld){ .md-button .md-button--primary }
[:material-file-document: 완전 예시](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/examples/valid/dataset-complete-kisti.jsonld){ .md-button }

## 식별자(Identifier) 정책

데이터셋의 D2 Identifier는 **DOI 권고**입니다.
- Google Dataset Search가 우선 인식
- 정식 인용 정보 자동 생성
- 영구적 식별자 보장

DOI 발급이 어려운 경우 Handle, URI 순으로 권고합니다.

## 통제어

- `IdentifierType` (D2.1) — DOI 권고
- `TitleType` (D3.1)
- `DatasetDateType` (D7.1) — Accepted, Available, Created, Issued 등 9종
- `ContributorType` (D10.1) — Funder, ResearchGroup, RightsHolder 등 22종
- `DatasetAccessType` (D14) — open, embargoed, restricted, closed
- `DatasetAccessRestrictionType` (D15)

[전체 값 목록 :material-arrow-right:](vocabularies.md)

## SHACL Shape

[:material-file-code: dataset.ttl 보기](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/shapes/dataset.ttl)
