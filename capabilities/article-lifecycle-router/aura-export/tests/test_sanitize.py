"""Basic tests for the sanitize module."""

from aura_export import sanitize


def test_scan_detects_email():
    text = "Contact alice@example.com for details."
    result = sanitize.scan_text(text, cfg={
        "sensitive_patterns": [
            {"name": "email", "pattern": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"}
        ]
    })
    assert not result["passed"]
    assert any(f["name"] == "email" for f in result["findings"])


def test_scan_passes_clean_text():
    text = "A general pattern for knowledge gardens is to start with a folksonomy."
    result = sanitize.scan_text(text, cfg={
        "sensitive_patterns": [
            {"name": "email", "pattern": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"}
        ]
    })
    assert result["passed"]


def test_abstraction_examples_required():
    payload = {}
    errors = sanitize.check_abstraction_examples(payload)
    assert any("required" in e.lower() for e in errors)


def test_abstraction_examples_valid():
    payload = {
        "abstraction_examples": [
            {"original": "client-x-dashboard", "abstracted": "example-analytics-dashboard"}
        ]
    }
    errors = sanitize.check_abstraction_examples(payload)
    assert not errors


def test_source_allow_list_requires_exact_or_subdomain_match():
    payload = {"sources": [{"url": "https://evilgithub.com/post"}]}
    warnings = sanitize.check_sources(payload, cfg={"source_allow_list": ["github.com"]})
    assert warnings

    payload = {"sources": [{"url": "https://docs.github.com/post"}]}
    warnings = sanitize.check_sources(payload, cfg={"source_allow_list": ["github.com"]})
    assert not warnings


def test_source_allow_list_strips_only_www_prefix():
    payload = {"sources": [
        {"url": "https://www.w3.org/TR/WCAG22/"},
        {"url": "https://www.google.com/search?q=knowledge+garden"},
        {"url": "https://docs.github.com/post"},
    ]}

    warnings = sanitize.check_sources(
        payload,
        cfg={"source_allow_list": ["w3.org", "google.com", "github.com"]},
    )

    assert not warnings


def test_source_allow_list_normalizes_allowed_www_domains():
    payload = {"sources": [{"url": "https://www.w3.org/TR/WCAG22/"}]}

    warnings = sanitize.check_sources(payload, cfg={"source_allow_list": ["www.w3.org"]})

    assert not warnings
