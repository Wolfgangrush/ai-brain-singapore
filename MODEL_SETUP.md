# 🤖 AI Model Setup — Singapore · Honest Privacy Guide

The tool itself stores everything on your laptop. But to do "smart" work (drafting, conversation, reasoning) you connect it to an AI model. **Where that model runs determines your privacy.**

This guide is honest about every option. No marketing fluff. Read before you pick.

> **For client matters and PDPA-sensitive work: use local-only mode (Option A).**

---

## 🎯 The honest privacy table

| Option | Where it runs | Who can see your queries | Cost | Best for |
|---|---|---|---|---|
| 🥇 **Ollama + Qwen3 (local)** | Your laptop | ONLY you | S$0 forever | **Client matters · PDPA-sensitive · LPCR Rule 8 confidentiality work** |
| 🥈 **DeepSeek API** | DeepSeek servers (China) | DeepSeek (unless opted-out) | ~S$2-5/mo moderate use | NON-client work · drafting templates · research summaries |
| 🥉 **Claude API** | Anthropic servers (USA) | Anthropic (per their privacy policy) | ~S$25-80/mo | Heavy daily users after first paid engagement |
| 🥉 **Gemini API** | Google servers (USA + globally) | Google | ~S$8-30/mo | Long-PDF reads · large research synthesis |

---

## 🥇 Option A — Ollama + Qwen3 (local · RECOMMENDED · DEFAULT)

### Why this is the right choice for Singapore practice

- Model runs ON YOUR LAPTOP. Your queries never leave the machine.
- No internet needed after one-time model download.
- No PDPA Section 26 cross-border transfer concern.
- No LPCR Rule 8 confidentiality concern.
- Suitable for handling actual client matters, draft pleadings, confidential research.
- Compatible with Singapore Judiciary AI Guidelines October 2024 on confidentiality preservation.

### One-command install (NEW — local-AI bridge)

```bash
ailawfirm-singapore connect-local
```

This single command:
1. Detects if Ollama is installed; installs it if missing (macOS via Homebrew · Linux via shell script · Windows: prompts you to download)
2. Downloads the recommended model (Qwen3:14b for 16GB+ RAM · Qwen3:7b for 8GB RAM)
3. Writes `~/.ailawfirm-singapore/config.json` with the right Ollama settings
4. Runs a smoke test to confirm local connectivity
5. Reports ready

After this, every CLI invocation routes to local Ollama. **No queries leave your laptop.**

### Manual install (if you prefer)

**Mac:** `brew install ollama` (or download from https://ollama.com/download/Mac)
**Windows:** Download installer from https://ollama.com/download
**Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

```
ollama pull qwen3:14b
```

Alternative models if you have less storage:
- `ollama pull qwen3:7b` — 4 GB · slightly worse quality, faster
- `ollama pull llama3.3:8b` — 5 GB · Meta's model, decent
- `ollama pull mistral:7b` — 4 GB · good European model

Then edit `~/.ailawfirm-singapore/config.json`:

```json
{
  "ai_provider": "ollama",
  "ollama_model": "qwen3:14b",
  "ollama_host": "http://localhost:11434"
}
```

Restart `ailawfirm-singapore`. It now uses local Ollama.

### Tradeoffs (honest)

- Slower than cloud APIs (maybe 2-5x slower depending on your laptop)
- Quality is slightly lower than top cloud models (but improving rapidly)
- Uses laptop battery + RAM during use
- Best on machines with 16 GB+ RAM (will work on 8 GB but tightly)

### Hardware reality check

- MacBook Air M1/M2 8GB: works with `qwen3:7b` (smaller model)
- MacBook Air M2/M3/M4 16GB+: works smoothly with `qwen3:14b`
- Windows laptop with 16GB RAM + dedicated GPU: works well with `qwen3:14b`
- Older Windows laptops (4-8GB RAM, no GPU): use `qwen3:7b` or smaller
- Phone/tablet: not supported for local model (use Option B/C/D)

---

## 🥈 Option B — DeepSeek API (cheap cloud · NOT for client work)

### Why solo advocates sometimes use DeepSeek

- **Cheapest** capable cloud model right now (~10-20× cheaper than Claude/GPT)
- Anthropic-compatible API
- Strong on agentic / tool-use workloads

### MANDATORY privacy setup before any use

DeepSeek's default ToS permits use of API inputs for model training. **You must opt out.**

1. Go to https://platform.deepseek.com → Settings → Privacy
2. Toggle OFF "Allow my API requests to be used for model training"
3. Save

Even after opt-out, DeepSeek servers (located in China) process your queries in transit. This may have implications under PDPA Section 26 (cross-border transfer requires comparable protection or appropriate safeguards). **For client matter data, do NOT use DeepSeek even with opt-out.**

### Use case

DeepSeek is acceptable for:
- Drafting generic templates (no client data)
- Researching public statute summaries
- Generating non-confidential learning notes

DeepSeek is NOT acceptable for:
- Client matter analysis
- Pleadings involving named parties
- Anything covered by LPCR Rule 8 confidentiality
- Anything covered by PDPA Section 26 restrictions

### Setup

```bash
ailawfirm-singapore connect-cloud --provider deepseek --cloud-warning-acknowledged
```

You will be prompted to paste your DeepSeek API key. The key is stored in `~/.ailawfirm-singapore/config.json` (file mode 0600, owner-readable only).

---

## 🥉 Option C — Claude API (Anthropic)

Best for power users who want top-tier reasoning. Privacy posture: Anthropic does not use API inputs for training (per their public policy). But queries still cross into Anthropic's USA servers — still cross-border for Singapore, still PDPA Section 26 territory.

```bash
ailawfirm-singapore connect-cloud --provider anthropic --cloud-warning-acknowledged
```

---

## 🥉 Option D — Gemini API (Google)

Best for long-PDF synthesis. Privacy posture: Google's terms vary by tier (paid Workspace tier has better data-isolation than free tier). Read the specific tier's terms before use.

```bash
ailawfirm-singapore connect-cloud --provider gemini --cloud-warning-acknowledged
```

---

## ⚠️ Cloud-mode consent screen

Whenever you enable any cloud option, the CLI displays:

```
⚠️  CLOUD MODE WARNING

You are about to enable cloud AI processing via [VENDOR].

Your queries will leave your laptop and be processed on [VENDOR]'s servers.

DO NOT use cloud mode for:
  ❌ Confidential client matter data
  ❌ Personal data of identified individuals
  ❌ Anything covered by LPCR Rule 8 confidentiality
  ❌ Anything covered by PDPA Section 26 cross-border restrictions

The publisher (wolfgang_rush) is NOT in this data path. You contract directly
with [VENDOR] under their terms of service.

Type 'I understand · proceed' to continue, or press Ctrl+C to cancel.
```

You must type the exact phrase to proceed. This friction is intentional.

---

## Switching back to local-only

```bash
ailawfirm-singapore connect-local
```

This overwrites the cloud configuration and restores local Ollama as the active provider. Your cloud API keys are NOT deleted (you can switch back later); they are just inactive.

---

---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

If you integrate this Software with **any third-party AI service, CLI tool, or AI-assisted IDE** — including but not limited to: **Anthropic Claude API · Claude CLI · Claude Code · OpenAI API · Codex CLI · Google Gemini API · Gemini CLI · DeepSeek API · OpenCode · Cursor · GitHub Copilot · JetBrains AI · Mistral · Cohere · HuggingFace inference · Groq · Together AI · Qwen API · or any other model provider, CLI, IDE, or AI-assisted tool** — you do so **at your own risk** and under the terms of service of that third-party tool.

The publisher (wolfgang_rush · Rushikesh R. Mahajan):

- Does **NOT** recommend any specific third-party tool
- Does **NOT** receive any compensation, referral fee, or benefit from any third-party tool's adoption
- Does **NOT** verify any third-party tool's privacy posture, security, or compliance with your jurisdiction's law
- Accepts **NO** responsibility for your choice of third-party tooling
- Accepts **NO** responsibility for any data leakage, confidentiality breach, professional-conduct violation, regulatory non-compliance, or any other harm resulting from your use of third-party tools alongside this Software
- Makes **NO** warranty that any third-party tool is suitable for legal-professional use in any jurisdiction

**You are solely responsible** for:

- Reading the privacy policy and terms of service of each third-party tool before connecting it
- Ensuring compliance with all confidentiality rules, data-protection laws, sectoral regulations, and bar conduct rules that apply to your practice
- Obtaining client consent where required before routing client data through any third-party tool
- Verifying that the third-party tool does not retain, train on, or share your queries in ways that breach your professional obligations
- Managing API keys, access tokens, and credentials securely (do not commit them to version control; use environment variables or a password manager)
- Independently verifying any output produced by a third-party tool before client-facing use

**This warning applies regardless of which third-party tool you choose, and regardless of any privacy claim that tool makes.** The responsibility to verify and the liability for use rest entirely with you.

---


*This document references LEGAL_EXPOSURE_PLAYBOOK §2(a) (Local-AI-Only Default pillar), §3.V4 (Data Protection). Playbook version: v0.1.*
