# tta_0976 — Python Package

TTA-0976 AI-Ready Application Profile Pydantic 모델.

## 설치

```bash
pip install pydantic>=2.0
# 패키지는 D:\ARD\packages\tta-0976\3_code\ 에 위치
# PYTHONPATH에 추가하거나 setup.py 작성 후 pip install -e . 로 설치
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
- **Decision-Q4**: ★ Boolean Activation Slot — QualityManagement="yes" 시 hasQualityMetadata 권장 (warning 발생)
- **Decision-2**: Subject Class → SKOS Concept 변환 (`Subject.to_skos_concept()`)
- **Decision-3.1**: FileCoverage dual-purpose (시간/공간 Union 타입)
- **Issue-002**: 3-valued boolean (BooleanPlus enum: yes/no/unknown)
- **FileSizeUnit 정규화**: 'Mega Byte' → 'MB' 자동 변환

## 테스트 실행

```bash
cd D:\ARD\packages\tta-0976\3_code
pytest tests/             # pytest 사용
python tests/test_models.py  # 직접 실행 (pytest 없이)
```

## 패키지 구조

```
3_code/
├── tta_0976/
│   ├── __init__.py     (export 정의)
│   ├── models.py       (4 Layer + 12 Enum + Helpers, ~330 lines)
│   ├── loader.py       (JSON-LD → Pydantic, ~95 lines)
│   └── serializers.py  (Pydantic → JSON-LD, ~70 lines)
├── tests/
│   └── test_models.py  (10 테스트 케이스)
└── README.md           (이 파일)
```
