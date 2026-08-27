"""deadline_agent — Singapore Limitation Act 1959 calculator.

Keyword-classifies a claim, applies the relevant limitation period, and
(if a date is found in the payload) computes deadline + days_remaining.

House convention: a year is approximated as 365 days.
"""

import datetime
import re

# Date patterns: DD-MM-YYYY, DD/MM/YYYY, YYYY-MM-DD,
# "12 January 2020", "January 12 2020".
_DATE_PATTERNS = [
    re.compile(r"\b(\d{1,2})[-/](\d{1,2})[-/](\d{4})\b"),  # DD-MM-YYYY or DD/MM/YYYY
    re.compile(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b"),  # YYYY-MM-DD
    re.compile(
        r"\b(\d{1,2})\s+(January|February|March|April|May|June|"
        r"July|August|September|October|November|December)\s+(\d{4})\b",
        re.I,
    ),
    re.compile(
        r"\b(January|February|March|April|May|June|"
        r"July|August|September|October|November|December)\s+(\d{1,2})\s+(\d{4})\b",
        re.I,
    ),
]

_MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

_NOTE = (
    "AI-generated period. Limitation must be specially pleaded (s 4). "
    "Acknowledgement/part-payment (ss 26-27) or fraud/concealment (s 29) "
    "can alter time. Verify against the Limitation Act 1959 before relying."
)


def _extract_date(text: str):
    """Return a datetime.date if a recognisable date appears in *text*, else None."""
    m = _DATE_PATTERNS[0].search(text)
    if m:
        try:
            return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            pass
    m = _DATE_PATTERNS[1].search(text)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    m = _DATE_PATTERNS[2].search(text)
    if m:
        mo = _MONTHS.get(m.group(2).lower())
        if mo:
            try:
                return datetime.date(int(m.group(3)), mo, int(m.group(1)))
            except ValueError:
                pass
    m = _DATE_PATTERNS[3].search(text)
    if m:
        mo = _MONTHS.get(m.group(1).lower())
        if mo:
            try:
                return datetime.date(int(m.group(3)), mo, int(m.group(2)))
            except ValueError:
                pass
    return None


def _classify(text: str):
    """Return (category, period_days, article) — first keyword match wins."""
    t = text.lower()
    if re.search(r"\brecover[a-z]*\s+land\b|\bland\b|\bimmovable\b|\bpossession\b", t):
        return ("Recovery of land", 12 * 365, "s 9 Limitation Act 1959")
    if re.search(r"\benforce[a-z]*\s+judgment\b|\bjudgment\s+debt\b|\bexecution\b", t):
        return ("Enforcement of judgment", 12 * 365, "s 6(3) Limitation Act 1959")
    if re.search(r"\bpersonal\s+injur|\bnegligence\b.*\binjur|\baccident\b", t):
        return (
            "Personal injury / latent damage",
            3 * 365,
            "s 24A Limitation Act 1959 (long-stop 15y s 24B)",
        )
    if re.search(
        r"\bcontract\b|\bbreach\b|\bdebt\b|\bloan\b|\brecover[a-z]*\s+(money|amount)",
        t,
    ):
        return ("Contract", 6 * 365, "s 6(1)(a) Limitation Act 1959")
    if re.search(r"\btort\b|\bnegligence\b|\bnuisance\b|\btrespass\b|\bdamage\b", t):
        return ("Tort", 6 * 365, "s 6(1)(a) Limitation Act 1959")
    return ("General / residuary", 6 * 365, "s 6 Limitation Act 1959")


def handle(payload: str) -> dict:
    text = payload or ""
    category, period_days, article = _classify(text)
    start = _extract_date(text)
    if start is not None:
        deadline = start + datetime.timedelta(days=period_days)
        days_remaining = (deadline - datetime.date.today()).days
    else:
        deadline = None
        days_remaining = None
    years = period_days // 365
    return {
        "agent": "deadline_agent",
        "status": "ok",
        "category": category,
        "article": article,
        "period": f"{years} year{'s' if years != 1 else ''}",
        "start_date": start.isoformat() if start else None,
        "deadline": deadline.isoformat() if deadline else None,
        "days_remaining": days_remaining,
        "note": _NOTE,
    }
