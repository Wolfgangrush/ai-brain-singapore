"""court_agent — wraps singapore_court_lookup MCP tool.
PROVENANCE: STRUCTURAL (delegates to MCP tool which has CITED provenance)."""


def handle(payload: str) -> dict:
    from aibrain_singapore.mcp_tools.court_lookup import singapore_court_lookup

    result = singapore_court_lookup(payload.strip())
    return {
        "agent": "court_agent",
        "status": "v0.1 — court lookup wrapped",
        "result": result,
    }
