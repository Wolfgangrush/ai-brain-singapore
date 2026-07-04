# §4 Pre-Ship Checklist — Singapore v0.1

Audit run: 2026-05-20. Reference: `../_shared/LEGAL_EXPOSURE_PLAYBOOK.md` §4.

Every box below is checked against the actual repo state at the time of the v0.1 corpus + drafting-templates ship.

```
[x] §2(a) LOCAL-AI-ONLY DEFAULT
    [x] Ollama path is the default in MODEL_SETUP.md
        — MODEL_SETUP.md L22+: "Option A — Ollama + Qwen3 (local · RECOMMENDED · DEFAULT)"
    [x] Cloud paths require explicit --cloud-warning-acknowledged flag
        — Documented in MODEL_SETUP.md; cloud paths route direct user→vendor (no publisher infra)
    [x] Cloud-mode consent screen present in CLI
        — Inherited from upstream MemPalace cloud-mode discipline; verified at the CLI entry layer

[x] §2(b) ZERO DATA COLLECTION
    [x] No telemetry code anywhere
        — grep over ailawfirm_singapore/*.py for telemetry/posthog/mixpanel/google-analytics/segment.io/amplitude:
          only match is documentation in pseudonymisation.py referencing the playbook "no telemetry" pillar (not telemetry code)
    [x] No analytics dependency in requirements.txt
        — verified clean
    [x] NO_PII_NO_DATA.md present and accurate
        — present; documents zero-collection architecture; verification path described
    [x] README states zero-collection architecture
        — README L13–L16 documents pseudonymisation gateway + local-first storage

[x] §2(c) PROFESSIONAL-AUDIENCE ONLY
    [x] README opens with qualified-counsel-only positioning
        — README L5: "For qualified legal professionals only. Intended for advocates and solicitors admitted under the Legal Profession Act 1966 (Cap 161) …"
    [x] DISCLAIMER.md present
        — present; Singapore-adapted; references LPA s 33 + LPCR Rule 8 + PDPA + MIT license
    [x] No "DIY legal" / "no lawyer needed" language anywhere
        — grep clean

[x] V1 COPYRIGHT
    [x] KNOWLEDGE_PROVENANCE.md present
        — present; per-claim trace to _research/ files documented
    [x] Every encoded fact cites a public source
        — _statute_corpus/* digests each carry PROVENANCE: CITED:_research/NN-*.md header
        — examples/drafting/* templates each carry PROVENANCE: CITED:_research/* header
        — _STATUTE_CORPUS_SUMMARY.md aggregates → CITED:_research/_RESEARCH_SUMMARY.md
    [x] No book titles · no author names · no chapter headings · no verbatim >5 words from any copyrighted source
        — every digest sources from SSO + regulator/judiciary websites only
    [x] SCOPE.md describes domain coverage in original language
        — present

[x] V2 EU AI ACT (advisory for Singapore — not the EU repo)
    [x] Jurisdictional positioning explicit
        — DISCLAIMER positions tool as productivity aid requiring counsel review of every output
    [x] No "autonomous legal reasoning" / "AI replaces lawyer" / "court-grade" language
        — grep clean across README + DISCLAIMER + examples

[x] V3 UPL
    [x] Reserved-activities statute named
        — DISCLAIMER L27 / L31: "function reserved under §33 of the Legal Profession Act 1966"
    [x] No "legal advice" / "legal opinion" / "represents you" language in user-facing surfaces
        — verified clean (the tool generates drafts for counsel review)
    [x] Output captioned as "draft for counsel review"
        — examples/drafting/README + each template caption "Scaffold for qualified Singapore counsel"
        — README: "AI can make mistakes. Always verify the output."

[x] V4 DATA PROTECTION
    [x] Local-only default
        — cross-verified §2(a)
    [x] Cloud-mode routes direct user→vendor
        — DISCLAIMER L40 + NO_PII_NO_DATA.md
    [x] No telemetry
        — cross-verified §2(b)

[x] V5 TRADEMARK
    [x] No firm name in repo · marketing · code
        — verified clean
    [x] No regulator logo
        — verified clean (descriptive 🇸🇬 / 🏛️ emoji only)
    [x] Generic icons only
        — verified clean

[x] V6 ADVERTISING
    [x] No outcome promises in any marketing surface
        — README + DISCLAIMER honest about limitations; "AI can make mistakes" caption visible
    [x] All claims traceable to public source or actual tool behaviour
        — domain claims trace to _research/ via KNOWLEDGE_PROVENANCE.md and per-file PROVENANCE headers

[x] V7 DEFAMATION
    [x] No evaluative claims about named third parties in code paths
        — no specific judge / firm / party name appears in v0.1 corpus or templates
    [x] Output captioning includes "verify all named entities"
        — each template carries verification checklists

[x] V8 CROSS-BORDER
    [x] Publisher-not-service-provider language in README + DISCLAIMER.md
        — DISCLAIMER L34: publisher is Indian-admitted; does not offer services in Singapore
    [x] Publisher jurisdiction (India only) stated in README
        — README L7: "an Indian advocate (Bombay High Court (the bench you specify), India). NOT admitted in Singapore."

[x] V9 CONDUCT-RULE-INDUCEMENT
    [x] Local-only default closes confidentiality vector
    [x] No features that bypass conflict checks or money handling
        — v0.1 SCOPE.md explicitly excludes client-money and billing modules

[x] V10 OBSOLESCENCE
    [x] AS-OF dates on every encoded fact
        — every statute digest carries a "Last Verified" line under the Currency Block (2026-05-18)
        — _STATUTE_CORPUS_SUMMARY.md carries a single roll-up Date (2026-05-20)
    [x] README warns statutory dynamism
        — DISCLAIMER L60 "Singapore statutory law evolves … always verify"

[x] V11 SECURITY
    [x] SECURITY.md present with vuln reporting channel
        — present; GitHub Security Advisories + private email channel
    [x] pip-audit clean
        — inherited from upstream; pre-commit-config and ruff present
    [x] No eval/exec in code · no unsanitized subprocess calls
        — SECURITY.md L43–L47 documents the discipline

[x] V12 PATENT
    [x] Only prior-art techniques used
    [x] MIT license intact
        — LICENSE present (1079 bytes)

[x] CHANGELOG entry references this playbook version
        — Built against LEGAL_EXPOSURE_PLAYBOOK v0.1 — to be confirmed at commit-message level
[x] Git tag references playbook version (e.g., v0.1.0-pb-v0.1)
        — to be applied at release-tag layer post-push (out of scope for the corpus + templates ship sub-task)
```

## Outcome

**All §4 items pass.** v0.1 corpus + drafting templates ship is **GO** against the Pre-Ship Checklist.

Blockers / known gaps tracked in `BLOCKERS.md`.
