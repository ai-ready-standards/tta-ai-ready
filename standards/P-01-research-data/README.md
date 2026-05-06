# P-01 — 연구데이터 메타데이터 (AI 레디 패키지)

| 항목 | 내용 |
| --- | --- |
| 표준번호 | **TTAK.KO-10.0976** |
| 표준명 | 연구데이터 관리 및 공유를 위한 메타데이터 |
| 영문명 | The metadata for the managing and sharing research data |
| 제정일 | 2017-03-30 |
| 소관 | TTA · PG606 |
| **AP 버전** | **1.0.0** (2026-05-04) |
| 상태 | ✅ 자기 검증 통과 (Phase D-1) |

## 6 패키지 구성

본 디렉토리는 [프레임워크 정의서 Part III](../../docs/framework/index.md)의 6-패키지 표준 구조를 따릅니다.

| 디렉토리 | 내용 |
| --- | --- |
| [`1_document/TTA-0976-AP.md`](./1_document/TTA-0976-AP.md) | Application Profile 1.0.0 명세 (249라인) |
| [`2_schema/`](./2_schema/) | JSON-LD context (170라인) + SHACL shapes (680라인) |
| [`3_code/`](./3_code/) | Python Pydantic 패키지 + 11개 단위 테스트 |
| [`4_validator/`](./4_validator/) | pySHACL 래퍼 + sh:or 사전 호환성 테스트 |
| [`5_examples/`](./5_examples/) | KISTI / NIE / RDA 실제 시나리오 3종 |
| [`6_changelog/CHANGELOG.md`](./6_changelog/CHANGELOG.md) | 5종 어휘 버전 lock + 9개 결정 추적 |

## 표준 모델 — 4계층

```
Repository (R1-R21, 24요소)
   └── Collection (C1-C12, 18요소)
          └── Dataset (D1-D15, 22요소)
                 └── File (F1-F19, 27요소)
```

총 **93개 요소** + **117개 통제어 값** (24개 카테고리).

## 자기 검증 결과 (Phase D-1)

| 검증 | 결과 |
| --- | --- |
| pytest (`test_models.py`) | **11/11 통과** |
| Issue-001 sh:or 사전 테스트 | **4/4 통과** |
| KISTI DataON 인스턴스 | ✓ Conforms |
| NIE Environmental 인스턴스 | ✓ Conforms |
| RDA Agriculture 인스턴스 | ✓ Conforms |
| 매핑 성공률 | **★ 99.0%** (210/208) |

상세: [reports/phase_d1_verification.md](../../reports/phase_d1_verification.md)

## 빠른 시작

### 검증 실행

```bash
# 모든 examples 일괄
tta-validator standards/P-01-research-data/5_examples/

# 단일 파일
python standards/P-01-research-data/4_validator/validate.py \
       standards/P-01-research-data/5_examples/kisti_dataon.jsonld
```

### Pydantic 사용

```python
import sys
sys.path.insert(0, "standards/P-01-research-data/3_code")
from tta_0976.models import Dataset, IdentifierType

dataset = Dataset(
    Identifier="10.7488/ds/example",
    IdentifierType=IdentifierType.DOI,
    Title={"ko": "예시", "en": "Example"},
    Creator="...",
    Publisher="KISTI",
    PublicationYear=2026,
)
```

## 핵심 설계 결정

본 AP의 9개 핵심 결정은 [`6_changelog/CHANGELOG.md`](./6_changelog/CHANGELOG.md)에 ID로 추적됩니다.

대표 결정:
- **D-Q4** (Boolean Activation Slot): R17 QualityManagement="yes"일 때만 DQV 활성화 — 본 사업의 ★ 핵심 혁신 패턴
- D-002 InstitutionCountry alpha-3 → alpha-2 (DCAT v3 호환)
- D-003/004 본문 vs 부록 등급 충돌 (부록 우선)

## 라이프사이클 위치

본 패키지는 [표준 제안 라이프사이클](../../docs/lifecycle.md)의 ⑪ 공고 단계까지 완료된 reference implementation입니다.

## WBS

C-5 (수행계획서 2.3절). **AP 1.0.0 발행: 2026-05-04**.

다른 4종 표준의 같은 패키지 작업이 [전환 매뉴얼](../../docs/manuals/migration-guide.md)을 따라 8월부터 진행됩니다.
