# SCOPE — AI Brain · Singapore · Solo · v0.1

## In scope (v0.1 must-haves)

- [x] Forked from MemPalace 3.0.0 (MIT) — `_research/` preserved
- [x] Package renamed to `aibrain_singapore`
- [x] pyproject.toml v0.1.0 with Singapore Solo metadata
- [x] README positioned for Singapore solo practitioners · MemPalace credited
- [x] SCOPE.md (this file)
- [x] KNOWLEDGE_PROVENANCE.md (every claim traces to a `_research/` file)
- [x] `core/ontology.py` — Singapore matter types · court hierarchy · statute registry · LPCR Rule 8
- [x] `core/calendar/` — ICS writer + publisher abstraction (ADR-002 D4)
- [x] `brain/` — 10-intent classifier (added CALENDAR_QUERY + CALENDAR_ADD) + router
- [x] `agents/` — 7 specialist agents (calendar_agent NEW)
- [x] MCP tool 1: `singapore_court_lookup` (5+ court stubs)
- [x] MCP tool 2: `singapore_citation_validator` (SLR · SGCA · SGHC)
- [x] MCP tool 3: `singapore_calendar_sync` (write .ics + publish)
- [x] Test suite covering ontology · MCP tools · brain end-to-end · ICS validity
- [x] MCP server wired with the 3 new tools
- [x] All tests passing
- [x] Local commits clean

## Explicitly out of scope (NOT v0.1)

- [ ] Firm mode (multi-user · roles · billing) — v0.3+
- [ ] Real statute verbatim text — needs source PDFs · v0.2+
- [ ] Drafting templates — wolfgang_rush plugin family · separate repo
- [ ] LawNet / SAL / SingaporeLaw.sg database lookup — v0.4+
- [ ] Matter calendar UI / matter dashboard — v0.2+
- [ ] Client billing module — v0.2+
- [ ] Apple EventKit native integration — v0.2 (macOS only)
- [ ] CalDAV bidirectional sync — v0.2+
- [ ] Google Calendar API direct (REJECTED — see ADR-002 D6)
- [ ] GitHub publish — post-publisher-verify
- [ ] Production deployment — post-hardening
- [ ] UI (terminal or web) beyond CLI stubs — post-v0.1
- [ ] AI generation of legal advice — LPCR Rule 8 firewall · forbidden permanently

## Verification path

v0.1 is verified by the publisher (wolfgang_rush) before any GitHub publish.

## Falsification

If v0.1 cannot achieve all "in scope" items in < 100 minutes of build session (Singapore is ~25% larger than India v0.1 due to calendar inclusion), halt and report — do not pad scope to declare victory.
