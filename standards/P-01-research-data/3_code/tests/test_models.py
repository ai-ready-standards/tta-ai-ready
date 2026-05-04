"""TTA-0976 Pydantic models — 핵심 테스트."""
import pytest
from datetime import date

from tta_0976 import (
    Repository, Collection, Dataset, File,
    Subject, MultilingualText, QualityMetadata,
    IdentifierType, TitleType, DatasetDateType, CollectionDateType,
    ContributorType, AccessType, AccessRestriction, RepositoryType,
    BooleanPlus, FileType, FileSizeUnitType,
)
from tta_0976.loader import (
    normalize_country, normalize_unit, load_from_dict
)
from tta_0976.serializers import to_jsonld
from tta_0976.models import MultilingualText


# =============================================================================
# Layer Class 기본 검증
# =============================================================================

def test_repository_minimum_required():
    """Repository — 필수 필드 모두 채움."""
    repo = Repository(
        RepositoryUrl="https://dataon.kisti.re.kr",
        RepositoryIdentifier="10.5072/REP-001",
        RepositoryIdentifierType=IdentifierType.DOI,
        RepositoryName=MultilingualText(ko="DataON", en="DataON"),
        RepositoryType=RepositoryType.institutional,
        RepositoryLanguage="kor",
        RepositorySubject=[Subject(SubjectName="Information Science")],
        InstitutionName=MultilingualText(ko="한국과학기술정보연구원", en="KISTI"),
        InstitutionCountry="KR",
        DatabaseAccessType=AccessType.open,
        DataAccessType=AccessType.open,
        DataLicenseName="Creative Commons Attribution 4.0 International",
        DataLicenseUrl="http://creativecommons.org/licenses/by/4.0/",
        DataUpload=AccessType.restricted,
        Versioning=BooleanPlus.yes,
        EnhancedPublication=BooleanPlus.no,
        QualityManagement=BooleanPlus.no,
    )
    assert repo.RepositoryName.ko == "DataON"
    assert repo.InstitutionCountry == "KR"
    assert repo.QualityManagement == BooleanPlus.no


def test_decision_002_alpha2_enforced():
    """Decision-002: InstitutionCountry는 alpha-2 (KR)만 허용. alpha-3 (KOR)은 거부."""
    with pytest.raises(Exception):  # ValidationError or ValueError
        Repository(
            RepositoryUrl="https://example.com",
            RepositoryIdentifier="x",
            RepositoryIdentifierType=IdentifierType.DOI,
            RepositoryName=MultilingualText(ko="x"),
            RepositoryType=RepositoryType.institutional,
            RepositoryLanguage="kor",
            RepositorySubject=[Subject(SubjectName="x")],
            InstitutionName=MultilingualText(ko="x"),
            InstitutionCountry="KOR",  # ← alpha-3, 거부되어야 함
            DatabaseAccessType=AccessType.open,
            DataAccessType=AccessType.open,
            DataLicenseName="x",
            DataLicenseUrl="https://example.com/license",
            DataUpload=AccessType.open,
            Versioning=BooleanPlus.no,
            EnhancedPublication=BooleanPlus.no,
            QualityManagement=BooleanPlus.no,
        )


def test_decision_q4_boolean_activation_slot():
    """Decision-Q4: QualityManagement='yes' 시 hasQualityMetadata 권장 (warning)."""
    import warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        Repository(
            RepositoryUrl="https://example.com",
            RepositoryIdentifier="x",
            RepositoryIdentifierType=IdentifierType.DOI,
            RepositoryName=MultilingualText(ko="x"),
            RepositoryType=RepositoryType.institutional,
            RepositoryLanguage="kor",
            RepositorySubject=[Subject(SubjectName="x")],
            InstitutionName=MultilingualText(ko="x"),
            InstitutionCountry="KR",
            DatabaseAccessType=AccessType.open,
            DataAccessType=AccessType.open,
            DataLicenseName="x",
            DataLicenseUrl="https://example.com/license",
            DataUpload=AccessType.open,
            Versioning=BooleanPlus.no,
            EnhancedPublication=BooleanPlus.no,
            QualityManagement=BooleanPlus.yes,  # ← yes
            # hasQualityMetadata 누락 → warning
        )
        assert any("DQV" in str(x.message) for x in w), "Decision-Q4 warning 미발생"


def test_decision_003_dataset_identifiertype_optional():
    """Decision-003: D2.1 IdentifierType은 부록 우선 적용으로 Optional."""
    ds = Dataset(
        DatasetIdentifier="10.5072/DS-001",
        # DatasetIdentifierType 생략 가능 (O로 변경됨)
        DatasetTitle=MultilingualText(ko="테스트 데이터셋"),
        DatasetTitleType=TitleType.Other,
        DatasetCreator="홍길동",
        PublicationYear=2026,
    )
    assert ds.DatasetIdentifierType is None  # 비어있어도 valid
    assert ds.PublicationYear == 2026


def test_decision_2_subject_skos_concept():
    """Decision-2: Subject Class → SKOS Concept 변환."""
    subj = Subject(
        SubjectScheme="DFG",
        SubjectID="31702",
        SubjectName="Human Geography",
    )
    skos = subj.to_skos_concept()
    assert skos["@type"] == "skos:Concept"
    assert skos["skos:prefLabel"] == "Human Geography"
    assert skos["skos:inScheme"]["@id"] == "DFG"
    assert skos["skos:notation"] == "31702"


def test_collection_datetype_subset():
    """CollectionDateType은 3개 값만 (DataCite의 부분집합)."""
    # Created/Updated/Deleted은 valid
    col = Collection(
        CollectionIdentifier="x",
        CollectionIdentifierType=IdentifierType.DOI,
        CollectionTitle=MultilingualText(ko="x"),
        CollectionDateType=CollectionDateType.Deleted,  # 3개 값 중 하나
    )
    assert col.CollectionDateType == CollectionDateType.Deleted

    # DatasetDateType의 다른 값(Issued, Submitted)은 거부되어야 함 (Pydantic Enum 검증)
    with pytest.raises(Exception):
        Collection(
            CollectionIdentifier="x",
            CollectionIdentifierType=IdentifierType.DOI,
            CollectionTitle=MultilingualText(ko="x"),
            CollectionDateType="Issued",  # ← CollectionDateType에 없음
        )


def test_file_size_unit_normalization():
    """FileSizeUnit 'Mega Byte' → 'MB' 정규화."""
    assert normalize_unit("Mega Byte") == "MB"
    assert normalize_unit("Giga Byte") == "GB"
    assert normalize_unit("MB") == "MB"  # 이미 정규화된 값


def test_country_alpha3_to_alpha2():
    """alpha-3 → alpha-2 변환."""
    assert normalize_country("KOR") == "KR"
    assert normalize_country("USA") == "US"
    assert normalize_country("KR") == "KR"  # 이미 alpha-2

    with pytest.raises(ValueError):
        normalize_country("XYZ")  # 미지원 코드


def test_loader_normalization_applied():
    """loader가 alpha-3 → alpha-2 자동 변환."""
    data = {
        "@type": "Repository",
        "RepositoryUrl": "https://example.com",
        "RepositoryIdentifier": "x",
        "RepositoryIdentifierType": "DOI",
        "RepositoryName": {"ko": "x"},
        "RepositoryType": "institutional",
        "RepositoryLanguage": "kor",
        "RepositorySubject": [{"SubjectName": "x"}],
        "InstitutionName": {"ko": "x"},
        "InstitutionCountry": "KOR",  # ← alpha-3 입력
        "DatabaseAccessType": "open",
        "DataAccessType": "open",
        "DataLicenseName": "x",
        "DataLicenseUrl": "https://example.com/license",
        "DataUpload": "open",
        "Versioning": "no",
        "EnhancedPublication": "no",
        "QualityManagement": "no",
    }
    repo = load_from_dict(data)
    assert repo.InstitutionCountry == "KR"  # ← 자동 변환됨


def test_serialization_roundtrip():
    """Pydantic → JSON-LD → Pydantic 라운드트립."""
    repo = Repository(
        RepositoryUrl="https://example.com",
        RepositoryIdentifier="10.5072/X",
        RepositoryIdentifierType=IdentifierType.DOI,
        RepositoryName=MultilingualText(ko="테스트"),
        RepositoryType=RepositoryType.institutional,
        RepositoryLanguage="kor",
        RepositorySubject=[Subject(SubjectName="x")],
        InstitutionName=MultilingualText(ko="기관"),
        InstitutionCountry="KR",
        DatabaseAccessType=AccessType.open,
        DataAccessType=AccessType.open,
        DataLicenseName="CC-BY-4.0",
        DataLicenseUrl="http://creativecommons.org/licenses/by/4.0/",
        DataUpload=AccessType.open,
        Versioning=BooleanPlus.no,
        EnhancedPublication=BooleanPlus.no,
        QualityManagement=BooleanPlus.no,
    )
    jsonld = to_jsonld(repo)
    assert jsonld["@type"] == "Repository"
    assert jsonld["RepositoryName"]["ko"] == "테스트"

    # Subject가 SKOS Concept으로 변환되었는지
    assert jsonld["RepositorySubject"][0]["@type"] == "skos:Concept"


def test_file_coverage_dual_purpose():
    """★ Decision-3.1: FileCoverage는 시간/공간 모두 가능 (sh:or 패턴)."""
    # 시간 형식
    f1 = File(
        FileIdentifier="x", FileIdentifierType=IdentifierType.DOI,
        FileTitle=MultilingualText(ko="x"),
        FileCreator="x", FilePublisher="x", FilePublicationYear=2026,
        FileContributorType=ContributorType.DataCollector,
        FileDateType=DatasetDateType.Created,
        FileCoverage=date(2026, 5, 4),  # 시간
    )
    # 공간 형식 (자유 텍스트)
    f2 = File(
        FileIdentifier="x", FileIdentifierType=IdentifierType.DOI,
        FileTitle=MultilingualText(ko="x"),
        FileCreator="x", FilePublisher="x", FilePublicationYear=2026,
        FileContributorType=ContributorType.DataCollector,
        FileDateType=DatasetDateType.Created,
        FileCoverage="서울시",  # 공간
    )
    assert f1.FileCoverage == date(2026, 5, 4)
    assert f2.FileCoverage == "서울시"


if __name__ == "__main__":
    # pytest 없이 직접 실행 가능
    import sys
    test_repository_minimum_required()
    test_country_alpha3_to_alpha2()
    test_file_size_unit_normalization()
    test_decision_2_subject_skos_concept()
    test_collection_datetype_subset()
    test_file_coverage_dual_purpose()
    test_loader_normalization_applied()
    test_serialization_roundtrip()
    test_decision_003_dataset_identifiertype_optional()
    print("✓ All tests passed (excluding pytest-required ones)")
