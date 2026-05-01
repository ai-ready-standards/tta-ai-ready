# 검증해보기

본인의 메타데이터(JSON-LD)를 본 표준에 맞춰 자동 검증할 수 있습니다.

## 권장 방법: GitHub Codespaces (브라우저)

설치 없이 브라우저 안에서 즉시 검증 환경을 사용할 수 있습니다. GitHub 무료 계정이면 충분합니다.

[:material-rocket: Codespaces 열기](https://codespaces.new/ai-ready-standards/tta-ai-ready?quickstart=1){ .md-button .md-button--primary }

위 버튼을 누르면:

1. GitHub이 본 저장소를 클라우드 컨테이너에 자동 배포
2. Python 3.11 + 검증 도구가 자동 설치됨
3. VS Code 인터페이스가 브라우저에 열림
4. 터미널에서 다음 명령으로 즉시 검증

```bash
tta-validator standards/P-01-research-data/examples/valid/
```

본인 파일을 업로드하려면 VS Code 좌측 파일 트리에 드래그·드롭하면 됩니다.

## 로컬 설치 (재사용·자동화 시)

### macOS / Linux

```bash
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
python3.11 -m venv venv
source venv/bin/activate
pip install -e tools/validator/
```

### Windows (PowerShell)

```powershell
git clone https://github.com/ai-ready-standards/tta-ai-ready.git
cd tta-ai-ready
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e tools/validator/
```

## 검증 실행

### 단일 파일

```bash
tta-validator your-file.jsonld
```

### 디렉토리 일괄

```bash
tta-validator path/to/your/datasets/
```

### CI 모드 (M 위반 시 exit 1)

```bash
tta-validator path/ --ci
```

## 결과 해석

```
검증 대상: 1개 파일 / shapes: standards/P-01-research-data/shapes
------------------------------------------------------------
  ✓ your-dataset.jsonld  (M:0 R:2 O:0)
------------------------------------------------------------
합계: 1개 / 위반(M)=0  경고(R)=2  정보(O)=0
```

| 마커 | 의미 |
| --- | --- |
| ✓ | M(필수) 위반 0건 — **통과** |
| ✗ | M 위반 1건 이상 — 필수 필드 누락 또는 통제어 외 값 |

| 카운터 | 의미 | 처리 |
| --- | --- | --- |
| **M** (Mandatory) | 필수 위반 | 즉시 수정 필요 |
| **R** (Recommended) | 권고 미준수 | 가능하면 보완 |
| **O** (Optional) | 정보성 | 통계 / 리포팅 용도 |

## 의도된 오류로 동작 확인

본 저장소의 음성 테스트 케이스로 검증 도구가 정확히 오류를 잡는지 확인할 수 있습니다.

```bash
tta-validator standards/P-01-research-data/examples/invalid/ --expect-fail -v
```

이 명령은 의도된 D2/D5 누락을 정확히 보고하며, **M 위반이 발견되면 통과**(exit 0)로 처리됩니다.

## 자주 묻는 질문

??? question "어떤 SHACL shapes가 적용되나요?"
    `--shapes-dir` 옵션으로 명시하지 않으면 P-01의 4개 shape(`collection.ttl`, `dataset.ttl`, `file.ttl`, `repository.ttl`)이 적용됩니다. 다른 표준의 shape를 사용하려면:
    
    ```bash
    tta-validator your-file.jsonld --shapes-dir standards/P-04-agriculture/shapes
    ```

??? question "JSON-LD 문법 오류는 어떻게 진단하나요?"
    `tta-validator`의 출력에서 `[parse-error]`로 표시됩니다. 가장 흔한 원인은 `@context` 경로 오류 또는 따옴표 누락입니다.

??? question "Phase B에 추가될 온라인 검증 폼은 언제 나오나요?"
    사업 후반부(11월 이후)에 검토 후 결정됩니다. 우선은 Codespaces 옵션을 권장합니다.
