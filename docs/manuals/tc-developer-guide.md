# TC 개발 가이드 — 신규 표준 작성 매뉴얼

| 항목 | 내용 |
| --- | --- |
| 매뉴얼 ID | D-2 |
| 버전 | **v0.5 초안** (2026-05-05) |
| 대상 | TTA의 새 표준을 작성하는 **TC 담당자·표준 초안 작성자** |
| 정식 발행 | 2026-12 (사업 종료 시) |

> 본 매뉴얼은 **새 표준을 처음부터 AI 레디 형태로 작성하는 방법**을 다룹니다. 이미 등록된 표준을 AI 레디로 전환하시려면 [기존 표준 전환 매뉴얼](migration-guide.md)을 참조하세요.

---

## 0. 시작 전 점검

표준 작성을 시작하기 전 다음을 확인하세요.

- [ ] PG606 표준화 운영팀과 표준 제안 이미 협의 완료
- [ ] 표준의 **자원 모델**(Repository / Collection / Dataset / File 등) 결정
- [ ] 본 표준이 **ML 학습 데이터** 표준인가? → c4 운영 시맨틱 활성 결정
- [ ] [프레임워크 정의서](../framework/index.md) Part II 7개 구성요소 모델 통독

---

## 1. 표준 본문 작성 시 — 7개 구성요소 의식

### 1.1 본문 작성 체크리스트

새 표준 본문(HWP/PDF)을 작성할 때 **각 요소에 대해** 다음 7가지를 의식적으로 결정하세요.

| 구성요소 | 본문에 명시 사항 | P-01 사례 |
| --- | --- | --- |
| **c1 시맨틱** | "관련 출처: DCMI 참조: dc:title" 식으로 외부 어휘 명시 | "DCMI 참조: dc:title" (line 1303) |
| **c2 데이터 모델** | 카디널리티 (M/R/O) + 형식 제약 | "Property", "M(필수)" |
| **c3 신태틱** | 표현 형식 (XML/JSON-LD 예시) | "XML 사례", "JSON 사례" |
| **c4 운영 시맨틱** | (ML 표준만) ML 프레임워크 연동 의도 | NA — 일반 연구데이터 |
| **c5 출처·계보** | Date/Creator/Contributor 항목에 ProvType 매핑 가능성 | DateType, ContributorType 통제어 |
| **c6 품질** | QualityManagement 통제어 (yes/no/unknown) | R17 QualityManagement |
| **c7 접근·사용 제약** | License + AccessType 명시 | R12 DataLicenseName, R13 DataLicenseUrl |

### 1.2 작성 형식 권고

P-01(TTAK.KO-10.0976)을 본보기로 다음 형식을 권고합니다:

```
ID         : 요소 식별자 (C1, C2, C2.1 등)
요소 이름  : 영문 식별자 (CamelCase)
표시 상수  : 한글 표시명
요소 유형  : Property / SEP / Class / CVP
요소 설명  : 의미 정의
활용 예시  : 사용 시나리오
관련 출처  : ★ 외부 어휘 IRI 명시 (DCMI 참조: dc:title 등)
```

**핵심**: "관련 출처"를 **모든 요소에 빠짐없이** 적어주세요. 이게 곧 c1 시맨틱 매핑이 됩니다.

---

## 2. 부록 작성 — 통제어를 명확하게

본문에 사용된 **모든 통제어(CVP)**를 부록 II-1에 정확히 정의하세요.

### 2.1 통제어 작성 권고 형식

```
TitleType
참조: DataCite

  AlternativeTitle
  Subtitle
  TranslatedTitle
  other
```

### 2.2 통제어 작성 시 주의 사항

- **외부 어휘에서 직접 인용** 권고 (예: DataCite contributorType의 22개 값 그대로)
- 한국 고유 값은 **명시적 보강** (P-01의 IdentifierType에 UCI 추가)
- 'other' 폴백은 신중히 — 자동 검증이 약화됨
- **부록 II-2 요소 인덱스**에 M/R/O 명시

---

## 3. M/R/O 등급 부여 원칙

### 3.1 등급 결정 기준

| 등급 | 부여 기준 |
| --- | --- |
| **M (Mandatory)** | 이 요소가 없으면 자원의 식별·인용·접근이 불가능한 경우 |
| **R (Recommended)** | 권장 사항이지만 부재 시 자원 활용은 가능 |
| **O (Optional)** | 추가 정보. 풍부함을 위함 |

### 3.2 등급 부여 시 의식해야 할 것

- **M 등급은 신중히** — CI에서 위반 시 머지 차단됨
- **본문 vs 부록 충돌 방지** — 동일 요소에 양쪽 등급 다르게 표기되는 경우 매핑 단계에서 [CONFLICT] 발생
- **글로벌 어휘 호환** — DataCite의 Identifier가 mandatory이면 본 표준에서도 M으로 통일하는 것이 자연스러움

P-01 사례:
- D2 IdentifierType: 본문 M / 부록 O — Decision-003에서 부록 우선 결정 (부록이 정식 적용)
- D5 Publisher: 본문 M / 부록 R — Decision-004에서 부록 우선 결정

→ 가능하면 **본문과 부록의 등급을 일치**시키세요.

---

## 4. 글로벌 어휘 정합성 사전 고려

### 4.1 권고 어휘 (자원 유형별)

| 자원 유형 | 1차 어휘 | 보조 어휘 |
| --- | --- | --- |
| 데이터셋 일반 | DCMI Terms + DCAT v3 | schema.org |
| 식별자·인용 | DataCite Schema 4.5 | — |
| 리포지토리 | re3data Schema 3.1 | — |
| 출처·계보 | W3C PROV-O | — |
| 품질 | W3C DQV | ISO/IEC 5259 |
| ML 학습 데이터 | MLCommons Croissant 1.0 | — |
| 의료·민감 데이터 | DUO (Data Use Ontology) | — |

### 4.2 매핑 시 고려 사항

- **하나의 IRI를 두 요소에 동시 매핑하지 마세요** — predicate 충돌 발생 (P-01 Decision-Q1 참조)
- **DCMI 권고**: 가능하면 dcterms 우선 (가장 안정적·범용)
- **언어 태그**: 다국어 필드는 `@container: @language` 사용

---

## 5. 패키지 작성 (Phase C)

표준 본문이 완성되면 6 패키지 디렉토리 구조로 작성합니다.

### 5.1 패키지 구조

```
P-XX-domain/
├── 1_document/<표준ID>-AP.md
├── 2_schema/
│   ├── context.jsonld
│   └── shapes.shacl.ttl
├── 3_code/
├── 4_validator/
├── 5_examples/
└── 6_changelog/CHANGELOG.md
```

### 5.2 단계별 작성 순서

1. **1_document/<표준ID>-AP.md 먼저 작성** (사람이 이해할 수 있는 형식으로)
2. **2_schema/context.jsonld** — Application Profile의 매핑을 JSON-LD로
3. **2_schema/shapes.shacl.ttl** — M/R/O를 SHACL severity로
4. **3_code/** — Pydantic 모델로 타입 안전성 확보
5. **5_examples/** — 실제 사용 시나리오 3종 이상 작성
6. **4_validator/** — pySHACL 래퍼 작성 (P-01 템플릿 복사 권장)
7. **6_changelog/CHANGELOG.md** — 어휘 버전 lock + 결정 기록

자세한 작성 방법은 **[기존 표준 전환 매뉴얼](migration-guide.md)** Phase C 섹션을 참고하세요.

---

## 6. 검증 (Phase D)

### 6.1 자동 검증 도구

```bash
# 어휘 매핑 검증
tta-verify-mappings

# Pydantic 모델 테스트
cd standards/P-XX-domain/3_code && pytest tests/

# SHACL 검증
python standards/P-XX-domain/4_validator/validate.py \
  standards/P-XX-domain/5_examples/*.jsonld
```

### 6.2 통과 기준

| 검증 | 기준 |
| --- | --- |
| 매핑 검증 | **100%** — 모든 IRI가 정식 어휘에 정의됨 |
| Pydantic 테스트 | **모두 통과** + 커버리지 80% 이상 |
| SHACL Conforms | **3 examples 모두 Conforms** |
| 매핑 매트릭스 | primary 80%+ + high 신뢰도 75%+ |

P-01 결과: 매핑 99.0%, pytest 11/11, examples 3/3 conform.

---

## 7. 발행 (PG606 심의 → SPC 심의)

### 7.1 PG606 심의

1. 본 매뉴얼대로 작성된 패키지를 PG606 워크숍에 발표
2. 7개 구성요소 적용 결과 시연 (라이브 검증 포함)
3. PG606 의견 반영 → 패키지 갱신

### 7.2 SPC 심의

1. 표준화 지침 개정안에 따라 자동 검증 통과를 의무 사항으로
2. SPC에서 본 패키지의 자동 검증 통과 여부 확인
3. 통과 시 정식 발행

---

## 8. 자주 묻는 질문

??? question "M/R/O를 본문과 부록에 다르게 적어도 되나요?"
    원칙적으로는 **일치시키세요**. 다른 경우 [CONFLICT]로 식별되어 매핑 시 결정이 필요합니다. P-01에서는 부록 우선 원칙을 적용했습니다.

??? question "통제어에 'other' 값을 넣어도 되나요?"
    가능하지만 **자동 검증이 약화됩니다**. 'other'는 모든 미지의 값을 허용하므로 SHACL `sh:in` 제약이 사실상 우회됩니다. 가능하면 enumerate 가능한 값으로 한정하세요.

??? question "글로벌 어휘에 매핑되지 않는 한국 고유 항목이 있어요"
    P-01의 **UCI**(Korean Universal Content Identifier) 같은 케이스입니다. 이때:
    
    1. 본 표준 namespace에 자체 IRI 정의 (예: `tta0976cv:UCI`)
    2. 매핑 매트릭스의 mapping_priority를 `none`으로 표기
    3. decision_basis에 사유 명시 ("한국 고유 식별 체계")
    4. PG606 워크숍에서 향후 ISO 등재 가능성 검토

??? question "신규 표준에 기존 표준의 일부를 재사용하고 싶어요"
    `@context`에서 기존 표준의 prefix를 import하는 패턴 권고:
    
    ```json
    "@context": [
      "https://standards.tta.or.kr/0976/context.jsonld",
      {
        "MyNewElement": "..."
      }
    ]
    ```

---

## 부록 — 작성 체크리스트

```
□ 본문 작성 시
  □ 모든 요소에 "관련 출처" 명시 (외부 어휘 IRI)
  □ 모든 통제어가 부록 II-1에 정의됨
  □ M/R/O 등급이 본문과 부록에서 일치
  □ 다국어 필드의 @language 처리 결정

□ 패키지 작성 시
  □ 1_document/<표준ID>-AP.md 6 섹션 모두 작성
  □ 2_schema/ 작성 (context + shapes)
  □ 5_examples/ 최소 3개 실제 시나리오
  □ 6_changelog 어휘 버전 lock
  □ 모든 결정에 Decision-NNN ID 부여

□ 검증
  □ tta-verify-mappings 100% 통과
  □ pytest 100% 통과 + 커버리지 80%+
  □ 모든 examples Conforms

□ PG606 심의 준비
  □ 라이브 검증 시연 가능
  □ 매핑 매트릭스 충돌 분석 보고서 첨부
  □ 7개 구성요소 적용 결과 슬라이드
```
