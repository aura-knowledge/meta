#!/usr/bin/env python3
"""Validate The Long Human Road to AI research method files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WORK_PACKAGE_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
OUTSIDE_ALLOWLIST_MARKERS = (
    "outside the default allow-list",
    "outside the default source allow-list",
)


def load_yaml(path: Path, errors: list[str]) -> object:
    if yaml is None:
        errors.append("PyYAML is required: python3 -m pip install PyYAML")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: failed to parse YAML: {exc}")
        return {}


def missing(value: object) -> bool:
    return value is None or value == "" or value == []


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def source_allow_list(canon: dict) -> set[str]:
    snapshot = canon.get("default_allow_list_reference", {}).get("snapshot", [])
    if not isinstance(snapshot, list):
        return set()
    return {str(item).lower().lstrip("www.") for item in snapshot if item}


def domain_allowed(domain: str, allow_list: set[str]) -> bool:
    return any(domain == allowed or domain.endswith(f".{allowed}") for allowed in allow_list)


def validate_source_canon(research_dir: Path, errors: list[str]) -> tuple[dict, set[str]]:
    canon = load_yaml(research_dir / "source-canon.yaml", errors)
    if not isinstance(canon, dict):
        errors.append("source-canon.yaml must parse to a mapping")
        return {}, set()

    id_policy = canon.get("id_policy", {})
    try:
        source_id_re = re.compile(str(id_policy["pattern"]))
    except Exception:
        errors.append("source-canon.yaml id_policy.pattern must be a valid regex")
        source_id_re = re.compile(r"^$")
    max_id_length = int(id_policy.get("max_length", 999))

    required = canon.get("source_entry_contract", {}).get("required_fields", [])
    if not required:
        errors.append("source-canon.yaml must define source_entry_contract.required_fields")

    authority_values = set(canon.get("authority_classes", {}).keys())
    source_type_values = set(canon.get("source_type_values", []))
    public_access_values = set(canon.get("public_access_values", []))
    visual_reuse_values = set(canon.get("visual_reuse_values", []))
    allow_list = source_allow_list(canon)

    sources = canon.get("sources", [])
    if not isinstance(sources, list) or not sources:
        errors.append("source-canon.yaml sources must be a non-empty list")
        return canon, set()

    source_ids: list[str] = []
    for index, source in enumerate(sources):
        loc = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{loc} must be a mapping")
            continue

        for field in required:
            if missing(source.get(field)):
                errors.append(f"{loc} missing required field: {field}")

        source_id = source.get("id")
        if isinstance(source_id, str):
            source_ids.append(source_id)
            if len(source_id) > max_id_length:
                errors.append(f"{loc}.id exceeds max length: {source_id}")
            if not source_id_re.fullmatch(source_id):
                errors.append(f"{loc}.id fails pattern: {source_id}")

        if source.get("authority") and source.get("authority") not in authority_values:
            errors.append(f"{loc}.authority has unknown value: {source.get('authority')}")
        if source.get("source_type") and source_type_values and source.get("source_type") not in source_type_values:
            errors.append(f"{loc}.source_type has unknown value: {source.get('source_type')}")
        if source.get("public_access") and public_access_values and source.get("public_access") not in public_access_values:
            errors.append(f"{loc}.public_access has unknown value: {source.get('public_access')}")
        source_url = source.get("url")
        if source_url and not valid_url(source_url):
            errors.append(f"{loc}.url must be an http or https URL")
        elif source_url and allow_list:
            domain = urlparse(str(source_url)).netloc.lower().lstrip("www.")
            access_notes = str(source.get("access_notes", ""))
            if domain and not domain_allowed(domain, allow_list) and not any(
                marker in access_notes for marker in OUTSIDE_ALLOWLIST_MARKERS
            ):
                errors.append(
                    f"{loc} domain '{domain}' is outside the default allow-list; "
                    "access_notes must justify public citability"
                )
        if source.get("accessed") and not DATE_RE.fullmatch(str(source.get("accessed"))):
            errors.append(f"{loc}.accessed must be YYYY-MM-DD")
        if source.get("status") not in {"active", "deprecated"}:
            errors.append(f"{loc}.status must be active or deprecated")
        if source.get("status") == "deprecated" and not source.get("deprecation_notes"):
            errors.append(f"{loc}.deprecation_notes is required when status is deprecated")

        for list_field in ("best_for", "limitations"):
            if list_field in source and not (
                isinstance(source[list_field], list)
                and all(isinstance(item, str) and item for item in source[list_field])
            ):
                errors.append(f"{loc}.{list_field} must be a list of strings")

        visual_use = source.get("visual_use")
        if not isinstance(visual_use, dict):
            errors.append(f"{loc}.visual_use must be a mapping")
        else:
            reuse = visual_use.get("reuse")
            if missing(reuse):
                errors.append(f"{loc}.visual_use.reuse is required")
            elif visual_reuse_values and reuse not in visual_reuse_values:
                errors.append(f"{loc}.visual_use.reuse has unknown value: {reuse}")
            if missing(visual_use.get("notes")):
                errors.append(f"{loc}.visual_use.notes is required")

    if len(source_ids) != len(set(source_ids)):
        errors.append("source-canon.yaml has duplicate source IDs")

    known_ids = set(source_ids)
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            continue
        replacement_ids = source.get("replacement_ids", [])
        if replacement_ids and not isinstance(replacement_ids, list):
            errors.append(f"sources[{index}].replacement_ids must be a list")
            continue
        for replacement_id in replacement_ids:
            if replacement_id not in known_ids:
                errors.append(f"sources[{index}].replacement_ids unknown source id: {replacement_id}")

    return canon, known_ids


def validate_card_schema(research_dir: Path, errors: list[str]) -> dict:
    schema = load_yaml(research_dir / "card-schema.yaml", errors)
    if not isinstance(schema, dict):
        errors.append("card-schema.yaml must parse to a mapping")
        return {}
    if not isinstance(schema.get("required_fields"), list):
        errors.append("card-schema.yaml must define required_fields")
    if not isinstance(schema.get("enums"), dict):
        errors.append("card-schema.yaml must define enums")
    return schema


def validate_source_id_map(research_dir: Path, source_ids: set[str], errors: list[str]) -> None:
    path = research_dir / "source-id-map.yaml"
    if not path.exists():
        return

    source_map = load_yaml(path, errors)
    if not isinstance(source_map, dict):
        errors.append("source-id-map.yaml must parse to a mapping")
        return
    packages = source_map.get("packages")
    if not isinstance(packages, dict) or not packages:
        errors.append("source-id-map.yaml must define packages")
        return
    for package, mappings in packages.items():
        if not isinstance(mappings, dict) or not mappings:
            errors.append(f"source-id-map.yaml packages.{package} must be a non-empty mapping")
            continue
        for local_id, canon_id in mappings.items():
            if not isinstance(local_id, str) or missing(local_id):
                errors.append(f"source-id-map.yaml packages.{package} has an invalid local source id")
            if not isinstance(canon_id, str) or missing(canon_id):
                errors.append(f"source-id-map.yaml packages.{package}.{local_id} must map to a canon source id")
            elif canon_id not in source_ids:
                errors.append(
                    f"source-id-map.yaml packages.{package}.{local_id} unknown canon id: {canon_id}"
                )


def card_id_validator(schema: dict) -> tuple[re.Pattern[str], int]:
    id_policy = schema.get("id_policy", {})
    pattern = str(id_policy.get("card_id_pattern", r"^$"))
    max_length = int(id_policy.get("max_id_length", 999))
    return re.compile(pattern), max_length


def card_files(cards_dir: Path) -> list[Path]:
    if not cards_dir.exists():
        return []
    return sorted(
        path
        for path in cards_dir.rglob("*.yaml")
        if path.is_file() and not any(part.startswith("_") for part in path.relative_to(cards_dir).parts)
    )


def validate_card_path(cards_dir: Path, path: Path, card: dict, errors: list[str]) -> None:
    rel = path.relative_to(cards_dir)
    if len(rel.parts) != 2:
        errors.append(f"{path}: card path must be research/cards/<work-package>/<card-id>.yaml")
        return
    work_package, filename = rel.parts
    if not WORK_PACKAGE_RE.fullmatch(work_package):
        errors.append(f"{path}: work package directory must be lowercase kebab-case")
    if filename != f"{card.get('id')}.yaml":
        errors.append(f"{path}: filename must match card id")


def validate_card(
    path: Path,
    cards_dir: Path,
    card: object,
    schema: dict,
    source_ids: set[str],
    source_status: dict[str, str],
    source_visual_reuse: dict[str, str],
    errors: list[str],
) -> None:
    if not isinstance(card, dict):
        errors.append(f"{path}: card must parse to a mapping")
        return

    validate_card_path(cards_dir, path, card, errors)

    card_id_re, max_card_id_length = card_id_validator(schema)
    card_id = card.get("id")
    if not isinstance(card_id, str) or not card_id_re.fullmatch(card_id):
        errors.append(f"{path}: card id fails pattern: {card_id}")
    elif len(card_id) > max_card_id_length:
        errors.append(f"{path}: card id exceeds max length: {card_id}")

    optional_empty_fields = {
        "analogy_candidate",
        "analogy_limits",
        "visual_candidates",
        "visual_license_notes",
        "review_flags",
    }
    for field in schema.get("required_fields", []):
        if field not in card:
            errors.append(f"{path}: missing required field: {field}")
        elif field not in optional_empty_fields and missing(card.get(field)):
            errors.append(f"{path}: required field {field} must be non-empty")

    enums = schema.get("enums", {})
    enum_fields = (
        "human_capability",
        "lane",
        "geography_or_tradition",
        "story_role",
        "claim_type",
        "confidence",
        "uncertainty",
    )
    for field in enum_fields:
        values = set(enums.get(field, []))
        if card.get(field) and card.get(field) not in values:
            errors.append(f"{path}: {field} has unknown value: {card.get(field)}")

    review_flags = card.get("review_flags", [])
    if not isinstance(review_flags, list):
        errors.append(f"{path}: review_flags must be a list")
        review_flags = []
    else:
        known_flags = set(enums.get("review_flag", []))
        for flag in review_flags:
            if flag not in known_flags:
                errors.append(f"{path}: review_flags has unknown value: {flag}")

    cited_sources = card.get("source_ids", [])
    if not isinstance(cited_sources, list) or not all(isinstance(item, str) for item in cited_sources):
        errors.append(f"{path}: source_ids must be a list of source IDs")
        cited_sources = []
    for source_id in cited_sources:
        if source_id not in source_ids:
            errors.append(f"{path}: unknown source id: {source_id}")
        if source_status.get(source_id) == "deprecated" and not (
            {"source-deprecated", "needs-source-cross-check"} & set(review_flags)
        ):
            errors.append(f"{path}: deprecated source requires source-deprecated or needs-source-cross-check")

    claim_type = card.get("claim_type")
    if claim_type in {"fact", "analogy", "speculation"} and not cited_sources:
        errors.append(f"{path}: {claim_type} cards require at least one source_id")
    if claim_type == "interpretation":
        if not cited_sources:
            errors.append(f"{path}: interpretation cards require at least one source_id")
        if len(cited_sources) < 2 and not (
            {"needs-source-cross-check", "needs-primary-source", "needs-secondary-source"} & set(review_flags)
        ):
            errors.append(f"{path}: interpretation cards with one source require a source review flag")
    if claim_type == "speculation" and card.get("uncertainty") != "speculative":
        errors.append(f"{path}: speculation cards require uncertainty: speculative")

    has_analogy = (
        claim_type == "analogy"
        or card.get("story_role") == "analogy"
        or bool(card.get("analogy_candidate"))
    )
    if has_analogy and not card.get("analogy_limits"):
        errors.append(
            f"{path}: analogy_limits is required when analogy_candidate, story_role, or claim_type uses analogy"
        )
    if claim_type == "analogy" and not card.get("analogy_candidate"):
        errors.append(f"{path}: analogy cards require analogy_candidate")

    visual_candidates = card.get("visual_candidates", [])
    if not isinstance(visual_candidates, list):
        errors.append(f"{path}: visual_candidates must be a list")
        return
    if visual_candidates and missing(card.get("visual_license_notes")):
        errors.append(f"{path}: visual_license_notes is required when visual_candidates is not empty")

    visual_types = set(enums.get("visual_type", []))
    visual_provenance = set(enums.get("visual_provenance", []))
    required_visual_fields = schema.get("visual_candidate_shape", {}).get("required_fields", [])
    reusable = {"public-domain", "permissive-license"}

    for index, visual in enumerate(visual_candidates):
        loc = f"{path}: visual_candidates[{index}]"
        if not isinstance(visual, dict):
            errors.append(f"{loc} must be a mapping")
            continue
        for field in required_visual_fields:
            if missing(visual.get(field)):
                errors.append(f"{loc}.{field} is required")
        if visual.get("type") and visual.get("type") not in visual_types:
            errors.append(f"{loc}.type has unknown value: {visual.get('type')}")
        if visual.get("provenance") and visual.get("provenance") not in visual_provenance:
            errors.append(f"{loc}.provenance has unknown value: {visual.get('provenance')}")

        visual_source_ids = visual.get("source_ids", [])
        if visual_source_ids and not isinstance(visual_source_ids, list):
            errors.append(f"{loc}.source_ids must be a list")
            visual_source_ids = []
        for source_id in visual_source_ids:
            if source_id not in source_ids:
                errors.append(f"{loc} unknown source id: {source_id}")

        if visual.get("provenance") in reusable:
            if not visual.get("license_url"):
                errors.append(f"{loc}.license_url is required for reusable visual provenance")
            if not visual.get("attribution"):
                errors.append(f"{loc}.attribution is required for reusable visual provenance")
        if visual.get("provenance") == "rights-review-needed" and "visual-rights-needed" not in review_flags:
            errors.append(f"{path}: rights-review-needed visuals require visual-rights-needed review flag")
        if visual.get("type") == "artifact-photo" and visual.get("provenance") == "original-diagram":
            errors.append(f"{loc}.provenance cannot be original-diagram for artifact-photo")
        for source_id in visual_source_ids:
            reuse = source_visual_reuse.get(source_id)
            if reuse in {"metadata-only", "prohibited"} and visual.get("provenance") in reusable:
                errors.append(f"{loc} cites {source_id}, which is marked visual_use.reuse: {reuse}")


def validate_cards(research_dir: Path, schema: dict, canon: dict, source_ids: set[str], errors: list[str]) -> int:
    sources = canon.get("sources", []) if isinstance(canon, dict) else []
    source_status = {
        source["id"]: source.get("status", "")
        for source in sources
        if isinstance(source, dict) and isinstance(source.get("id"), str)
    }
    source_visual_reuse = {
        source["id"]: source.get("visual_use", {}).get("reuse", "")
        for source in sources
        if isinstance(source, dict) and isinstance(source.get("id"), str)
    }
    cards_dir = research_dir / "cards"
    files = card_files(cards_dir)
    for path in files:
        card = load_yaml(path, errors)
        validate_card(path, cards_dir, card, schema, source_ids, source_status, source_visual_reuse, errors)
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate LHRA research source canon and cards")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--proposal", default="proposals/long-human-road-to-ai", help="Proposal path")
    args = parser.parse_args()

    root = Path(args.root)
    research_dir = root / args.proposal / "research"
    errors: list[str] = []

    if not research_dir.exists():
        errors.append(f"research directory not found: {research_dir}")
        card_count = 0
    else:
        canon, source_ids = validate_source_canon(research_dir, errors)
        schema = validate_card_schema(research_dir, errors)
        validate_source_id_map(research_dir, source_ids, errors)
        card_count = validate_cards(research_dir, schema, canon, source_ids, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if card_count:
        print(f"LHRA research validation passed ({card_count} card file(s))")
    else:
        print("LHRA research validation passed (no card files found)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
