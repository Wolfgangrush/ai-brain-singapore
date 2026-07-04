"""
singapore_citation_validator MCP tool — v0.1.

Validates and parses Singapore legal citations: SLR · SGCA · SGHC.
PROVENANCE: CITED:_research/13-citation-format-primary.md (SLR · SGCA · SGHC)
PROVENANCE: CITED:_research/14-citation-format-secondary.md (MLJ regional)
"""

import re
from ailawfirm_singapore.core.ontology import Citation


_SLR_PATTERN = re.compile(r"^\[(?P<year>\d{4})\]\s+(?P<volume>\d+)\s+SLR\s+(?P<page>\d+)$")
_SGCA_PATTERN = re.compile(r"^\[(?P<year>\d{4})\]\s+SGCA\s+(?P<serial>\d+)$")
_SGHC_PATTERN = re.compile(r"^\[(?P<year>\d{4})\]\s+SGHC\s+(?P<serial>\d+)$")
_MLJ_PATTERN = re.compile(r"^\[(?P<year>\d{4})\]\s+(?P<volume>\d+)\s+MLJ\s+(?P<page>\d+)$")


def singapore_citation_validator(citation_string: str) -> dict:
    if not isinstance(citation_string, str):
        return _to_dict(
            Citation(
                raw=str(citation_string), format="UNKNOWN", parse_notes="input was not a string"
            )
        )

    s = citation_string.strip()

    m = _SLR_PATTERN.match(s)
    if m:
        return _to_dict(
            Citation(
                raw=s,
                format="SLR",
                year=int(m.group("year")),
                volume_or_court=m.group("volume"),
                page_or_serial=int(m.group("page")),
                valid=True,
            )
        )

    m = _SGCA_PATTERN.match(s)
    if m:
        return _to_dict(
            Citation(
                raw=s,
                format="SGCA",
                year=int(m.group("year")),
                volume_or_court="SGCA",
                page_or_serial=int(m.group("serial")),
                valid=True,
            )
        )

    m = _SGHC_PATTERN.match(s)
    if m:
        return _to_dict(
            Citation(
                raw=s,
                format="SGHC",
                year=int(m.group("year")),
                volume_or_court="SGHC",
                page_or_serial=int(m.group("serial")),
                valid=True,
            )
        )

    m = _MLJ_PATTERN.match(s)
    if m:
        return _to_dict(
            Citation(
                raw=s,
                format="MLJ",
                year=int(m.group("year")),
                volume_or_court=m.group("volume"),
                page_or_serial=int(m.group("page")),
                valid=True,
            )
        )

    return _to_dict(
        Citation(raw=s, format="UNKNOWN", valid=False, parse_notes="no SLR/SGCA/SGHC/MLJ match")
    )


def _to_dict(c: Citation) -> dict:
    return {
        "raw": c.raw,
        "format": c.format,
        "year": c.year,
        "court_or_reporter": c.volume_or_court,
        "page_or_serial": c.page_or_serial,
        "valid": c.valid,
        "parse_notes": c.parse_notes,
    }
