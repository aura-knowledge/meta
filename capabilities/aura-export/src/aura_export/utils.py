"""Shared utilities for aura-export."""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


RE_NONWORD = re.compile(r"[^\w\s-]+", re.UNICODE)
RE_WHITESPACE = re.compile(r"[-\s]+", re.UNICODE)


def slugify(value: str) -> str:
    """Convert a string to a lowercase kebab-case slug."""
    value = RE_NONWORD.sub("", value)
    value = RE_WHITESPACE.sub("-", value).strip("-").lower()
    return value


def find_project_root(start: Path | str | None = None) -> Path:
    """Find the nearest directory containing a .git folder or pyproject.toml.

    Falls back to the current working directory if nothing is found.
    """
    if start is None:
        start = Path.cwd()
    else:
        start = Path(start).resolve()

    for path in [start, *start.parents]:
        if (path / ".git").exists() or (path / "pyproject.toml").exists():
            return path
    return start


def load_json(path: Path | str) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path | str, data: Any, indent: int = 2) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent, ensure_ascii=False)
        fh.write("\n")


def run_command(
    cmd: list[str],
    cwd: Path | str | None = None,
    check: bool = False,
    capture_output: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a shell command and return the completed process."""
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=check,
        capture_output=capture_output,
        text=True,
        env=merged_env,
    )


def git_available(cwd: Path | str | None = None) -> bool:
    result = run_command(["git", "rev-parse", "--git-dir"], cwd=cwd, check=False)
    return result.returncode == 0


def git_diff(cwd: Path | str | None = None, staged: bool = False) -> str:
    cmd = ["git", "diff", "--stat"]
    if staged:
        cmd.append("--staged")
    result = run_command(cmd, cwd=cwd, check=False)
    if result.returncode != 0:
        return ""

    # Return a bounded amount of diff content to avoid accidental leakage of large changes.
    cmd = ["git", "diff"]
    if staged:
        cmd.append("--staged")
    result = run_command(cmd, cwd=cwd, check=False)
    return result.stdout if result.returncode == 0 else ""


def truncate_text(text: str, max_chars: int = 4000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n\n... [{len(text) - max_chars} characters truncated]"


def merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge override into base. Lists from override replace base lists."""
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
