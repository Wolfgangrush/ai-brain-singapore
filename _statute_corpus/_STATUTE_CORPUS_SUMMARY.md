# Statute Corpus Summary — Singapore

PROVENANCE: CITED:_research/_RESEARCH_SUMMARY.md (aggregate — individual statute provenance is cited per-digest in s01..s17)

## Date: 2026-05-20
## Statutes digested: 17 (Tier 1)
## Tier 1 coverage: 17/17 (mandatory set complete for v0.1)
## Tier 2 coverage: 0/9 (deferred to v0.2)
## Tier 3 coverage: 0 (deferred)

## Authoritative sources used
- **Singapore Statutes Online (sso.agc.gov.sg)** — primary substrate for every digest (PDPA, Contract Acts, CA 1967, PC 1871, EA 1893, LA 1959, LPA 1966, PAA 1934, Wills Act 1838, WC 1961, EA 1968, LTA 1993, CLPA 1886, IRDA 2018, MCA 2008, CPFTA 2003, CA 2021, ETA 2010).
- **Personal Data Protection Commission (pdpc.gov.sg)** — PDPA Advisory Guidelines and Notifiable Data Breach guidance.
- **Singapore Judiciary (judiciary.gov.sg)** — ROC 2021 court forms (OC / OA), AI in Courts Guidelines (October 2024), e-Litigation procedural notes.
- **Singapore Land Authority (sla.gov.sg)** — Torrens system + caveat practice.
- **Office of the Public Guardian (opg.gov.sg)** — LPA Form 1 + Certificate Issuer guidance.
- **Competition and Consumer Commission of Singapore (cccs.gov.sg)** — CPFTA enforcement.
- **Law Society of Singapore (lawsociety.org.sg)** — Practice Directions + Professional Conduct Rules 2015 references for LPA digest cross-reference.
- **Legal Services Regulatory Authority (lsra.gov.sg)** — law-practice licensing context for LPA Part 9A.
- **Singapore Academy of Law (sal.org.sg)** — Style Guide 2021 + citation conventions (cross-reference for examples/).

## Sources tried but rejected
- Major firm "thought leadership" pages (used only as discovery aids — every claim was traced back to SSO or the regulator before encoding).
- Pre-ROC-2021 procedural commentary (rejected in favour of the 2021 Rules; pre-2022 "Writ of Summons" mechanics are out-of-scope for v0.1).
- Commentary on the pre-2021 Copyright Act (the 2021 Act materially changed default ownership; pre-2021 framing rejected).

## Sections / topics covered per statute
v0.1 digests are **topic-level** (key facts + verbatim anchor quote per statute) rather than section-by-section. This is deliberate: the corpus is a **navigational substrate** for solo advocates, not a replacement for SSO. Each digest names the operative sections to enable downstream code paths and human verification on SSO.

Section-by-section depth (Australian-pattern coverage) is planned for v0.2 on the statutes most-queried in practice (likely PDPA, ROC, LPA, MCA).

## Currency warnings to surface
- **Family Law:** DMA (Divorce by Mutual Agreement) effective July 2024 — non-fault path.
- **AML/CFT:** 2025 Proliferation Financing amendments effective July 2025.
- **AI in courts:** Judiciary AI Guidelines (October 2024) mandatory; tool surfaces must caption AI-generated content.
- **Copyright Act 2021:** default ownership of commissioned works shifted to the creator (vs 1987 Act position).
- **ROC 2021:** OC / OA replaced Writ / Originating Summons from 1 April 2022.
- **Penal Code:** 2019/2020 reforms substantially modernised sexual-offence and computer-crime provisions. Pre-reform caselaw on "consent" / "hurt" must be checked against current wording.
- **PDPA:** 2020 amendments introduced mandatory data-breach notification + raised the financial-penalty ceiling.
- **Employment Act:** 2019 amendments extended coverage to all PMEs regardless of salary band.

## Known gaps (handoff)
- **Court-form internal sub-types** (e.g. specific tribunal forms for stay-of-execution, niche SCT/ECT applications) — partially out-of-scope; verify on judiciary.gov.sg.
- **Local Bar customs** (unwritten mentions / chamber etiquette) — outside corpus scope; practitioner experience required.
- **Singapore International Commercial Court (SICC)** — distinct procedural regime; deferred to v0.2 as a separate digest.
- **Tax** (Income Tax Act + GST Act) — specialist scope; deferred.
- **Securities / Financial Services** (SFA 2001) — specialist scope; deferred.

## Cross-references
- Court hierarchy + jurisdictional thresholds — `../_research/01-court-hierarchy.md`.
- Civil procedure framework — `../_research/02-court-rules-civil.md`.
- Criminal procedure framework — `../_research/03-court-rules-criminal.md`.
- Bar regulation (Rule 36 firewall · solicitation prohibition · publicity rules) — `../_research/10-bar-rule-publicity-solicitation.md`, `../_research/11-bar-rule-conflict-of-interest.md`, `../_research/12-bar-rule-confidentiality.md`, `../_research/38-bar-rule-fees-billing.md`, `../_research/44-bar-rule-client-money.md`.
- Citation format — `../_research/13-citation-format-primary.md`, `../_research/14-citation-format-secondary.md`.
- Drafting templates that consume this corpus — `../examples/`.

## Recommended next step (v0.2)
1. Section-by-section depth on PDPA, MCA, LPA (the three most-queried by solo advocates).
2. Add s18 — Arbitration Act 2001 + s19 — International Arbitration Act 1994 (commercial-disputes coverage).
3. Add s20 — Mediation Act 2017 (mandatory mediation pathways in family / employment).
4. Section-text verification (move from topic-level to verbatim-section-text) on Tier-1 set.
