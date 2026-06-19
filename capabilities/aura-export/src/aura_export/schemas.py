"""JSON Schema loading and validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json


REPO_SCHEMA_DIR = Path(__file__).resolve().parents[4] / "schemas"
PACKAGED_SCHEMA_DIR = Path(__file__).resolve().parents[2] / "schemas"


def schema_path(name: str) -> Path:
    repo_schema = REPO_SCHEMA_DIR / name
    if repo_schema.exists():
        return repo_schema
    return PACKAGED_SCHEMA_DIR / name


def load_schema(name: str) -> dict[str, Any]:
    return load_json(schema_path(name))


def _local_schema_store() -> dict[str, dict[str, Any]]:
    """Map public schema IDs to their local schema documents."""
    store: dict[str, dict[str, Any]] = {}
    for path in (PACKAGED_SCHEMA_DIR, REPO_SCHEMA_DIR):
        if not path.exists():
            continue
        for schema_file in path.glob("*.schema.json"):
            schema = load_json(schema_file)
            schema_id = schema.get("$id")
            if isinstance(schema_id, str):
                store[schema_id] = schema
    return store


def _jsonschema_validator(jsonschema: Any, validator_cls: Any, schema: dict[str, Any]) -> Any:
    store = _local_schema_store()
    try:
        from referencing import Registry, Resource

        resources = [
            (schema_id, Resource.from_contents(local_schema))
            for schema_id, local_schema in store.items()
        ]
        return validator_cls(schema, registry=Registry().with_resources(resources))
    except (ImportError, TypeError):
        resolver = jsonschema.RefResolver.from_schema(schema, store=store)
        return validator_cls(schema, resolver=resolver)


def _check_required(payload: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Basic required-field validator."""
    errors: list[str] = []
    if not isinstance(payload, dict):
        return [f"{path}: expected object, got {type(payload).__name__}"]

    required = schema.get("required", [])
    for key in required:
        if key not in payload:
            errors.append(f"{path}: missing required field '{key}'")

    props = schema.get("properties", {})
    if schema.get("additionalProperties") is False:
        for key in payload:
            if key not in props:
                errors.append(f"{path}: unexpected field '{key}'")
    for key, value in payload.items():
        if key not in props:
            continue
        subschema = props[key]
        errors.extend(_check_value(value, subschema, f"{path}.{key}"))
    return errors


def _check_value(value: Any, schema: dict[str, Any], path: str) -> list[str]:
    errors: list[str] = []
    stype = schema.get("type")

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected {schema['const']!r}, got {value!r}")

    if stype == "object":
        if not isinstance(value, dict):
            errors.append(f"{path}: expected object, got {type(value).__name__}")
        else:
            errors.extend(_check_required(value, schema, path))
    elif stype == "array":
        if not isinstance(value, list):
            errors.append(f"{path}: expected array, got {type(value).__name__}")
        elif "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: expected at least {schema['minItems']} items, got {len(value)}")
        else:
            items_schema = schema.get("items", {})
            for i, item in enumerate(value):
                errors.extend(_check_value(item, items_schema, f"{path}[{i}]"))
    elif stype == "string":
        if not isinstance(value, str):
            errors.append(f"{path}: expected string, got {type(value).__name__}")
        else:
            if "minLength" in schema and len(value) < schema["minLength"]:
                errors.append(
                    f"{path}: expected length >= {schema['minLength']}, got {len(value)}"
                )
            if "maxLength" in schema and len(value) > schema["maxLength"]:
                errors.append(
                    f"{path}: expected length <= {schema['maxLength']}, got {len(value)}"
                )
            if "enum" in schema and value not in schema["enum"]:
                errors.append(f"{path}: value '{value}' not in allowed enum {schema['enum']}")
            pattern = schema.get("pattern")
            if pattern:
                import re

                if not re.search(pattern, value):
                    errors.append(f"{path}: value does not match pattern {pattern}")
    elif stype == "boolean":
        if not isinstance(value, bool):
            errors.append(f"{path}: expected boolean, got {type(value).__name__}")
        elif "enum" in schema and value not in schema["enum"]:
            errors.append(f"{path}: value {value!r} not in allowed enum {schema['enum']}")

    if "$ref" in schema:
        ref_name = schema["$ref"]
        sub = load_schema(ref_name)
        errors.extend(_check_required(value, sub, path))

    return errors


def validate(payload: dict[str, Any], schema_name: str) -> list[str]:
    """Validate a payload against a schema.

    Returns a list of error messages. An empty list means the payload is valid.
    """
    schema = load_schema(schema_name)

    # Try jsonschema if available for stricter validation.
    try:
        import jsonschema

        validator_cls = (
            jsonschema.Draft202012Validator
            if "2020-12" in schema.get("$schema", "")
            else jsonschema.Draft7Validator
        )
        validator = _jsonschema_validator(jsonschema, validator_cls, schema)
        return [str(e.message) for e in validator.iter_errors(payload)]
    except ImportError:
        pass

    return _check_required(payload, schema)


def validate_article_proposal(payload: dict[str, Any]) -> list[str]:
    return validate(payload, "article-proposal.schema.json")


def validate_org_feedback(payload: dict[str, Any]) -> list[str]:
    return validate(payload, "org-feedback.schema.json")


def validate_provenance_bundle(payload: dict[str, Any]) -> list[str]:
    return validate(payload, "provenance-bundle.schema.json")
