# 시작하기

대상에 따라 출발점이 다릅니다.

## 제안자

새로운 단체표준을 AI 레디 형식으로 제안하시거나, 기존 표준 보유자로서 AI 레디로 전환하시는 분. (단체표준 제안권을 가진 외부 주체 — 연구자·기관·기업·정부 등)

### 1. 표준 선택 및 분석

본 사업 5종 시범 표준 중 가장 비슷한 도메인을 참고합니다.

| 도메인 | 참고 표준 |
| --- | --- |
| 과학기술 연구 | [P-01](standards/p-01.md) |
| 공공데이터 | [P-02](standards/p-02.md) |
| AI 학습데이터 | [P-03](standards/p-03.md) |
| 농업 / 산업 | [P-04](standards/p-04.md), [P-05](standards/p-05.md) |

### 2. 7개 구성요소 점검

작성하실 표준이 다음 7개를 갖추도록 설계합니다.

| # | 구성요소 | 도구 |
| --- | --- | --- |
| 1 | 의미 정의 | 본문 표 |
| 2 | 구조 정의 | JSON-LD `@context` |
| 3 | 코드값 정의 | 부록 통제어 |
| 4 | 검증 규칙 | SHACL Shape |
| 5 | 출처·계보 | PROV-O |
| 6 | 사용 제약 | DUO / CC URI |
| 7 | 품질 프로파일 | ISO/IEC 5259 |

### 3. 매뉴얼 (Phase B 제공 예정)

수행계획서 D-2 산출물인 **TC 개발 가이드 매뉴얼**이 4단계(2026.11) 완료 시 본 사이트의 [매뉴얼 섹션](manuals/index.md)에 게시됩니다.

---

## 데이터 사용자

연구데이터를 직접 만들거나 재사용하시는 분.

### 1. 가장 가까운 템플릿 받기

[:material-download: NIE 환경 Dataset 예시](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/5_examples/nie_environmental.jsonld){ .md-button .md-button--primary }
[:material-download: RDA 농업 Dataset 예시](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/5_examples/rda_agriculture.jsonld){ .md-button }

### 2. 자기 정보로 채우기

```json
{
  "@context": "https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/2_schema/context.jsonld",
  "@id": "여기에 데이터셋 식별자",
  "@type": "Dataset",

  "Identifier": "DOI 또는 URI",
  "IdentifierType": "DOI",
  "Title": {"ko": "데이터셋 이름", "en": "Dataset Name"},
  "Creator": "본인 이름",
  "Publisher": "소속 기관",
  "PublicationYear": "2026"
}
```

### 3. 검증

[:material-test-tube: 검증해보기](validate.md){ .md-button }

### 4. 활용

검증을 통과한 JSON-LD 파일을:

- 자기 데이터셋과 함께 발행
- 기관 리포지토리에 등록
- DOI 등록 정보로 활용
- (Phase B 예정) PyTorch / HuggingFace에서 직접 로딩

---

## 개발자

AI 시스템·데이터 파이프라인을 본 표준과 통합하시는 분.

### 1. 검증 도구 설치

```bash
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
python3.11 -m venv venv
source venv/bin/activate
pip install -e tools/validator/
```

### 2. JSON-LD 로딩

```python
import rdflib
g = rdflib.Graph()
g.parse("your-dataset.jsonld", format="json-ld")
# 이제 표준 어휘로 SPARQL 쿼리·SHACL 검증 가능
```

### 3. SHACL 검증을 코드에서

```python
from tta_validator.validate import validate_file
from pathlib import Path

result = validate_file(
    Path("your-dataset.jsonld"),
    Path("standards/P-01-research-data/2_schema"),
)
print(f"M:{result.violations}  R:{result.warnings}  O:{result.infos}")
if result.violations > 0:
    print(result.text)
```

### 4. CI 통합

`.github/workflows/ci.yml`에 검증 단계를 추가하면 PR마다 자동 실행됩니다.

```yaml
- name: TTA AI 레디 표준 검증
  run: |
    pip install tta-ai-ready-validator
    tta-validator your-data/ --ci
```

### 5. (Phase B) 카탈로그 사용

본 저장소의 `catalog.jsonld`를 사용해 5종 표준을 자동 발견·로딩할 수 있습니다.

```python
import json, urllib.request
catalog = json.loads(urllib.request.urlopen(
    "https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/catalog.jsonld"
).read())
for ds in catalog["dataset"]:
    print(ds["title"]["ko"], ds["homepage"])
```

---

## 평가위원 / 발주처

본 사업의 진행 상황과 산출물을 검토하시는 분.

- [사업 문서 / 프레임워크](framework/index.md)
- [사업 문서 / 매뉴얼 3종](manuals/index.md)
- [사업 문서 / 리포지토리 설계서](repository/index.md)
- [GitHub 저장소](https://github.com/ai-ready-standards/tta-ai-ready)
- [Pull Request 목록](https://github.com/ai-ready-standards/tta-ai-ready/pulls?q=is%3Apr) — 모든 산출물 변경 이력
