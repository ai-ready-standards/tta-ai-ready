"""TTA-0976 JSON-LD loader → Pydantic models.

Includes value normalization (Decision-002 alpha-3↔alpha-2, FileSizeUnit 'Mega Byte'→'MB').
"""
import json
from pathlib import Path
from typing import Any

from .models import Repository, Collection, Dataset, File


# Decision-002: ISO 3166-1 alpha-3 → alpha-2 변환 테이블 (자주 쓰이는 30개국)
ALPHA3_TO_ALPHA2 = {
    "KOR": "KR", "USA": "US", "DEU": "DE", "FRA": "FR", "GBR": "GB",
    "JPN": "JP", "CHN": "CN", "RUS": "RU", "BRA": "BR", "IND": "IN",
    "CAN": "CA", "AUS": "AU", "ITA": "IT", "ESP": "ES", "MEX": "MX",
    "IDN": "ID", "TUR": "TR", "SAU": "SA", "ARG": "AR", "ZAF": "ZA",
    "EGY": "EG", "NGA": "NG", "VNM": "VN", "THA": "TH", "MYS": "MY",
    "PHL": "PH", "POL": "PL", "NLD": "NL", "BEL": "BE", "CHE": "CH",
}

# FileSizeUnit 정규화 ('Mega Byte' → 'MB' 등)
UNIT_NORMALIZE = {
    "Byte": "B", "byte": "B",
    "Mega Byte": "MB", "MegaByte": "MB", "megabyte": "MB",
    "Giga Byte": "GB", "GigaByte": "GB", "gigabyte": "GB",
    "Tera Byte": "TB", "TeraByte": "TB", "terabyte": "TB",
}


def normalize_country(value: str) -> str:
    """alpha-3 → alpha-2 변환. 이미 alpha-2면 그대로 반환."""
    if not value:
        return value
    if len(value) == 2 and value.isupper():
        return value
    if value in ALPHA3_TO_ALPHA2:
        return ALPHA3_TO_ALPHA2[value]
    raise ValueError(f"InstitutionCountry '{value}'를 alpha-2로 변환할 수 없음. "
                     f"표 보강 필요. ALPHA3_TO_ALPHA2에 추가하거나 직접 alpha-2 사용.")


def normalize_unit(value: str) -> str:
    """FileSizeUnit 정규화."""
    if not value:
        return value
    return UNIT_NORMALIZE.get(value, value)


def _normalize_data(data: dict) -> dict:
    """JSON-LD dict 전체에 정규화 적용 (재귀)."""
    if not isinstance(data, dict):
        return data
    out = {}
    for k, v in data.items():
        if k == "InstitutionCountry" and isinstance(v, str):
            out[k] = normalize_country(v)
        elif k == "FileUnit" and isinstance(v, str):
            out[k] = normalize_unit(v)
        elif isinstance(v, dict):
            out[k] = _normalize_data(v)
        elif isinstance(v, list):
            out[k] = [_normalize_data(x) if isinstance(x, dict) else x for x in v]
        else:
            out[k] = v
    return out


def load_from_dict(data: dict) -> Any:
    """JSON-LD dict → 적절한 Layer 클래스 인스턴스."""
    data = _normalize_data(data)
    type_value = data.get("@type", "")

    # @type 기반 라우팅 (JSON-LD 단축 형식 또는 IRI 형식 모두 지원)
    if type_value in ("Repository", "ttaap:Repository"):
        # @id 등 JSON-LD reserved key 제거 후 모델에 전달
        clean_data = {k: v for k, v in data.items() if not k.startswith("@")}
        return Repository(**clean_data)
    elif type_value in ("Collection", "dctype:Collection"):
        clean_data = {k: v for k, v in data.items() if not k.startswith("@")}
        return Collection(**clean_data)
    elif type_value in ("Dataset", "dcat:Dataset"):
        clean_data = {k: v for k, v in data.items() if not k.startswith("@")}
        return Dataset(**clean_data)
    elif type_value in ("File", "dcat:Distribution"):
        clean_data = {k: v for k, v in data.items() if not k.startswith("@")}
        return File(**clean_data)
    else:
        raise ValueError(
            f"Unknown @type: {type_value!r}. Expected one of: "
            "Repository, Collection, Dataset, File"
        )


def load_from_jsonld(path: str | Path) -> Any:
    """JSON-LD 파일 로드 → 적절한 Layer 클래스 인스턴스."""
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return load_from_dict(data)
