"""
singapore_court_lookup MCP tool — v0.1.

Resolves court name (fuzzy) to structured court info.
PROVENANCE: CITED:_research/01-court-hierarchy.md
PROVENANCE: STUB for pecuniary_limit precision (verify against CURRENT SSO before quoting in client work)
"""

from typing import Optional
from aibrain_singapore.core.ontology import SingaporeCourt


_COURT_INFO: dict[SingaporeCourt, dict] = {
    SingaporeCourt.SC_CA: {
        "name": "Court of Appeal of Singapore",
        "location": "Supreme Court Building, 1 Supreme Court Lane",
        "tier": "apex",
        "jurisdiction_class": "final appellate (criminal + civil)",
        "procedural_code": "Rules of Court 2021",
        "pecuniary_limit": None,
        "research_ref": "01-court-hierarchy.md",
    },
    SingaporeCourt.SC_HC_GD: {
        "name": "Singapore High Court — General Division",
        "location": "Supreme Court Building",
        "tier": "superior",
        "jurisdiction_class": "original civil typically >= S$250k · criminal capital · admiralty · IP · etc.",
        "procedural_code": "Rules of Court 2021",
        "pecuniary_limit": "typically >= S$250,000 · CURRENCY-VERIFY",
        "research_ref": "01-court-hierarchy.md",
    },
    SingaporeCourt.SC_HC_AD: {
        "name": "Singapore High Court — Appellate Division",
        "location": "Supreme Court Building",
        "tier": "intermediate_appellate",
        "jurisdiction_class": "civil appeals from General Division + State Courts (per ROC schedule)",
        "procedural_code": "Rules of Court 2021",
        "pecuniary_limit": None,
        "research_ref": "01-court-hierarchy.md",
    },
    SingaporeCourt.SICC: {
        "name": "Singapore International Commercial Court",
        "location": "Supreme Court Building",
        "tier": "specialised_international",
        "jurisdiction_class": "international commercial · CFA permitted (LPA s107 exception)",
        "procedural_code": "Rules of Court 2021 + SICC PD",
        "pecuniary_limit": None,
        "research_ref": "01-court-hierarchy.md",
    },
    SingaporeCourt.STATE_DC: {
        "name": "State Courts — District Court",
        "location": "State Courts, 1 Havelock Square",
        "tier": "district",
        "jurisdiction_class": "civil S$60k-S$250k · most criminal · family pre-FJC",
        "procedural_code": "Rules of Court 2021 + Criminal Procedure Code 2010",
        "pecuniary_limit": "S$60,000 – S$250,000 · CURRENCY-VERIFY",
        "research_ref": "01-court-hierarchy.md",
    },
    SingaporeCourt.STATE_MC: {
        "name": "State Courts — Magistrates' Court",
        "location": "State Courts",
        "tier": "magistrate",
        "jurisdiction_class": "civil <= S$60k · minor criminal",
        "procedural_code": "Rules of Court 2021 + CPC 2010",
        "pecuniary_limit": "<= S$60,000",
        "research_ref": "01-court-hierarchy.md",
    },
}


def _fuzzy_match(query: str) -> Optional[SingaporeCourt]:
    q = query.lower().strip()
    if not q:
        return None
    for court in SingaporeCourt:
        if q in court.value.lower():
            return court
    return None


def singapore_court_lookup(court_name: str) -> dict:
    if not isinstance(court_name, str):
        return {"found": False, "error": "court_name must be a string"}
    matched = _fuzzy_match(court_name)
    if matched is None or matched not in _COURT_INFO:
        return {"found": False, "query": court_name}
    info = dict(_COURT_INFO[matched])
    info["matched_enum"] = matched.name
    info["found"] = True
    return info
