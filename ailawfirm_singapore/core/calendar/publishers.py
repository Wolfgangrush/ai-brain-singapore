"""
Calendar publishers — where to drop the .ics file.

v0.1 supports 'local' (default ~/.ailawfirm-singapore/calendar.ics).
v0.2+ adds 'icloud_drive', 'dropbox', 'local_http_server'.

PROVENANCE: STRUCTURAL.
"""

from pathlib import Path


def default_local_path() -> Path:
    """Default local publish path. iPhone Calendar can subscribe via file:// URL
    or via a local HTTP server pointed at this file."""
    return Path.home() / ".ailawfirm-singapore" / "calendar.ics"


def publish_local(ics_path: Path, target_path: Path = None) -> dict:
    """Copy/move the .ics to its publish location (default = same as write)."""
    target = target_path or default_local_path()
    if ics_path != target:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(ics_path.read_bytes())
    return {
        "ok": True,
        "publish_path": str(target),
        "subscribe_url": f"file://{target}",
        "note": "Subscribe in iPhone Calendar via Add Calendar -> Add Subscription Calendar -> paste path",
    }
