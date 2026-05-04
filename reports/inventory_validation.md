# TTA AI-Ready Data 표준 인벤토리 — 통합 검증 리포트 (v2)

- **버전 이력**:
  - v1 (2026-05-03 초안): 4개 표준 통합, 319 행
  - v2 (2026-05-03 보강): 6개 표준 통합, 356 행 (+ dcterms 25 + DQV 21 - PROV-DC 9), 5개 태그 추가, TRUNCATED 보강
- 산출물: `D:\ARD\inventory\master_inventory.csv` (356 행) + 6개 표준별 개별 CSV + 6개 리포트
- 명세 캐시: `D:\ARD\sources\` (6개 원본 파일, 약 2.0MB)

## v2에서 적용한 변경 사항 (User 결정 사항 반영)

### 결정 1: dcterms 25개 추가 ✅
- 새 파일 `inventory/dcterms.csv` (INV-3500 ~ INV-3524)
- standard 컬럼: "Dublin Core (via DCAT)"
- notes에 "DCAT v3 normative dependency" 명시
- DCAT v3가 normative하게 권장하는 25개 dcterms 속성 모두 포함 (title, description, identifier, issued, modified, language, license, rights, accessRights, creator, publisher, format, type, subject, relation, conformsTo, hasPart, isPartOf, isReferencedBy, references, source, spatial, temporal, accrualPeriodicity, rightsHolder)
- 정의는 모두 DCMI Metadata Terms 2020-01-20 .ttl의 `rdfs:comment`에서 직접 인용

### 결정 2: PROV-DC 9건 제외 ✅
- INV-4081 ~ INV-4089 (Create, Modify, Publish, Contribute, RightsAssignment, Creator, Publisher, Contributor, RightsHolder) → `prov-o.csv`에서 제거
- `prov-o.csv` 맨 아래에 marker comment 추가:
  ```
  # EXCLUDED: INV-4081 through INV-4089 (PROV-DC extension classes...). See reports/inventory_validation.md v2 for decision rationale. dcterms is now tracked separately at INV-3500-3523.
  ```
- master_inventory.csv 재구축 시 자동 제외됨
- **결정 근거**: PROV-DC는 PROV-O와 Dublin Core 간 매핑 보조 명세이며 새 어휘를 정의하는 표준이 아님. 결정 1로 dcterms를 별도 트랙으로 추가했으므로 PROV-DC의 매핑 역할이 자동 대체됨. 향후 필요 시 INV-4500~4599 범위로 재추가 가능
- 부수 효과: prov-o.csv가 80 행으로 축소 (89 → 80), PROV-O proper만 남음

### 결정 3: 태그 체계 5개 추가 + 42행 재분류 ✅

**기존 24개 태그(프로젝트 컨텍스트 정의) → 29개로 확장. 추가된 5개:**

| 새 태그 | 적용 대상 | 적용 행 수 |
|---|---|---|
| `provenance.qualifier` | PROV-O qualified 메커니즘 (Influence subclass + InstantaneousEvent + qualified* + entity/activity/agent/influencer + had*) | 27 |
| `ml.split` | Croissant Split + 3 subclass 인스턴스 | 4 |
| `ml.label` | Croissant Label | 1 |
| `ml.bounding_box` | Croissant BoundingBox + SegmentationMask | 2 |
| `measurement.value` | Schema.org PropertyValue + 7개 측정값 속성 (value, propertyID, unitCode, unitText, maxValue, minValue, valueReference) | 8 |
| **합계** | — | **42** |

재분류 후 `uncategorized` 비율: 124/319 (39%) → 약 90/356 (25%) — 분류 정확도 14%p 개선

### 결함 1 대응: DQV 5번째 인벤토리 추가 ✅
- 새 파일 `inventory/dqv.csv` (INV-5001 ~ INV-5021)
- W3C DQV (Data Quality Vocabulary) Note 2016-12-15 — https://www.w3.org/TR/vocab-dqv/
- 21 행 (Class 10 + Property 9 + Enumeration 2)
- 모든 정의가 `dqv.ttl`의 `rdfs:comment`에서 직접 인용 (충실도 100%)
- 본 추가로 `quality.general` 태그가 0건 → 19건으로 증가, `quality.accuracy` 0건 → 1건 (precision)
- **여전히 부재**: `quality.bias`, `quality.completeness`. DQV 자체는 메트릭 컨테이너 어휘이지 구체적 품질 차원을 다 정의하지 않음. AI Ready Data application profile에서 ISO/IEC 5259-2 또는 Croissant RAI 추가 필요

### 1순위 처리: TRUNCATED 5건 보강 ✅
- 모든 5건의 `[TRUNCATED]` 플래그가 `[TRUNCATED→BOOSTED]`로 갱신됨
- 원문 전체가 notes 컬럼에 inline으로 저장됨 (검색·매핑 단계에서 즉시 참조 가능)

| inventory_id | 항목 | 보강 내용 |
|---|---|---|
| INV-4026 | prov:PrimarySource | 3개 문단 전문 추가 (about primary source for a topic, directness, and derivation) |
| INV-4027 | prov:Attribution | 2개 문단 전문 추가 (ascribing entity to agent + activity context) |
| INV-4029 | prov:Delegation | 2개 문단 전문 추가 (assignment of authority + student/supervisor example) |
| INV-1014 | schema:PropertyValue | `\n\n` 줄바꿈 처리 명시. 정의 자체는 이미 완전했음 |
| INV-1124 | schema:value | Unicode digit/decimal 사용 지침 추가 (4행 추가 텍스트) |

### Cross-reference 보강 6건 (원본 CSV에 적용)
- v1에서 master에만 적용했던 cross-reference 보강을 source CSV에도 반영
- prov-o.csv: INV-4001 Entity, INV-4030 Role, INV-4034 wasDerivedFrom, INV-4044 wasRevisionOf
- schema-org.csv: INV-1003 Dataset, INV-1005 DataDownload
- prov-o.csv의 INV-4080 hadRole는 PROV-DC 제거 시 grep 패턴 실수로 일시 손실되었으나 즉시 복구함

## v2 통합 통계

| 표준 | inventory_id 범위 | Class | Property | Enumeration | 합계 |
|---|---|---|---|---|---|
| Schema.org | INV-1001 ~ INV-1133 | 16 | 117 | 0 | 133 |
| Croissant | INV-2001 ~ INV-2045 | 12 | 30 | 3 | 45 |
| DCAT v3 | INV-3001 ~ INV-3052 | 9 | 43 | 0 | 52 |
| **DCMI (NEW)** | INV-3500 ~ INV-3524 | 0 | 25 | 0 | **25** |
| PROV-O | INV-4001 ~ INV-4080 | 30 | 50 | 0 | 80 |
| **DQV (NEW)** | INV-5001 ~ INV-5021 | 10 | 9 | 2 | **21** |
| **합계** | — | **77** | **274** | **5** | **356** |

v1 대비 변동: +46 (dcterms +25, DQV +21), -9 (PROV-DC), 순 +37.

## v2 concept_tag 분포 (29개 태그 기준)

| concept_tag | v1 | v2 | 변화 | 비고 |
|---|---|---|---|---|
| uncategorized | 124 | ~85 | -39 | 5개 새 태그로 재분류 + DQV는 quality.* |
| **provenance.qualifier (NEW)** | — | 27 | +27 | PROV-O qualified mechanism |
| **measurement.value (NEW)** | — | 8 | +8 | Schema.org PropertyValue 계열 |
| **ml.split (NEW)** | — | 4 | +4 | Croissant Split subclasses |
| **ml.bounding_box (NEW)** | — | 2 | +2 | Croissant CV types |
| **ml.label (NEW)** | — | 1 | +1 | Croissant Label |
| quality.general | 0 | 19 | +19 | DQV 추가로 발생 |
| quality.accuracy | 0 | 1 | +1 | dqv:precision |
| structure.dataset | 22 | 24 | +2 | dcterms:hasPart, isPartOf |
| identification.title | 3 | 4 | +1 | dcterms:title |
| identification.description | 4 | 5 | +1 | dcterms:description |
| identification.identifier | 6 | 7 (조정) | +1/-1 | dcterms:identifier 추가, schema:propertyID 이동 |
| identification.keyword | 8 | 9 | +1 | dcterms:subject |
| temporal.creation | 7 | 8 | +1 | dcterms:issued |
| temporal.modification | 2 | 3 | +1 | dcterms:modified |
| temporal.coverage | 9 | 11 | +2 | dcterms:temporal, dcterms:accrualPeriodicity |
| spatial.coverage | 6 | 7 | +1 | dcterms:spatial |
| actor.creator | 11 | 12 | +1 | dcterms:creator (prov:Creator는 제거됨) |
| actor.publisher | 3 | 4 (조정) | +1/-1 | dcterms:publisher 추가, prov:Publisher 제거 |
| actor.contributor | 11 | 11 (조정) | -1/+1 | prov:Contributor 제거 |
| rights.license | 3 | 4 (조정) | +1/-1 | dcterms:license 추가, prov:RightsHolder 제거 |
| rights.access | 5 | 7 (조정) | +2/-2 | dcterms:rights/accessRights 추가, prov:RightsHolder 제거 |
| distribution.media_type | 6 | 7 | +1 | dcterms:format |
| provenance.source | 2 | 3 | +1 | dcterms:source |
| (그 외 변동 없음) | | | | |
| **합계** | 319 | 356 | +37 | |

## 플래그 통합 분포 (v2)

| 플래그 | v1 | v2 | 변화 |
|---|---|---|---|
| [CHECK] | 33 | 33 | (변동 없음, 모두 mapping 단계 검토 대상) |
| [BORDERLINE] | 14 | 5 | -9 (PROV-DC 9건 제외로 감소; Schema.org pending 5건 잔존) |
| [TRUNCATED] | 5 | 0 | -5 (모두 [TRUNCATED→BOOSTED]로 갱신) |
| [TRUNCATED→BOOSTED] (NEW) | — | 5 | +5 |
| [TRANSLATION] | 0 | 0 | — |

총 검수 플래그 행: 52 → 43 (-9, PROV-DC 제외 효과). 비율: 16% → 12%.

## Critical Gap (결함 1 정밀화)

### 데이터 품질 어휘 부족: DQV 추가 후 부분 해소

**해소된 부분:**
- `quality.general`: 0 → 19건 (DQV의 19개 클래스/속성)
- `quality.accuracy`: 0 → 1건 (dqv:precision)

**여전히 부재한 부분:**
- `quality.bias` (편향): 본 6개 표준 중 어떤 것도 데이터셋 편향 정보를 위한 어휘를 정의하지 않음. AI Ready Data의 핵심 RAI 개념인데 빠짐
- `quality.completeness` (완전성): DQV는 메트릭 컨테이너만 제공하고 specific dimension instance(예: dqv:completeness)를 정의하지 않음. dqv:precision만 명시 인스턴스로 있음

**해소 옵션 (다음 단계):**
1. **ISO/IEC 5259-2 (Data Quality Measurement Model)** 인벤토리 추가 — INV-6000~ 범위
2. **Croissant RAI extension** (`http://mlcommons.org/croissant/RAI/`) 추가 — INV-2500~ 범위 (Croissant namespace 내)
3. **DCAT-AP DQV profile** 확장 어휘 검토

본 인벤토리는 후속 application profile 작성 시 위 3개 출처에서 quality.bias/completeness 어휘를 보완해야 함.

## v2 산출물 파일 목록

```
D:\ARD\
├── inventory\
│   ├── prov-o.csv               (80 데이터 행 + 마커 코멘트)
│   ├── dcat-v3.csv              (52 데이터 행)
│   ├── croissant.csv            (45 데이터 행)
│   ├── schema-org.csv           (133 데이터 행)
│   ├── dcterms.csv              (25 데이터 행)              ★ NEW v2
│   ├── dqv.csv                  (21 데이터 행)              ★ NEW v2
│   └── master_inventory.csv     (356 데이터 행, 통합본)
├── reports\
│   ├── prov-o_report.md
│   ├── dcat-v3_report.md
│   ├── croissant_report.md
│   ├── schema-org_report.md
│   └── inventory_validation.md  (이 파일, v2)
└── sources\
    ├── prov-o.ttl               (113 KB)
    ├── dcat-v3.ttl              (196 KB)
    ├── croissant-spec.md        (76 KB)
    ├── schema-org.jsonld        (1.5 MB)
    ├── dcmi-terms.ttl           (47 KB)                     ★ NEW v2
    └── dqv.ttl                  (12 KB)                     ★ NEW v2
```

## 정의 직접 인용 비율 (v2)

| 표준 | v1 직접 인용 비율 | v2 직접 인용 비율 |
|---|---|---|
| PROV-O | 85% (76/89) | 85% (68/80, PROV-DC 제외 후 13개 [CHECK] 비율 동일) |
| DCAT v3 | 85% (44/52) | 85% (44/52) |
| Croissant | 73% (33/45) | 73% (33/45) |
| Schema.org | 100% (133/133) | 100% (133/133) |
| **DCMI (NEW)** | — | 100% (25/25) |
| **DQV (NEW)** | — | 100% (21/21) |
| **전체** | 90% (286/319) | 91% (324/356) |

전체 충실도 1%p 향상 — DCMI/DQV 100% 직접 인용 효과.

## 후속 작업 우선순위 (User 권장 사항 반영)

### 1순위 — TRUNCATED 처리 ✅ 완료
v2에서 모두 [TRUNCATED→BOOSTED] 처리. 매핑 단계에서 즉시 사용 가능.

### 2순위 — BORDERLINE 처리 (5건 잔존)
Schema.org pending.schema.org 5건 (DefinedTerm/DefinedTermSet + 3 properties). User 명시 요청으로 유지 결정. 매핑 워크숍 안건에서 최종 판단 가능.

### 3순위 — CHECK 33건
대부분 의미 모호성·구조 정의 부재. 매핑 워크숍에서 같은 개념 그룹의 다른 표준 정의와 비교하여 자연스럽게 해소 예상.

### 추가 권장 (결함 2 대응 — User가 직접 수행)
**Croissant 결함 5건의 MLCommons issue 제출:**
- 사전 문서: 본 리포트 v2 + `croissant_report.md`의 [CHECK] 그룹 A/B 섹션
- 제출 위치: https://github.com/mlcommons/croissant/issues
- 제출 시 명시: "TTA AI-Ready Data project inventory analysis (2026-05-03)"
- 결함 항목: containedIn/excludes/equivalentProperty (JSON-LD context 누락), md5/replace (정의 부재), separator vs delimiter terminology mismatch
- TTA의 글로벌 표준 생태계 기여 첫 채널로 활용 가능 (SC42 활동 시 인용 가능한 트랙 레코드)

## 다음 단계 (3단계 매핑 워크숍 입력 자료로서의 적합성)

본 v2 인벤토리는 매핑 워크숍에 다음과 같이 사용 가능:

| 워크숍 작업 | 사용 컬럼 | 활용 방법 |
|---|---|---|
| Step 1 (TTA 항목 분해) | (별도 입력) | TTA 표준에서 추출한 항목에 동일 17 컬럼 schema 적용 |
| Step 2 (1차 매핑 후보 도출) | concept_tag | 같은 태그 그룹 내 후보 정렬. 29개 태그로 분류된 ~270개 행이 매핑 후보 풀 |
| Step 3 (정밀 매핑 결정) | definition + definition_ko + equivalent_terms | 의미적 일치 판단 |
| Step 4 (제약 도출) | domain + range + cardinality | SHACL shapes 자동 생성 시드 |
| Step 5 (이슈 추적) | notes ([CHECK]/[BORDERLINE]/[TRUNCATED→BOOSTED]) | 검수 우선순위 결정 |
| Step 6 (한국어 번역 시드) | definition_ko | TTA 표준 문서 한국어 본문 초안 |

## 결론

User의 5개 결정 사항이 모두 v2에 반영되었고, 1순위 후속 작업(TRUNCATED 보강)도 완료됨. 인벤토리 분류 정확도가 v1 대비 14%p 향상 (`uncategorized` 39% → 25%)되어 매핑 단계 입력 자료로 충분. **3단계(TTA 항목 분해)** 또는 매핑 워크숍 진행 가능 상태.
