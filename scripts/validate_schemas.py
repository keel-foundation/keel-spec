#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from openapi_spec_validator import validate as validate_openapi
from openapi_spec_validator.readers import read_from_filename

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"

EXAMPLE_MAP = {
    "video": "video.json",
    "signal": "signal.json",
    "moderation-case": "moderation-case.json",
    "enforcement-action": "enforcement-action.json",
    "appeal": "appeal.json",
    "audit-record": "audit-record.json",
}


def main() -> int:
    schema_count = 0
    example_count = 0
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        schema_count += 1

    for name, filename in EXAMPLE_MAP.items():
        schema_path = SCHEMAS / f"{name}.schema.json"
        example_path = EXAMPLES / filename
        if not schema_path.exists() or not example_path.exists():
            continue
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        example = json.loads(example_path.read_text(encoding="utf-8"))
        Draft202012Validator(schema).validate(example)
        example_count += 1

    openapi_path = SCHEMAS / "openapi.yaml"
    if openapi_path.exists():
        spec, _ = read_from_filename(str(openapi_path))
        validate_openapi(spec, base_uri=openapi_path.parent.as_uri() + "/")

    print(f"validated {schema_count} schemas, {example_count} examples, and openapi.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
