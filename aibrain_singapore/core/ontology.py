"""
Ontology module — AI Brain · Singapore · Solo · v0.1

Singapore legal-practice enums. All values traced to _research/ files
per KNOWLEDGE_PROVENANCE.md.

PROVENANCE: CITED:_research/01-court-hierarchy.md for SingaporeCourt
PROVENANCE: CITED:_research/(multiple statute files) for SingaporeStatute
PROVENANCE: CITED:_research/10-bar-rule-publicity-solicitation.md for SingaporeBarRule
PROVENANCE: CITED:_research/02-court-rules-civil.md for MatterType (ROC 2021 process names)
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class MatterType(Enum):
    """Singapore matter type codes — non-exhaustive v0.1 set.
    PROVENANCE: CITED:02-court-rules-civil.md (ROC 2021 process reform)"""

    OS = "Originating Summons"
    OC = "Originating Claim"  # post-2022 ROC reform
    OA = "Originating Application"
    DC_CIVIL = "District Court Civil Suit"
    MC_CIVIL = "Magistrate's Court Civil Suit"
    SCT_CLAIM = "Small Claims Tribunal claim"
    CRIM_CASE = "Criminal Case"
    MA = "Magistrate's Appeal"
    HC_APPEAL = "High Court Appeal"
    CA_APPEAL = "Court of Appeal Appeal"
    JR = "Judicial Review"
    SIAC_ARB = "Singapore International Arbitration (SIAC)"
    SIMC_MED = "Singapore International Mediation (SIMC)"
    SICC_CASE = "Singapore International Commercial Court case"
    FAMILY_DMA = "Divorce by Mutual Agreement (post-2024)"
    FAMILY_CONTESTED = "Contested Family Proceeding"
    SYARIAH_CASE = "Syariah Court matter"
    OTHER = "Other (specify in description)"


class SingaporeCourt(Enum):
    """Singapore court hierarchy.
    PROVENANCE: CITED:01-court-hierarchy.md"""

    SC_CA = "Supreme Court — Court of Appeal"
    SC_HC_GD = "Supreme Court — High Court General Division"
    SC_HC_AD = "Supreme Court — High Court Appellate Division"
    SICC = "Singapore International Commercial Court"
    STATE_DC = "State Courts — District Court"
    STATE_MC = "State Courts — Magistrates' Court"
    STATE_CT = "State Courts — Coroner's Court"
    SCT = "Small Claims Tribunal"
    ECT = "Employment Claims Tribunal"
    FAMILY_JC = "Family Justice Courts"
    SYARIAH = "Syariah Court"
    OTHER = "Other (specify)"


class SingaporeStatute(Enum):
    """Singapore statute registry — v0.1 references only.
    Real text deferred to v0.2+. PROVENANCE: see KNOWLEDGE_PROVENANCE.md."""

    PDPA_2012 = "Personal Data Protection Act 2012 (as amended 2020)"
    PENAL_CODE_1871 = "Penal Code 1871 (revised)"
    CPC_2010 = "Criminal Procedure Code 2010"
    EVIDENCE_ACT_1893 = "Evidence Act 1893"
    COMPANIES_ACT_1967 = "Companies Act 1967"
    LEGAL_PROFESSION_ACT_1966 = "Legal Profession Act 1966"
    LPCR_2015 = "Legal Profession (Professional Conduct) Rules 2015"
    SOLICITORS_ACCOUNTS_RULES = "Legal Profession (Solicitors' Accounts) Rules"
    ROC_2021 = "Rules of Court 2021"
    LIMITATION_ACT = "Limitation Act"
    WOMENS_CHARTER_1961 = "Women's Charter 1961 (family law)"
    EMPLOYMENT_ACT = "Employment Act"
    INSOLVENCY_2018 = "Insolvency Restructuring and Dissolution Act 2018"
    COPYRIGHT_ACT = "Copyright Act (note: 2021 default-ownership shift for commissioned works)"
    ELECTRONIC_TXN_ACT = "Electronic Transactions Act"
    SFA_2001 = "Securities and Futures Act 2001"
    BANKING_ACT_1970 = "Banking Act 1970"
    MENTAL_CAPACITY_ACT = "Mental Capacity Act"


class SingaporeBarRule(Enum):
    """LPCR 2015 rule references.
    PROVENANCE: CITED:10-bar-rule-publicity-solicitation.md
                CITED:11-bar-rule-conflict-of-interest.md
                CITED:12-bar-rule-confidentiality.md
                CITED:44-bar-rule-client-money.md"""

    RULE_4_PARAMOUNT_DUTY = "LPCR 2015 Rule 4 — paramount duty to the Court"
    RULE_8_PUBLICITY = (
        "LPCR 2015 Rule 8 (Part 5) — restrictions on publicity, solicitation, and touting"
    )
    RULE_44_NO_MISLEADING_PUBLICITY = "LPCR 2015 Rule 44 — no false/misleading/deceptive publicity"
    RULE_45_NO_VULGAR_SENSATIONAL = "LPCR 2015 Rule 45 — no vulgar/sensational publicity"
    RULE_47_NO_TOUTING = "LPCR 2015 Rule 47 — no unfair attraction of business"
    RULE_20_22_CONFLICT = "LPCR 2015 Rules 20-22 — conflict of interest"
    RULE_19_CONFIDENTIALITY = "LPCR 2015 Rule 19 — confidentiality"
    SAR_CLIENT_MONEY = "Solicitors' Accounts Rules — client money handling (compliance gate)"


@dataclass
class Matter:
    """A single matter (case file) — v0.1 shape only.
    PROVENANCE: STUB — full lifecycle in v0.2+"""

    matter_id: str
    matter_type: MatterType
    court: SingaporeCourt
    short_title: str
    parties_plaintiff: list[str] = field(default_factory=list)
    parties_defendant: list[str] = field(default_factory=list)
    statutes_invoked: list[SingaporeStatute] = field(default_factory=list)
    filed_date: Optional[str] = None  # ISO YYYY-MM-DD
    next_hearing_date: Optional[str] = None  # used by calendar_agent
    next_hearing_location: Optional[str] = None
    status_note: Optional[str] = None


@dataclass
class Citation:
    """A parsed Singapore legal citation."""

    raw: str
    format: str  # 'SLR' | 'SGCA' | 'SGHC' | 'MLJ' | 'UNKNOWN'
    year: Optional[int] = None
    volume_or_court: Optional[str] = None
    page_or_serial: Optional[int] = None
    valid: bool = False
    parse_notes: Optional[str] = None


@dataclass
class CalendarEvent:
    """A calendar event written to the ICS feed by calendar_agent.
    PROVENANCE: STRUCTURAL (no domain claim) + ADR-002 D7 (alias summary discipline)."""

    event_id: str
    matter_id: Optional[str] = None
    summary_alias: str = ""  # lock-screen safe: "MAT-2026-042 | hearing | State Courts CR-23"
    body_full: str = ""  # hidden until tapped: full matter detail
    start_iso: str = ""  # YYYY-MM-DDTHH:MM:SS+08:00 (SGT)
    end_iso: str = ""  # YYYY-MM-DDTHH:MM:SS+08:00
    location: Optional[str] = None
    event_type: str = "hearing"  # hearing | deadline | reminder | client_meeting
