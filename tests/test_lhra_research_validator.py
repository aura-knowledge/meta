"""Tests for The Long Human Road to AI research validator."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate-lhra-research.py"
PROPOSAL = Path("proposals/long-human-road-to-ai")


def copy_proposal(tmp_path: Path) -> Path:
    target = tmp_path / PROPOSAL
    target.parent.mkdir(parents=True)
    shutil.copytree(REPO_ROOT / PROPOSAL, target)
    return target


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "python3",
            str(SCRIPT),
            "--root",
            str(root),
            "--proposal",
            str(PROPOSAL),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def valid_card() -> dict:
    return {
        "id": "card-human-computers",
        "title": "Human Computers as Organized Calculation",
        "date_or_period": "Before electronic computers",
        "geography_or_tradition": "europe",
        "human_capability": "counting",
        "lane": "programmable-machines",
        "event_or_claim": "The word computer referred to people who performed calculations before it referred mainly to machines.",
        "why_it_matters": "It shows that computation was first a human and institutional practice, not only a machine category.",
        "enabled": "It frames later calculating machines as attempts to mechanize organized procedures.",
        "story_role": "origin",
        "source_ids": ["src-sep-computing"],
        "claim_type": "fact",
        "confidence": "medium",
        "uncertainty": "settled",
        "analogy_candidate": "",
        "analogy_limits": "",
        "visual_candidates": [],
        "visual_license_notes": "",
        "technical_companion_notes": "Define effective method and distinguish occupation, machine, and theory.",
        "review_flags": [],
    }


def write_card(proposal: Path, card: dict, work_package: str = "01-source-method") -> None:
    card_dir = proposal / "research" / "cards" / work_package
    card_dir.mkdir(parents=True)
    card_path = card_dir / f"{card['id']}.yaml"
    card_path.write_text(yaml.safe_dump(card, sort_keys=False), encoding="utf-8")


def test_valid_canon_and_card(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    write_card(proposal, valid_card())

    result = run_validator(tmp_path)

    assert result.returncode == 0, result.stderr
    assert "LHRA research validation passed" in result.stdout


def test_missing_source_metadata(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    canon_path = proposal / "research" / "source-canon.yaml"
    canon = yaml.safe_load(canon_path.read_text(encoding="utf-8"))
    del canon["sources"][0]["authority"]
    canon_path.write_text(yaml.safe_dump(canon, sort_keys=False), encoding="utf-8")

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "sources[0] missing required field: authority" in result.stderr


def test_unknown_card_source(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    card = valid_card()
    card["source_ids"] = ["src-not-in-canon"]
    write_card(proposal, card)

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "unknown source id: src-not-in-canon" in result.stderr


def test_invalid_card_id_fails(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    card = valid_card()
    card["id"] = "BAD"
    write_card(proposal, card)

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "card id fails pattern: BAD" in result.stderr


def test_empty_required_card_fields_fail(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    card = valid_card()
    card["title"] = ""
    card["event_or_claim"] = ""
    write_card(proposal, card)

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "required field title must be non-empty" in result.stderr
    assert "required field event_or_claim must be non-empty" in result.stderr


def test_outside_allow_list_source_requires_specific_publicness_note(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    canon_path = proposal / "research" / "source-canon.yaml"
    canon = yaml.safe_load(canon_path.read_text(encoding="utf-8"))
    canon["sources"][0]["url"] = "https://example.com/source"
    canon["sources"][0]["access_notes"] = "Public page."
    canon_path.write_text(yaml.safe_dump(canon, sort_keys=False), encoding="utf-8")

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "domain 'example.com' is outside the default allow-list" in result.stderr


def test_analogy_limits_required(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    card = valid_card()
    card["story_role"] = "analogy"
    card["analogy_candidate"] = "A room of human computers works like an early computing system."
    write_card(proposal, card)

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "analogy_limits is required when analogy_candidate, story_role, or claim_type uses analogy" in result.stderr


def test_visual_rights_metadata(tmp_path: Path) -> None:
    proposal = copy_proposal(tmp_path)
    card = valid_card()
    card["visual_candidates"] = [
        {
            "type": "artifact-photo",
            "provenance": "public-domain",
            "source_ids": ["src-chm-timeline"],
            "rights_basis": "Repository page says public domain.",
        }
    ]
    write_card(proposal, card)

    result = run_validator(tmp_path)

    assert result.returncode == 1
    assert "license_url is required for reusable visual provenance" in result.stderr
