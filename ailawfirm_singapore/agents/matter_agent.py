"""matter_agent — local matter tracker (Singapore paths).

Stores matters at ~/.ailawfirm_singapore/matters.json. The module-level
_STORE_PATH is a pathlib.Path so tests can monkeypatch it to a temp file.
Pure stdlib; nothing leaves the machine.
"""
import datetime
import json
import os
import pathlib
import re

_STORE_PATH = pathlib.Path(
    os.path.expanduser("~/.ailawfirm_singapore/matters.json")
)


def _load():
    """Load the store. Never raises on a corrupt/missing store."""
    try:
        if _STORE_PATH.exists():
            with open(_STORE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and isinstance(data.get("matters"), list):
                    return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"matters": []}


def _save(data):
    """Persist the store. Swallows OS errors so handle() never raises."""
    try:
        _STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(_STORE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass


def handle(payload: str) -> dict:
    text = (payload or "").strip()
    data = _load()
    matters = data.get("matters", [])

    m = re.match(r"(?i)^(?:add|new)\s+matter\s+(.+)$", text)
    if m:
        name = m.group(1).strip()
        updated = datetime.datetime.now(datetime.timezone.utc).isoformat()
        existing = next(
            (x for x in matters if isinstance(x, dict) and x.get("name") == name),
            None,
        )
        if existing is not None:
            existing["updated"] = updated
            saved = existing
        else:
            saved = {"name": name, "note": "", "updated": updated}
            matters.append(saved)
        data["matters"] = matters
        _save(data)
        return {
            "agent": "matter_agent",
            "status": "ok",
            "action": "added",
            "matter": saved,
            "matters": matters,
        }

    if re.match(r"(?i)^(?:list|show|my)\s+matters$", text):
        return {
            "agent": "matter_agent",
            "status": "ok",
            "action": "list",
            "matters": matters,
        }

    m = re.match(r"(?i)^(?:status\s+of|about|matter)\s+(.+)$", text)
    if m:
        name = m.group(1).strip()
        found = next(
            (x for x in matters if isinstance(x, dict) and x.get("name") == name),
            None,
        )
        if found is not None:
            return {
                "agent": "matter_agent",
                "status": "ok",
                "action": "lookup",
                "matter": found,
                "matters": matters,
            }
        return {
            "agent": "matter_agent",
            "status": "not_found",
            "action": "lookup",
            "matter": {"name": name},
            "matters": matters,
        }

    return {"agent": "matter_agent", "status": "ok", "matters": matters}
