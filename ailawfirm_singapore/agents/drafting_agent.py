"""drafting_agent — Singapore document-type router (ROC 2021).

Keyword-classifies a drafting request into a Singapore document type
and points at the local Singapore template + the draft-with-docx skill.
It does NOT generate the draft — it classifies + points.
"""
import re


def _classify(text: str):
    """Return (doc_type, suggested_skill). First keyword match wins."""
    t = text.lower()
    if re.search(r"\boriginating\s+claim\b|\boc\b", t):
        return (
            "Originating Claim (ROC 2021 O.6)",
            "draft-with-docx (examples/drafting/originating-claim.md)",
        )
    if re.search(r"\boriginating\s+application\b|\boa\b", t):
        return (
            "Originating Application (ROC 2021 O.6)",
            "draft-with-docx (examples/drafting/originating-application.md)",
        )
    if re.search(r"\bdefence\b|\bcounterclaim\b", t):
        return (
            "Defence / Counterclaim",
            "draft-with-docx (examples/drafting/defence.md)",
        )
    if re.search(r"\bstatement\s+of\s+claim\b|\bsoc\b", t):
        return (
            "Statement of Claim",
            "draft-with-docx (examples/drafting/statement-of-claim.md)",
        )
    if re.search(r"\breply\b", t):
        return (
            "Reply",
            "draft-with-docx (examples/drafting/reply.md)",
        )
    if re.search(r"\baffidavit\b", t):
        return (
            "Supporting Affidavit",
            "draft-with-docx (examples/drafting/affidavit.md)",
        )
    if re.search(r"\bwritten\s+submission\b|\bbundle\b", t):
        return ("Court materials", "draft-with-docx")
    return ("General pleading (confirm doc type)", "draft-with-docx")


def handle(payload: str) -> dict:
    text = payload or ""
    doc_type, suggested_skill = _classify(text)
    return {
        "agent": "drafting_agent",
        "status": "ok",
        "doc_type": doc_type,
        "suggested_skill": suggested_skill,
        "next_step": (
            "Invoke draft-with-docx with the case folder; verify the prescribed "
            "Form against the current ROC 2021 Practice Direction."
        ),
        "note": (
            "Singapore ROC 2021 pleading classification. Confirm the precise Form "
            "number against the current ROC 2021 Practice Direction before filing."
        ),
    }
