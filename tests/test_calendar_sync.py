"""Calendar sync tests — Singapore v0.1."""

from aibrain_singapore.mcp_tools.calendar_sync import singapore_calendar_sync


def test_add_event_then_sync(tmp_path, monkeypatch):
    from aibrain_singapore.core.calendar import publishers

    monkeypatch.setattr(publishers, "default_local_path", lambda: tmp_path / "calendar.ics")

    singapore_calendar_sync("clear")

    r = singapore_calendar_sync(
        "add evt-001::MAT-2026-042::MAT-2026-042 | hearing | State Courts CR-23::"
        "Tan v Tan - CFA arrears::2026-06-09T10:00:00+08:00::2026-06-09T11:00:00+08:00::"
        "State Courts CR-23::hearing"
    )
    assert r["ok"] is True
    assert r["added"] == "evt-001"

    s = singapore_calendar_sync("sync")
    assert s["ok"] is True
    assert s["event_count"] == 1
    assert (tmp_path / "calendar.ics").exists()
    content = (tmp_path / "calendar.ics").read_bytes().decode()
    assert "BEGIN:VCALENDAR" in content
    assert "BEGIN:VEVENT" in content
    assert "MAT-2026-042" in content  # entity-aliasing summary present
    assert "Tan v Tan" in content  # body in DESCRIPTION


def test_list_events():
    singapore_calendar_sync("clear")
    singapore_calendar_sync(
        "add evt-002::MAT-2026-043::MAT-2026-043 | deadline | PDPA 3-day::"
        "client.045 breach notification::2026-06-10T17:00:00+08:00::2026-06-10T17:30:00+08:00::deadline"
    )
    r = singapore_calendar_sync("list")
    assert r["ok"] is True
    assert len(r["events"]) == 1
    assert r["events"][0]["id"] == "evt-002"


def test_alias_summary_no_real_name():
    """ADR-002 D7: SUMMARY must not contain plaintext names of clients."""
    singapore_calendar_sync("clear")
    r = singapore_calendar_sync(
        "add evt-003::MAT-2026-099::MAT-2026-099 | client meeting | Office::"
        "John Tan (plaintiff) discussing settlement::2026-06-15T14:00:00+08:00::"
        "2026-06-15T15:00:00+08:00::Office::client_meeting"
    )
    assert r["ok"] is True


def test_invalid_add_payload():
    r = singapore_calendar_sync("add not-enough-fields")
    assert r["ok"] is False
    assert "at least 6" in r["error"]


def test_unknown_command():
    r = singapore_calendar_sync("xyzzy")
    assert r["ok"] is False
