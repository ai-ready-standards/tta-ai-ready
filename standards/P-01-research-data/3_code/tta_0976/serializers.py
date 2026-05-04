"""TTA-0976 Pydantic models → JSON-LD serialization."""
import json
from typing import Any
from pydantic import BaseModel


CONTEXT_URL = "https://standard.tta.or.kr/ai-ready/profile/context.jsonld"


def to_jsonld(model: BaseModel, *, include_context: bool = True, indent: int = 2) -> dict:
    """Pydantic 모델 → JSON-LD dict 변환.

    Args:
        model: Repository / Collection / Dataset / File 인스턴스
        include_context: True 시 @context URL 포함
        indent: JSON 출력 시 들여쓰기

    Returns:
        JSON-LD dict (json.dumps 가능 형태)
    """
    # Pydantic 직렬화 (mode="json"으로 enum/date/etc 처리)
    data = model.model_dump(mode="json", exclude_none=True)

    # @type 추가 (클래스명 기반)
    cls_name = type(model).__name__
    type_map = {
        "Repository": "Repository",
        "Collection": "Collection",
        "Dataset": "Dataset",
        "File": "File",
    }
    if cls_name in type_map:
        data = {"@type": type_map[cls_name], **data}

    # Subject Class → SKOS Concept 변환 (Decision-2 적용)
    for key in list(data.keys()):
        if key.endswith("Subject") and isinstance(data[key], list):
            data[key] = [_subject_to_skos(s) for s in data[key]]

    # @context 추가
    if include_context:
        data = {"@context": CONTEXT_URL, **data}

    return data


def _subject_to_skos(subject_dict: dict) -> dict:
    """Subject dict → SKOS Concept 형식 (Decision-2)."""
    result = {
        "@type": "skos:Concept",
        "skos:prefLabel": subject_dict.get("SubjectName"),
    }
    if scheme := subject_dict.get("SubjectScheme"):
        result["skos:inScheme"] = {"@id": scheme}
    if sid := subject_dict.get("SubjectID"):
        result["skos:notation"] = sid
    return result


def to_jsonld_str(model: BaseModel, **kwargs) -> str:
    """JSON-LD 문자열로 직접 출력."""
    return json.dumps(
        to_jsonld(model, **kwargs),
        ensure_ascii=False,
        indent=kwargs.get("indent", 2),
    )
