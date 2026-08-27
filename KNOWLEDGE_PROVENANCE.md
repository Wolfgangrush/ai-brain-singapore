# KNOWLEDGE_PROVENANCE — AI Brain · Singapore · Solo · v0.1

This file maps every domain claim in the codebase to its source. The CORPUS-AS-VERIFIER-NOT-SOURCE doctrine applies — every assertion traces to a specific research file.

## v0.1 corpus + drafting surfaces (added 2026-05-20)

- **Statute corpus** lives in [`_statute_corpus/`](_statute_corpus/) — 17 Tier-1 digests + [INDEX.md](_statute_corpus/INDEX.md) + [_STATUTE_CORPUS_SUMMARY.md](_statute_corpus/_STATUTE_CORPUS_SUMMARY.md). Each digest's first non-title line is its `PROVENANCE: CITED:_research/<file>.md` header. Topic-level depth in v0.1; section-text verbatim depth deferred per [BLOCKERS.md](BLOCKERS.md) B2.
- **Drafting scaffolds** live in [`examples/drafting/`](examples/drafting/) — 6 ROC 2021 templates + [README.md](examples/drafting/README.md). Each template's `PROVENANCE: CITED:_research/` header lists every research file the template draws on (court forms + civil procedure + citation format).
- **Audit ledger** at [AUDIT_v0.1.md](AUDIT_v0.1.md) records the §4 Pre-Ship Checklist outcomes line-by-line.
- **Firewall scan record** at [PII_SCAN_v0.1.md](PII_SCAN_v0.1.md) — the native `scripts/leak_check.py` is the authoritative runner; this file documents the v0.1 sweep.

## Provenance categories

- **CITED:<filename>** — backed by a specific file in `_research/` that the verifier can inspect. ALL Singapore domain claims use this.
- **STUB** — placeholder for v0.2+ where real content lands. Flag with `# PROVENANCE: STUB — fill in v0.2`.

(Note: Unlike the India build, Singapore does NOT permit `TRAINED` provenance. the publisher cannot verify Singapore law from memory; the research files are the verification surface.)

## v0.1 claim ledger

### Court hierarchy (in `aibrain_singapore/core/ontology.py` — `SingaporeCourt` enum)

| Claim | Provenance |
|---|---|
| Supreme Court of Singapore = Court of Appeal + General Division + Appellate Division | CITED:01-court-hierarchy.md |
| State Courts = District Court + Magistrates' Court + Coroner's Court + SCT | CITED:01-court-hierarchy.md |
| Family Justice Courts exist | CITED:01-court-hierarchy.md |
| Syariah Court (Muslim family law) | CITED:01-court-hierarchy.md |
| SICC (Singapore International Commercial Court) | CITED:01-court-hierarchy.md |
| District Court pecuniary jurisdiction S$60k - S$250k | CITED:01-court-hierarchy.md (CURRENCY WARNING — verify if amended) |
| Magistrates' Court pecuniary jurisdiction ≤ S$60k | CITED:01-court-hierarchy.md |

### Statute registry (in `core/ontology.py` — `SingaporeStatute` enum)

| Statute | Provenance |
|---|---|
| PDPA 2012 + 2020 Amendments (S$1M / 10% turnover penalty · 3-day breach notification) | CITED:04-statute-data-protection.md |
| Penal Code 1871 (revised) | CITED:07-statute-criminal-code.md |
| Criminal Procedure Code 2010 | CITED:03-court-rules-criminal.md |
| Evidence Act 1893 | CITED:08-statute-evidence-act.md |
| Companies Act 1967 | CITED:06-statute-company-law-overview.md |
| Legal Profession Act 1966 | CITED:39-legal-profession-act-overview.md |
| Legal Profession (Professional Conduct) Rules 2015 — Rule 8 firewall | CITED:10-bar-rule-publicity-solicitation.md |
| Rules of Court 2021 | CITED:02-court-rules-civil.md |
| Limitation Act | CITED:09-statute-limitation-act.md |
| Women's Charter 1961 (family law) | CITED:32-statute-family-law-overview.md (CURRENCY WARNING — DMA July 2024) |
| Employment Act | CITED:33-statute-employment-act.md |
| Insolvency Restructuring and Dissolution Act 2018 | CITED:40-statute-insolvency-restructuring.md |
| Copyright Act | CITED:43-statute-copyright-intellectual-property.md (CURRENCY WARNING — 2021 default-ownership shift for commissioned works) |
| Electronic Transactions Act | CITED:45-statute-electronic-transactions.md |

### Bar Rules

| Rule | Provenance |
|---|---|
| LPCR 2015 Rule 8 — publicity / solicitation firewall | CITED:10-bar-rule-publicity-solicitation.md |
| LPCR 2015 conflict-of-interest provisions | CITED:11-bar-rule-conflict-of-interest.md |
| LPCR 2015 confidentiality | CITED:12-bar-rule-confidentiality.md |
| LPCR Solicitors' Accounts Rules (client money) — compliance gate | CITED:44-bar-rule-client-money.md |
| LPCR fees/billing (contingency fee prohibition · CFA exception SICC) | CITED:38-bar-rule-fees-billing.md |

### Citation formats (in `mcp_tools/citation_validator.py`)

| Format | Example | Provenance |
|---|---|---|
| SLR | `[2023] 1 SLR 100` | CITED:13-citation-format-primary.md |
| SGCA | `[2024] SGCA 12` | CITED:13-citation-format-primary.md |
| SGHC | `[2024] SGHC 89` | CITED:13-citation-format-primary.md |
| MLJ (regional) | `[2023] 4 MLJ 567` | CITED:14-citation-format-secondary.md |

### Compliance (compliance_agent keyword set)

| Concern | Provenance |
|---|---|
| AML/KYC for solo firms (S$5K threshold + 2025 PF amendments) | CITED:27-anti-money-laundering-obligations.md (CURRENCY WARNING — PF July 2025) |
| PDPC breach notification 3-day window | CITED:04-statute-data-protection.md |
| October 2024 Judiciary AI Guidelines — disclosure mandate | CITED:23-ai-law-firm-regulatory-stance.md |
| Data localization / cross-border transfer (PDPA s26) | CITED:25-cross-border-data-transfer.md |

### Calendar / cause-list

| Claim | Provenance |
|---|---|
| Cause list structure + access patterns | CITED:15-cause-list-system.md |
| eLitigation system + SAPT compliance | CITED:16-e-filing-system.md |
| Solo advocate pain — admin overhead · cash flow · isolation | CITED:20-solo-advocate-pain-points.md (informs calendar UX) |

## Currency warnings (auto-flagged from research summary)

These changes are recent enough that any v0.2+ encoding MUST verify currentness:
1. **Family Law — Divorce by Mutual Agreement (DMA)** — July 2024 new ground · non-fault
2. **AML — Proliferation Financing** — 2025 amendments effective July 2025
3. **AI — Judiciary Guidelines** — October 2024 mandate (must flag generated content)
4. **Copyright** — 2021 default-ownership shift for commissioned works

## Known gaps (from research summary)

1. **Specific tribunal form numbers** for niche applications (e.g., stay of execution) — requires deep CJTS access
2. **Local bar customs / "mentions" protocol** — tacit knowledge, not on paper

These gaps are flagged in v0.1 with STATUS markers. v0.2+ planning will address.

## Verification protocol

Before any v0.1 → v0.2 transition, the publisher reviews this file. Items flagged CURRENCY WARNING are re-verified against current Singapore Statutes Online + Judiciary website. Items flagged STUB get filled with CITED content (often requires NEW Gemini research pass).

## What this file is NOT

- Not a comprehensive Singapore legal database — that's a downstream goal
- Not a substitute for a practitioner's own research — the tool MUST NOT be presented as a source of legal advice (LPCR Rule 8 firewall)
- Not a fixed document — every change in domain content updates this file in the same commit
