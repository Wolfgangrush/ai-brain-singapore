"""
ICS writer — generates RFC 5545 iCalendar file from CalendarEvents.

Per ADR-002 D4: ICS feed is the primary calendar integration (local-first).
Per ADR-002 D7: SUMMARY field uses entity-aliasing code; full detail goes to DESCRIPTION.

PROVENANCE: STRUCTURAL (no Singapore-specific domain claim — ICS is RFC 5545).
"""

from typing import Iterable
from datetime import datetime
from pathlib import Path

try:
    from icalendar import Calendar, Event
    from icalendar.prop import vText
except ImportError:
    Calendar = None  # graceful fallback if icalendar not installed yet

from aibrain_singapore.core.ontology import CalendarEvent


def write_ics(events: Iterable[CalendarEvent], output_path: Path) -> dict:
    """Write a list of CalendarEvent to an RFC 5545 .ics file.

    Args:
        events: iterable of CalendarEvent
        output_path: where to write the .ics file

    Returns:
        dict {"ok": bool, "path": str, "event_count": int, "error": Optional[str]}
    """
    if Calendar is None:
        return {"ok": False, "error": "icalendar library not installed — run pip install icalendar"}

    cal = Calendar()
    cal.add("prodid", "-//wolfgang_rush//AI Brain Singapore Solo v0.1//EN")
    cal.add("version", "2.0")
    cal.add("x-wr-calname", "AI Brain — Singapore (matters)")
    cal.add("x-wr-timezone", "Asia/Singapore")

    count = 0
    for e in events:
        ev = Event()
        ev.add("uid", e.event_id)
        ev.add("summary", vText(e.summary_alias))  # entity-aliasing code only (lock-screen safe)
        if e.body_full:
            ev.add("description", vText(e.body_full))  # full detail (hidden until tap)
        try:
            ev.add("dtstart", datetime.fromisoformat(e.start_iso))
            ev.add("dtend", datetime.fromisoformat(e.end_iso))
        except (ValueError, TypeError):
            continue  # skip events with bad timestamps
        if e.location:
            ev.add("location", vText(e.location))
        ev.add("categories", e.event_type)
        cal.add_component(ev)
        count += 1

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(cal.to_ical())
        return {"ok": True, "path": str(output_path), "event_count": count}
    except Exception as ex:
        return {"ok": False, "error": f"write failed: {ex}"}
