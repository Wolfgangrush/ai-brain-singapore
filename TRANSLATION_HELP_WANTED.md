# TRANSLATION_HELP_WANTED.md — AI Brain · Singapore · v0.1

## Community language + jurisdiction review call

AI Brain Singapore ships in English (the default working language of Singapore courts + LPCR). Community reviewers from Singapore's multilingual practitioner base + Singapore-admitted advocates and solicitors are welcomed for:

1. Native-English Singapore-legal-register review of [`GETTING_STARTED.md`](GETTING_STARTED.md).
2. Future-language onboarding contributions (Mandarin · Bahasa Melayu · Tamil) for Singapore's multilingual public.
3. Singapore-admitted-practitioner review of statute digests + drafting templates for currency + accuracy against Practice Directions of the Supreme Court of Singapore + State Courts.

---

## How to help

1. **Pick a contribution area** from the table below.
2. **Read** the existing materials in this repo.
3. **Compare** against the current Singapore Statutes Online / Practice Direction state.
4. **Fix** anything inaccurate, outdated, or unidiomatic.
5. **Submit a PR** with the title:
   - `fix(i18n): <language> onboarding draft` for new language onboarding.
   - `fix(law): <statute|template> currency review` for legal currency updates.
   - `fix(register): native Singapore-legal-register review` for English review.

---

## Contribution areas

| Area | File / Folder | Status | Needs |
|---|---|---|---|
| English onboarding | [`GETTING_STARTED.md`](GETTING_STARTED.md) | AUTHORITATIVE | Singapore-admitted practitioner native-register review |
| Mandarin onboarding | (not yet created) | open | Singapore-Mandarin-speaking practitioner draft |
| Bahasa Melayu onboarding | (not yet created) | open | Singapore-Malay-speaking practitioner draft |
| Tamil onboarding | (not yet created) | open | Singapore-Tamil-speaking practitioner draft |
| ROC 2021 form numbers | [`_drafting_data/`](_drafting_data/) | shipped | Verify Form numbers against current Practice Direction |
| Statute currency | [`_statute_corpus/`](_statute_corpus/) | shipped | Verify against current Singapore Statutes Online |
| Practice Direction cross-refs | Various | shipped | Cross-check Supreme Court + State Courts PDs |
| FJC family law currency | `121-tribunal-small-claims-and-family-court.md` | shipped | Verify against current Family Justice Rules 2014 |

## What to look for

- **Singapore-specific legal terminology**: "Originating Claim" (post-ROC 2021) not "Writ of Summons" · "Originating Application" not "Originating Summons" · "Supreme Court of Singapore" subdivisions (General Division HC · Appellate Division HC · Court of Appeal).
- **SAL neutral-citation format**: `[YYYY] SGCA NN` · `[YYYY] SGHC NN` · `[YYYY] SGAD-HC NN`.
- **LPCR registers**: formal Singapore-court submissions vs client-advisory register.
- **Form numbers**: verify against current Supreme Court / State Courts / FJC Practice Directions.
- **Statute citations**: Singapore Statutes Online (sso.agc.gov.sg) authoritative.

---

## What we can't accept

- Translations of substantive legal advice (the templates are software anchors, not advice).
- Content that introduces internal codes, palace tags, or any maintainer-private references.
- PRs that move sensitive jurisdictional information into the public repo.

---

## Reporting issues

If you spot something that needs immediate attention but can't PR it yourself:

- 🐛 **File an issue** → [github.com/Wolfgangrush/ai-brain-singapore/issues](https://github.com/Wolfgangrush/ai-brain-singapore/issues)
- 💬 **General questions** → start a discussion in the repo
- 📚 **Authority verification** → [`KNOWLEDGE_PROVENANCE.md`](KNOWLEDGE_PROVENANCE.md) catalogues every authority cited

**Terima kasih · 谢谢 · நன்றி · Thank you for helping make AI Brain Singapore better for the entire Singapore solo bar.** 🇸🇬
