# 기존 표준 AI 레디화 전환 매뉴얼

| 항목 | 내용 |
| --- | --- |
| 매뉴얼 ID | D-3 |
| 버전 | **v0.5 초안** (2026-05-05) |
| 대상 | 이미 등록된 TTA 표준을 AI 레디 패키지로 전환하려는 **TC 담당자·연구자** |
| 정식 발행 | 2026-12 (사업 종료 시) |

> 본 매뉴얼은 P-01 (TTAK.KO-10.0976, 2017) 전환 사례를 그대로 따라 가는 형식입니다. 각 단계마다 P-01에서 실제 발견된 이슈와 해결 결정을 함께 보여줍니다.

---

## 0. 전환 가능성 판단 (5분)

자기 표준이 본 프레임워크로 전환 가능한지 다음을 빠르게 점검하세요.

### 빠른 체크리스트

- [ ] 표준 본문 PDF 또는 HWP를 갖고 있다
- [ ] 부록에 통제어가 정의되어 있다 (열거형 값 목록)
- [ ] 본문에 "관련 출처" 또는 "참조 표준"이 일부라도 있다
- [ ] 표준이 **데이터 메타데이터** 또는 **데이터 운영** 영역이다 (PG606 소관)

→ 4개 중 3개 이상이면 전환 가능. 모두 ✓이면 P-01과 유사한 매핑률 99% 가능.

### 전환 난이도 추정

| 조건 | 예상 난이도 | P-01과 비교 |
| --- | --- | --- |
| 본문에 외부 어휘 명시(DCMI 참조 등) 풍부 | 쉬움 | 동급 |
| ML 학습 데이터 표준 (c4 활성) | 보통 | +30% (Croissant 매핑 추가) |
| 도메인 특화 어휘 많음 (농업·철강 등) | 보통 | +20% |
| 외부 어휘 명시 거의 없음 | 어려움 | +50% (의미 추론 필요) |

---

## 1. 도구 설치 (10분)

### 가장 쉬운 방법 — Codespaces (브라우저)

설치 없이 브라우저에서 즉시 사용 가능.

[:material-rocket: Codespaces 열기](https://codespaces.new/ai-ready-standards/tta-ai-ready?quickstart=1){ .md-button .md-button--primary }

→ 1~2분 후 VS Code 인터페이스 자동 열림. tta-validator·pyshacl·pydantic 모두 설치된 상태.

### 로컬 설치 (장기 작업 시)

```bash
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
python3.11 -m venv venv
source venv/bin/activate           # Windows: .\venv\Scripts\Activate.ps1
pip install -e tools/validator/
pip install pydantic pyshacl rdflib pyld pytest
```

### 검증

```bash
tta-verify-mappings
# → ✓ 75/75 매핑 모두 정식 어휘에 존재 (100.0%)
```

이 메시지가 나오면 환경 정상.

---

## 2. Phase A — 표준 본문 추출 (1주)

### 2.1 작업 디렉토리 준비

자기 표준 ID를 결정합니다 (예: P-XX, 또는 표준번호 그대로).

```bash
mkdir -p tta-standards/<표준ID>/
mkdir -p standards/P-XX-<도메인>/{1_document,2_schema,3_code,4_validator,5_examples,6_changelog}
```

### 2.2 elements.csv 작성

표준 본문을 읽으며 모든 메타데이터 요소를 CSV에 옮깁니다.

**컬럼 (P-01 기준)**:

```csv
inventory_id,layer,id,name_ko,name_en,type,cardinality,
source_section,definition,examples,external_reference
```

P-01 사례:

```csv
TTA-0976-001,repository,R1,리포지터리,Repository,Class,O,
6.1,연구데이터를 담고 있는 시스템 및 서비스 정보를 기술함,,
TTA-0976-002,repository,R2,리포지터리 URL,RepositoryUrl,Property,M,
6.1,...,http://www.exampleRepository.ac.kr,re3data:repositoryURL
```

### 2.3 enumerations.csv 작성

부록 II-1 통제어를 모두 CSV에 옮깁니다.

```csv
cv_id,category,value_ko,value_en,source,
notes
TTA-0976-CV-001,IdentifierType,DOI,DOI,DataCite,
TTA-0976-CV-002,IdentifierType,Handle,Handle,DataCite,
...
```

### 2.4 추출 보고서 작성

`tta-standards/<표준ID>/extraction_report.md`에 다음 정리:

- 추출 일자·작업자
- 추출 통계 (요소 수·통제어 수)
- 본문 vs 부록 등급 충돌 [CONFLICT] 식별
- PG606에 확인 필요 사항 [CHECK]

---

## 3. Phase A.5 — 어휘 보강 (1~2일, 1회)

자기 표준에 매핑할 외부 어휘 중 **인벤토리에 없는 것**을 추가합니다.

### 3.1 누락 어휘 식별

P-01 작업 시 다음이 누락되어 있어 보강했습니다:

- DataCite Schema 4.5
- re3data Schema 3.1
- DCMI Type Vocabulary
- ISO 코드 표준

### 3.2 어휘 캐시에 추가

```bash
# 어휘 RDF 파일을 vocabularies/cached/에 복사
cp <vocab>.ttl vocabularies/cached/

# vocabularies/cached/MANIFEST.json에 entry 추가
```

### 3.3 인벤토리에 entry 추가

```bash
# inventory/<vocab>.csv 작성
# inventory/master_inventory.csv에 통합
```

자세한 형식: [Phase A.5 보고서](https://github.com/ai-ready-standards/tta-ai-ready/blob/main/reports/phase_a5_summary.md) 참조.

---

## 4. Phase B — 매핑 매트릭스 (3~4주)

### 4.1 매트릭스 파일 생성

`mappings/tta-<표준ID>_x_components.csv` 작성. 16컬럼:

```
tta_inventory_id, tta_element_name_ko, tta_layer, tta_cardinality,
c1_semantic, c2_data_model, c3_syntactic,
c4_operational_semantic, c5_provenance, c6_quality, c7_access_constraint,
mapping_priority, mapping_confidence,
conflict_notes, decision_basis, reviewer_notes
```

### 4.2 매핑 작업 흐름

각 요소(1행)에 대해:

1. **c1 시맨틱**: 글로벌 어휘 IRI 매핑
2. **c2 데이터 모델**: SHACL 제약 결정
3. **c3 신태틱**: JSON-LD 표현 결정
4. **c4 운영 시맨틱**: ML 표준이면 Croissant 매핑, 아니면 NA
5. **c5 출처·계보**: PROV-O 매핑 가능성 검토
6. **c6 품질**: DQV 매핑 (Boolean Slot 활성 여부)
7. **c7 접근·사용 제약**: License/Access/Rights 매핑

### 4.3 매핑 충돌 해결

매핑 시 충돌이 발생하면 다음 중 하나로 분류:

| 분류 | 사용 시점 | 행동 |
| --- | --- | --- |
| `[OVERRIDE]` | 본문 vs 부록 등급 충돌 | Decision-NNN ID 부여 + 결정 근거 |
| `[CONFLICT]` | 표준 자체 충돌 | 결정 + decision_basis 명시 |
| `[CHECK]` | PG606 사후 확인 필요 | 추적 + 워크숍 안건 |
| `[NA]` | 일관 처리 (예: 일반 표준의 c4) | 모든 행에 동일 표기 |

### 4.4 P-01 충돌 사례

| Decision | 충돌 | 결정 |
| --- | --- | --- |
| D-001 | Repository tta_iri | 임시 IRI 부여, TTA 공식 발급 시 갱신 |
| D-002 | InstitutionCountry alpha-3 vs alpha-2 | DCAT v3 호환을 위해 alpha-2 |
| D-003 | D2.1 IdentifierType (본문 M / 부록 O) | 부록 우선 |
| D-004 | D5 Publisher (본문 M / 부록 R) | 부록 우선 |
| D-Q4 | DQV 활성화 조건 | Boolean Activation Slot 패턴 |

### 4.5 매핑 통계 점검

작업 완료 시 다음 통계가 권고 기준을 충족하는지 확인:

| 지표 | 권고 | P-01 |
| --- | --- | --- |
| primary 비율 | 80% 이상 | 88.2% (82/93) |
| high confidence | 75% 이상 | 81.7% (76/93) |
| 종합 매핑 성공률 | 95% 이상 | **99.0%** (210/208) |

---

## 5. Phase C — 패키지 작성 (4~6주)

### 5.1 1_document/<표준ID>-AP.md

**P-01 AP 문서**를 템플릿으로 사용:

```bash
cp standards/P-01-research-data/1_document/TTA-0976-AP.md \
   standards/P-XX-<도메인>/1_document/<표준ID>-AP.md
```

필수 6 섹션:

1. 개요
2. 7개 구성요소 적용 결과
3. 4계층 ↔ DCAT 3계층 매핑
4. 통제어 카테고리
5. 핵심 매핑 결정 (Decision-NNN 표)
6. 사용 가이드

### 5.2 2_schema/context.jsonld

JSON-LD `@context`로 prefix·요소·매핑을 통합 정의.

P-01 템플릿:

```json
{
  "@context": {
    "@version": 1.1,
    "@base": "https://standard.tta.or.kr/<표준ID>/",
    
    "ttaap": "https://standard.tta.or.kr/ai-ready/profile#",
    "tta<ID>": "https://standard.tta.or.kr/<표준ID>#",
    "tta<ID>cv": "https://standard.tta.or.kr/<표준ID>/cv#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "datacite": "http://datacite.org/schema/kernel-4#",
    "re3data": "https://www.re3data.org/schema#",
    
    "Title": {"@id": "dcterms:title", "@container": "@language"},
    ...
  }
}
```

### 5.3 2_schema/shapes.shacl.ttl

SHACL NodeShape로 카디널리티·통제어 제약.

핵심 패턴:

```turtle
ttaap:DatasetShape a sh:NodeShape ;
    sh:targetClass ttaap:Dataset ;
    sh:property [
        sh:path dcterms:title ;
        sh:minCount 1 ;
        sh:severity sh:Violation ;  # M = Violation
        sh:or (                       # 다국어 필드
            [sh:datatype xsd:string]
            [sh:datatype rdf:langString]
        )
    ] .
```

**주의**: 다국어 필드는 `sh:or` 패턴 필수. P-01 Issue-001 참조.

### 5.4 3_code/ Pydantic 패키지

```python
# models.py
from pydantic import BaseModel, Field
from enum import Enum

class IdentifierType(str, Enum):
    DOI = "DOI"
    Handle = "Handle"
    URL = "URL"
    # ... 모든 통제어 값

class Dataset(BaseModel):
    Title: dict[str, str]  # 다국어
    Identifier: str
    IdentifierType: IdentifierType
    # ...
```

`tests/test_models.py`에 모든 결정(Decision-NNN)에 대한 단위 테스트 작성.

### 5.5 4_validator/

P-01 validator를 그대로 복사 후 표준 ID만 변경:

```bash
cp standards/P-01-research-data/4_validator/* \
   standards/P-XX-<도메인>/4_validator/
```

### 5.6 5_examples/

**최소 3개 실제 도메인 시나리오**를 JSON-LD로 작성. 가상 데이터 X, 실제 기관·실제 식별자 사용.

P-01 사례:

- `kisti_dataon.jsonld` — KISTI DataON Repository
- `nie_environmental.jsonld` — 국립생태원 Dataset
- `rda_agriculture.jsonld` — 농촌진흥청 Dataset

### 5.7 6_changelog/CHANGELOG.md

- 어휘 버전 lock (DCMI Terms 2020-01-20, DataCite 4.5 등)
- Decision-NNN 모두 기록
- Issue-NNN 추적

---

## 6. Phase D — 검증 (2~3주)

### 6.1 D-1 자기 검증

```bash
# 1. 어휘 매핑 100% 통과
tta-verify-mappings

# 2. Pydantic 단위 테스트
cd standards/P-XX-<도메인>/3_code
PYTHONPATH=. pytest tests/ -v --cov=tta_<id>

# 3. SHACL 검증
cd standards/P-XX-<도메인>
python 4_validator/test_sh_or.py        # 사전 호환성
for f in 5_examples/*.jsonld; do
  python 4_validator/validate.py "$f"
done
```

모든 검증 통과 시 D-1 완료. 검증 보고서를 `reports/phase_d1_verification.md`에 작성.

### 6.2 검증 결과 해석

| 결과 | 의미 | 행동 |
| --- | --- | --- |
| ✓ Conforms: True | 적합 | 다음 단계 진행 |
| ✗ Violation | M 위반 — 필수 필드 누락 | 데이터 수정 또는 매핑 재검토 |
| ⚠️ Warning | R 위반 — 권고 사항 미충족 | 가능하면 보완 |
| ℹ️ Info | O 위반 — 정보성 | 무시 가능 |

### 6.3 흔한 검증 실패 원인 + 해결

??? failure "다국어 필드에서 datatype mismatch"
    `xsd:string` 강제하면 `@container: @language`로 생성된 `rdf:langString`과 불일치.
    
    **해결**: `sh:or ([sh:datatype xsd:string] [sh:datatype rdf:langString])` 패턴 사용

??? failure "sh:in 항목과 데이터의 datatype 불일치"
    `sh:in ("DOI" ...)`는 plain literal이지만 데이터는 `"DOI"^^xsd:string`.
    
    **해결**: `sh:in` 값에 `^^xsd:string` 명시. 또는 데이터를 plain literal로.

??? failure "동일 술어에 여러 값이 들어가 maxCount 위반"
    P-01의 `dcterms:title`이 RepositoryName + InstitutionName 둘 다 매핑되어 4개 langString 생성.
    
    **해결**: 다른 어휘로 분산 (P-01에서는 InstitutionName을 `re3data:institutionName`으로)

---

## 7. PG606 협의

### 7.1 워크숍 자료 준비

- 7개 구성요소 적용 결과 슬라이드
- 매핑 매트릭스 충돌 분석 보고서
- D-1 검증 결과 요약
- 라이브 검증 시연

### 7.2 협의 안건

- [CHECK] 항목 (PG606 확인 필요)에 대한 결정
- 본문 vs 부록 충돌의 정식 해결
- 표준 개정 후속 작업 (해당 시)

### 7.3 본 표준 SPC 심의 (해당 시)

표준화 지침 개정안에 따라 자동 검증 통과가 SPC 심의 통과의 전제 조건이 됩니다.

---

## 8. 자주 묻는 질문

??? question "표준 본문에 외부 어휘 참조가 거의 없어요. 매핑이 가능할까요?"
    가능하지만 **의미 추론 작업이 추가**됩니다. 작업량은 P-01 대비 +50% 정도. 다음 순서를 권고:
    
    1. 본문 정의를 영문으로 의역
    2. concept_tag(28개) 중 가장 가까운 것에 분류
    3. 동일 concept_tag의 다른 어휘 항목과 비교 → 가장 가까운 IRI 선택
    4. mapping_confidence를 medium 이하로 설정
    5. PG606 워크숍에서 검증

??? question "PG606이 아닌 다른 PG의 표준도 전환 가능한가요?"
    가능합니다. 다만:
    
    - 본 사업의 5종 시범 표준은 모두 PG606 — 검증된 사례
    - 다른 PG의 자원 모델이 다를 수 있음 (예: PG401은 단말 표준)
    - 7개 구성요소 모델은 자원 메타데이터 표준에 최적화됨
    - 자원 메타데이터가 아닌 표준(예: 통신 프로토콜)은 적용성 검토 필요

??? question "전환 전후로 표준 본문도 바뀌나요?"
    원칙은 **본문 변경 최소화**입니다. AI 레디화는 별도 패키지로 추가되며, 본문은 보통 다음 개정 시점까지 그대로 유지. 단, [CHECK] 항목이 본문 오류로 판명되면 PG606 심의를 거쳐 본문 정정.

??? question "어휘 매핑이 100%가 안 나오는데 어떻게 하나요?"
    P-01도 99.0%였습니다. 100% 미달 사유는:
    
    - **한국 고유 식별자** (UCI 등) → 글로벌 어휘 부재가 정당. 자체 IRI 부여
    - **'other' 폴백 값** → 의도적 미매핑. 매핑 priority `none`
    - **새 도메인 개념** → Phase A.5에서 어휘 보강 필요
    
    "글로벌 어휘 보유 가능 항목 100% 매핑"이 실질 목표입니다.

---

## 부록 — 전환 작업 일정 추정

| 표준 유형 | A | A.5 | B | C | D | 합계 |
| --- | --- | --- | --- | --- | --- | --- |
| 일반 데이터 (P-01형) | 1주 | 0~1주 | 3주 | 4주 | 2주 | **10~11주** |
| ML 학습 데이터 (P-03형) | 1주 | 1주 | 4주 | 5주 | 2주 | **13주** |
| 산업 도메인 (P-05형) | 1주 | 1주 | 3주 | 5주 | 2주 | **12주** |

→ 5종 동시 진행 시 (병행) 약 12~16주.
