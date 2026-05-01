# P-01 AI 레디 프로파일

본 문서는 TTAK.KO-10.0976 표준을 AI 시스템이 직접 임포트·검증·활용할 수 있도록 변환한 "AI 레디 패키지"의 설계 원칙과 구성요소를 설명한다.

## 1. 표준 모델 요약

```
Repository
   └── Collection (1..N)
          └── Dataset (1..N)
                 └── File (1..N)
```

- **Repository**: 연구데이터를 수집·저장·관리·서비스하는 시스템 (R1~R21, 24개 요소)
- **Collection**: 데이터셋의 논리적 그룹 (프로젝트·부서·연구과제 단위) (C1~C12, 18개 요소)
- **Dataset**: 공유·활용을 위해 파일을 그룹화한 집합. 파일 없이 메타데이터 단독 구성도 가능 (D1~D15, 22개 요소)
- **File**: 공유·재사용 가치가 있는 개별 단위 연구데이터 (F1~F19, 27개 요소)

## 2. 7개 AI 레디 구성요소 모델

본 패키지는 제안서(2.4절)의 7개 구성요소 모델에 따라 구성된다.

### 전환 3개 (기존 표준 자산 활용)

| # | 구성요소 | 본 패키지의 구현 |
| --- | --- | --- |
| 1 | 의미 정의 (Semantic Definitions) | TTAK.KO-10.0976 본문의 79개 요소 정의를 그대로 채택. 각 요소의 한글 설명을 `MAPPINGS.md`에 IRI와 함께 1:1 보존 |
| 2 | 구조 정의 (Structural Schema) | JSON-LD 1.1 스키마 (`schema/context.jsonml`). 동일한 요소가 RDF/Turtle로 자동 직렬화 가능 |
| 3 | 코드값 정의 (Controlled Vocabularies) | TTA 부록 II-1의 14종 통제어를 SHACL `sh:in` 제약으로 인라인. 향후 SKOS Concept Scheme으로 분리 예정 |

### 신규 4개 (AI 레디화 신규)

| # | 구성요소 | 본 패키지의 구현 |
| --- | --- | --- |
| 4 | 검증 규칙 (Validation Shapes) | pySHACL로 직접 실행 가능한 4종 SHACL shape. M(Mandatory) → `sh:Violation`, R(Recommended) → `sh:Warning`, O(Optional) → 정보성 |
| 5 | 출처·계보 (Provenance) | W3C PROV-O를 컨텍스트에 포함 (`prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAttributedTo`). 본 표준의 D10 Contributor + ContributorType 통제어와 결합 |
| 6 | 사용 제약 (Use Constraints) | TTA의 R12 DataLicenseName + R13 DataLicenseUrl을 `dct:license`(IRI)로 매핑. DUO(Data Use Ontology) 어휘를 컨텍스트에 포함 |
| 7 | 품질 프로파일 (Quality Profile) | Phase B 예정. ISO/IEC 5259 품질 차원을 본 표준의 M/R/O 분류와 결합 |

## 3. 표준 모델과 DCAT 매핑 결정 근거

본 패키지는 글로벌 검색 가능성(Google Dataset Search 등)을 확보하기 위해 W3C DCAT v3를 1차 어휘로 채택했다.

| TTA 클래스 | 매핑 어휘 | 결정 근거 |
| --- | --- | --- |
| Collection | `dcat:Catalog` + `dcmitype:Collection` | DCAT Catalog가 "데이터셋 메타데이터의 큐레이션된 컬렉션"으로 의미가 가장 가까움. DCMI Collection을 보조 타입으로 부여 |
| Dataset | `dcat:Dataset` | 1:1 매핑. DataCite Schema 4.5의 Dataset 자원 유형과도 호환 |
| File | `dcat:Distribution` + `schema:DataDownload` | DCAT Distribution = "데이터셋의 특정 표현(파일·API)". TTA의 File은 실제 데이터 파일이므로 의미적으로 일치 |
| Repository | `dcat:DataService` | DCAT v3에서 데이터 서비스를 표현하는 정식 클래스 |

## 4. M/R/O 등급의 SHACL 매핑

본 표준의 M/R/O 등급(부록 II-2)은 다음과 같이 SHACL severity로 변환된다.

| TTA 등급 | SHACL severity | 검증 결과 처리 |
| --- | --- | --- |
| M (Mandatory) | `sh:Violation` | CI 실패 — 머지 차단 |
| R (Recommended) | `sh:Warning` | 경고 — 머지 가능, 리포트 게시 |
| O (Optional) | `sh:Info` | 정보성 — 무시 또는 통계 수집 |

## 5. 식별자(Identifier) 정책

본 표준의 IdentifierType 통제어(19종: ARK·DOI·Handle·URI·UCI 등)를 모두 인정하되, AI 레디 사용성을 위해 다음을 권고한다.

- **데이터셋(D2)**: DOI 권고 — Google Dataset Search가 우선 인식
- **컬렉션(C2)**: Handle 또는 URI 권고
- **파일(F2)**: 데이터셋 DOI에 fragment(`#file=...`) 또는 별도 DOI
- **리포지토리(R3)**: re3data.org · OpenDOAR · ROAR 식별자

## 6. 본 패키지의 사용 시나리오

### 6.1 메타데이터 작성자
1. `examples/valid/`의 적절한 템플릿 복사
2. 자기 데이터셋의 정보로 채움
3. `tta-validator <file.jsonld>` 실행 → M 위반 0건 확인

### 6.2 ML 파이프라인 (PyTorch / HuggingFace)
1. 본 JSON-LD를 `mlcroissant` Python 라이브러리로 로딩 (Croissant 1.0 호환 변환은 Phase B)
2. 데이터셋 식별자(D2) → 자동 다운로드 URL 해석
3. 파일 메타데이터(F1~F19) → DataLoader 구성

### 6.3 검색엔진 (Google Dataset Search)
1. 본 JSON-LD를 schema.org Dataset로 자동 인식
2. `dct:identifier`(DOI) → 정식 인용 정보 생성
3. `dcat:keyword` → 검색 색인

## 7. 향후 확장 (Phase B)

- [ ] SKOS Concept Scheme 분리 (`vocabularies/` 디렉토리)
- [ ] Croissant 1.0 호환 자동 변환기
- [ ] PROV-O 시나리오 예시 3종 (생성·파생·기여)
- [ ] DUO permission code 통합 (R12/R13의 비공개·임상 데이터 케이스)
- [ ] ISO/IEC 5259 품질 차원 — 완전성·적시성·정확성 측정 SHACL
- [ ] 한글-영문 다국어 라벨 (`@language` 태깅)
