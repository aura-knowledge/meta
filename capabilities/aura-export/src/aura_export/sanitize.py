"""Privacy sanitization and scanning."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from . import config
from .provenance import log_transform
from .utils import merge_dicts


def scan_text(text: str, cfg: dict[str, Any] | None = None) -> dict[str, Any]:
    """Run all configured sensitive-pattern scanners over text."""
    if cfg is None:
        cfg = config.load_config()

    patterns = config.sensitive_patterns(cfg)
    findings: list[dict[str, Any]] = []
    for item in patterns:
        name = item["name"]
        pattern = item["pattern"]
        try:
            compiled = re.compile(pattern, re.IGNORECASE)
        except re.error as exc:
            findings.append({
                "name": name,
                "pattern": pattern,
                "error": f"invalid regex: {exc}",
            })
            continue
        for match in compiled.finditer(text):
            findings.append({
                "name": name,
                "pattern": pattern,
                "match": match.group(0),
                "start": match.start(),
                "end": match.end(),
            })

    return {"findings": findings, "passed": len(findings) == 0}


def check_sources(payload: dict[str, Any], cfg: dict[str, Any] | None = None) -> list[str]:
    """Check that cited sources are on the allow-list or explicitly justified."""
    if cfg is None:
        cfg = config.load_config()

    allow_list = config.source_allow_list(cfg)
    warnings: list[str] = []
    sources = payload.get("sources", [])
    for i, source in enumerate(sources):
        url = source.get("url", "")
        parsed = urlparse(url)
        domain = parsed.netloc.lower().lstrip("www.")
        if domain and not any(domain == allowed or domain.endswith(f".{allowed}") for allowed in allow_list):
            warnings.append(
                f"sources[{i}] domain '{domain}' is not in the allow-list; "
                "justify why it is public and cite-able."
            )
    return warnings


def check_abstraction_examples(payload: dict[str, Any]) -> list[str]:
    """Verify that abstraction examples are present and non-trivial."""
    examples = payload.get("abstraction_examples", [])
    errors: list[str] = []
    if not examples:
        errors.append("abstraction_examples is required: show at least one concrete-to-abstract translation.")
        return errors
    for i, example in enumerate(examples):
        original = example.get("original", example.get("concrete", "")).strip()
        abstracted = example.get("abstracted", example.get("abstract", "")).strip()
        if not original or not abstracted:
            errors.append(f"abstraction_examples[{i}] must have both original and abstracted values.")
        elif original.lower() == abstracted.lower():
            errors.append(f"abstraction_examples[{i}] original and abstracted values are identical.")
    return errors


def apply_abstraction_hints(text: str, cfg: dict[str, Any] | None = None) -> tuple[str, list[dict[str, str]]]:
    """Apply configured concrete-to-abstract replacements and return the transformed text plus log entries."""
    if cfg is None:
        cfg = config.load_config()

    hints = config.abstraction_hints(cfg)
    applied: list[dict[str, str]] = []
    transformed = text
    for hint in hints:
        concrete = hint.get("concrete", "")
        abstract = hint.get("abstract", "")
        if not concrete or concrete not in transformed:
            continue
        transformed = transformed.replace(concrete, abstract)
        applied.append({
            "transform": f"replaced '{concrete}' with '{abstract}'",
            "reason": "project-specific abstraction hint",
            "field": "raw_text",
        })
    return transformed, applied


def sanitize_draft(
    draft: dict[str, Any],
    cfg: dict[str, Any] | None = None,
    project_root: Path | None = None,
) -> dict[str, Any]:
    """Run a full sanitization pass on a draft.

    Returns an updated draft with:
    - sanitized_summary
    - privacy_report
    - source_warnings
    - abstraction_errors
    - status updated to 'sanitized' or 'needs-review'
    """
    if cfg is None:
        cfg = config.load_config(project_root)

    raw_text = draft.get("raw_text", "")
    title = draft.get("title", "")

    # Apply configured abstraction hints to raw text.
    transformed_text, hint_transforms = apply_abstraction_hints(raw_text, cfg)

    # Scan raw content and title.
    combined = f"{title}\n\n{transformed_text}"
    scan_result = scan_text(combined, cfg)

    # Build a sanitized summary if not already provided.
    if "sanitized_summary" not in draft or not draft["sanitized_summary"]:
        draft["sanitized_summary"] = _auto_summary(transformed_text)

    # Ensure abstraction examples exist.
    if "abstraction_examples" not in draft:
        draft["abstraction_examples"] = []

    abstraction_errors = check_abstraction_examples(draft)
    source_warnings = check_sources(draft, cfg)

    # Build/extend provenance bundle.
    provenance = draft.get("provenance_bundle", {})
    for t in hint_transforms:
        provenance = log_transform(provenance, t["transform"], t["reason"], t["field"])
    draft["provenance_bundle"] = provenance

    draft["privacy_report"] = {
        "scanned_at": _now_iso(),
        **scan_result,
        "source_warnings": source_warnings,
        "abstraction_errors": abstraction_errors,
    }

    if scan_result["passed"] and not abstraction_errors and not source_warnings:
        draft["status"] = "sanitized"
    else:
        draft["status"] = "needs-review"

    return draft


def privacy_report_markdown(report: dict[str, Any]) -> str:
    """Render a privacy report as markdown."""
    lines: list[str] = []
    lines.append("## Privacy scan report")
    passed = report.get("passed", False)
    lines.append(f"- **Passed:** {'yes' if passed else 'no'}")
    findings = report.get("findings", [])
    if findings:
        lines.append(f"- **Findings:** {len(findings)}")
        for f in findings[:10]:
            name = f.get("name", "unknown")
            match = f.get("match", "")
            lines.append(f"  - `{name}`: `{match}`")
        if len(findings) > 10:
            lines.append(f"  - ... and {len(findings) - 10} more")
    else:
        lines.append("- **Findings:** none")

    warnings = report.get("source_warnings", [])
    if warnings:
        lines.append("- **Source warnings:**")
        for w in warnings:
            lines.append(f"  - {w}")

    errors = report.get("abstraction_errors", [])
    if errors:
        lines.append("- **Abstraction errors:**")
        for e in errors:
            lines.append(f"  - {e}")

    return "\n".join(lines)


def _auto_summary(text: str, max_chars: int = 1200) -> str:
    """Create a fallback sanitized summary from the first few non-empty paragraphs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    summary = "\n\n".join(paragraphs[:3])
    if len(summary) > max_chars:
        summary = summary[:max_chars].rsplit(" ", 1)[0] + "..."
    return summary


def _now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat()
