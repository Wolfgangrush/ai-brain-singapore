# PII Firewall Sweep — Singapore v0.1

Sweep run: 2026-05-20. Reference: pre-push discipline aligned with the publisher's broader leak-prevention posture across country repos.

## Tool used

`scripts/leak_check.py` (the repo's native pre-push leak check). All vectors covered by the script's banned-pattern list are verified by running the script. See the script itself for the authoritative pattern set.

## Vectors covered by the native script

The script's banned-pattern list (paraphrased without quoting the banned tokens):
- Palace-personal chamber matter names (real people from the publisher's practice).
- Compression-dialect vocabulary (the publisher's internal alias-coding spec; pattern names, identifier prefixes, attribute names, and constants).
- Publisher's personal entity-alias codes (real people coded in the publisher's private knowledge graph).
- Palace internal paths (the publisher's machine path; the upstream open-source palace data-directory path constant).
- Lawtech-arc personal-build references.

Indian PII identifiers (Aadhaar / PAN / GSTIN / IFSC / RuPay) are intentionally NOT flagged — they are legitimate diaspora-client coverage. Singapore has South Asian residents whose matters legitimately include Indian-context PII.

## Outcome

Run: `python3 scripts/leak_check.py` from the repo root.

This file is itself authored to comply with the script's banned-pattern list — it neither quotes the publisher's private entity-alias codes nor the dialect-vocabulary tokens that the script flags. The patterns are described by category, not by literal token.

## Adjacent verifications run

- Cross-border data transfer language present in `NO_PII_NO_DATA.md` (PDPA s 26 stance: publisher transfers no data; user-initiated cloud-mode is the user's transfer).
- Publisher-attribution surfaces (DISCLAIMER, pyproject.toml authors, MODEL_SETUP, SECURITY, SCOPE) intentionally retained per the LEGAL_EXPOSURE_PLAYBOOK §8 Personal-Jurisdiction-Shield doctrine — these are required, not leaks.

## Redactions applied before push

`_research/_RESEARCH_SUMMARY.md` carried legacy authoring-process references (handoff phrasing, default-template phrasing) that contained the publisher's private entity-alias code. Three lines were rewritten with semantic-equivalent replacements:
- "handoff to <author-process> / <publisher-alias>" → "handoff to publisher review"
- "may need <publisher-alias>'s practitioner experience" → "may need a Singapore-admitted practitioner's experience to surface"
- "<author-process>'s default family-law templates" → "any default family-law template"

No legal-substance content was changed.

## Discipline note

This audit document was rewritten after an initial draft was caught by `scripts/leak_check.py` for quoting banned tokens verbatim while describing them. Quoting tokens to describe a banned-token list is itself a leak. The fix is to describe by category, not by token. This pattern is recorded so future audit docs (across country repos) avoid the same trap.
