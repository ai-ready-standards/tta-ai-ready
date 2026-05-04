#!/usr/bin/env python3
"""TTA-0976 SHACL Validator — pySHACL 래퍼 CLI.

사용법:
    python validate.py <data.jsonld>
    python validate.py --shapes <custom_shapes.ttl> <data.jsonld>
    python validate.py --shapes ../2_schema/shapes.shacl.ttl --verbose <data.jsonld>

Issue-001 완화: pySHACL의 sh:or 지원이 불확실한 경우 fallback 검증 활성화.
"""
import argparse
import json
import sys
from pathlib import Path

try:
    from pyshacl import validate as pyshacl_validate
    PYSHACL_AVAILABLE = True
except ImportError:
    PYSHACL_AVAILABLE = False


DEFAULT_SHAPES = Path(__file__).parent.parent / "2_schema" / "shapes.shacl.ttl"
DEFAULT_CONTEXT = Path(__file__).parent.parent / "2_schema" / "context.jsonld"
CONTEXT_URL = "https://standard.tta.or.kr/ai-ready/profile/context.jsonld"


def inline_local_context(data_path: Path, context_path: Path = None) -> str:
    """JSON-LD 파일을 읽고, @context URL이 TTA-AP context면 로컬 파일 내용으로 치환.

    네트워크 fetch 회피용. 반환값은 inline된 JSON 문자열.
    """
    context_path = context_path or DEFAULT_CONTEXT
    with open(data_path, "r", encoding="utf-8") as f:
        doc = json.load(f)
    if doc.get("@context") == CONTEXT_URL and context_path.exists():
        with open(context_path, "r", encoding="utf-8") as f:
            ctx_doc = json.load(f)
        doc["@context"] = ctx_doc["@context"]
    return json.dumps(doc, ensure_ascii=False)


def colorize(text: str, color: str) -> str:
    """간단한 ANSI 컬러 (Windows cmd 호환은 별도 처리 필요)."""
    codes = {"green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m",
             "blue": "\033[94m", "reset": "\033[0m"}
    return f"{codes.get(color, '')}{text}{codes['reset']}"


def format_report(conforms: bool, results_text: str, verbose: bool = False) -> str:
    """pySHACL 결과를 사람이 읽기 쉬운 형식으로 포맷."""
    lines = []
    if conforms:
        lines.append(colorize("✓ Conforms: True", "green"))
        lines.append("  데이터가 모든 SHACL shape 제약을 통과했습니다.")
    else:
        lines.append(colorize("✗ Conforms: False", "red"))
        lines.append("  데이터가 일부 SHACL shape 제약을 위반했습니다.")
        if verbose:
            lines.append("")
            lines.append("─" * 60)
            lines.append("상세 위반 내용:")
            lines.append(results_text)
    return "\n".join(lines)


def validate_jsonld(
    data_path: Path,
    shapes_path: Path = None,
    verbose: bool = False,
) -> tuple[bool, str]:
    """JSON-LD 데이터 파일을 SHACL shapes로 검증.

    Returns:
        (conforms: bool, report: str)
    """
    if not PYSHACL_AVAILABLE:
        msg = (
            "pyshacl 미설치. 'pip install pyshacl' 실행 후 재시도.\n"
            "Fallback: 본 도구의 Pydantic 모델 검증으로 대체 가능 (3_code/ 참조)."
        )
        return False, msg

    shapes_path = shapes_path or DEFAULT_SHAPES
    if not data_path.exists():
        return False, f"데이터 파일 없음: {data_path}"
    if not shapes_path.exists():
        return False, f"SHACL shapes 파일 없음: {shapes_path}"

    # @context URL을 로컬 파일로 치환하여 네트워크 fetch 회피
    try:
        data_str = inline_local_context(data_path)
    except Exception as e:
        return False, f"JSON-LD 로드 실패: {e}"

    # pySHACL 검증
    try:
        conforms, results_graph, results_text = pyshacl_validate(
            data_str,
            shacl_graph=str(shapes_path),
            data_graph_format="json-ld",
            shacl_graph_format="turtle",
            inference="rdfs",
            debug=verbose,
        )
    except Exception as e:
        return False, f"검증 중 오류 발생: {e}"

    return conforms, format_report(conforms, results_text, verbose)


def validate_with_pydantic_fallback(data_path: Path, verbose: bool = False) -> tuple[bool, str]:
    """pySHACL 미설치 또는 sh:or 지원 부재 시 fallback (Pydantic 검증).

    Issue-001 완화: pySHACL의 sh:or 패턴 지원이 불확실하면 Pydantic 모델 검증으로 대체.
    """
    try:
        # tta_0976 패키지 import (3_code 경로 추가 필요)
        sys.path.insert(0, str(Path(__file__).parent.parent / "3_code"))
        from tta_0976.loader import load_from_jsonld

        try:
            instance = load_from_jsonld(data_path)
            return True, colorize(
                f"✓ Pydantic validation passed (type: {type(instance).__name__})", "green"
            )
        except Exception as e:
            return False, colorize(f"✗ Pydantic validation failed: {e}", "red")
    except ImportError:
        return False, "Fallback (Pydantic) 검증도 사용 불가. 3_code 패키지 설치 필요."


def main():
    parser = argparse.ArgumentParser(
        description="TTA-0976 SHACL Validator (pySHACL 래퍼)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python validate.py ../5_examples/kisti_dataon.jsonld
  python validate.py --shapes ../2_schema/shapes.shacl.ttl --verbose data.jsonld
  python validate.py --fallback-pydantic data.jsonld    # pySHACL 없이 Pydantic만 검증

Issue-001 완화 옵션:
  --fallback-pydantic   pySHACL의 sh:or 지원이 불확실한 경우 사용
""",
    )
    parser.add_argument("data", help="검증할 JSON-LD 파일 경로")
    parser.add_argument("--shapes", help="SHACL shapes 파일 (기본: 2_schema/shapes.shacl.ttl)")
    parser.add_argument("--verbose", "-v", action="store_true", help="상세 출력")
    parser.add_argument(
        "--fallback-pydantic", action="store_true",
        help="pySHACL 대신 Pydantic 모델로 검증 (Issue-001 fallback)",
    )
    args = parser.parse_args()

    data_path = Path(args.data)
    shapes_path = Path(args.shapes) if args.shapes else None

    print(colorize("TTA-0976 SHACL Validator v1.0.0", "blue"))
    print(f"Data: {data_path}")
    if not args.fallback_pydantic:
        print(f"Shapes: {shapes_path or DEFAULT_SHAPES}")
    print()

    if args.fallback_pydantic:
        conforms, report = validate_with_pydantic_fallback(data_path, args.verbose)
    else:
        conforms, report = validate_jsonld(data_path, shapes_path, args.verbose)

    print(report)
    sys.exit(0 if conforms else 1)


if __name__ == "__main__":
    main()
