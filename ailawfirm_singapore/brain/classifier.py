"""Rule-based intent detection — Singapore v0.1."""

from ailawfirm_singapore.brain.intents import Intent

_RULES: list[tuple[list[str], Intent]] = [
    (
        ["calendar", "schedule", "diary", "next week", "show today", "what's on", "agenda"],
        Intent.CALENDAR_QUERY,
    ),
    (
        ["add to calendar", "schedule for", "remind me", "set reminder", "block out"],
        Intent.CALENDAR_ADD,
    ),
    (["citation", "slr", "sgca", "sghc", "lawnet", "cite", "cited"], Intent.CITATION_LOOKUP),
    (
        [
            "court",
            "jurisdiction",
            "state courts",
            "supreme court",
            "high court",
            "district court",
            "sicc",
            "family justice",
            "syariah",
        ],
        Intent.COURT_QUERY,
    ),
    (
        ["draft", "drafting", "originating", "affidavit", "submissions", "pleadings"],
        Intent.DRAFTING_NEED,
    ),
    (
        ["deadline", "limitation", "time bar", "directions", "case management", "sapt"],
        Intent.DEADLINE_CHECK,
    ),
    (
        [
            "rule 8",
            "lpcr",
            "publicity",
            "solicit",
            "touting",
            "pdpa",
            "pdpc",
            "ethics",
            "aml",
            "kyc",
            "accounts rules",
        ],
        Intent.COMPLIANCE_FLAG,
    ),
    (["client", "client said", "client called", "client wants"], Intent.CLIENT_COMM),
    (["matter", "hearing", "order received", "argued", "filed"], Intent.MATTER_UPDATE),
]


def classify(text: str) -> Intent:
    if not isinstance(text, str) or not text.strip():
        return Intent.UNKNOWN
    t = text.lower()
    for keywords, intent in _RULES:
        if any(kw in t for kw in keywords):
            return intent
    return Intent.UNKNOWN
