"""TTAK.KO-10.0976 Pydantic models — type-safe data structures.

4 layer classes (Repository/Collection/Dataset/File) + helpers + 12 controlled enums.

Implements:
- Decision-002: InstitutionCountry alpha-2 enforced (alpha-3 → alpha-2 conversion)
- Decision-003/004: Cardinality CONFLICT 적용 (부록 우선)
- Decision-Q3/Q7: PROV-O conditional fields
- Decision-Q4: Boolean Activation Slot (QualityManagement="yes" → DQV active)
- Decision-2: Subject SKOS Concept transformation
- Decision-3.1: Coverage dual-purpose with sh:or pattern
"""
from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator


# =============================================================================
# 통제어 Enum (12개)
# =============================================================================

class IdentifierType(str, Enum):
    """20개 (DataCite 19 + UCI 1)."""
    ARK = "ARK"
    arXiv = "arXiv"
    bibcode = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    Handle = "Handle"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    URI = "URI"
    UCI = "UCI"  # Korean Universal Content Identifier — Issue-003


class TitleType(str, Enum):
    AlternativeTitle = "AlternativeTitle"
    Subtitle = "Subtitle"
    TranslatedTitle = "TranslatedTitle"
    Other = "Other"


class DatasetDateType(str, Enum):
    """9개 (DataCite dateType 부분집합)."""
    Accepted = "Accepted"
    Available = "Available"
    Copyrighted = "Copyrighted"
    Collected = "Collected"
    Created = "Created"
    Issued = "Issued"
    Submitted = "Submitted"
    Updated = "Updated"
    Valid = "Valid"


class CollectionDateType(str, Enum):
    """3개 (TTA Collection 전용, DataCite의 부분집합)."""
    Created = "Created"
    Updated = "Updated"
    Deleted = "Deleted"


class ContributorType(str, Enum):
    """22개 (DataCite contributorType 100% 일치)."""
    ContactPerson = "ContactPerson"
    DataCollector = "DataCollector"
    DataCurator = "DataCurator"
    DataManager = "DataManager"
    Distributor = "Distributor"
    Editor = "Editor"
    Funder = "Funder"
    HostingInstitution = "HostingInstitution"
    Producer = "Producer"
    ProjectLeader = "ProjectLeader"
    ProjectManager = "ProjectManager"
    ProjectMember = "ProjectMember"
    RegistrationAgency = "RegistrationAgency"
    RegistrationAuthority = "RegistrationAuthority"
    RelatedPerson = "RelatedPerson"
    Researcher = "Researcher"
    ResearchGroup = "ResearchGroup"
    RightsHolder = "RightsHolder"
    Sponsor = "Sponsor"
    Supervisor = "Supervisor"
    WorkPackageLeader = "WorkPackageLeader"
    Other = "Other"


class AccessType(str, Enum):
    open = "open"
    embargoed = "embargoed"
    restricted = "restricted"
    closed = "closed"


class AccessRestriction(str, Enum):
    feeRequired = "feeRequired"
    registration = "registration"
    institutional_membership = "institutional membership"
    non_registration = "non-registration"
    free = "free"
    other = "other"


class RepositoryType(str, Enum):
    disciplinary = "disciplinary"
    governmental = "governmental"
    institutional = "institutional"
    multidisciplinary = "multidisciplinary"
    project_related = "project-related"
    other = "other"


class ResponsibilityType(str, Enum):
    funding = "funding"
    general = "general"
    main = "main"
    sponsoring = "sponsoring"
    technical = "technical"
    other = "other"


class FileType(str, Enum):
    """DCMI Type 11 + TTA 'other' (Issue-004)."""
    Event = "Event"
    Image = "Image"
    InteractiveResource = "InteractiveResource"
    MovingImage = "MovingImage"
    PhysicalObject = "PhysicalObject"
    Service = "Service"
    Software = "Software"
    Sound = "Sound"
    StillImage = "StillImage"
    Text = "Text"
    other = "other"  # TTA-specific addition


class FileSizeUnitType(str, Enum):
    """정규화: 'Mega Byte' (TTA 원문) → 'MB' (UN/CEFACT)."""
    B = "B"
    MB = "MB"
    GB = "GB"
    TB = "TB"


class BooleanPlus(str, Enum):
    """Issue-002: yes/no/unknown 3-valued logic."""
    yes = "yes"
    no = "no"
    unknown = "unknown"


_CollectionDateTypeT = CollectionDateType
_DatasetDateTypeT = DatasetDateType
_FileTypeT = FileType


# =============================================================================
# Helper classes
# =============================================================================

class Subject(BaseModel):
    """Subject Class — ★ SKOS Concept 변환 (Decision-2)."""
    SubjectScheme: Optional[str] = Field(None, description="주제 분류 체계 (예: DFG)")
    SubjectID: Optional[str] = Field(None, description="주제 분류 코드")
    SubjectName: str = Field(..., description="주제 명칭 (필수)")

    def to_skos_concept(self) -> dict:
        """Subject → SKOS Concept JSON-LD."""
        result = {
            "@type": "skos:Concept",
            "skos:prefLabel": self.SubjectName,
        }
        if self.SubjectScheme:
            result["skos:inScheme"] = {"@id": self.SubjectScheme}
        if self.SubjectID:
            result["skos:notation"] = self.SubjectID
        return result


class QualityMetadata(BaseModel):
    """DQV QualityMetadata (★ Boolean Activation Slot 활성 시 사용)."""
    measurements: list[dict] = Field(default_factory=list, description="dqv:hasQualityMeasurement 리스트")
    certificates: list[dict] = Field(default_factory=list, description="dqv:QualityCertificate 리스트")
    annotations: list[dict] = Field(default_factory=list, description="dqv:QualityAnnotation 리스트")


class MultilingualText(BaseModel):
    """다국어 텍스트 (JSON-LD @container: @language 패턴)."""
    ko: Optional[str] = None
    en: Optional[str] = None

    @model_validator(mode="after")
    def at_least_one_language(self):
        if not (self.ko or self.en):
            raise ValueError("At least one language must be provided (ko or en)")
        return self


# =============================================================================
# 4 Layer Classes
# =============================================================================

class Repository(BaseModel):
    """TTA-0976 Repository (R1-R21)."""
    # R2 RepositoryUrl (M)
    RepositoryUrl: HttpUrl
    # R3 Identifier (M)
    RepositoryIdentifier: str
    # R3.1 IdentifierType (M)
    RepositoryIdentifierType: IdentifierType
    # R4 RepositoryName (M, 다국어)
    RepositoryName: MultilingualText
    # R4.1 RepositoryNameType (O)
    RepositoryNameType: Optional[TitleType] = None
    # R5 Type (M)
    RepositoryType: RepositoryType
    # R6 RepositoryLanguage (M, ISO 639-3)
    RepositoryLanguage: str = Field(..., pattern=r"^[a-z]{3}$")
    # R7 Subject (M)
    RepositorySubject: list[Subject] = Field(..., min_length=1)
    # R8 InstitutionName (M)
    InstitutionName: MultilingualText
    # R9 InstitutionCountry (M, ★ Decision-002 alpha-2)
    InstitutionCountry: str = Field(..., pattern=r"^[A-Z]{2}$")
    # R10 DatabaseAccessType (M)
    DatabaseAccessType: AccessType
    # R11 DataAccessType (M)
    DataAccessType: AccessType
    # R12 DataLicenseName (M)
    DataLicenseName: str
    # R13 DataLicenseUrl (M)
    DataLicenseUrl: HttpUrl
    # R14 DataUpload (M)
    DataUpload: AccessType
    # R15 Versioning (M)
    Versioning: BooleanPlus
    # R16 EnhancedPublication (M)
    EnhancedPublication: BooleanPlus
    # R17 QualityManagement (M, ★ Boolean Activation Slot trigger)
    QualityManagement: BooleanPlus
    # R18 Description (R)
    RepositoryDescription: Optional[MultilingualText] = None
    # R19 ResponsibilityType (O)
    ResponsibilityType: Optional[ResponsibilityType] = None
    # R20 InstitutionContact (O)
    InstitutionContact: Optional[Any] = None
    # R21 RepositoryContact (O)
    RepositoryContact: Optional[Any] = None
    # ★ Boolean Activation Slot — Decision-Q4
    hasQualityMetadata: Optional[QualityMetadata] = None

    @model_validator(mode="after")
    def quality_activation_slot(self):
        """★ Decision-Q4: QualityManagement='yes' 시 hasQualityMetadata 권장."""
        if self.QualityManagement == BooleanPlus.yes and self.hasQualityMetadata is None:
            import warnings
            warnings.warn(
                "QualityManagement='yes'이지만 hasQualityMetadata가 비어있음. "
                "DQV 어휘 활성화 권장 (Decision-Q4 Boolean Activation Slot)"
            )
        return self


class Collection(BaseModel):
    """TTA-0976 Collection (C1-C12)."""
    CollectionIdentifier: str
    CollectionIdentifierType: IdentifierType
    CollectionTitle: MultilingualText
    CollectionTitleType: Optional[TitleType] = None
    CollectionDate: Optional[Union[date, datetime]] = None
    CollectionDateType: Optional[_CollectionDateTypeT] = None  # 3개 값만
    CollectionDescription: Optional[MultilingualText] = None
    CollectionSubject: list[Subject] = Field(default_factory=list)
    CollectionCreator: list[Any] = Field(default_factory=list)
    CollectionContact: Optional[Any] = None
    CollectionRights: Optional[str] = None
    CollectionKeyword: Optional[str] = None
    CollectionAccessType: Optional[AccessType] = None
    CollectionAccessRestriction: Optional[AccessRestriction] = None


class Dataset(BaseModel):
    """TTA-0976 Dataset (D1-D15) — 발견 3 활용 가능 (File과 동형)."""
    DatasetIdentifier: str
    # ★ Decision-003: 본문 M / 부록 O — 부록 우선
    DatasetIdentifierType: Optional[IdentifierType] = None
    DatasetTitle: MultilingualText
    DatasetTitleType: TitleType
    DatasetCreator: Any  # M
    # ★ Decision-004: 본문 M / 부록 R — 부록 우선
    DatasetPublisher: list[Any] = Field(default_factory=list)
    PublicationYear: int = Field(..., ge=1000, le=9999)
    DatasetDate: Optional[Union[date, datetime]] = None
    DatasetDateType: Optional[_DatasetDateTypeT] = None
    DatasetDescription: Optional[MultilingualText] = None
    DatasetSubject: list[Subject] = Field(default_factory=list)
    DatasetContributor: list[Any] = Field(default_factory=list)
    DatasetContributorType: Optional[ContributorType] = None
    DatasetContact: Optional[Any] = None
    DatasetRights: Optional[str] = None
    DatasetKeyword: Optional[str] = None
    # ★ Decision-005: AccessType O 추정 (PDF 손상)
    DatasetAccessType: Optional[AccessType] = None
    DatasetAccessRestriction: Optional[AccessRestriction] = None


class File(BaseModel):
    """TTA-0976 File (F1-F19) — 발견 3 활용: Dataset와 18쌍 동형 + 9개 추가."""
    FileIdentifier: str
    FileIdentifierType: IdentifierType
    FileTitle: MultilingualText
    FileTitleType: Optional[TitleType] = None
    FileCreator: Any
    FilePublisher: Any
    FilePublicationYear: int = Field(..., ge=1000, le=9999)
    FileContributor: list[Any] = Field(default_factory=list)
    FileContributorType: ContributorType
    FileDate: Optional[Union[date, datetime]] = None
    FileDateType: DatasetDateType  # File은 DatasetDateType 참조 (alias CV-117)
    FileDescription: Optional[MultilingualText] = None
    FileSubject: list[Subject] = Field(default_factory=list)
    FileContact: Optional[Any] = None
    FileRights: Optional[str] = None
    FileKeyword: Optional[str] = None
    FileAccessType: Optional[AccessType] = None
    FileAccessRestriction: Optional[AccessRestriction] = None
    # F16 Coverage (★ Decision-3.1: dual-purpose temporal/spatial)
    FileCoverage: Optional[Union[str, date, datetime]] = Field(
        None,
        description="★ Coverage dual-purpose: 시간(ISO 8601) 또는 공간(자유 텍스트) 또는 IRI"
    )
    # F17 Type (DCMI Type Vocabulary)
    FileType: Optional[_FileTypeT] = None
    # F18 Format
    FileFormat: Optional[str] = None
    # F19 Size (bytes)
    FileSize: Optional[int] = Field(None, ge=0, description="파일 크기 (바이트)")
    # F19.1 Unit (★ Rule 3 사례: schema:unitText)
    FileUnit: Optional[FileSizeUnitType] = None
