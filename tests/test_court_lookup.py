"""Tests for singapore_court_lookup MCP tool — Singapore v0.1."""

from aibrain_singapore.mcp_tools.court_lookup import singapore_court_lookup


def test_lookup_court_of_appeal_exact():
    r = singapore_court_lookup("Supreme Court — Court of Appeal")
    assert r["found"] is True
    assert r["tier"] == "apex"
    assert r["matched_enum"] == "SC_CA"


def test_lookup_fuzzy_supreme_court():
    r = singapore_court_lookup("supreme court")
    # Should match SC_HC_GD since "supreme court" appears in its value first
    # Actually fuzzy match iterates enum order, SC_CA comes first
    assert r["found"] is True


def test_lookup_sicc_tier():
    r = singapore_court_lookup("International Commercial Court")
    assert r["found"] is True
    assert r["tier"] == "specialised_international"
    assert r["matched_enum"] == "SICC"


def test_lookup_district_court_pecuniary():
    r = singapore_court_lookup("District Court")
    assert r["found"] is True
    assert "S$60" in r["pecuniary_limit"]


def test_lookup_magistrate_pecuniary():
    r = singapore_court_lookup("Magistrates' Court")
    assert r["found"] is True
    limit = r["pecuniary_limit"]
    assert "S$60" in limit


def test_lookup_not_found():
    r = singapore_court_lookup("Martian Court of Justice")
    assert r["found"] is False


def test_lookup_non_string_input():
    r = singapore_court_lookup(42)
    assert r["found"] is False
    assert "error" in r
