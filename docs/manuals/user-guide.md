# 리포지토리 사용자 가이드

| 항목 | 내용 |
| --- | --- |
| 매뉴얼 ID | D-4 |
| 버전 | **v0.5 초안** (2026-05-05) |
| 대상 | 본 저장소를 사용하는 모든 사용자 (3개 시나리오) |
| 정식 발행 | 2026-12 (사업 종료 시) |

> 본 매뉴얼은 **3개 사용자 시나리오**별로 구성되어 있습니다. 자기 시나리오에 해당하는 섹션만 읽으면 됩니다.

---

## 시나리오 선택

```
나는 ...

  □ 표준을 검색하고 자기 데이터에 적용하고 싶다
       ──→ [시나리오 1: 일반 사용자](#시나리오-1-일반-사용자)
  
  □ TC 담당자로서 자기 표준을 게시·수정하고 싶다
       ──→ [시나리오 2: 제안자](#시나리오-2-제안자)
  
  □ 개발자로서 본 표준을 시스템에 자동 연동하고 싶다
       ──→ [시나리오 3: 개발자](#시나리오-3-개발자-자동화-연동)
```

---

## 시나리오 1: 일반 사용자

연구자·데이터 사용자·메타데이터 작성자.

### 1.1 표준 찾기

GitHub Pages 사이트에서 검색:

🌐 **https://ai-ready-standards.github.io/tta-ai-ready/**

상단 검색창에 키워드 입력 (예: "DataCite", "DCAT", "농업").

### 1.2 5종 표준 일람

| ID | 표준번호 | 도메인 |
| --- | --- | --- |
| [P-01](../standards/p-01.md) | TTAK.KO-10.0976 | 연구데이터 |
| [P-02](../standards/p-02.md) | (예정) | 공공데이터 |
| [P-03](../standards/p-03.md) | TTAK.KO-10.1343-Part2 | AI 학습데이터 |
| [P-04](../standards/p-04.md) | TTAK.KO-10.1533 | 농업 AI |
| [P-05](../standards/p-05.md) | TTAK.KO-10.1571 | 철강 제조 |

### 1.3 자기 데이터에 표준 적용 — 4단계

#### Step 1: 가장 가까운 예시 다운로드

P-01의 가장 단순한 데이터셋 예시:

[:material-download: dataset-minimal.jsonld](https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/5_examples/kisti_dataon.jsonld){ .md-button .md-button--primary }

#### Step 2: 자기 정보로 채우기

```json
{
  "@context": "https://standard.tta.or.kr/ai-ready/profile/context.jsonld",
  "@type": "Dataset",
  "@id": "https://my-org.kr/dataset/001",
  
  "Identifier": "10.7488/ds/my-001",
  "IdentifierType": "DOI",
  "Title": {
    "ko": "내 데이터셋 이름",
    "en": "My Dataset Name"
  },
  "Creator": "내 이름",
  "Publisher": "내 소속 기관",
  "PublicationYear": "2026"
}
```

#### Step 3: 검증 (Codespaces 사용 — 설치 불필요)

[:material-rocket: Codespaces 열기](https://codespaces.new/ai-ready-standards/tta-ai-ready?quickstart=1){ .md-button }

브라우저에서 VS Code가 열린 후 터미널에 다음 입력:

```bash
# 자기 파일 업로드 후
python standards/P-01-research-data/4_validator/validate.py my-dataset.jsonld
```

→ `✓ Conforms: True` 가 나오면 표준 준수 완료.

#### Step 4: 활용

- 자기 데이터 발행 시 본 메타데이터 함께 공개
- 기관 리포지토리 등록 시 첨부
- DOI 등록 시 인용 정보로 사용

### 1.4 자주 묻는 질문 (일반 사용자)

??? question "Codespaces가 무엇인가요?"
    GitHub의 클라우드 개발 환경입니다. **GitHub 계정만 있으면 무료**로 매월 60시간 사용 가능. 설치 없이 브라우저 안에서 검증 환경 사용 가능합니다.

??? question "표준 적용에 비용이 드나요?"
    무료입니다. 본 저장소 산출물은 **Apache License 2.0**으로 공개되어 있습니다. 자유롭게 사용·수정·배포 가능.

??? question "표준 미준수 시 어떻게 되나요?"
    검증이 실패합니다 (`✗`). 머지 차단 같은 강제는 본 저장소에 PR을 올릴 때만 적용됩니다. 자기 데이터에 자유롭게 적용 가능.

---

## 시나리오 2: 제안자

새 단체표준을 AI 레디 형식으로 본 저장소에 제안하거나, 기존 표준 보유자로서 AI 레디로 전환·수정하려는 사용자. (단체표준 제안권을 가진 외부 주체 — 연구자·기관·기업·정부 등)

### 2.1 권한 요청

본 저장소는 **코어 팀만 직접 푸시 가능**합니다. 권한 요청:

1. 본 저장소 PM에게 GitHub 핸들 전달
2. ai-ready-standards Organization 멤버 초대 받기
3. 영역별 CODEOWNERS 등록

또는 **fork → PR** 방식으로 기여 가능 (권한 불필요).

### 2.2 새 표준 추가 흐름

```
1. 표준 본문 확보 (PDF/HWP)
       ↓
2. [기존 표준 전환 매뉴얼] 따라 패키지 작성
       ↓
3. 자기 GitHub 계정으로 본 저장소 fork
       ↓
4. 새 브랜치 생성: feat/p-XX-domain
       ↓
5. standards/P-XX-domain/ 추가
       ↓
6. PR 생성 → CI 통과 확인
       ↓
7. PM·TTA 주관 자문위원회 리뷰
       ↓
8. PG606 워크숍 발표
       ↓
9. 머지 → 사이트 자동 갱신
```

### 2.3 기존 표준 수정 흐름

본 저장소에 이미 있는 표준에 변경 적용 시:

#### 마이너 수정 (오타·예시 추가 등)

```
1. 본 저장소 fork
2. 새 브랜치: fix/p-01-typo
3. 파일 수정
4. PR 생성 + CI 통과
5. CODEOWNERS 리뷰 → 머지
```

#### 메이저 수정 (스키마 변경, 통제어 추가 등)

```
1. CHANGELOG에 Decision-NNN 추가
2. PR 본문에 영향 분석 첨부
3. 영향 받는 examples 모두 갱신
4. PG606 사전 협의 후 머지
```

### 2.4 자기 표준의 자동 검증 통과 확인

PR 페이지 하단에 4개 CI job 결과 표시:

| Job | 통과 기준 |
| --- | --- |
| 국제 어휘 매핑 100% 검증 | 모든 IRI가 정식 어휘에 정의 |
| Pydantic 모델 테스트 | 모든 단위 테스트 통과 |
| SHACL 인스턴스 검증 | 모든 examples conform |
| 코드 린트 | ruff 경고 0 |

빨간 ❌ 표시되면 클릭하여 로그 확인 → 수정 → 재push.

### 2.5 자주 묻는 질문 (제안자)

??? question "TC 의장만 등록 가능한가요?"
    TC 의장 또는 TC 의장의 위임을 받은 작성자가 등록 가능. CODEOWNERS에 표준별 소유자가 지정됩니다.

??? question "표준 본문 PDF도 함께 올려야 하나요?"
    **올리지 마세요**. TTA 저작권 자료입니다. 본 저장소에는 추출된 elements.csv·enumerations.csv만 등록.

??? question "사이트 갱신은 언제 되나요?"
    PR 머지 후 1~2분 내 자동 배포. https://ai-ready-standards.github.io/tta-ai-ready/ 에서 확인.

---

## 시나리오 3: 개발자 (자동화 연동)

ML 파이프라인·데이터 카탈로그·검색 시스템을 본 표준과 통합하려는 개발자.

### 3.1 설치

```bash
# 검증 도구 (현재)
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
pip install -e tools/validator/
pip install pydantic pyshacl rdflib pyld

# pip install (Phase B 예정)
pip install tta-ai-ready-validator    # TestPyPI에 배포 예정
```

### 3.2 Python에서 사용

```python
from tta_validator.validate import validate_file
from pathlib import Path

# 데이터셋 메타데이터 검증
result = validate_file(
    Path("my-dataset.jsonld"),
    Path("standards/P-01-research-data/2_schema"),
)
print(f"M: {result.violations}, R: {result.warnings}, O: {result.infos}")
```

### 3.3 Pydantic 모델 직접 사용 (P-01)

```python
import sys
sys.path.insert(0, "standards/P-01-research-data/3_code")

from tta_0976.models import Repository, Dataset, IdentifierType

dataset = Dataset(
    Identifier="10.7488/ds/example",
    IdentifierType=IdentifierType.DOI,
    Title={"en": "My Dataset", "ko": "내 데이터셋"},
    Creator="Suntae Kim",
    Publisher="KISTI",
    PublicationYear=2026,
)
# 형식 오류 즉시 raise
```

### 3.4 카탈로그 자동 발견

본 저장소의 5종 표준은 DCAT v3 카탈로그로 발행됨:

```python
import json
import urllib.request

catalog = json.loads(urllib.request.urlopen(
    "https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/catalog.jsonld"
).read())

for ds in catalog["dataset"]:
    print(f"- {ds['title']['ko']}: {ds.get('homepage', '')}")
```

### 3.5 SPARQL 쿼리 (RDF 변환 후)

```python
import rdflib

g = rdflib.Graph()
g.parse("my-dataset.jsonld", format="json-ld")

# 모든 데이터셋 제목 조회
results = g.query("""
PREFIX dcterms: <http://purl.org/dc/terms/>
SELECT ?title WHERE {
    ?dataset dcterms:title ?title .
}
""")
for row in results:
    print(row.title)
```

### 3.6 CI 통합 (자기 프로젝트에)

자기 프로젝트의 GitHub Actions에 본 검증 추가:

```yaml
# .github/workflows/metadata-check.yml
name: TTA AI-Ready Metadata Check
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install pyshacl rdflib pyld
      - run: |
          curl -L -O https://raw.githubusercontent.com/ai-ready-standards/tta-ai-ready/main/standards/P-01-research-data/2_schema/shapes.shacl.ttl
          for f in metadata/*.jsonld; do
            pyshacl -s shapes.shacl.ttl -d "$f"
          done
```

### 3.7 ML 프레임워크 연동 (P-03/P-04, Phase B 예정)

Croissant 1.0 호환 어댑터가 추가되면 다음과 같이 한 줄 로딩 가능:

```python
import mlcroissant as mlc
ds = mlc.Dataset(jsonld="my-tta-dataset.jsonld")
records = ds.records("default")
```

→ Phase B에서 P-03(태깅·라벨링) AP 작성 시 함께 제공.

### 3.8 자주 묻는 질문 (개발자)

??? question "REST API가 있나요?"
    **현재 없습니다**. 본 저장소는 정적 콘텐츠 + GitHub Pages입니다. 표준 정의·예시는 raw GitHub URL로 접근하시면 됩니다.

??? question "Java/Node.js 클라이언트는 언제?"
    Phase B(11월 이후) 검토 예정. 현재 Python만 공식 지원.

??? question "자체 SHACL shape를 추가하고 싶어요"
    자기 프로젝트의 SHACL shape를 본 저장소의 shapes와 함께 사용 가능:
    
    ```python
    from pyshacl import validate
    validate(
        data_graph=...,
        shacl_graph=combine([base_shapes, my_extension])
    )
    ```

---

## 부록 A — Git 기초 (기여하려는 사람용)

### A.1 PR 생성 (가장 흔한 흐름)

```bash
# 1. 본 저장소 fork (GitHub 웹에서 Fork 버튼)

# 2. 자기 fork 클론
git clone https://github.com/<자기계정>/tta-ai-ready.git
cd tta-ai-ready

# 3. 새 브랜치 생성
git checkout -b fix/p-01-typo

# 4. 파일 편집

# 5. 커밋
git add <변경 파일>
git commit -m "fix(P-01): typo in description"

# 6. push
git push origin fix/p-01-typo

# 7. GitHub 웹에서 "Compare & pull request" 클릭
```

### A.2 본 저장소 최신 변경 동기화

```bash
git remote add upstream https://github.com/ai-ready-standards/tta-ai-ready.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### A.3 PR이 거절되었을 때

CI가 실패한 경우:

1. PR 페이지의 빨간 ❌ 클릭 → 로그 확인
2. 자기 컴퓨터에서 동일 명령 재현
3. 수정 후 같은 브랜치에 새 커밋 push (PR이 자동 갱신)

리뷰어가 변경 요청한 경우:

1. 코멘트의 요청 사항 검토
2. 동의하면 수정 후 push
3. 동의하지 않으면 코멘트로 응답·논의

---

## 부록 B — 자주 사용하는 명령

```bash
# 환경 설정
pip install -e tools/validator/

# 매핑 검증
tta-verify-mappings

# Pydantic 모델 테스트
cd standards/P-01-research-data/3_code && pytest tests/

# SHACL 검증 (단일 파일)
python standards/P-01-research-data/4_validator/validate.py <file>.jsonld

# SHACL 검증 (디렉토리 일괄)
for f in *.jsonld; do
  python standards/P-01-research-data/4_validator/validate.py "$f"
done

# 사이트 로컬 미리보기
pip install mkdocs-material
mkdocs serve
# → http://127.0.0.1:8000

# 사이트 빌드
mkdocs build --strict
```

---

## 부록 C — 도움 받기

| 채널 | 용도 |
| --- | --- |
| [GitHub Issues](https://github.com/ai-ready-standards/tta-ai-ready/issues) | 버그 신고 · 기능 요청 |
| [GitHub Discussions](https://github.com/ai-ready-standards/tta-ai-ready/discussions) | (활성화 시) 질의응답 |
| TTA PG606 사무국 | 표준 자체에 대한 문의 |

---

## 변경 이력

| 버전 | 날짜 | 변경 |
| --- | --- | --- |
| **v0.5 초안** | 2026-05-05 | 3개 시나리오별 가이드 초안 작성 |
| (예정) v1.0 | 2026-12-15 | 사업 종료 시 정식 발행 |
