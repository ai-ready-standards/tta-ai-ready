# File (F1~F19)

파일은 연구데이터의 **개별 단위**(원시 데이터, raw data)입니다. 27개 요소로 구성되며, 본 표준에서 가장 많은 요소를 가진 클래스입니다.

## DCAT 매핑

`File` → `dcat:Distribution` (+ `schema:DataDownload`)

DCAT의 Distribution은 "데이터셋의 특정 표현(파일·API)"으로, 본 표준의 File과 의미적으로 일치합니다.

## 요소 일람 (요약)

| ID | 요소명 | 유형 | M/R/O | JSON-LD 키 |
| --- | --- | --- | --- | --- |
| F1 | File | Class | O | `File` |
| **F2** | **Identifier** | Property | **M** | `identifier` |
| **F2.1** | **IdentifierType** | CVP | **M** | `identifierType` |
| **F3** | **Title** | Property | **M** | `title` |
| F3.1 | TitleType | CVP | O | `titleType` |
| **F4** | **Creator** | Property | **M** | `creator` |
| **F5** | **Publisher** | Property | **M** | `publisher` |
| **F6** | **PublicationYear** | SEP | **M** | `publicationYear` |
| F7 | Contributor | Property | R | `contributor` |
| F7.1 | ContributorType | CVP | M | `contributorType` |
| F8 | Date | SEP | R | `date` |
| F8.1 | DateType | CVP | M | `dateType` |
| F9 | Description | Property | R | `description` |
| F10 | Subject | Class | R | `subject` |
| F10.1 | SubjectScheme | CVP | R | `subjectScheme` |
| F10.2 | SubjectID | Property | R | `subjectId` |
| **F10.3** | **SubjectName** | Property | **M** | `subjectName` |
| F11 | Contact | Property | R | `contact` |
| F12 | Rights | Property | R | `rights` |
| F13 | Keyword | Property | O | `keyword` |
| F14 | AccessType | CVP | O | `accessType` |
| F15 | AccessRestriction | CVP | O | `accessRestriction` |
| F16 | Coverage | SEP | O | `coverage` |
| F17 | Type | CVP | O | `type` |
| F18 | Format | Property | O | `format` |
| F19 | Size | Property | O | `size` |
| F19.1 | Unit | CVP | O | `sizeUnit` |

## 파일 고유 요소

다른 클래스에는 없고 File에만 있는 요소들:

- **F16 Coverage** (시간·공간 범위) — W3CDTF 형식 또는 자유 기술
- **F17 Type** (파일 유형) — DCMI FileType (Image, Text, MovingImage 등 11종)
- **F18 Format** (파일 형식) — 확장자명 (예: `Tiff`, `Text`, `PPT`)
- **F19 Size + F19.1 Unit** — 파일 크기 (Byte / Mega Byte / Giga Byte / Tera Byte)

## 통제어

- `FileType` (F17) — DCMI 11종: Event, Image, InteractiveResource, MovingImage, PhysicalObject, Service, Software, Sound, StillImage, Text, other
- `FileSizeUnitType` (F19.1) — Byte, Mega Byte, Giga Byte, Tera Byte

[전체 값 목록 :material-arrow-right:](vocabularies.md)

## SHACL Shape

[:material-file-code: file.ttl 보기](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/shapes/file.ttl)
