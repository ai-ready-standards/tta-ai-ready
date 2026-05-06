# tta_0976 — Python Package

TTA-0976 AI 레디 Application Profile Pydantic 모델.

## 설치

```bash
# 저장소 루트에서
pip install pydantic>=2.0

# tta_0976 패키지는 PYTHONPATH 추가로 사용 (현재)
cd standards/P-01-research-data/3_code
PYTHONPATH=. python -c "from tta_0976 import Repository"

# 또는 (Phase B 정식 배포 후)
pip install tta-0976-models
```

## 사용법

```python
from tta_0976 import Repository, Dataset, File, MultilingualText, Subject
from tta_0976.models import (
    IdentifierType, RepositoryType, AccessType, BooleanPlus
)
from tta_0976.loader import load_from_jsonld
from tta_0976.serializers import to_jsonld_str

# 객체 생성 (타입 검증 자동)
repo = Repository(
    RepositoryUrl="https://dataon.kisti.re.kr",
    RepositoryIdentifier="10.5072/REP-001",
    RepositoryIdentifierType=IdentifierType.DOI,
    RepositoryName=MultilingualText(ko="DataON", en="DataON"),
    RepositoryType=RepositoryType.institutional,
    RepositoryLanguage="kor",
    RepositorySubject=[Subject(SubjectName="Information Science")],
    InstitutionName=MultilingualText(ko="한국과학기술정보연구원", en="KISTI"),
    InstitutionCountry="KR",  # alpha-2 (Decision-002 OVERRIDE)
    DatabaseAccessType=AccessType.open,
    DataAccessType=AccessType.open,
    DataLicenseName="Creative Commons Attribution 4.0 International",
    DataLicenseUrl="http://creativecommons.org/licenses/by/4.0/",
    DataUpload=AccessType.restricted,
    Versioning=BooleanPlus.yes,
    EnhancedPublication=BooleanPlus.no,
    QualityManagement=BooleanPlus.yes,  # ★ Boolean Activation Slot trigger
)

# JSON-LD 출력
print(to_jsonld_str(repo))

# JSON-LD 파일 로드 (alpha-3 자동 변환)
repo2 = load_from_jsonld('../5_examples/kisti_dataon.jsonld')
```

## 반영된 결정 사항

- **Decision-002**: InstitutionCountry alpha-2 강제 (loader가 alpha-3 → alpha-2 자동 변환)
- **Decision-003/004**: Dataset IdentifierType/Publisher 카디널리티 부록 우선
- **Decision-Q3/Q7**: PROV-O 보조 매핑 (조건부)
- **Decision-Q4**: ★ Boolean Activation Slot — QualityManagement="yes" 시 hasQualityMetadata 권장
- **Decision-2**: Subject Class → SKOS Concept 변환 (`Subject.to_skos_concept()`)
- **Decision-3.1**: FileCoverage dual-purpose (시간/공간 Union 타입)
- **Issue-002**: 3-valued boolean (BooleanPlus enum: yes/no/unknown)
- **FileSizeUnit 정규화**: 'Mega Byte' → 'MB' 자동 변환

## 테스트 실행

```bash
# 저장소 루트에서
cd standards/P-01-research-data/3_code
PYTHONPATH=. pytest tests/ -v

# 또는 단순 실행 (pytest 없이)
PYTHONPATH=. python tests/test_models.py
```

## 패키지 구조

```
3_code/
├── tta_0976/
│   ├── __init__.py     (export 정의)
│   ├── models.py       (4 Layer + 12 Enum + Helpers, ~350 lines)
│   ├── loader.py       (JSON-LD → Pydantic, ~100 lines)
│   └── serializers.py  (Pydantic → JSON-LD, ~70 lines)
├── tests/
│   └── test_models.py  (11 테스트 케이스)
└── README.md           (본 파일)
```

## 참고

- 본 모델의 검증 통과 결과: [`reports/phase_d1_verification.md`](../../../reports/phase_d1_verification.md)
- AP 1.0.0 명세: [`1_document/TTA-0976-AP.md`](../1_document/TTA-0976-AP.md)
- 결정 사항 상세: [`6_changelog/CHANGELOG.md`](../6_changelog/CHANGELOG.md)
