#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from openapi_spec_validator import validate as validate_openapi
from openapi_spec_validator.readers import read_from_filename
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"

EXAMPLE_MAP = {
    "actor": "actor.json",
    "channel": "channel.json",
    "playback-manifest": "playback-manifest.json",
    "video": "video.json",
    "signal": "signal.json",
    "moderation-case": "moderation-case.json",
    "enforcement-action": "enforcement-action.json",
    "appeal": "appeal.json",
    "audit-record": "audit-record.json",
}


def build_registry() -> Registry:
    registry = Registry()
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        resource = Resource.from_contents(schema, default_specification=DRAFT202012)
        registry = registry.with_resource(path.as_uri(), resource)
        if "$id" in schema:
            registry = registry.with_resource(schema["$id"], resource)
    return registry


def main() -> int:
    registry = build_registry()

    schema_count = 0
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        schema_count += 1

    example_count = 0
    for name, filename in EXAMPLE_MAP.items():
        schema_path = SCHEMAS / f"{name}.schema.json"
        example_path = EXAMPLES / filename
        if not schema_path.exists() or not example_path.exists():
            continue
        example = json.loads(example_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(
            {"$ref": schema_path.as_uri()}, registry=registry
        )
        validator.validate(example)
        example_count += 1

    openapi_path = SCHEMAS / "openapi.yaml"
    if openapi_path.exists():
        spec, _ = read_from_filename(str(openapi_path))
        validate_openapi(spec, base_uri=openapi_path.parent.as_uri() + "/")

    print(f"validated {schema_count} schemas, {example_count} examples, and openapi.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
