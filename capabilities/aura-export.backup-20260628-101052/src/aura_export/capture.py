"""Capture raw findings from files, git diffs, markers, or explicit text."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from . import config
from .utils import (
    find_project_root,
    git_available,
    git_diff,
    load_json,
    save_json,
    slugify,
    truncate_text,
)


DEFAULT_TITLE = "Untitled aura-export finding"


def capture_from_file(path: Path | str, max_chars: int = 8000) -> dict[str, Any]:
    """Capture content from a single file."""
    path = Path(path).resolve()
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = _extract_title(text) or path.name
    return {
        "source_file": str(path),
        "title": title,
        "raw_text": truncate_text(text, max_chars),
        "captured_at": _now_iso(),
    }


def capture_from_text(text: str, title: str | None = None) -> dict[str, Any]:
    """Capture from an explicit text snippet."""
    return {
        "title": title or _first_line(text) or DEFAULT_TITLE,
        "raw_text": text,
        "captured_at": _now_iso(),
    }


def capture_from_diff(
    project_root: Path | str | None = None,
    staged: bool = False,
    max_chars: int = 8000,
) -> dict[str, Any]:
    """Capture recent git diff."""
    if project_root is None:
        project_root = find_project_root()
    project_root = Path(project_root)

    if not git_available(project_root):
        raise RuntimeError("No git repository found; cannot capture from diff.")

    diff_text = git_diff(project_root, staged=staged)
    if not diff_text.strip():
        raise RuntimeError("No diff to capture.")

    return {
        "source_file": str(project_root),
        "title": "Finding from recent changes",
        "raw_text": truncate_text(diff_text, max_chars),
        "git_diff": True,
        "captured_at": _now_iso(),
    }


def capture_from_markers(
    project_root: Path | str | None = None,
    markers: list[str] | None = None,
    max_chars: int = 4000,
) -> dict[str, Any]:
    """Scan the project for files containing export-candidate markers."""
    if project_root is None:
        project_root = find_project_root()
    project_root = Path(project_root)

    cfg = config.load_config(project_root)
    if markers is None:
        markers = config.export_markers(cfg)

    matches: list[dict[str, Any]] = []
    for root, dirs, files in os.walk(project_root):
        # Skip hidden and common dependency directories.
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in {"node_modules", "venv", ".venv", "__pycache__", "target", "dist", "build"}]
        for filename in files:
            if not filename.endswith((".md", ".txt", ".py", ".js", ".ts", ".go", ".rs", ".java", ".yaml", ".yml", ".json")):
                continue
            filepath = Path(root) / filename
            try:
                text = filepath.read_text(encoding="utf-8", errors="ignore")
            except (OSError, UnicodeDecodeError):
                continue
            for marker in markers:
                if marker in text:
                    snippet = _extract_around_marker(text, marker, max_chars)
                    matches.append({
                        "file": str(filepath.relative_to(project_root)),
                        "marker": marker,
                        "snippet": snippet,
                    })
                    break

    if not matches:
        raise RuntimeError(f"No export markers found: {markers}")

    combined = "\n\n---\n\n".join(
        f"File: {m['file']}\nMarker: {m['marker']}\n\n{m['snippet']}" for m in matches
    )
    return {
        "title": "Finding from export markers",
        "raw_text": truncate_text(combined, max_chars * 2),
        "marker_matches": matches,
        "captured_at": _now_iso(),
    }


def build_draft(
    capture_result: dict[str, Any],
    lane: str | None = None,
    project_root: Path | None = None,
) -> dict[str, Any]:
    """Wrap a capture result in a draft envelope."""
    if project_root is None:
        project_root = find_project_root()

    title = capture_result.get("title") or DEFAULT_TITLE
    slug = slugify(title)
    draft = {
        "schema_version": "1.0.0",
        "slug": slug,
        "lane": lane,
        "status": "captured",
        **capture_result,
    }
    return draft


def save_draft(
    draft: dict[str, Any],
    path: Path | str | None = None,
    cfg: dict[str, Any] | None = None,
    project_root: Path | None = None,
) -> Path:
    """Save a draft to disk."""
    if project_root is None:
        project_root = find_project_root()
    project_root = Path(project_root)

    if cfg is None:
        cfg = config.load_config(project_root)

    if path is None:
        draft_dir = config.draft_dir(cfg, project_root)
        slug = draft.get("slug") or slugify(draft.get("title", "draft"))
        path = draft_dir / f"{slug}.draft.json"
    else:
        path = Path(path)

    path.parent.mkdir(parents=True, exist_ok=True)
    save_json(path, draft)
    return path


def load_draft(path: Path | str) -> dict[str, Any]:
    return load_json(path)


def _extract_title(text: str) -> str | None:
    lines = text.splitlines()
    for line in lines[:10]:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if stripped.startswith("<!--") or stripped.startswith("#"):
            continue
        if stripped:
            return stripped[:120]
    return None


def _first_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped[:120]
    return ""


def _extract_around_marker(text: str, marker: str, max_chars: int) -> str:
    idx = text.find(marker)
    start = max(0, idx - max_chars // 2)
    end = min(len(text), idx + len(marker) + max_chars // 2)
    snippet = text[start:end]
    return snippet.strip()


def _now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat()
