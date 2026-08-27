"""Tests for singapore_citation_validator MCP tool — Singapore v0.1."""

from aibrain_singapore.mcp_tools.citation_validator import singapore_citation_validator


def test_valid_slr():
    r = singapore_citation_validator("[2023] 1 SLR 100")
    assert r["valid"] is True
    assert r["format"] == "SLR"
    assert r["year"] == 2023
    assert r["page_or_serial"] == 100


def test_valid_sgca():
    r = singapore_citation_validator("[2024] SGCA 12")
    assert r["valid"] is True
    assert r["format"] == "SGCA"
    assert r["year"] == 2024
    assert r["page_or_serial"] == 12


def test_valid_sghc():
    r = singapore_citation_validator("[2024] SGHC 89")
    assert r["valid"] is True
    assert r["format"] == "SGHC"
    assert r["year"] == 2024


def test_valid_mlj():
    r = singapore_citation_validator("[2023] 4 MLJ 567")
    assert r["valid"] is True
    assert r["format"] == "MLJ"


def test_invalid_missing_brackets():
    r = singapore_citation_validator("2023 1 SLR 100")
    assert r["valid"] is False


def test_invalid_wrong_format():
    r = singapore_citation_validator("[2023] SGHCF 50")
    assert r["valid"] is False
    assert r["format"] == "UNKNOWN"


def test_invalid_empty_string():
    r = singapore_citation_validator("")
    assert r["valid"] is False


def test_invalid_non_string():
    r = singapore_citation_validator(None)
    assert r["valid"] is False
    assert "not a string" in r["parse_notes"]


def test_invalid_garbage():
    r = singapore_citation_validator("hello world")
    assert r["valid"] is False


def test_slr_volume_captured():
    r = singapore_citation_validator("[2023] 1 SLR 100")
    assert r["court_or_reporter"] == "1"
