<div align="center">

<img src="docs/banner.png" width="820"/>

**A local-first practice brain for Singapore lawyers.**

Visit the live site: [wolfgangrush.github.io](https://wolfgangrush.github.io)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Local-first](https://img.shields.io/badge/local--first-yes-blue.svg)](#)
[![Built for Singapore lawyers](https://img.shields.io/badge/built_for-Singapore_lawyers-red.svg)](#)
[![Anti-fabrication](https://img.shields.io/badge/principle-anti--fabrication-orange.svg)](#)

</div>

# 🇸🇬 AI Brain for Singapore Lawyers

> **Free practice OS for every Singapore solo advocate and solicitor. Terminal-native. Local-first by default (Ollama + Qwen3 — nothing leaves your laptop). Cloud-LLM optional with the [Pseudonymisation Gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) sanitising PII before any prompt leaves the machine. Built by an Indian advocate, for the global solo bar.**

**For qualified legal professionals only.** Intended for advocates and solicitors admitted under the Legal Profession Act 1966 (Cap 161), in-house counsel of Singapore entities, foreign lawyers registered with the SICC, or paralegals working under their supervision. **If you are not a qualified legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 2.0.0 · **License:** MIT · **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). NOT admitted in Singapore. This is a software publication for Singapore-admitted practitioners. · **Engine:** Built on [MemPalace](https://github.com/MemPalace/mempalace) (MIT)

## 🆕 New in v2.0 — the terminal brain now works end-to-end

Earlier the brain (classify → route → specialists) was not wired to the terminal and several agents were placeholders. **Now it is a working second brain you talk to:**

| Command | What it does |
|---|---|
| `reception` | **"turn it on"** — greets you, checks every specialist is online, loads your retrospective memory |
| `ask "<question>"` | one-shot — routes your question to the right specialist and answers |
| `chat` | interactive session — keep asking; every line is routed for you (no commands to memorise) |
| `recap` | what you did in past sessions (memory persists across runs) |

Every specialist is **AI-backed** by whatever host you launch it under (Claude · GLM · Codex — it reads your `ANTHROPIC_*` environment), grounded on a deterministic engine so answers stay anchored to it. It runs under **any** host CLI — a `UserPromptSubmit` hook + `AGENTS.md` route every query through the brain instead of the model free-answering. Free public edition — no enterprise features.


> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

> 🛡️ **Privacy primitive: PII pseudonymisation** via [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) (wolfgang_rush · MIT). This firm uses the `singapore` jurisdiction module + Indian-diaspora overlay for cross-jurisdiction PII coverage. Open-source · zero runtime deps · session-scoped · in-memory only · never writes PII to disk.


> 🛡️ **Pseudonymisation coverage (v0.1.1):** The privacy gateway pseudonymises PII before any cloud-API call; any residue the scanner can't fully resolve is surfaced to you and audit-logged — you retain the final call (v0.3 honest-disclosure). Covers Singapore-native identifiers (NRIC · FIN · UEN · CPF references · SG phone · SGD amounts · SGCA/SGHC/SGDC case numbers) and Indian-diaspora identifiers (Aadhaar · PAN · GSTIN · IFSC · Indian phone — Singapore has substantial South Asian diaspora, ~9.2% of population). Generic patterns (email · names with honorifics · dates · case numbers) work cross-jurisdiction.

> **🧠 AI Brain that LEARNS.** Every session makes the next one smarter. Two built-in Claude Code skills power this: `/retrospective` saves what the firm learned at session end — every jurisdiction, statute, argument pattern, and procedural rule you touched is logged so the firm's knowledge compounds. `/wake` loads that accumulated context the next time you start, so you never begin from zero. The firm is your second brain, and it gets sharper with every case.

---

## 🌐 Choose your language

| Script | Language | Audience | Guide |
|---|---|---|---|
| 🇬🇧 | **English** | Singapore default · Working language | [GETTING_STARTED.md](GETTING_STARTED.md) |
| 🇨🇳 | **中文 (Simplified Chinese)** | Mandarin-speaking community | (community PR welcome) |
| 🇲🇾 | **Bahasa Melayu** | Malay community | (community PR welcome) |
| 🇮🇳 | **தமிழ் (Tamil)** | Tamil community | (community PR welcome) |

> 🙏 **Honest note:** Singapore's working language for legal practice is English. Multi-language guides for Mandarin · Bahasa · Tamil are placeholders — **native-speaker PRs warmly welcome** via [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md).

---

## 💛 Why this exists

> Singapore solo practitioners face a unique pressure stack:
> - **Highest regulatory density per practitioner in the region** — PDPA 2020 Amendments · 2025 AML Proliferation Financing Rules · October 2024 Judiciary AI Guidelines · LPCR 2015 · Solicitors' Accounts Rules
> - **5 court hierarchies** (Supreme · State · Family · Syariah · SICC) + tribunals
> - **Singapore Bar's elite-firm career path** dominates — solo practice gets less institutional support
> - **PDPC enforcement is active** with S$1M / 10% turnover penalty exposure

Large firms have armies of associates to navigate this complexity. Solo advocates don't. We built this so a Singapore solo practitioner — ex-Big-Four or career-solo — can have a second brain that costs **S$0 forever**, runs locally by default (Ollama + Qwen3), and supports LPCR Rule 8 confidentiality + PDPA Section 24 reasonable security at the architecture layer — either by absence of transmission (local mode) or by Pseudonymisation Gateway sanitisation (cloud mode, with PDPA Section 26 cross-border-transfer obligations remaining YOUR responsibility). Honest about its limitations throughout.

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | Listens to what you say. Figures out who you need. Calls the right specialist. You never memorize commands. |
| 📂 | **The Matter Manager** | Holds every active case file — parties, prayers, hearings, orders, draft state. Open court · context comes back instantly. |
| 📜 | **The Citation Clerk** | Parses Singapore citations — SLR · SGCA · SGHC · SGDC · SGMC · MLJ regional cross-refs. No more eyeballing whether `[2023] SGCA 12` is well-formed at 11:48 PM. |
| 🏛️ | **The Court Registrar** | Knows the Singapore court hierarchy: Court of Appeal · HC General Division · HC Appellate Division · State Courts · Family Justice Courts · Syariah Court · SICC. Pecuniary jurisdictions, e-filing systems, contact patterns. |
| ✍️ | **The Drafting Assistant** | Ships with **6 ROC 2021 drafting scaffolds** in [`examples/drafting/`](examples/drafting/) (Originating Claim · Originating Application · Statement of Claim · Defence · Reply · Affidavit) **plus 55 drafting templates** in [`_drafting_data/`](_drafting_data/) covering: civil pleadings (counterclaim · third-party notice · particulars · amendment · pre-action production) · motions (summary judgment · striking-out · security for costs · anti-suit · stay · Mareva · Anton Piller) · evidence + disclosure (production · privilege log · expert evidence · default judgment) · enforcement (WSS · garnishee · EJD · charging order · committal · RECJA/REFJA/CCAA foreign judgments) · appeals (CoA · AD-HC · State Courts to HC · grounds + skeletals) · skeletons + counsel briefing (trial · interim · brief to counsel · advice on merits) · judicial review (Order 24 + GPA) · trial documentation (bundles · chronology · written closing) · ADR (Mediation Act 2017 + Singapore Convention) · insolvency (IRDA 2018 — winding-up · judicial management · bankruptcy) · tribunals (ECT · TADM · SCT · FJC) · commercial backbone (sale of goods · services · employment · NDA · shareholders · loan · tenancy) · regulatory (PDPA — DPA · breach · privacy policy · cross-border · IMDA AI · Cybersecurity Act CII · Online Safety Act · MAS Notice 644). Each template carries a `PROVENANCE: CITED:_research/` header. |
| 📚 | **The Statute Corpus** | 17 Tier-1 statute digests live in [`_statute_corpus/`](_statute_corpus/) (PDPA · Contract · CA 1967 · Penal Code · Evidence · Limitation · LPA · Probate · Women's Charter · Employment · Tort · Property/Land · IRDA · MCA · CPFTA · Copyright · ETA). Each digest cites its `_research/` substrate via `PROVENANCE:` header. Topic-level depth for v0.1; section-text verbatim depth in v0.2 on PDPA / LPA / MCA. |
| 🛡️ | **The Compliance Officer** | Watches your LinkedIn posts, website copy, marketing for **LPCR Rule 8 (publicity/solicitation)** firewall risks BEFORE you publish. Also flags PDPA gaps, AML/KYC red flags, and Solicitors' Accounts Rules concerns. |
| 📅 | **The Calendar Sync** | ICS feed sync to iPhone Calendar / Google Calendar / Outlook — no third-party API, no data processor. code-aliased summary line (lock-screen safe) · full matter detail in event body (hidden until tap). Timezone Asia/Singapore (UTC+8, no DST). |

---

## 🚀 Install in 30 minutes

### Step 1 — Pick your operating system

| OS | Guide |
|---|---|
| 🍎 **Mac** | Standard Python install (Terminal) |
| 🐧 **Linux** | Same commands as Mac |
| 🪟 **Windows** | PowerShell · same install flow |

### Step 2 — Install Python (one-time) + the tool

```bash
pip install git+https://github.com/Wolfgangrush/ai-brain-singapore.git
```

### Step 3 — Connect an AI brain (ONE COMMAND)

```bash
ailawfirm-singapore connect-local
```

This single command:
1. Detects if Ollama is installed; if not, prints platform-specific install instructions
2. Detects your laptop's RAM
3. Recommends and downloads the right Qwen3 model (14b for 16GB+ · 7b for 8GB · 1.7b for older laptops)
4. Writes config so all subsequent calls route to local Ollama
5. Runs a smoke test to confirm local connectivity

After this, **no queries leave your laptop**.

Three honest model options — see [MODEL_SETUP.md](MODEL_SETUP.md):

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Local Ollama + Qwen3** | S$0 forever | 🟢 Perfect — nothing leaves your laptop · PDPA Sections 24 + 26 not triggered (no transmission occurs) | **Client matters · LPCR Rule 8 confidentiality · PDPA-sensitive work · use this tier when zero cross-border data flow is required** |
| 🥈 **DeepSeek API** | ~S$2-5/mo | ⚠️ Pseudonymisation Gateway sanitises NRIC/FIN/UEN/CPF/Aadhaar + names before transmission, BUT Singapore PDPA Section 26 cross-border restrictions still apply to the pseudonymised China-routed transmission | Non-client work · public-law research · drafting templates |
| 🥉 **Claude / Gemini API** | ~S$25-80/mo | 🟢 Strong (enterprise privacy default-ON) — Gateway sanitises before transmission | Heavy daily users with executed Article 28 DPA equivalents + PDPA Section 26 consent-or-adequacy posture. Gateway sanitisation supports your reasonable-security-arrangements (Section 24) duty but does NOT discharge the Section 26 consent/adequacy obligation. |

### Step 4 — Run

**▶ Quickstart — the commands that now work:**
```bash
python3 -m ailawfirm_singapore reception                 # turn it on: greeting + systems check + memory
python3 -m ailawfirm_singapore ask "validate a case citation"
python3 -m ailawfirm_singapore ask "which court has jurisdiction over my matter"
python3 -m ailawfirm_singapore chat                      # interactive — type anything, it routes for you
python3 -m ailawfirm_singapore recap                     # what you did last time
```
Inside a host CLI (Claude / GLM / Codex) opened in this folder, just say **"turn it on"** — the receptionist greets you, Advocate & Solicitor, and routes everything through the brain.


```bash
ailawfirm-singapore
```

Sample commands:

```
> tell me about SICC jurisdiction
> validate [2023] SGCA 42
> check this post: "Award-winning Singapore litigator"
> what's the limitation for a contract claim under the Limitation Act?
> add hearing MAT-2026-042 State Courts CR-23 2026-06-09 10:00 SGT
> sync calendar
```

---

## 🔒 Privacy & Data Handling — what stays where

**Architecture — three pieces decide your privacy posture:**

**(1) Local-only state.** Your matters, drafts, audit logs, calendar entries, and configuration live in `~/.ailawfirm-singapore/`. Never uploaded by the tool. Never synced to a third-party cloud by the tool. No telemetry. No "anonymous usage statistics." The publisher operates zero infrastructure and cannot access this folder. Verifiable via `grep -ri "telemetry\|analytics\|requests.post\|urlopen" ailawfirm_singapore/` — should return only user-initiated cloud-LLM calls.

**(2) LLM backend — you choose.** The default `connect-local` command configures Ollama + Qwen3 to run the language model on your laptop (truly nothing leaves; PDPA Sections 24 + 26 are not triggered in this configuration because no transmission occurs). If you opt into a cloud-LLM tier (DeepSeek / Claude / Gemini) for quality reasons, see the tier table above for cost + privacy trade-offs.

**(3) Pseudonymisation Gateway — always-on for cloud mode.** When you configure a cloud-LLM provider in `~/.ailawfirm_singapore/config.json`, the internalised `PseudonymisationGateway` (source: `ailawfirm_singapore/pseudonymisation.py`) automatically substitutes real names, government IDs (NRIC · FIN · UEN · CPF · Aadhaar for Indian-diaspora matters), contact identifiers (phone · email), and case references (SGCA · SGHC · SGDC numbers) with deterministic placeholders BEFORE the prompt leaves your machine. The placeholder ↔ original map lives in memory only (never written to disk; destroyed when the gateway goes out of scope). Cloud vendors see only the abstract structure of the matter; the user sees real values restored in the response.

**⚠️ PDPA Section 24 + Section 26 in cloud mode.** Gateway sanitisation supports your **Section 24** *reasonable security arrangements* duty (the data crossing the border is structurally pseudonymised — meaningful technical safeguard). But Gateway sanitisation does NOT discharge your **Section 26** *cross-border transfer* obligation, which requires either (a) the individual's consent OR (b) the recipient jurisdiction being on a comparable-protection list per PDPC guidance OR (c) contractual safeguards equivalent to the Singapore standard. Document the basis in your audit log before invoking cloud mode for client work.

**LPCR Rule 8 confidentiality** applies in either configuration — Gateway sanitisation in cloud mode supports your Rule 8 posture but does not displace it.

**Cybersecurity Act (CII)** + **IMDA AI Verify** + **MAS Notice 644 (for financial-services-adjacent practice)** + **October 2024 Judiciary AI Guidelines** all apply atop the dual-mode architecture. The Compliance Officer agent flags applicable regimes based on matter context.

The wedge: every other cloud-AI legal tool sends raw client PII to the LLM by default. wolfgang_rush AI Brain — Singapore ships Ollama-first AND ships the Gateway as the privacy primitive that closes the gap when you choose cloud mode for quality reasons — while remaining honest that Section 26 / Rule 8 / sectoral regulator obligations remain yours to execute.

### What goes to the API provider during each query

Each time the firm reasons about a matter, the following are sent to your chosen API provider:
- Your prompt (the question or instruction)
- Relevant context the firm pulls from your local matter folder (current draft state, recent orders, citations being verified)

Your full matter history, audit logs, and unrelated cases are NOT sent. The firm sends the minimum context needed to answer the current question.

### What API providers contractually guarantee

| Provider | Trains on your data? | Retention | Source |
|---|---|---|---|
| **Claude API** (Anthropic) | ❌ No — Commercial Services data is not used for training | ~30 days for safety/abuse review (Zero Data Retention available on enterprise contract) | [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy) · [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) |
| **OpenAI API** (GPT-4) | ❌ No — API data not used for training since March 2023 | ~30 days for abuse review (ZDR available) | [OpenAI API Data Usage Policies](https://openai.com/policies/api-data-usage-policies) |
| **Gemini API (paid via Vertex AI)** | ❌ No — paid-tier API data not used for training | Per Google Cloud contract | [Vertex AI data governance](https://cloud.google.com/vertex-ai/docs/general/data-governance) |
| **Gemini Free Tier** | ⚠️ **YES — Google AI uses free-tier prompts to improve products** | — | [Google AI Studio terms](https://ai.google.dev/gemini-api/terms) — **DO NOT use free-tier Gemini for confidential client matters.** |
| **DeepSeek V4 Pro API** | ❌ No — per DeepSeek API terms, inputs/outputs not used for model training | Retention policy less documented than OpenAI/Anthropic; verify for matter sensitivity | [DeepSeek API ToS](https://platform.deepseek.com/api-docs/legal) · **Note:** provider is China-based; consider jurisdictional data-residency requirements |

### What that does NOT mean — solicitor's residual risk

Even though API data is not used for training:

1. **Data IS in transit** during each query — it passes through the provider's infrastructure
2. **Brief logging retention** (typically 30 days) means the provider holds the data for that window
3. **Lawful access requests** — a subpoena, lawful intercept warrant, PDPA data-subject access request, or provider security incident could expose data during the retention window
4. **Provider-side breach risk** — however small, it exists

This is fundamentally different from local-LLM mode (where no data leaves your machine, ever, period). The `connect-local` command already configures Ollama + Qwen3 as the v0.1 default — solicitors handling confidential, privileged, or special-category data should stay in local-LLM mode for that work. The cloud-LLM tier exists for non-confidential research, public-law analysis, and template scaffolding where contractual no-training is a sufficient safeguard.

### Solicitor's decision

If your matter is:
- **General commercial / corporate / contract drafting** → Claude / OpenAI / paid Gemini API are appropriate. Contractual no-training protections are strong. Audit logs are local.
- **Legal-privileged client communication / privileged litigation strategy** → Evaluate against your jurisdiction's professional conduct rules. Most regulators permit reasoned use of cloud-AI with disclosure to the client. (See Singapore (LSRA) guidance.) Document the choice in your audit log.
- **PDPA special-category data / health / criminal record / political opinion** → Stay in `connect-local` (Ollama + Qwen3) mode. Do not opt into any cloud-LLM tier for these matters; do not use free-tier Gemini.
- **State secrets / classified material / under-seal court orders** → Stay in `connect-local` (Ollama + Qwen3) mode. For physically air-gapped networks where the pip-install / model-download / auto-update paths are also prohibited, await the v0.3+ signed offline-install bundle below.

The firm's audit log captures every API call (timestamp, agent, prompt-summary, output-summary) at `~/.ailawfirm-singapore/audit_logs/`. Logs never leave your machine. They are your professional-conduct compliance trail.

### v0.3+ roadmap

> What v0.1 already ships: (a) local-LLM default via `connect-local` (Ollama + Qwen3 — nothing leaves your laptop in local mode), (b) configurable cloud-LLM tier covering Claude / OpenAI / paid Gemini / DeepSeek, (c) Pseudonymisation Gateway sanitising PII before any cloud-LLM call, and (d) no first-party telemetry. The items below extend the floor — they are not a future replacement for what is already shipped.

- **Signed offline-install bundle** — the `pip install` path currently touches PyPI and the Ollama model registry; v0.3+ ships a signed offline-installable archive with the Qwen3 model pre-bundled, removing the last network-touch point even at install time. For solicitors on physically air-gapped networks (under-seal court matter rooms, state-secret-clearance environments).
- **In-firm LLM tenant adapter** — drop-in config for Azure OpenAI / private Vertex / on-prem vLLM endpoints. Distinct from the today-shipped public-API cloud-LLM tier; targets solicitors whose firm already provisions LLM infrastructure under its own DPA.
- **Expanded local-model surface** — Llama 3.3 70B / Qwen 2.5 72B / DeepSeek V4 Pro (open-weights via Ollama), for solicitors with larger laptops who want better-than-Qwen3-14b local reasoning.

Tracked at: [drafting-agents-core issues](https://github.com/Wolfgangrush/drafting-agents-core/issues).

---

## Recent fixes

- Unified the ChromaDB collection name across the MCP server and the CLI / search paths — drawers filed via MCP are now findable from the CLI, and vice-versa (the canonical name lives in `BrainConfig().collection_name`).
- Removed dead code: `KnowledgeGraph.seed_from_entity_facts` (referenced a non-existent `fact_checker.py` and was never called) and a no-op `signal_categories - {"pronoun"}` line in `entity_detector.py`.
- Consolidated two duplicate stop-word sets (`entity_detector.STOPWORDS` and `dialect._STOP_WORDS`) into a single shared module (`ailawfirm_singapore/stopwords.py`) imported by both; `mcp_server.py` now logs a warning on metadata-aggregation failures instead of swallowing them.

---

**No agenda · no telemetry · no cloud-default · MIT licensed · S$0 forever.**

**Singapore (LSRA) Rule compliance built into the tool's audit + transparency-gate architecture.** Solicitor remains professionally responsible for every output. The firm is a force-multiplier, not a substitute for judgment.

---

## 📁 Where your data lives

```
~/.ailawfirm-singapore/              ← Mac/Linux
C:\Users\YourName\.ailawfirm-singapore\  ← Windows
├── palace/                          ← all matter/client/citation memory (ChromaDB)
├── config.json                      ← your settings (AI provider · timezone · prefs)
├── calendars/                       ← generated .ics feeds for iPhone/Outlook subscribe
└── people_map.json                  ← optional client alias system (lock-screen safety)
```

Copy this folder to a USB drive · OneDrive · iCloud Drive · Dropbox = complete backup of your practice in 5 seconds.

---

## 🔄 How to update your firm

When a new version of AI Brain — Singapore is published, you pull it in with **one command**. Your matter data + your project-root `CLAUDE.md` are **never touched** — only the firm's installed code, skills, and prompts refresh.

### Path 1 — Plain terminal

```
ailawfirm-singapore update
```

Under the hood this runs `pip install --upgrade git+https://github.com/Wolfgangrush/ai-brain-singapore.git`. After it finishes, restart any open `ailawfirm-singapore` session so the new skills + prompts load.

### Path 2 — Inside Claude Code

Type:

```
/update
```

Claude runs the same command for you and reports the result.

### Path 3 — Inside Gemini CLI

Type:

```
/update
```

Same outcome — Gemini calls `ailawfirm-singapore update` for you.

### When to update

- **The publisher tells you** a new version is out → update.
- **Monthly hygiene** → update once a month so you stay current on skills + bug fixes.
- **After hitting a bug** → first thing to try is updating, in case it is already fixed upstream.

### What does NOT update (by design)

- Your matter folders (`~/Desktop/<your-firm>/<matter>/...`)
- Your project-root `CLAUDE.md` (your customisations always win)
- Your `~/.ailawfirm-singapore/` config + palace data
- Your chosen AI model setup (Ollama · DeepSeek · Claude · Gemini)

Only the firm's installed Python code, skills, and template files refresh. Your practice is unaffected.

### One catch — existing users + new template rules

If a new version updates the template `CLAUDE.md` (the firm's standing rules), your project-root `CLAUDE.md` is preserved because your customisations always win. To see what changed in the template after an update:

```
diff CLAUDE.md "$(python3 -c 'import ailawfirm_singapore, os; print(os.path.join(os.path.dirname(ailawfirm_singapore.__file__), "templates/CLAUDE.md"))')"
```

Review the diff and merge what you want into your own `CLAUDE.md`.

---

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(shipped)* — bootstrap: architecture, brain layer with 10-intent classifier, 7 specialist agents (4 live · 3 stubs), 3 working MCP tools (court · citation · calendar), connect-local one-command CLI, **17 Tier-1 statute digests** in `_statute_corpus/` (topic-level), **6 ROC 2021 drafting scaffolds** in `examples/drafting/`, LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance (audit checklist in [`AUDIT_v0.1.md`](AUDIT_v0.1.md)), Pseudonymisation Gateway privacy primitive wired in, native `scripts/leak_check.py` pre-push firewall
- **v0.2 — knowledge layer** *(shipped 2026-05-28)* — **55 drafting templates** in [`_drafting_data/`](_drafting_data/) covering the full litigation + commercial + regulatory backbone for Singapore solo practice: (a) civil pleadings extending the scaffolds — 5 templates (counterclaim · third-party notice · particulars · amendment · pre-action production); (b) motions and interim applications — 7 templates (summary judgment · striking-out · security for costs · anti-suit injunction · stay [IAA / AA / CCAA / forum non conveniens] · Mareva freezing · Anton Piller search); (c) evidence + disclosure + default judgment — 4 templates (production of documents · privilege log · expert letter of instruction · default judgment + set aside); (d) enforcement — 5 templates (WSS · garnishee · EJD · charging order + RECJA/REFJA/CCAA foreign-judgment recognition · committal under AJPA 2016); (e) appeals — 4 templates (CoA + Fifth Schedule · AD-HC default route · State Courts to HC · grounds + skeletal-arguments format); (f) skeleton arguments + counsel briefing — 4 templates (trial · interim · brief to counsel · counsel's advice on merits); (g) judicial review — leave + grounds (ROC 2021 Order 24 + GPA); (h) trial documentation — 3 templates (bundle + authorities · chronology + cast list + reading list · written closing submissions); (i) ADR — 2 templates (Mediation Act 2017 + Singapore Convention compliance); (j) insolvency under IRDA 2018 — 3 templates (winding-up Part 8 · judicial management Part 7 · bankruptcy Part 16); (k) tribunals — 2 templates (Employment Claims Tribunal + TADM · Small Claims Tribunal + Family Justice Courts); (l) commercial backbone — 7 templates (sale of goods · services · employment + PME · NDA + Man Financial restraint · shareholders + s 216 oppression · loan + Moneylenders Act · tenancy + commercial lease); (m) regulatory compliance — 8 templates (PDPA — DPA · breach · privacy policy · cross-border · IMDA AI governance + Model Card · Cybersecurity Act CII · Online Safety Act · MAS Notice 644 + TRM). All templates carry `PROVENANCE: CITED:_research/` cross-references.
- **v0.2 — frontend / UX layer** *(in progress)* — section-by-section statute depth on PDPA / LPA / MCA (verbatim section text from SSO) · Tier-2 statute coverage (Arbitration Act · IAA · Mediation Act · SoGA · AML statute-level) · ROC 2021 Form-number lock per court (Supreme Court / State Courts / FJC) · SICC procedural digest · matter dashboard · AML Tranche 2 readiness check — see [`BLOCKERS.md`](BLOCKERS.md) for the full v0.2 backlog
- **v0.3** *(following milestone)* — **firm mode** for multi-advocate practices · role/permission · matter assignment · conflict-check (LPCR Rule 21) · Solicitors' Accounts Rules-compliant client-account ledger
- **v0.4+** — LawNet / Singapore Statutes Online / Open Judgments cross-reference · Apple EventKit native integration · CalDAV bidirectional sync · property-conveyancing templates · trusts + estate planning · tax-controversy templates · sectoral specialisms (admiralty · SOPA construction · IP licensing · syariah court)

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇬🇧 UK · 🇦🇺 Australia · 🇦🇪 Dubai-DIFC · 🇪🇺 EU · 🇺🇸 USA — each as its own MIT-licensed repo.

---

## 🌐 Family Status (honest · cross-firm)

The wolfgang_rush AI Brain family ships across 7 jurisdictions. Honest status of the v0.2 legal-knowledge layer (statute corpus + drafting data) per firm:

| Firm | Statute corpus | Drafting corpus | Shared agents | GitHub |
|------|---|---|---|---|
| 🇮🇳 **India** | Native knowledge base · maintainer-curated | wolfgang_rush plugins (14 Indian-litigation plugins · separate stack) | Not applicable — Indian-specific | ✅ LIVE |
| 🇪🇺 **EU** | ✅ 11 statutes · 8/8 Tier-1 | ✅ **56 templates** · litigation + commercial complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇺 **Australia** | ✅ 13 Tier-1 statute digests + 39 research files | ✅ **79 templates** · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇪 **Dubai-DIFC** | ✅ 24 statute digests · dual-track (15 DIFC + 9 Mainland UAE Federal) · v0.2 closed 2026-05-29 | ✅ **81 templates** · dual-track DIFC + Mainland · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇸🇬 **Singapore** | ✅ 17 statute digests Tier-1 | ✅ **55 templates + 6 scaffolds** · litigation + commercial + regulatory complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇬🇧 **UK** | ✅ 10 statute digests Tier-1 | ✅ **107 templates** · litigation + commercial + Tier-3 specialist + procedural anchors complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇺🇸 **USA** | ✅ 23 federal-first Tier-1 statute digests | ✅ **89 templates** · all 13 litigation categories + commercial + corporate complete (v0.2 closed 2026-05-29) | ✅ Migrated | ✅ LIVE |

**Plus:**
- **AI Startup Firm — India v0.1** (legal-ops brain for founders)
- **GC In-House Brain** (multi-jurisdictional, 8 modules — 3 live · 5 shipping v0.2+)

Both share the same `drafting-agents-core` architecture pattern.

All firms migrated to the central [drafting-agents-core](https://github.com/Wolfgangrush/drafting-agents-core) agent library on 2026-05-20 (Path B-Lite) — single source of truth for the agent layer; jurisdictional knowledge stays per-firm.

---

## 📚 Documentation

| File | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Layman-friendly 30-minute tour |
| [DISCLAIMER.md](DISCLAIMER.md) | Full legal disclaimer · LPCR Rule 8 firewall · PDPA controller/processor analysis · UPL exclusion |
| [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) | Zero-collection architecture · PDPA Section 26 cross-border analysis |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting · coordinated disclosure · security hygiene |
| [MODEL_SETUP.md](MODEL_SETUP.md) | Honest privacy table · local vs cloud · third-party CLI tool warning |
| [SCOPE.md](SCOPE.md) | What's in v0.1, what's not, falsification rules |
| [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) | Every domain claim's source (CITED:<research-file>) |
| [_statute_corpus/INDEX.md](_statute_corpus/INDEX.md) | Statute corpus index — 17 Tier-1 digests + coverage map + v0.2 backlog |
| [_statute_corpus/_STATUTE_CORPUS_SUMMARY.md](_statute_corpus/_STATUTE_CORPUS_SUMMARY.md) | Corpus summary — authoritative sources used · currency warnings · gaps |
| [examples/drafting/README.md](examples/drafting/README.md) | Drafting scaffolds README — 6 ROC 2021 templates + discipline notes |
| [BLOCKERS.md](BLOCKERS.md) | Known limitations + v0.2 backlog (8 tracked items) |
| [AUDIT_v0.1.md](AUDIT_v0.1.md) | LEGAL_EXPOSURE_PLAYBOOK §4 Pre-Ship Checklist run |
| [PII_SCAN_v0.1.md](PII_SCAN_v0.1.md) | Pre-push firewall sweep (run via `python3 scripts/leak_check.py`) |

---

## 🙏 Credits

- **Engine — all architectural credit:** [MemPalace](https://github.com/MemPalace/mempalace) — the highest-scoring open-source AI memory system ever benchmarked (96.6% LongMemEval R@5), MIT-licensed. Downstream fork of MemPalace 3.0.0. All architectural credit to the MemPalace Contributors.
- **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). MIT-licensed legal-tech publisher.
- **Inspired by:** every Singapore solo advocate who's worked Saturday morning on a State Courts mention list.

---

## ⚠️ Disclaimer

This tool helps you organize your practice. It does **NOT** give legal advice. It does **NOT** replace your professional judgment. It does **NOT** solicit work on your behalf. LPCR Rule 8 publicity/solicitation firewall is built in but **YOU** remain responsible for compliance with all bar conduct rules, PDPA, AML/CTF, and Solicitors' Accounts Rules.

The publisher is not admitted in Singapore. The publisher does not offer legal services in Singapore. This is a software publication under the MIT License.

Ships AS-IS without warranty. See [LICENSE](LICENSE).

---

## 📞 Support

- **Issues / bugs:** https://github.com/Wolfgangrush/ai-brain-singapore/issues
- **Translation help:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) (Mandarin · Bahasa · Tamil PRs welcome)
- **Want to add a feature?** Open an issue with `[feature-request]` label

---

`Let's begin. 让我们开始. Mari kita mulakan. ஆரம்பிக்கலாம்.` 🙏
