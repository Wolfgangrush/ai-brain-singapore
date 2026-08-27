"""Tests for ontology module — Singapore v0.1."""

from aibrain_singapore.core.ontology import (
    MatterType,
    SingaporeCourt,
    SingaporeStatute,
    SingaporeBarRule,
    Matter,
    CalendarEvent,
)


def test_matter_type_has_originating_claim():
    assert MatterType.OC.value == "Originating Claim"


def test_matter_type_has_dma():
    """Post-2024 Divorce by Mutual Agreement (research currency warning)."""
    assert "Mutual Agreement" in MatterType.FAMILY_DMA.value


def test_singapore_court_has_court_of_appeal():
    assert SingaporeCourt.SC_CA.value == "Supreme Court — Court of Appeal"


def test_singapore_court_has_sicc():
    assert "International Commercial" in SingaporeCourt.SICC.value


def test_singapore_statute_pdpa_with_2020_amendments():
    """PDPA must reference the 2020 amendments per research currency warning."""
    assert "2020" in SingaporeStatute.PDPA_2012.value


def test_singapore_statute_includes_lpcr_2015():
    assert SingaporeStatute.LPCR_2015.value.startswith(
        "Legal Profession (Professional Conduct) Rules"
    )


def test_solicitors_accounts_rules_present():
    """Compliance gate per research file 44."""
    assert SingaporeStatute.SOLICITORS_ACCOUNTS_RULES.value.startswith(
        "Legal Profession (Solicitors' Accounts)"
    )


def test_lpcr_rule_8_publicity_firewall():
    assert "Rule 8" in SingaporeBarRule.RULE_8_PUBLICITY.value
    assert (
        "publicity" in SingaporeBarRule.RULE_8_PUBLICITY.value.lower()
        or "solicitation" in SingaporeBarRule.RULE_8_PUBLICITY.value.lower()
    )


def test_lpcr_rule_4_paramount_duty():
    assert "paramount duty" in SingaporeBarRule.RULE_4_PARAMOUNT_DUTY.value.lower()


def test_no_duplicate_matter_type_values():
    values = [m.value for m in MatterType]
    assert len(values) == len(set(values))


def test_no_duplicate_court_values():
    values = [c.value for c in SingaporeCourt]
    assert len(values) == len(set(values))


def test_no_duplicate_statute_values():
    values = [s.value for s in SingaporeStatute]
    assert len(values) == len(set(values))


def test_matter_dataclass_minimal():
    m = Matter(
        matter_id="OS-2026-1234",
        matter_type=MatterType.OS,
        court=SingaporeCourt.SC_HC_GD,
        short_title="Tan v Tan",
    )
    assert m.matter_id == "OS-2026-1234"
    assert m.next_hearing_date is None


def test_calendar_event_alias_summary():
    e = CalendarEvent(
        event_id="evt-001",
        matter_id="MAT-2026-042",
        summary_alias="MAT-2026-042 | hearing | State Courts CR-23",
        body_full="Tan v Tan · CFA arrears · contested",
        start_iso="2026-06-09T10:00:00+08:00",
        end_iso="2026-06-09T11:00:00+08:00",
        event_type="hearing",
    )
    assert "MAT-2026-042" in e.summary_alias
    assert "+08:00" in e.start_iso  # SGT timezone enforced
