# 용어집·약어 (Glossary)

본 사업은 여러 표준·기관·체계의 교차점에 있어서 약어가 많습니다. 본 페이지는 사이트·문서 어디에서든 모르는 약어를 만났을 때 즉시 확인할 수 있는 **약어 사전**입니다.

!!! warning "본 페이지는 두 종류의 용어를 함께 정리합니다"
    본 사업의 산출물은 **두 영역**으로 나뉘며, 본 용어집의 약어들도 그에 맞춰 두 영역에 속합니다.

    | 영역 | 정체 | 본 페이지의 해당 섹션 |
    | --- | --- | --- |
    | **A. 표준 관련** | 5종 시범 표준의 본문에 등장하거나, 표준 매핑에 사용되는 외부 어휘 | ① 표준 요소 ID · ⑤ 외부 어휘·표준·기관 |
    | **B. 사업 운영** | 표준을 만들기 위한 본 사업의 방법론·작업 분해·결정 기록 | ② 7-구성요소(c1~c7) · ③ Decision ID · ④ WBS 코드 · ⑥ 본 사업 내부 약어 |

    이 구분이 중요한 이유: B 영역의 약어(c1~c7, WBS, D-Q4 등)는 **표준 본체의 일부가 아닙니다**. 5종 표준을 사용·구현하는 분께는 A 영역만 필요할 가능성이 높습니다.

!!! tip "빠른 검색"
    브라우저의 페이지 내 검색(Ctrl/Cmd + F)으로 약어를 바로 찾으실 수 있습니다.

---

## 한 눈에 보기 — 약어 6가지 유형

본 사업에서 만나는 약어는 다음 6가지 유형으로 나뉩니다.

| 유형 | 형식 | 예 |
| --- | --- | --- |
| ① 표준 요소 ID | 대문자 + 숫자 | `R17`, `D2`, `C3.1` |
| ② 7개 구성요소 | 소문자 c + 숫자 | `c5`, `c6` |
| ③ Decision ID | D-숫자 또는 D-Q숫자 | `D-001`, `D-Q4` |
| ④ WBS 코드 | A/B/C/D + 숫자 | `B-3`, `C-5` |
| ⑤ 외부 어휘 | 알파벳 약어 | `PROV-O`, `DCAT`, `DQV` |
| ⑥ 사업 내부 | 알파벳 약어 | `TTA`, `PG606`, `AP`, `M/R/O` |

---

## ① 표준 요소 ID (4계층 구조)

> **분류**: A. 표준 관련 — 5종 표준의 본문에 등장하는 식별자

TTAK.KO-10.0976 본문의 **자원 종류 + 일련번호**로 모든 메타데이터 요소를 식별합니다.

| 글자 | 자원 종류 | 한글 | 범위 |
| --- | --- | --- | --- |
| **C** | Collection | 컬렉션 (논리적 그룹) | C1 ~ C12 |
| **D** | Dataset | 데이터셋 | D1 ~ D15 |
| **F** | File | 파일 (개별 데이터) | F1 ~ F19 |
| **R** | Repository | 리포지토리 (시스템) | R1 ~ R21 |

### 읽는 법

| 표기 | 의미 |
| --- | --- |
| `R17` | Repository의 **17번째** 요소 → QualityManagement |
| `D2` | Dataset의 **2번째** 요소 → Identifier |
| `D2.1` | D2의 **하위 요소 1** → IdentifierType |
| `F19.1` | File의 19번째 요소(Size)의 하위 요소 1 → Unit |

### 자주 만나는 요소 5가지

| ID | 영문명 | 한글 | M/R/O |
| --- | --- | --- | --- |
| **D2** | Identifier | 식별자 | M (필수) |
| **D3** | Title | 제목 | M (필수) |
| **D4** | Creator | 생성자 | M (필수) |
| **R17** | QualityManagement | 품질 관리 | M (필수) |
| **D7.1** | DateType | 날짜 유형 | M (Date 있을 때) |

전체 93개 요소: [`tta-standards/0976/elements.csv`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/tta-standards/0976/elements.csv)

---

## ② 7개 구성요소 (c1 ~ c7)

> **분류**: B. 사업 운영 — 본 사업의 프레임워크 정의서가 정의하는 방법론적 구성요소. 5종 표준이 갖춰야 할 요건을 본 사업 내부 어휘로 표현한 것이며, 표준 본문 자체는 아니다.

본 사업 프레임워크의 **모든 AI 레디 표준이 갖춰야 할 7가지 구성요소**.

| ID | 이름 | 유형 | 핵심 도구 |
| --- | --- | --- | --- |
| **c1** | 시맨틱 (Semantic) | 전환 | JSON-LD `@context` |
| **c2** | 데이터 모델 (Data Model) | 전환 | SHACL `sh:NodeShape` |
| **c3** | 신태틱 (Syntactic) | 전환 | JSON-LD 1.1 |
| **c4** | 운영 시맨틱 (Operational) | 신규 | Croissant 1.0 (해당 시) |
| **c5** | 출처·계보 (Provenance) | 신규 | W3C PROV-O |
| **c6** | 품질 프로파일 (Quality) | 신규 | W3C DQV |
| **c7** | 접근·사용 제약 (Access) | 신규 | dcterms:license + DUO/CC |

상세: [프레임워크 정의서 Part II](framework/index.md#part-ii-7개-구성요소-모델)

---

## ③ Decision ID — 매핑 결정 추적

> **분류**: B. 사업 운영 — 본 사업의 매핑 작업(Phase B) 중 발생한 내부 결정 기록.

매핑 작업(Phase B) 중 발생한 **결정에 부여된 ID**. 두 종류:

| 형식 | 의미 |
| --- | --- |
| **D-001 ~ D-005** | 일반 결정 (단순 결정) |
| **D-Q1 ~ D-Q9** | **Q**uestion형 결정 — 매핑 시 질문을 명시하고 답한 것 |

### 본 사업의 9개 결정

| Decision | 무엇을 결정했나 | 적용 영역 |
| --- | --- | --- |
| **D-001** | Repository tta_iri 임시 부여 | 모든 표준 |
| **D-002** | InstitutionCountry alpha-3 → alpha-2 | R9 |
| **D-003** | D2.1 IdentifierType 본문/부록 충돌 (부록 우선) | D2.1 |
| **D-004** | D5 Publisher 본문/부록 충돌 (부록 우선) | D5 |
| **D-005** | D14 AccessType (PDF 손상) | D14 |
| **D-Q3** | PROV-O Date 매핑 (DateType=Created 시 활성) | c5 |
| **D-Q4** | DQV 활성화 (Boolean Slot — yes일 때만) | c6 + R17 |
| **D-Q5** | 통제어 매핑 단위 (값 단위) | 모든 통제어 |
| **D-Q7** | Repository PROV (D-Q3와 일관) | c5 |

전체 결정 추적: [`6_changelog/CHANGELOG.md`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/6_changelog/CHANGELOG.md)

---

## ④ WBS 코드 (수행계획서 업무)

> **분류**: B. 사업 운영 — 본 사업의 작업 분해 구조. 발주처(TTA)와 본 사업 수행사 간 작업 식별자.

수행계획서의 **업무 ID**. 형식이 Decision ID와 비슷해 보이지만 다릅니다 (혼동 주의).

| 글자 | 카테고리 | 책임자 | 업무 수 |
| --- | --- | --- | --- |
| **A** | 분석·조사 | 김주섭 박사 | A-1 ~ A-8 |
| **B** | 표준화 지침 개정 | 박천웅 박사 | B-1 ~ B-11 |
| **C** | 기술 개발 | 김장원 교수 | C-1 ~ C-12 |
| **D** | 보급·확산 | PM (본인) | D-1 ~ D-9 |

### 자주 보게 될 WBS 코드 (★ = 발주처 납품 주요 산출물)

| ID | 산출물 |
| --- | --- |
| A-6 | ★ 현황 분석 보고서 |
| **B-3** | ★ **AI 레디 표준 프레임워크 정의서** |
| B-10 | ★ 표준화 지침 개정안 최종본 |
| C-1 | ★ 리포지토리 아키텍처 설계서 |
| C-5 ~ C-9 | P-01 ~ P-05 패키지 개발 |
| C-12 | ★ 파일럿 결과보고서 5건 |
| D-2/D-3/D-4 | 매뉴얼 3종 |
| D-6 | 통합 설명회 |
| D-9 | ★ 운영 이관 패키지 (v1.2 신설) |

### Decision ID vs WBS 코드 — 혼동 방지

| | Decision ID | WBS 코드 |
| --- | --- | --- |
| 형식 | `D-001`, `D-Q4` | `D-2`, `B-3` |
| `D-` 의미 | "**D**ecision" | "카테고리 **D** 보급·확산" |
| 숫자 | 결정 일련번호 | 카테고리 내 업무 일련번호 |
| 예 | D-Q4 = 4번째 질의형 결정 | D-4 = D 카테고리 4번째 업무 |

→ **`D-` 다음에 숫자만 있으면 WBS, `Q+숫자`거나 `001` 같은 3자리 숫자면 Decision ID**.

---

## ⑤ 외부 어휘·표준·기관 약어

> **분류**: A. 표준 관련 — 5종 표준이 매핑·인용하는 외부 표준 어휘. 표준 본문에서 직접 만나게 됨.

### 외부 어휘·표준 (통합)

본 사업이 참조·매핑하는 모든 외부 어휘·표준을 단일 표로 정리한다. 발행 기관 컬럼으로 W3C 발행 여부를 식별할 수 있다.

| 약어 | 풀이 | 발행 기관 | 본 사업 사용처 |
| --- | --- | --- | --- |
| **DCAT** | **D**ata **C**atalog **V**ocabulary | W3C | 데이터셋 표현 (P-01·P-02) |
| **DCMI** | **D**ublin **C**ore **M**etadata **I**nitiative | DCMI (W3C 협력) | 모든 표준 (기본) |
| **dcterms** | DCMI Terms | DCMI | 가장 많이 쓰는 어휘 (32 매핑) |
| **dctype** | DCMI Type | DCMI | 자원 유형 분류 |
| **PROV-O** | PROV Ontology (출처·계보) | W3C | c5 (Provenance) |
| **DQV** | **D**ata **Q**uality **V**ocabulary | W3C | c6 (Quality) |
| **SHACL** | **Sh**apes **C**onstraint **L**anguage | W3C | 검증 규칙 언어 |
| **SKOS** | **S**imple **K**nowledge **O**rganization **S**ystem | W3C | 통제어 분류 |
| **OWL** | Web Ontology Language | W3C | 온톨로지 (KG 프로파일) |
| **schema.org** | schema.org Vocabulary | schema.org Community Group (Google·Microsoft·Yahoo·Yandex 공동 출범) | 외부 정합성 매핑 (`aird-datatype-to-schemaorg.ttl`, PR-001 도입) |
| **DataCite** | DataCite Schema 4.5 | DataCite | 식별자·인용 (P-01) |
| **re3data** | Registry of Research Data Repositories | re3data.org | Repository 메타데이터 |
| **Croissant** | MLCommons Croissant 1.0 | MLCommons | ML 운영 시맨틱 (P-03·P-04) |
| **DUO** | **D**ata **U**se **O**ntology | EBI / EBISPOT | 사용 제약 (P-03) |
| **CC** | Creative Commons | Creative Commons | 라이선스 |
| **FOAF** | **F**riend **o**f **a** **F**riend | FOAF Project | 인물·조직 |
| **DDI** | Data Documentation Initiative | DDI Alliance | 통계 프로파일 |
| **SDMX** | Statistical Data and Metadata eXchange | SDMX Consortium | 공식 통계 프로파일 |

> **변경 이력**: 본 표는 PR-002 에서 기존 "W3C 표준 어휘" / "메타데이터 표준 (외부 기관)" 두 표를 통합하고 schema.org를 추가한 결과이다 (사유: PR-001이 schema.org 매핑을 도입했으나 본 용어집이 동시 갱신되지 않은 갭 H 시연). 발행 기관 컬럼으로 W3C 발행 여부를 명시한다.

### 형식·언어

| 약어 | 풀이 | 역할 |
| --- | --- | --- |
| **JSON-LD** | JSON for **L**inked **D**ata | RDF의 JSON 표현 (본 사업 1차 표현 형식) |
| **RDF** | **R**esource **D**escription **F**ramework | 시맨틱 웹 데이터 모델 |
| **Turtle** | Terse RDF Triple Language | RDF 텍스트 표현 (`.ttl` 파일) |
| **OWL** | Web Ontology Language | 온톨로지 정의 |
| **IRI/URI/URL** | International/Uniform Resource Identifier/Locator | 자원 식별자 |

### 표준화 기관

| 약어 | 풀이 |
| --- | --- |
| **TTA** | 한국정보통신기술협회 (Telecommunications Technology Association) |
| **W3C** | World Wide Web Consortium |
| **ISO** | International Organization for Standardization |
| **IEC** | International Electrotechnical Commission |
| **MLCommons** | ML 표준화 컨소시엄 (Croissant 발행) |
| **RDA** | Research Data Alliance |
| **schema.org Community Group** | schema.org 공동 운영체 (Google·Microsoft·Yahoo·Yandex 공동 출범, W3C Community Group 형태) |
| **DCMI** | Dublin Core Metadata Initiative (DCMI Terms 발행) |
| **DDI Alliance** | DDI 표준 발행 컨소시엄 |
| **SDMX Consortium** | SDMX 표준 발행 컨소시엄 (BIS·ECB·Eurostat·IMF·OECD·UN·World Bank) |
| **EBI / EBISPOT** | European Bioinformatics Institute / Samples, Phenotypes and Ontologies Team (DUO 발행) |

---

## ⑥ 본 사업 내부 약어

> **분류**: B. 사업 운영 — 본 사업의 거버넌스·운영 용어. 5종 표준 본문과 무관.

### TTA 거버넌스

| 약어 | 풀이 | 역할 |
| --- | --- | --- |
| **PG606** | Project Group 606 | TTA의 **메타데이터 프로젝트 그룹** (본 사업 5종 표준 모두 PG606 소관) |
| **TC** | Technical Committee | 기술위원회 (각 표준의 의장단) |
| **SPC** | Standards Policy Committee | 표준화 정책 위원회 (지침 개정 심의) |

### 표준 작성 용어

| 약어 | 풀이 | 의미 |
| --- | --- | --- |
| **AP** | **A**pplication **P**rofile | 응용 프로파일 — 표준의 구체적 적용 명세 |
| **CV** | **C**ontrolled **V**ocabulary | 통제어 (예: open/embargoed/restricted/closed) |
| **CVP** | **C**ontrolled **V**ocabulary **P**roperty | 통제어 속성 |
| **SEP** | **S**yntax **E**ncoding **P**roperty | 형식 제약 속성 (예: ISO 8601 날짜) |
| **M/R/O** | **M**andatory / **R**ecommended / **O**ptional | 필수 / 권고 / 선택 등급 |

### 사업 운영 용어

| 약어 | 풀이 |
| --- | --- |
| **WBS** | **W**ork **B**reakdown **S**tructure (작업 분해 구조) |
| **RACI** | **R**esponsible / **A**ccountable / **C**onsulted / **I**nformed (책임 매트릭스) |
| **PM** | Project Manager (사업 책임자) |
| **MM** | Man-Month (인력 투입 단위, %로 표기) |
| **PR** | Pull Request (GitHub의 변경 합치기 요청) |
| **CI/CD** | Continuous Integration / Continuous Deployment (자동 검증·배포) |
| **L1~L4** | 4계층 품질 보증 (작성자·PM·외부전문가·자동검증) |

---

## 자주 만나는 약어 조합 — 읽는 법

### 예시 1 — Decision-Q4 설명문

> "★ **D-Q4** (**Boolean Activation Slot**): **R17 QualityManagement** = 'yes'일 때 **dqv:hasQualityMetadata** 활성"

풀어 읽기:

- **D-Q4** = "4번째 질의형 결정"
- **Boolean Activation Slot** = 본 사업의 신규 패턴 (yes/no 값으로 검증을 켜고 끔)
- **R17** = Repository(리포지토리)의 17번째 요소 = QualityManagement(품질 관리)
- **dqv:hasQualityMetadata** = W3C DQV의 "품질 메타데이터를 가진다" 술어

→ **"리포지토리의 품질 관리(R17) 항목이 'yes'일 때만 DQV의 품질 메타데이터 검증을 자동 활성화"**

### 예시 2 — WBS B-3

> "WBS **B-3** (수행계획서 2.2절) = AI 레디 표준 프레임워크 정의서"

풀어 읽기:

- **WBS** = 작업 분해 구조
- **B** = 카테고리 B (표준화 지침 개정)
- **3** = B 카테고리의 3번째 업무
- **수행계획서 2.2절** = 본 업무가 정의된 문서의 위치

→ **"표준화 지침 개정 카테고리의 3번째 업무인 프레임워크 정의서 작성"**

### 예시 3 — c5 PROV-O 조건부 활성

> "c5 출처·계보 — Decision-Q3/Q7. Date+DateType 조합이 특정 값일 때 PROV 필드 활성"

풀어 읽기:

- **c5** = 7개 구성요소 중 5번 (출처·계보)
- **Decision-Q3, Q7** = 두 개의 질의형 결정
- **Date+DateType** = TTA 표준의 D7 + D7.1 한 쌍
- **PROV** = W3C PROV-O 어휘

→ **"5번 구성요소(출처·계보) 영역에서 Q3과 Q7 두 결정이 적용됨. 표준의 Date 필드 옆 DateType 값이 'Created' 같은 특정 값일 때만 PROV-O 어휘를 자동으로 추가"**

---

## 추가 자료

- [프레임워크 정의서](framework/index.md) — 7개 구성요소(c1~c7) 상세
- [매핑 자료실](methodology/index.md) — 매핑 매트릭스 + Decision 추적
- [P-01 적용 사례](standards/p-01.md) — 모든 약어가 실제 적용된 예
- [매뉴얼 3종](manuals/index.md) — TC 담당자·사용자 가이드

---

## 약어가 추가되면

본 사업 진행 중 새로운 약어가 등장하면 이 페이지에 추가됩니다. 모르는 약어를 만나면 GitHub Issue로 신고해 주세요.

[:material-bug: 약어 누락 신고](https://github.com/ai-ready-standards/tta-ai-ready/issues/new?labels=documentation&title=glossary%3A+){ .md-button }
