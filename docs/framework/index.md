# AI 레디 표준 프레임워크 정의서 (v1.0 초안)

| 항목 | 내용 |
| --- | --- |
| 문서명 | AI 레디 표준 프레임워크 정의서 |
| 버전 | **v1.0 초안** (2026-05-05) |
| 사업 | AI 레디(AI-Ready) 표준 생태계 조성을 위한 표준화 전략 수립 용역 |
| 발주처 | 한국정보통신기술협회(TTA) |
| WBS | **B-3** (수행계획서 2.2절) |
| 정식 발행 | 2단계 완료 (2026-08-31 예정) |
| 책임자 | 박천웅 박사 + 김장원 교수 |

> 본 문서는 **본 사업의 핵심 제도적 산출물**입니다. 신규 표준이 작성될 때, 또는 기존 표준이 AI 레디화될 때 본 프레임워크를 따라야 합니다. 본 v1.0은 P-01(TTAK.KO-10.0976) 적용을 통해 검증된 결과를 바탕으로 작성되었으며, 2단계 완료 시점에 P-02~P-05 적용 결과를 반영하여 v1.1로 정식 발행됩니다.

---

## Part I. 개요

### 1.1 본 정의서의 목적

본 정의서는 한국정보통신기술협회(TTA) 표준이 **"사람이 읽는 문서"**에서 **"AI 시스템이 직접 임포트·검증·활용하는 코드"**로 전환되도록 하는 **표준화된 패키지 작성 규칙**을 정의한다.

본 프레임워크를 따르면 다음이 보장된다:

- ✅ **글로벌 어휘 정합성**: DCAT v3 · DataCite · re3data · Croissant · PROV-O 등 11종 국제 어휘에 1:1 매핑
- ✅ **자동 검증 가능**: SHACL + Pydantic 이중 검증으로 적합성 자동 확인
- ✅ **즉시 ML 사용**: PyTorch · HuggingFace 등에서 한 줄 로딩
- ✅ **검색엔진 자동 연동**: Google Dataset Search · re3data 등에 자동 색인
- ✅ **거버넌스 추적**: 모든 결정·변경이 결정 ID로 추적

### 1.2 본 프레임워크의 적용 범위

| 적용 시점 | 대상 |
| --- | --- |
| **즉시** | 본 사업 5종 시범 표준 (P-01 ~ P-05, 모두 PG606 소관) |
| 본 사업 후 | TTA PG606 소관 메타데이터 표준 162건 (단계적 전환) |
| 향후 | TTA 전체 신규 표준 제·개정 (개정된 표준화 지침 의무 사항) |

### 1.3 본 정의서와 다른 산출물의 관계

```
┌─────────────────────────────────────────────────────────────┐
│ AI 레디 표준 프레임워크 정의서 (본 문서) — 규범적 (Normative)  │
└────────────┬────────────────────────────────────────────────┘
             │ 정의·적용
             ↓
┌─────────────────────────────────────────────────────────────┐
│ 표준화 지침 개정(안) — 본 프레임워크를 TTA 거버넌스에 통합     │
└────────────┬────────────────────────────────────────────────┘
             │ 의무화
             ↓
┌─────────────────────────────────────────────────────────────┐
│ 5종 파일럿 패키지 (P-01~P-05) — 본 프레임워크 적용 결과       │
└────────────┬────────────────────────────────────────────────┘
             │ 사용 가이드
             ↓
┌─────────────────────────────────────────────────────────────┐
│ 매뉴얼 3종 — TC 담당자/사용자 관점의 적용 가이드              │
└─────────────────────────────────────────────────────────────┘
```

---

## Part II. 7개 구성요소 모델

본 프레임워크의 핵심은 **모든 AI 레디 표준이 7개 구성요소를 갖춘다**는 원칙이다. 7개 중 3개는 기존 표준에서 전환되는 것이고, 4개는 AI 레디화로 신규 도입된다.

### 2.1 7개 구성요소 일람

| # | 구성요소 | 유형 | 역할 | 구현 형식 |
| --- | --- | --- | --- | --- |
| **c1** | 시맨틱 (Semantic) | 전환 | 각 요소의 의미를 글로벌 어휘로 표현 | JSON-LD `@context` 매핑 |
| **c2** | 데이터 모델 (Data Model) | 전환 | 카디널리티·제약·구조 정의 | SHACL `sh:NodeShape` |
| **c3** | 신태틱 (Syntactic) | 전환 | 표현 형식과 의미를 동시 처리 | JSON-LD 1.1 |
| **c4** | 운영 시맨틱 (Operational) | 신규 | ML 프레임워크에서의 동작 정의 | Croissant 1.0 어휘 (해당 시) |
| **c5** | 출처·계보 (Provenance) | 신규 | 데이터의 생성·변경·기여 이력 | W3C PROV-O |
| **c6** | 품질 프로파일 (Quality) | 신규 | 데이터 품질 차원의 기계화 | DQV (Boolean Activation Slot) |
| **c7** | 접근·사용 제약 (Access) | 신규 | 라이선스·권리·접근 정책 | dcterms:license + DUO/CC URI |

### 2.2 c1 시맨틱 (전환)

각 표준 요소의 의미를 **글로벌 RDF 어휘의 IRI**에 매핑한다.

**원칙**:

- 자체 IRI(`tta0976:Title`)와 글로벌 IRI(`dcterms:title`)를 **동시 정의**
- 매핑 우선순위: `primary` (직접 1:1) > `secondary` (의미 유사) > `loose` (느슨한 관계)
- 매핑 신뢰도: `high` / `medium` / `low`

**P-01 적용 예시**:

```json
"Title": {
  "@id": "dcterms:title",
  "@container": "@language"
}
```

### 2.3 c2 데이터 모델 (전환)

표준 본문의 M/R/O 등급과 카디널리티를 **SHACL 제약으로 변환**한다.

**M/R/O → SHACL severity 매핑**:

| 등급 | SHACL severity | CI 처리 |
| --- | --- | --- |
| **M** (Mandatory) | `sh:Violation` | 머지 차단 |
| **R** (Recommended) | `sh:Warning` | 경고 표시 |
| **O** (Optional) | `sh:Info` | 정보성 |

**P-01 적용 예시** (D2 Identifier가 M):

```turtle
ttaap:DatasetShape a sh:NodeShape ;
    sh:targetClass ttaap:Dataset ;
    sh:property [
        sh:path dcterms:identifier ;
        sh:minCount 1 ;
        sh:severity sh:Violation ;
    ] .
```

### 2.4 c3 신태틱 (전환)

표현 형식을 **JSON-LD 1.1**로 통일한다. JSON-LD를 선택한 이유:

- JSON 계열로 개발자에게 친숙
- `@context`로 의미와 표현을 동시 처리
- RDF/Turtle/N-Triples로 자동 직렬화 가능
- Google·schema.org·DCAT 모두 채택

### 2.5 c4 운영 시맨틱 (신규) — 조건부 적용

**ML 학습 데이터 표준에만 적용된다.** 일반 데이터 표준은 NA 처리.

ML 프레임워크(PyTorch DataLoader, TensorFlow Dataset)가 메타데이터를 직접 임포트하여 데이터 로딩까지 자동화하는 운영 의미를 정의한다.

**대상 표준**:

- ✅ P-03 비정형 태깅·라벨링
- ✅ P-04 농업 AI 학습 데이터
- ❌ P-01 연구데이터 (일반)
- ❌ P-02 공공데이터 (일반)

**구현**: MLCommons Croissant 1.0 어휘를 1차 매핑.

### 2.6 c5 출처·계보 (신규)

데이터의 **언제·누가·무엇으로부터** 생성되었는지를 W3C PROV-O로 표현한다.

**핵심 어휘**:

- `prov:wasGeneratedBy` — 어떤 활동의 산출물인지
- `prov:wasDerivedFrom` — 어떤 자원에서 파생되었는지
- `prov:wasAttributedTo` — 누구의 책임인지
- `prov:generatedAtTime` — 언제 생성되었는지

**조건부 활성화 패턴** (Decision-Q3/Q7): 본 표준의 Date+DateType 조합이 특정 값일 때만 PROV 필드 활성화.

### 2.7 c6 품질 프로파일 (신규)

데이터 품질 차원을 **W3C DQV(Data Quality Vocabulary)**로 기계화한다.

**★ Boolean Activation Slot 패턴 (본 사업의 핵심 혁신)**:

```turtle
# QualityManagement="yes"일 때만 dqv:hasQualityMetadata 활성
ttaap:QualityActivationShape a sh:NodeShape ;
    sh:targetClass ttaap:Repository ;
    sh:property [
        sh:path ttaap:QualityManagement ;
        sh:hasValue "yes" ;
    ] .
    # 활성 시: dqv:hasQualityMetadata 1..* 강제
```

**적용 차원**:

- 완전성 (Completeness)
- 적시성 (Timeliness)
- 정확성 (Accuracy)
- ISO/IEC 5259 정의 차용

### 2.8 c7 접근·사용 제약 (신규)

데이터의 **라이선스·접근 권한·사용 제약**을 기계 판독 가능한 IRI로 표현한다.

**필수 어휘**:

- `dcterms:license` — IRI 형식 (예: `https://creativecommons.org/licenses/by/4.0/`)
- `dcterms:accessRights` — 통제어 (open/embargoed/restricted/closed)
- DUO (Data Use Ontology) — 의료·민감 데이터의 세밀한 사용 제약

---

## Part III. 6 패키지 요소

본 프레임워크를 따르는 모든 표준은 **6개 디렉토리 구조**로 발행된다.

### 3.1 패키지 구조 일람

```
P-XX-domain/
├── 1_document/         AP (Application Profile) 명세 — 사람이 읽음
├── 2_schema/           기계 판독 스키마 — JSON-LD + SHACL
├── 3_code/             타입 안전 모델 — Python Pydantic
├── 4_validator/        검증 도구 — pySHACL CLI
├── 5_examples/         실제 시나리오 예시 — JSON-LD 인스턴스
└── 6_changelog/        버전·결정·결정 추적
```

### 3.2 1_document/ — Application Profile 명세

| 항목 | 내용 |
| --- | --- |
| 파일명 | `<표준ID>-AP.md` (예: `TTA-0976-AP.md`) |
| 형식 | Markdown |
| 필수 섹션 | (1) 개요, (2) 7개 구성요소 적용 결과, (3) 4계층/3계층 구조 매핑, (4) 통제어 카테고리, (5) 핵심 매핑 결정, (6) 사용 가이드 |
| 길이 | 200~400 라인 권고 |

### 3.3 2_schema/ — 스키마

| 파일 | 형식 | 내용 |
| --- | --- | --- |
| `context.jsonld` | JSON-LD 1.1 | prefix 정의 + 요소별 IRI 매핑 |
| `shapes.shacl.ttl` | Turtle (SHACL) | NodeShape + 보조 Shape (Activation 등) |

### 3.4 3_code/ — Python Pydantic 패키지

| 모듈 | 역할 |
| --- | --- |
| `models.py` | 4계층 클래스 + 통제어 Enum |
| `loader.py` | JSON-LD → Pydantic |
| `serializers.py` | Pydantic → JSON-LD |
| `tests/test_models.py` | 단위 테스트 (Decision 추적용) |

### 3.5 4_validator/ — 검증 도구

| 파일 | 역할 |
| --- | --- |
| `validate.py` | pySHACL 래퍼 + `inline_local_context()` |
| `test_sh_or.py` | sh:or 패턴 사전 호환성 테스트 |

### 3.6 5_examples/ — 예시

각 표준은 **최소 3개의 실제 도메인 예시**를 제공한다.

P-01 사례:

- `kisti_dataon.jsonld` — KISTI DataON Repository
- `nie_environmental.jsonld` — 국립생태원 Dataset
- `rda_agriculture.jsonld` — 농촌진흥청 Dataset

### 3.7 6_changelog/ — 버전·결정 추적

| 항목 | 형식 |
| --- | --- |
| 버전 | Semantic Versioning (1.0.0, 1.1.0, ...) |
| 어휘 lock | 채택한 5종 어휘의 정확한 버전 명시 |
| 결정 기록 | Decision-001, Decision-Q1 등 ID 부여 |
| Issue 추적 | Issue-001 등 호환성·버그 추적 |

---

## Part IV. 4 목적별 프로파일

동일한 표준을 **사용 목적**에 따라 다르게 활용할 수 있도록 4개 프로파일을 제공한다.

| 프로파일 | 적용 목적 | 핵심 어휘 | c4 활성 |
| --- | --- | --- | --- |
| **ML** | ML 학습 파이프라인 (PyTorch/TF/JAX) | Croissant 1.0 + DCAT v3 | ✅ |
| **RAG** | 검색 증강 생성 (RAG) | DCAT v3 + schema.org | ⚠️ 부분 |
| **KG** | 지식 그래프 구축 | OWL + SKOS + PROV-O | ❌ |
| **통계** | 통계 분석·공식 통계 | DDI + SDMX + ISO 5259 | ❌ |

### 4.1 프로파일 선택 결정 트리

```
이 데이터셋을 어디에 쓸 것인가?

  ML 학습 (PyTorch/HF) ──→ ML 프로파일
  RAG 시스템         ──→ RAG 프로파일
  지식 그래프 구축      ──→ KG 프로파일
  통계 분석          ──→ 통계 프로파일
  일반 보존·재사용     ──→ 프로파일 없음 (기본 7-구성요소)
```

### 4.2 프로파일 간 호환성

모든 프로파일은 **동일한 c1~c7 7-구성요소** 위에 작성된다. 프로파일은 c4(운영 시맨틱)와 c6(품질)에서 차이가 가장 크다.

---

## Part V. 국제 표준 어휘 정합성

### 5.1 11종 어휘 통합 원칙

| Prefix | 어휘 | 사용처 | RDF 발행 |
| --- | --- | --- | --- |
| `dcterms:` | DCMI Terms | 모든 표준 (기본) | ✅ |
| `dcat:` | DCAT v3 | 데이터셋 표현 (P-01·P-02) | ✅ |
| `dctype:` | DCMI Type | 자원 유형 분류 | ✅ |
| `prov:` | W3C PROV-O | 출처·계보 | ✅ |
| `dqv:` | W3C DQV | 데이터 품질 | ✅ |
| `sh:` | W3C SHACL | 검증 규칙 | ✅ |
| `skos:` | W3C SKOS | 통제어 분류 | ✅ |
| `schema:` | Schema.org | 검색엔진 색인 | ✅ |
| `foaf:` | FOAF | 인물·조직 | ✅ |
| `cc:` | Creative Commons | 라이선스 | ✅ |
| `datacite:` (kernel-4) | DataCite | 식별자·인용 | ❌ XSD |
| `re3data:` | re3data Schema | 리포지토리 | ❌ XSD |
| `cr:` | Croissant 1.0 | ML 운영 (선택) | ✅ |
| `duo:` | Data Use Ontology | 사용 제약 (선택) | ✅ |

### 5.2 어휘 캐시와 자동 검증

본 프레임워크는 **모든 RDF 발행 어휘를 git 저장소에 캐시**한다 (`vocabularies/cached/`). 이를 통해:

1. **재현성**: 어휘 버전을 git으로 고정
2. **속도**: CI에서 외부 네트워크 의존 제거
3. **검증**: 매핑 IRI가 실제 어휘에 정의되어 있는지 자동 확인

**자동 검증 명령**: `tta-verify-mappings`

- ✅ 본 사업 P-01에서 75/75 IRI = **100% 통과** 확인됨

### 5.3 매핑 결정 패턴 (필수 기록)

매핑 시 충돌이 발생하면 다음 중 하나로 분류한다:

| 분류 | 의미 | 처리 |
| --- | --- | --- |
| `[OVERRIDE]` | 본 AP가 본문 vs 부록 충돌을 한쪽으로 우선 결정 | Decision-NNN으로 기록 |
| `[CONFLICT]` | 표준 자체에 충돌 존재 | 해결 결정 명시 |
| `[CHECK]` | PG606 사후 확인 필요 | 추적 후 PG606 워크숍 |
| `[NA]` | 일관 처리 (예: 일반 표준의 c4) | 모든 행에 일관 적용 |

---

## Part VI. 표준 적용 방법론 (Phase A → D)

본 프레임워크를 새 표준에 적용하는 **5단계 워크플로우**.

### 6.1 Phase A — 표준 본문 추출 (1주)

| 산출물 | 형식 | 행 수 (P-01 사례) |
| --- | --- | --- |
| `tta-standards/<id>/elements.csv` | CSV | 93 (요소) |
| `tta-standards/<id>/enumerations.csv` | CSV | 117 (통제어) |
| `tta-standards/<id>/extraction_report.md` | Markdown | 추출 과정 문서 |

### 6.2 Phase A.5 — 어휘 보강 (1~2주, 1회)

표준 매핑에 필요한 외부 어휘 중 누락된 것을 인벤토리에 추가한다.

P-01 적용 결과: 11종 어휘 478행 통합 인벤토리 완성.

### 6.3 Phase B — 매핑 매트릭스 작성 (3~4주)

표준 요소 × 7개 구성요소 매트릭스를 작성한다.

| 컬럼 | 내용 |
| --- | --- |
| tta_inventory_id | TTA-XXXX-NNN |
| tta_layer / cardinality | 4계층·M/R/O |
| **c1~c7** | 각 구성요소별 매핑 |
| mapping_priority | primary/secondary/loose/none |
| mapping_confidence | high/medium/low |
| conflict_notes | 충돌 사항 |
| decision_basis | 결정 근거 |

P-01 결과: **210/208 = 99.0% 매핑 성공** (목표 95% 대비 +4%p).

### 6.4 Phase C — 패키지 작성 (4~6주)

위 6개 디렉토리 구조로 패키지 작성. P-01 결과: 17 파일 / 3,093 라인.

### 6.5 Phase D — 검증·발행 (2~3주)

| 단계 | 검증 항목 |
| --- | --- |
| D-1 자기 검증 | pytest + sh:or + 3 examples |
| D-2 SHACL-AF 강화 | (해당 시) |
| D-3 다른 표준 적용 | 확장성 검증 |
| D-4 배포 | git tag + DOI 등록 |
| D-5 PG606 워크숍 | 표준 개정 트리거 |

---

## Part VII. 검증 프레임워크

### 7.1 4계층 품질 보증

| 계층 | 주체 | 시점 |
| --- | --- | --- |
| L1 작성자 셀프 체크 | 작성 담당자 | 산출물 작성 직후 |
| L2 PM 검토 | PM (박사급) | 주간 PM 회의 |
| L3 외부 전문가 Peer Review | 외부 2인 이상 | 단계별 마일스톤 |
| L4 자동 검증 (CI/CD) | GitHub Actions | 커밋 시점 |

### 7.2 자동 검증 도구

| 도구 | 검증 대상 |
| --- | --- |
| `tta-verify-mappings` | IRI 매핑이 정식 어휘에 존재 |
| `pytest tests/` | Pydantic 모델 동작 |
| `validate.py` | SHACL 적합성 |
| `test_sh_or.py` | pySHACL sh:or 호환성 |

### 7.3 산출물 유형별 정량 통과 기준

| 산출물 | 기준 |
| --- | --- |
| JSON-LD 스키마 | 문법 오류 0건, 매핑 100% 검증 |
| SHACL 검증 파일 | 테스트 케이스 90% 이상 통과 |
| Python 코드 | 단위 테스트 커버리지 80% 이상 |
| 예시 데이터셋 | 로딩 성공률 100% |

---

## Part VIII. 거버넌스

### 8.1 버전 관리

**Semantic Versioning**:

- `MAJOR.MINOR.PATCH`
- MAJOR: 호환성 깨짐 (예: 매핑 IRI 변경)
- MINOR: 호환 추가 (예: 새 통제어 값)
- PATCH: 버그 수정

### 8.2 결정 추적

모든 의미 있는 결정은 **Decision ID**를 부여하여 6_changelog/CHANGELOG.md에 기록.

P-01 결정 사례: D-001 (IRI 부여), D-002 (alpha-3 → alpha-2), D-003/004 (본문 vs 부록 충돌), D-Q4 (Boolean Activation Slot) 등 9건.

### 8.3 어휘 변경 대응

외부 어휘(DCAT, Croissant 등)가 새 버전을 발행하면:

1. `vocab-refresh.yml` 워크플로우가 주 1회 자동 감지
2. 변경 PR 자동 생성
3. PM 리뷰 → 영향 분석 → 매핑 갱신 결정
4. 본 정의서 또는 패키지 MINOR 버전 증가

---

## Part IX. 적용 사례 — P-01 (TTAK.KO-10.0976)

### 9.1 적용 결과 요약

| 항목 | 값 |
| --- | --- |
| 표준 | TTAK.KO-10.0976 (2017, PG606) |
| 본 AP 버전 | **1.0.0** (2026-05-04) |
| 매핑 성공률 | **★ 99.0%** (210/208) |
| Phase D-1 검증 | pytest 11/11 + sh:or 4/4 + 3 examples conform |
| 핵심 혁신 | Boolean Activation Slot (Decision-Q4) |

### 9.2 P-01 → P-02~P-05 확장 계획

| 표준 | 본 프레임워크 적용 시 예상 작업량 |
| --- | --- |
| P-02 공공데이터 | Phase A~D 6주 (DCAT v3 활용 = P-01과 유사) |
| P-03 태깅·라벨링 | Phase A~D 8주 (c4 운영 시맨틱 활성 = Croissant 매핑 추가) |
| P-04 농업 AI | Phase A~D 8주 (c4 + c6 모두 활성) |
| P-05 철강 제조 | Phase A~D 8주 (c5 PROV-O 비중 큼) |

→ 본 프레임워크의 재사용성 덕분에 4종 합계 **약 30주** 추정 (사업 일정 9~11월 = 약 12주 안에 가능).

---

## 부록 A — 새 표준 적용 체크리스트

새 TTA 표준을 본 프레임워크로 AI 레디화할 때 점검 사항.

### Phase A

- [ ] 표준 본문 PDF/HWP 확보
- [ ] elements.csv 추출 (모든 요소를 표준 ID와 함께)
- [ ] enumerations.csv 추출 (통제어 모두)
- [ ] M/R/O 등급 정확히 보존 확인
- [ ] 본문 vs 부록 충돌 식별 및 [CONFLICT] 마킹

### Phase A.5

- [ ] 매핑에 필요한 외부 어휘 식별
- [ ] 캐시에 없는 어휘 추가 + MANIFEST.json 갱신
- [ ] vocab-refresh CI 통과 확인

### Phase B

- [ ] 7개 구성요소 매트릭스 작성 (모든 행에 c1~c7 결정)
- [ ] mapping_priority 분포 확인 (primary 80%+ 권고)
- [ ] mapping_confidence 분포 확인 (high 75%+ 권고)
- [ ] 매핑 충돌 분석 보고서 작성

### Phase C

- [ ] 6 디렉토리 구조 생성
- [ ] 1_document/<id>-AP.md 작성 (필수 6 섹션)
- [ ] 2_schema/context.jsonld + shapes.shacl.ttl 작성
- [ ] 3_code/ Pydantic 모델 + 단위 테스트 (모든 결정 사항 반영)
- [ ] 4_validator/ validate.py 적응
- [ ] 5_examples/ 최소 3개 실제 시나리오
- [ ] 6_changelog/CHANGELOG.md 작성

### Phase D

- [ ] tta-verify-mappings 100% 통과
- [ ] pytest 100% 통과
- [ ] 모든 examples conform
- [ ] CI 통과 후 PR 머지
- [ ] git tag <표준ID>/v1.0.0

---

## 부록 B — 참고 산출물

| 산출물 | 위치 |
| --- | --- |
| 인벤토리 478행 | [`inventory/master_inventory.csv`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/inventory/master_inventory.csv) |
| P-01 매핑 매트릭스 | [`mappings/tta-0976_x_components.csv`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/mappings/tta-0976_x_components.csv) |
| P-01 AP 1.0.0 명세 | [`standards/P-01-research-data/1_document/TTA-0976-AP.md`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/standards/P-01-research-data/1_document/TTA-0976-AP.md) |
| Phase 보고서 | [`reports/phase_*_summary.md`](https://github.com/ai-ready-standards/tta-ai-ready/tree/main/reports) |
| 매핑 충돌 분석 | [`reports/tta-0976_mapping_conflicts.md`](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/tta-0976_mapping_conflicts.md) |

---

## 변경 이력

| 버전 | 날짜 | 변경 |
| --- | --- | --- |
| **v1.0 초안** | 2026-05-05 | P-01 검증 결과 기반 초기 발행 |
| (예정) v1.0 | 2026-08-31 | 2단계 완료 시 정식 발행 (P-02~P-05 적용 결과 반영) |
| (예정) v1.1 | 2026-12-15 | 사업 종료 시 최종본 (PG606 워크숍 피드백 반영) |
