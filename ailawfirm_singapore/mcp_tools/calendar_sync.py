"""
singapore_calendar_sync MCP tool — v0.1.

Writes the current matter calendar to an .ics file and publishes it.
PROVENANCE: STRUCTURAL + ADR-002 D4-D7.
"""

from ailawfirm_singapore.core.calendar import publishers
from ailawfirm_singapore.core.calendar.ics_writer import write_ics
from ailawfirm_singapore.core.ontology import CalendarEvent


# v0.1 stub: in-memory event store. v0.2+: persistent matter store integration.
_EVENT_STORE: list[CalendarEvent] = []


def singapore_calendar_sync(payload: str) -> dict:
    """Calendar sync MCP entry point.

    v0.1 commands (whitespace-tolerant):
        "sync" / "publish"  -> write all events to .ics + publish
        "add <event_id>|<matter_id>|<summary_alias>|<body>|<start_iso>|<end_iso>|<location>|<type>"
                            -> register an event in the in-memory store
        "list"              -> list events currently in store
        "clear"             -> reset event store (v0.1 dev convenience)
    """
    if not isinstance(payload, str):
        return {"ok": False, "error": "payload must be a string"}

    p = payload.strip().lower()

    if p in ("sync", "publish", ""):
        return _do_sync()
    if p.startswith("add"):
        return _do_add(payload.strip())
    if p == "list":
        return {
            "ok": True,
            "events": [
                {"id": e.event_id, "summary": e.summary_alias, "start": e.start_iso}
                for e in _EVENT_STORE
            ],
        }
    if p == "clear":
        _EVENT_STORE.clear()
        return {"ok": True, "note": "event store cleared"}

    return {"ok": False, "error": f"unknown command: {payload[:40]}"}


def _do_sync() -> dict:
    out = publishers.default_local_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    w = write_ics(_EVENT_STORE, out)
    if not w["ok"]:
        return w
    pub = publishers.publish_local(out)
    return {
        "ok": True,
        "wrote_path": w["path"],
        "event_count": w["event_count"],
        "publish": pub,
        "subscribe_via": pub["subscribe_url"],
    }


def _do_add(payload: str) -> dict:
    """Parse 'add <event_id>::<matter_id>::<summary>::<body>::<start>::<end>[::<location>][::<type>]'"""
    body = payload[3:].strip()
    parts = body.split("::")
    if len(parts) < 6:
        return {
            "ok": False,
            "error": "add requires at least 6 ::-separated fields: "
            "event_id::matter_id::summary_alias::body_full::start_iso::end_iso[::location][::type]",
        }
    e = CalendarEvent(
        event_id=parts[0].strip(),
        matter_id=parts[1].strip() or None,
        summary_alias=parts[2].strip(),
        body_full=parts[3].strip(),
        start_iso=parts[4].strip(),
        end_iso=parts[5].strip(),
        location=parts[6].strip() if len(parts) > 6 else None,
        event_type=parts[7].strip() if len(parts) > 7 else "hearing",
    )
    _EVENT_STORE.append(e)
    return {"ok": True, "added": e.event_id, "store_size": len(_EVENT_STORE)}
