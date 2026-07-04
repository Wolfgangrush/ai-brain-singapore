"""MCP server smoke test — Singapore v0.1."""

from ailawfirm_singapore.mcp_server import TOOLS, handle_request


def test_singapore_tools_registered():
    assert "singapore_court_lookup" in TOOLS
    assert "singapore_citation_validator" in TOOLS
    assert "singapore_calendar_sync" in TOOLS


def test_tools_list_returns_all_tools():
    req = {"method": "tools/list", "params": {}, "id": 1}
    resp = handle_request(req)
    tools = resp["result"]["tools"]
    tool_names = [t["name"] for t in tools]
    assert "singapore_court_lookup" in tool_names
    assert "singapore_citation_validator" in tool_names
    assert "singapore_calendar_sync" in tool_names


def test_court_lookup_tool_callable():
    req = {
        "method": "tools/call",
        "params": {"name": "singapore_court_lookup", "arguments": {"court_name": "Supreme Court"}},
        "id": 2,
    }
    resp = handle_request(req)
    assert "result" in resp
    assert "content" in resp["result"]
    import json

    data = json.loads(resp["result"]["content"][0]["text"])
    assert data["found"] is True


def test_citation_validator_tool_callable():
    req = {
        "method": "tools/call",
        "params": {
            "name": "singapore_citation_validator",
            "arguments": {"citation_string": "[2024] SGCA 12"},
        },
        "id": 3,
    }
    resp = handle_request(req)
    assert "result" in resp
    import json

    data = json.loads(resp["result"]["content"][0]["text"])
    assert data["valid"] is True
    assert data["format"] == "SGCA"


def test_calendar_sync_tool_callable():
    # Clear first
    req = {
        "method": "tools/call",
        "params": {"name": "singapore_calendar_sync", "arguments": {"payload": "clear"}},
        "id": 4,
    }
    resp = handle_request(req)
    assert "result" in resp


def test_unknown_tool_still_errors():
    req = {
        "method": "tools/call",
        "params": {"name": "nonexistent_tool", "arguments": {}},
        "id": 99,
    }
    resp = handle_request(req)
    assert "error" in resp
