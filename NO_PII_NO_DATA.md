# NO_PII_NO_DATA — Zero-Collection Architecture

> ## ⛔ CORRECTION (2026-08-16) — the local-only mode referred to below is NOT IMPLEMENTED
>
> This document points you to "local-only mode" for confidential work. **That mode is not wired
> in this release.** No code path routes inference to a local model, so **no obligation described
> below is discharged by absence of transmission today.**
>
> What IS true: the cloud path sanitises identifiers through the pseudonymisation gateway before
> any prompt leaves the machine, on every egress, covered by tests. That is a real technical
> safeguard — but it is a safeguard, not the "no transmission occurs" position, and it does not
> discharge your own controller/fiduciary duties.
>
> **Treat every AI answer as cloud-processed until this notice is removed.** For work you cannot
> transmit, do not use the AI features of this tool at present.



**This document explains, in detail, why AI Brain — Singapore collects no personal data from you.**

## The short version

The publisher (wolfgang_rush) operates **zero infrastructure** that touches your data. There is no server. There is no telemetry. There is no analytics. There is no "anonymous usage improvement data." The tool runs entirely on your laptop.

## The architectural guarantee

AI Brain — Singapore is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** You can verify this by grepping the source: `grep -ri "telemetry\|analytics\|tracking\|requests.post\|urlopen" aibrain_singapore/` will return only legitimate cloud-AI calls (which are user-initiated and routed direct to your chosen vendor, not to the publisher).

**(2) The publisher operates no server.** There is no AI Brain Singapore API. There is no AI Brain Singapore cloud service. There is no AI Brain Singapore database. The publisher's only infrastructure is the GitHub repository (a US-based code hosting service) and the publisher's personal MemPalace (which holds no user data — it holds the publisher's development notes).

**(3) Storage is on your laptop.** Your matter data, citation cache, calendar entries, configuration, and any other persistent state live on your local filesystem under `~/.aibrain-singapore/`. The publisher has no access to this folder.

**(4) Network calls are limited to:**
- Package installation (PyPI download during `pip install`)
- User-initiated AI cloud calls (if you opt into cloud mode — routes direct to vendor, not through publisher)
- Optional update checks (if v0.2+ adds this, it will be opt-in and check GitHub releases only — no data sent)

## Cloud-mode (when you opt in)

If you choose to use cloud AI processing (DeepSeek · Anthropic · Google Gemini · etc.), your queries route **directly from your laptop to the AI vendor**. The publisher is not in the data path. The publisher cannot see your queries. The publisher does not know what you process.

The contract for cloud-mode usage is between **you** and the **AI vendor** under their terms of service. The publisher is not a party to that contract.

For client-confidential work, do NOT use cloud mode. Use the local-only mode (Ollama + Qwen3 or equivalent). See [MODEL_SETUP.md](MODEL_SETUP.md).

## Singapore PDPA implications

Singapore's Personal Data Protection Act 2012 (as amended 2020) imposes obligations on "organizations" that process personal data.

Because the publisher:
- Operates no server processing user input
- Collects no personal data
- Has no access to user files or queries

...the publisher is **neither a data intermediary nor a data controller** under the PDPA with respect to your tool usage.

If you use the tool to process personal data of your clients, **you** are the controller for that processing and your PDPA obligations apply (notification consent · access correction · breach notification within 3 calendar days · DPO appointment · etc.). The tool does not transmit such data anywhere unless you have explicitly enabled cloud mode and used a cloud feature.

## Cross-border data transfer

The PDPA Section 26 restricts cross-border transfer of personal data unless the receiving jurisdiction provides comparable protection or appropriate safeguards. Because the publisher transfers no personal data anywhere, Section 26 does not apply to the publisher's activity.

If you opt into cloud mode and the cloud vendor processes data outside Singapore, the cross-border transfer is YOUR action; YOUR PDPA Section 26 obligations apply.

## Verification path

You can independently verify zero-collection by:

1. `grep -ri "telemetry\|analytics\|posthog\|mixpanel\|segment\|amplitude\|google-analytics\|datadog\|sentry" aibrain_singapore/` — should return zero results.
2. `cat requirements.txt` — should contain no analytics or telemetry libraries.
3. Run the tool offline (`pip install` from cache · disconnect network · `aibrain-singapore --version`) — should work fully (cloud-AI calls will fail, but that's expected and visible).
4. Inspect network traffic during use with `nettop` (macOS) or `nethogs` (Linux) — should show traffic only to user-initiated cloud-AI endpoints if cloud mode is on.

## If this changes

If a future version of the tool adds telemetry, opt-in update checks, or any cloud touchpoint that involves the publisher's infrastructure, that change will be:
- Announced in CHANGELOG with the change line
- Default OFF · user-opt-in only
- Documented in this file with the change date and the specific data category

This file will always represent the current state. If it differs from the code, the code is the truth — file an issue.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection), §3.V9 (Conduct-Rule Inducement). Playbook version: v0.1.*
