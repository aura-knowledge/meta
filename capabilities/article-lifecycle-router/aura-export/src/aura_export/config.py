"""Configuration loading for aura-export."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

from .utils import find_project_root, load_json, merge_dicts


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yaml"
USER_CONFIG_DIR = Path.home() / ".config" / "aura-export"
USER_CONFIG_PATH = USER_CONFIG_DIR / "config.yaml"


def load_yaml(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_config(
    project_root: Path | str | None = None,
    extra_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Load merged configuration.

    Precedence (highest first):
    1. extra_overrides argument
    2. ./.aura-export/config.yaml in the project
    3. ~/.config/aura-export/config.yaml
    4. built-in capabilities/article-lifecycle-router/aura-export/config.yaml
    """
    config = load_yaml(DEFAULT_CONFIG_PATH)

    if USER_CONFIG_PATH.exists():
        config = merge_dicts(config, load_yaml(USER_CONFIG_PATH))

    if project_root is None:
        project_root = find_project_root()
    project_root = Path(project_root)

    project_config_path = project_root / ".aura-export" / "config.yaml"
    if project_config_path.exists():
        config = merge_dicts(config, load_yaml(project_config_path))

    if extra_overrides:
        config = merge_dicts(config, extra_overrides)

    return config


def ensure_user_config() -> Path:
    """Create a default user config file if it does not exist."""
    if not USER_CONFIG_PATH.exists():
        USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        default = load_yaml(DEFAULT_CONFIG_PATH)
        with open(USER_CONFIG_PATH, "w", encoding="utf-8") as fh:
            yaml.safe_dump(default, fh, default_flow_style=False, sort_keys=False)
    return USER_CONFIG_PATH


def repo_labels(config: dict[str, Any]) -> dict[str, str]:
    return config.get("labels", {})


def sensitive_patterns(config: dict[str, Any]) -> list[dict[str, str]]:
    return config.get("sensitive_patterns", [])


def source_allow_list(config: dict[str, Any]) -> list[str]:
    return config.get("source_allow_list", [])


def export_markers(config: dict[str, Any]) -> list[str]:
    return config.get("export_markers", [])


def abstraction_hints(config: dict[str, Any]) -> list[dict[str, str]]:
    return config.get("abstraction_hints", [])


def draft_dir(config: dict[str, Any], project_root: Path) -> Path:
    return project_root / config.get("local_draft_dir", ".aura-export/drafts")


def provenance_dir(config: dict[str, Any], project_root: Path) -> Path:
    return project_root / config.get("local_provenance_dir", ".aura-export/provenance")


def github_repo(config: dict[str, Any]) -> str:
    meta = config.get("meta", {})
    return f"{meta.get('owner', 'aura-knowledge')}/{meta.get('repo', 'meta')}"
