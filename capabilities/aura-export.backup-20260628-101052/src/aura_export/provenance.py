"""Provenance logging for sanitization and review."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import config
from .utils import save_json


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_provenance_bundle(
    origin_workspace_type: str = "personal",
    sanitization_steps: list[str] | None = None,
    reviewer_agents: list[str] | None = None,
    confidence_at_origin: str = "medium",
    export_decision_rationale: str = "",
    origin_path: str | None = None,
) -> dict[str, Any]:
    """Build a provenance bundle compatible with provenance-bundle.schema.json."""
    bundle: dict[str, Any] = {
        "schemaVersion": 1,
        "origin_workspace_type": origin_workspace_type,
        "sanitization_steps": sanitization_steps or [],
        "reviewer_agents": reviewer_agents or [],
        "confidence_at_origin": confidence_at_origin,
        "export_decision_rationale": export_decision_rationale,
    }
    return bundle


def log_transform(
    bundle: dict[str, Any],
    transform: str,
    reason: str,
    field: str = "",
) -> dict[str, Any]:
    """Append a sanitization transform to an existing bundle."""
    step = f"{transform}; reason: {reason}"
    if field:
        step = f"{step}; field: {field}"
    bundle.setdefault("sanitization_steps", []).append(step)
    return bundle


def save_provenance(
    bundle: dict[str, Any],
    slug: str,
    cfg: dict[str, Any] | None = None,
    project_root: Path | None = None,
) -> Path:
    """Save a provenance bundle to the local provenance directory."""
    if cfg is None:
        cfg = config.load_config(project_root)
    if project_root is None:
        from .utils import find_project_root

        project_root = find_project_root()
    prov_dir = config.provenance_dir(cfg, project_root)
    path = prov_dir / f"{slug}.provenance.json"
    save_json(path, bundle)
    return path
