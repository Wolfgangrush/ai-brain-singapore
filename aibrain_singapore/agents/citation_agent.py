"""citation_agent — wraps singapore_citation_validator MCP tool.
PROVENANCE: STRUCTURAL (delegates to MCP tool which has CITED provenance)."""


def handle(payload: str) -> dict:
    from aibrain_singapore.mcp_tools.citation_validator import singapore_citation_validator

    result = singapore_citation_validator(payload.strip())
    return {
        "agent": "citation_agent",
        "status": "v0.1 — citation validator wrapped",
        "result": result,
    }
