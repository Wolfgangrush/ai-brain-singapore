"""compliance_agent — LPCR Rule 8 + PDPA + AML keyword firewall.
PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md, 04-statute-data-protection.md, 27-anti-money-laundering-obligations.md"""

from ailawfirm_singapore.core.ontology import SingaporeBarRule


def handle(payload: str) -> dict:
    p = payload.lower()
    flags = []
    if any(k in p for k in ["solicit", "advertis", "promot", "touting"]):
        flags.append(
            {
                "rule": SingaporeBarRule.RULE_8_PUBLICITY.value,
                "concern": "potential LPCR Rule 8 violation (publicity / solicitation / touting)",
                "research_ref": "10-bar-rule-publicity-solicitation.md",
            }
        )
    if "pdpa" in p or "personal data" in p or "data breach" in p:
        flags.append(
            {
                "rule": "PDPA 2012 (with 2020 Amendments)",
                "concern": "PDPA compliance — note 3-day breach notification window + S$1M/10% turnover penalty",
                "research_ref": "04-statute-data-protection.md",
            }
        )
    if "aml" in p or "kyc" in p or "money laundering" in p or "proliferation" in p:
        flags.append(
            {
                "rule": "AML obligations (with 2025 PF amendments)",
                "concern": "AML check needed — note 2025 Proliferation Financing amendments effective July 2025",
                "research_ref": "27-anti-money-laundering-obligations.md",
            }
        )
    if "client money" in p or "accounts" in p or "trust account" in p:
        flags.append(
            {
                "rule": SingaporeBarRule.SAR_CLIENT_MONEY.value,
                "concern": "Solicitors' Accounts Rules — compliance gate per research summary",
                "research_ref": "44-bar-rule-client-money.md",
            }
        )
    return {
        "agent": "compliance_agent",
        "status": "v0.1 — keyword firewall (Singapore-specific)",
        "flags": flags,
    }
