"""TTAK.KO-10.0976 AI-Ready Application Profile — Python package.

Version: 1.0.0 (2026-05-04)
"""

from .models import (
    Repository,
    Collection,
    Dataset,
    File,
    Subject,
    QualityMetadata,
    MultilingualText,
    # Controlled vocabulary enums
    IdentifierType,
    TitleType,
    DatasetDateType,
    CollectionDateType,
    ContributorType,
    AccessType,
    AccessRestriction,
    RepositoryType,
    ResponsibilityType,
    FileType,
    FileSizeUnitType,
    BooleanPlus,
)
from .loader import load_from_jsonld, load_from_dict
from .serializers import to_jsonld

__version__ = "1.0.0"
__all__ = [
    # Layer classes
    "Repository", "Collection", "Dataset", "File",
    # Helper classes
    "Subject", "QualityMetadata", "MultilingualText",
    # Controlled vocabularies
    "IdentifierType", "TitleType", "DatasetDateType", "CollectionDateType",
    "ContributorType", "AccessType", "AccessRestriction", "RepositoryType",
    "ResponsibilityType", "FileType", "FileSizeUnitType", "BooleanPlus",
    # I/O
    "load_from_jsonld", "load_from_dict", "to_jsonld",
]
