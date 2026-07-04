"""calendar_agent — wraps singapore_calendar_sync MCP tool.
PROVENANCE: STRUCTURAL (no domain claim) + ADR-002 D4 (ICS primary)."""

from ailawfirm_singapore.mcp_tools.calendar_sync import singapore_calendar_sync


def handle(payload: str) -> dict:
    """Pass payload to calendar sync tool.

    v0.1: assumes payload is a structured request like 'add hearing MAT-2026-042 ...'
    or 'show this week'. v0.2+: parses natural-language richly.
    """
    result = singapore_calendar_sync(payload.strip())
    return {
        "agent": "calendar_agent",
        "status": "v0.1 — calendar sync wrapped",
        "result": result,
    }
