# Getting Started — AI Brain for Singapore Lawyers · v0.1

**🙏 Welcome — your AI Brain begins here.**

This guide takes you from zero to running your own AI-powered Singapore practice OS in about 30 minutes.

---

## What this is

AI Brain Singapore is a **memory-first practice management assistant** for Singapore solo advocates and solicitors. It runs entirely on your machine — no cloud, no API keys (for the local-first mode), no telemetry. Your case files never leave your computer.

Built on MemPalace (MIT), it remembers your matters, checks deadlines, validates SAL neutral citations + Singapore Statutes Online references, looks up Singapore courts (State Courts · High Court · Court of Appeal · SICC · Family Justice Courts), syncs your practice calendar to ICS, and flags compliance risks before they become Legal Profession Act / LPCR disciplinary problems.

**It does NOT:** perform judicial reasoning, predict case outcomes, or draft substantive legal arguments. See [`DISCLAIMER.md`](DISCLAIMER.md) for LPCR Rule 8 firewall + PDPA controller/processor analysis + UPL exclusion.

---

## Before you start

You need:
- macOS, Linux, or WSL2 on Windows
- Python 3.9 or later
- Terminal (Terminal.app, iTerm2, GNOME Terminal, etc.)
- 30 minutes of focus

---

## Install (one command)

```bash
# Clone the repo
cd ~/Desktop
git clone https://github.com/Wolfgangrush/ai-law-firm-singapore.git
cd ai-law-firm-singapore

# Install in development mode
pip install -e .

# Connect to your AI brain (choose ONE — see MODEL_SETUP.md for full options)
ailawfirm-sg connect-local
```

That's it. You now have a Singapore practice OS running on your laptop.

---

## What you get out of the box

**Statute corpus** (`_statute_corpus/`) — 17 Tier-1 Singapore statute digests:
- PDPA · Contract · CA 1967 · Penal Code · Evidence · Limitation · LPA
- Probate · Women's Charter · Employment · Tort · Property/Land
- IRDA · MCA · CPFTA · Copyright · ETA

**Drafting corpus** (`_drafting_data/`) — 55 templates + 6 ROC 2021 scaffolds:
- Pleadings · motions (summary judgment · Mareva · Anton Piller · stay)
- Disclosure + privilege log · expert evidence · enforcement (WSS · garnishee · EJD)
- Appeals · skeleton arguments · counsel briefing · judicial review
- Trial documentation · ADR (Mediation Act + Singapore Convention)
- Insolvency (IRDA 2018) · tribunals (ECT · SCT · FJC)
- Commercial backbone · PDPA + IMDA AI + Cybersecurity Act + OSA + MAS regulatory

**Research substrate** (`_research/`) — court hierarchy · court rules civil/criminal · statute overviews · bar rules · citation format.

---

## First-run checklist

1. ✅ **Install** — `pip install -e .`
2. ✅ **Pick an AI brain** — Claude / OpenAI / DeepSeek / Gemini paid / local Llama / local Qwen. See [`MODEL_SETUP.md`](MODEL_SETUP.md).
3. ✅ **Read disclaimers** — [`DISCLAIMER.md`](DISCLAIMER.md) + [`NO_PII_NO_DATA.md`](NO_PII_NO_DATA.md).
4. ✅ **Audit checklist** — [`AUDIT_v0.1.md`](AUDIT_v0.1.md) walks the LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance.
5. ✅ **Privacy** — read [`PII_SCAN_v0.1.md`](PII_SCAN_v0.1.md) for the Pseudonymisation Gateway design.
6. ✅ **Start using** — `ailawfirm-sg --help` for commands.

---

## Privacy + LPCR compliance

The system applies a three-layer privacy firewall before any text leaves your machine when using a cloud-API brain (substitution → LLM-blind → re-substitution). The Publisher [wolfgang_rush](https://github.com/Wolfgangrush) never sees your case facts, party names, financial figures, or generated outputs.

For special-category data (PDPA Section 26 special-category · health · criminal record · political opinion), prefer the local-LLM track (no data leaves your machine, ever) or wait for v0.3+ true-air-gap mode. See [`DISCLAIMER.md`](DISCLAIMER.md) for the full LPCR Rule 8 + UPL exclusion analysis.

---

## Reporting issues + contributing

- 🐛 **Bug reports** → file an issue at [github.com/Wolfgangrush/ai-law-firm-singapore/issues](https://github.com/Wolfgangrush/ai-law-firm-singapore/issues)
- 💬 **General questions** → start a discussion in the repo
- 🌐 **Translation reviews** → [`TRANSLATION_HELP_WANTED.md`](TRANSLATION_HELP_WANTED.md)
- 📚 **Authority verification** → [`KNOWLEDGE_PROVENANCE.md`](KNOWLEDGE_PROVENANCE.md) catalogues every authority cited

---

## Next steps

- Read [`SCOPE.md`](SCOPE.md) — what's IN scope (v0.1) and what's NOT (deferred to v0.2/v0.3/v0.4+).
- Read [`SECURITY.md`](SECURITY.md) — security architecture + supply-chain audit.
- Browse [`_drafting_data/00_DRAFTING_INDEX.md`](_drafting_data/00_DRAFTING_INDEX.md) — full template inventory.
- Browse [`_statute_corpus/INDEX.md`](_statute_corpus/INDEX.md) — full statute digest inventory.

**You're ready. Welcome to your AI Brain — Singapore edition.** 🇸🇬
