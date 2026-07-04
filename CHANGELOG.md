# Changelog

## [0.1.1] — 2026-06-05 · Dual-mode disclosure refinement (with PDPA Section 24 + Section 26 cloud-mode clarification)

### Changed
- **README.md** — refined headline tagline, "Why this exists" closing line, tier table rows (Local Ollama · DeepSeek · Claude/Gemini), and "Privacy & Data Handling — what stays where" section to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.

  **PDPA Section 24 (reasonable security arrangements)** + **Section 26 (cross-border transfer obligation)** are now explicitly framed dual-mode:
  - Local Ollama tier: Sections 24 + 26 not triggered (no transmission occurs)
  - Cloud tier: Section 24 supported by Gateway sanitisation (meaningful technical safeguard); Section 26 NOT discharged by Gateway — user must still establish consent OR adequacy basis OR equivalent contractual safeguards

  **LPCR Rule 8** confidentiality remains the practitioner's responsibility in either configuration.

  **Cybersecurity Act CII + IMDA AI Verify + MAS Notice 644 + October 2024 Judiciary AI Guidelines** named as sectoral overlays that apply atop the dual-mode architecture.

  Prior wording overstated by treating local-only as architectural fact across all tiers; the architecture is in fact **local-default with cloud-optional + Gateway-sanitised cloud transmission**.

### Why this matters
A Singapore solo practitioner relying on the prior *"Your data stays on your machine"* line who configured a cloud-LLM provider for PDPA-sensitive work would have been misled about the Section 26 obligation surface (consent / adequacy / contractual safeguards) which Gateway sanitisation supports but does not discharge. The refinement is honest disclosure; the Gateway as a privacy primitive is materially stronger than what most cloud-AI legal tools offer; the wedge for choosing this tool over commodity cloud AI is preserved.

### Unchanged
- All agents, drafting templates (55 + 6 ROC 2021 scaffolds + 17 statute digests), tests, getting-started guides, and the Pseudonymisation Gateway itself are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change.
