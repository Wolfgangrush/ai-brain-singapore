# Singapore Statute Corpus — Index

This index tracks the Tier-1 statutes digested for the Singapore AI Brain corpus (v0.1).

Each digest carries a `PROVENANCE: CITED:<research-file>` header tracing the underlying public-source research. The substrate for every digest is Singapore Statutes Online (sso.agc.gov.sg) plus authoritative regulator and judiciary sources (PDPC · LSRA · Judiciary · SAL · OPG · CCCS · SLA).

## Collected Statutes (v0.1)

- [x] **s01 — Personal Data Protection Act 2012 (incl. 2020 Amendments)** — [s01-pdpa-data-protection.md](./s01-pdpa-data-protection.md)
- [x] **s02 — Contract Law (Statute + Common Law)** — [s02-contract-law-overview.md](./s02-contract-law-overview.md)
- [x] **s03 — Companies Act 1967** — [s03-companies-act.md](./s03-companies-act.md)
- [x] **s04 — Penal Code 1871 (2019/2020 reform)** — [s04-penal-code.md](./s04-penal-code.md)
- [x] **s05 — Evidence Act 1893** — [s05-evidence-act.md](./s05-evidence-act.md)
- [x] **s06 — Limitation Act 1959** — [s06-limitation-act.md](./s06-limitation-act.md)
- [x] **s07 — Legal Profession Act 1966** — [s07-legal-profession-act.md](./s07-legal-profession-act.md)
- [x] **s08 — Probate and Administration of Estates** — [s08-probate-administration.md](./s08-probate-administration.md)
- [x] **s09 — Women's Charter 1961 (Family Law)** — [s09-womens-charter-family.md](./s09-womens-charter-family.md)
- [x] **s10 — Employment Act 1968** — [s10-employment-act.md](./s10-employment-act.md)
- [x] **s11 — Tort Law Overview** — [s11-tort-law-overview.md](./s11-tort-law-overview.md)
- [x] **s12 — Property and Land Law (LTA 1993 + CLPA 1886)** — [s12-property-land-law.md](./s12-property-land-law.md)
- [x] **s13 — Insolvency, Restructuring and Dissolution Act 2018** — [s13-irda-insolvency.md](./s13-irda-insolvency.md)
- [x] **s14 — Mental Capacity Act 2008** — [s14-mental-capacity-act.md](./s14-mental-capacity-act.md)
- [x] **s15 — Consumer Protection (Fair Trading) Act 2003** — [s15-cpfta-consumer-protection.md](./s15-cpfta-consumer-protection.md)
- [x] **s16 — Copyright Act 2021** — [s16-copyright-act.md](./s16-copyright-act.md)
- [x] **s17 — Electronic Transactions Act 2010** — [s17-eta-electronic-transactions.md](./s17-eta-electronic-transactions.md)

## Coverage map (Tier-1 by practice area)

| Practice area | Primary digest(s) |
|---|---|
| Data protection / privacy | s01 |
| Commercial / contracts | s02, s17 |
| Corporate / regulatory | s03, s13 |
| Crime / regulatory enforcement | s04, s05 |
| Civil procedure / limitation | s05, s06 |
| Solicitor regulation | s07 |
| Wills / estates / capacity | s08, s14 |
| Family | s09 |
| Employment | s10 |
| Tort / personal injury / defamation | s11 |
| Real estate / conveyancing | s12 |
| Consumer / retail | s15 |
| IP / copyright | s16 |

## Deferred to v0.2+

- Arbitration Act 2001 + International Arbitration Act 1994 (covered partially in `_research/22-arbitration-mediation-frameworks.md`; full statute digest deferred).
- AML/CFT obligations for lawyers (covered in `_research/27-anti-money-laundering-obligations.md`; statute-form digest deferred to v0.2).
- Mediation Act 2017 (deferred to v0.2).
- Securities and Futures Act 2001 (commercial-specialist scope; deferred).
- Income Tax Act + GST Act (tax-specialist scope; deferred).
- Trade Marks Act 1998 + Patents Act 1994 + Registered Designs Act 2000 (IP-specialist scope; partial in s16; deferred).

## Currency warnings (v0.1 snapshot — 2026-05-18)

- **Family law:** Divorce by Mutual Agreement (DMA) effective July 2024. Verify any default templates account for non-fault grounds.
- **AML/CFT:** 2025 amendments on Proliferation Financing took effect July 2025. Solo advocates must update internal CDD manuals.
- **AI in courts:** October 2024 Judiciary Guidelines are mandatory. Any tool surface must caption AI-generated content for advocate review.
- **Copyright:** Default ownership of commissioned works shifted to the creator under the 2021 Act; older contracts may follow the 1987 Act position.
- **Court rules:** ROC 2021 fully replaced ROC 2014 from 1 April 2022. "Originating Claim" (OC) and "Originating Application" (OA) replaced "Writ" and "Originating Summons" respectively.

## Verification posture

Every digest in this corpus is marked `STATUS: VERIFIED` only if the underlying section text was checked against SSO on the date in the Currency Block. Anything that could not be verified at section-text level is flagged in `singapore/BLOCKERS.md`.
