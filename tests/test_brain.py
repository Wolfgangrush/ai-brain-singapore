"""Brain end-to-end tests — Singapore."""

from aibrain_singapore.brain.router import think
from aibrain_singapore.brain.classifier import classify
from aibrain_singapore.brain.intents import Intent


def test_citation_lookup_routes():
    assert classify("validate [2023] 1 SLR 100") == Intent.CITATION_LOOKUP


def test_compliance_flag_routes():
    assert classify("is this LPCR Rule 8 ok?") == Intent.COMPLIANCE_FLAG


def test_compliance_aml_detected():
    assert classify("new client AML check") == Intent.COMPLIANCE_FLAG


def test_unknown_fallback():
    assert classify("") == Intent.UNKNOWN
    assert classify("hello") == Intent.UNKNOWN


def test_calendar_query_by_next_week():
    """'hearing next week' matches CALENDAR_QUERY (next week comes first)."""
    assert classify("hearing next week") == Intent.CALENDAR_QUERY


def test_calendar_add_routes():
    assert classify("remind me about the deadline") == Intent.CALENDAR_ADD


def test_matter_agent_handles_stub():
    """matter_agent is a stub — should still respond with ok."""
    r = think("filed the OC")
    assert r["ok"] is True
    assert r["agent"] == "matter_agent"


def test_compliance_agent_routes():
    r = think("is this LPCR Rule 8 ok?")
    assert r["ok"] is True
    assert r["agent"] == "compliance_agent"
    assert "flags" in r["result"]


def test_calendar_query_classify():
    assert classify("show today's hearings") == Intent.CALENDAR_QUERY
