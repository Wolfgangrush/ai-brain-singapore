"""
Acceptance tests (TDD) — Singapore jurisdiction-native agents.

Opus-owned CONTRACT. Written RED against the v0.1 stubs; the delegate fleet
implements the three agents (drafting / deadline / matter) to GREEN.

Each agent is asserted on THREE axes:
  1. SHAPE      — return-dict keys stay compatible with brain.router + brain.specialists.
  2. SG-NATIVE  — Limitation Act 1959 (NOT the 1963 Act) · ROC 2021 doc types ·
                  ~/.ailawfirm_singapore matter store.
  3. NO RESIDUE — nothing Indian may appear in any output (CrPC/BNSS/writ/SLP/482/
                  Limitation Act 1963/indian-* skills/ailawfirm-india path).

Design intent: the SG agents mirror the SHAPE of India's real agents
(agents/{drafting,deadline,matter}_agent.py in ai-brain-india) but carry
Singapore content, so a Singapore lawyer who downloads THIS brain and drafts
gets ROC-2021 pleadings + Cap-163/1959 limitation periods — never Indian output.
"""

import inspect
import re


from ailawfirm_singapore.agents import deadline_agent, drafting_agent, matter_agent

# Any of these appearing in an OUTPUT = India residue leak = fail.
INDIA_RESIDUE = re.compile(
    r"\b1963\b|CrPC|BNSS|\bwrit\b|\bSLP\b|\b482\b|\b528\b|NI Act|Order VIII|"
    r"anticipatory\s+bail|indian-hc-drafting|supreme-court-drafting|"
    r"indian-rent-control|indian-tax|personaldraftingstack|"
    r"ailawfirm[-_]india|Limitation Act 1963",
    re.I,
)


def _flat(d: dict) -> str:
    return " ".join(str(v) for v in d.values())


# ────────────────────────── deadline_agent (Limitation Act 1959) ──────────────────────────
class TestDeadlineSingapore:
    def test_contract_six_years_LA1959(self):
        r = deadline_agent.handle("limitation period for a breach of contract claim")
        blob = _flat(r)
        assert "6 year" in blob.lower()
        assert re.search(r"Limitation Act 1959", blob), "must cite the SG statute"
        assert re.search(r"\bs\.?\s*6\b|section\s*6", blob, re.I)

    def test_tort_six_years(self):
        r = deadline_agent.handle("negligence tort claim for damage suffered")
        assert "6 year" in _flat(r).lower()

    def test_recovery_of_land_twelve_years(self):
        r = deadline_agent.handle("action to recover land / immovable property")
        assert "12 year" in _flat(r).lower()

    def test_enforce_judgment_twelve_years(self):
        r = deadline_agent.handle("enforce a judgment debt")
        assert "12 year" in _flat(r).lower()

    def test_personal_injury_three_years_s24A(self):
        r = deadline_agent.handle("personal injury claim from an accident")
        blob = _flat(r)
        assert "3 year" in blob.lower()
        assert "24A" in blob or "24a" in blob.lower()

    def test_computes_deadline_and_days_remaining_when_date_present(self):
        r = deadline_agent.handle("breach of contract that accrued on 12 January 2020")
        assert r.get("deadline"), "ISO deadline expected when a start-date is supplied"
        assert r.get("days_remaining") is not None

    def test_shape_keys(self):
        r = deadline_agent.handle("contract claim")
        for k in ("agent", "category", "article", "period"):
            assert k in r, f"missing key {k}"

    def test_no_india_residue(self):
        for q in ["contract claim", "appeal to court", "cheque dishonoured", "recover a debt"]:
            assert not INDIA_RESIDUE.search(_flat(deadline_agent.handle(q))), q


# ────────────────────────── drafting_agent (ROC 2021 → SG templates) ──────────────────────────
class TestDraftingSingapore:
    def test_statement_of_claim_routes_to_sg_template(self):
        r = drafting_agent.handle("draft a statement of claim for a debt-recovery matter")
        blob = _flat(r).lower()
        assert "statement of claim" in r.get("doc_type", "").lower()
        # must point at the SG template / local draft-with-docx skill, not an Indian plugin
        assert ("statement-of-claim" in blob) or ("draft-with-docx" in blob)

    def test_originating_claim_recognised(self):
        r = drafting_agent.handle("draft an originating claim under ROC 2021")
        assert "originating claim" in r.get("doc_type", "").lower()

    def test_defence_recognised(self):
        r = drafting_agent.handle("draft a defence to the statement of claim")
        assert "defence" in r.get("doc_type", "").lower()

    def test_affidavit_recognised(self):
        r = drafting_agent.handle("draft a supporting affidavit")
        assert "affidavit" in r.get("doc_type", "").lower()

    def test_shape_keys(self):
        r = drafting_agent.handle("draft an originating application")
        assert "doc_type" in r and "suggested_skill" in r

    def test_no_india_residue(self):
        # even Indian-flavoured requests must NOT echo Indian doc types / plugins
        for q in [
            "draft a statement of claim",
            "draft a writ petition",
            "draft an SLP",
            "draft a bail application",
        ]:
            assert not INDIA_RESIDUE.search(_flat(drafting_agent.handle(q))), q


# ────────────────────────── matter_agent (SG local store) ──────────────────────────
class TestMatterSingapore:
    def test_store_path_is_singapore_not_india(self):
        src = inspect.getsource(matter_agent)
        assert ".ailawfirm_singapore" in src, "matter store must live under ~/.ailawfirm_singapore"
        assert ".ailawfirm-india" not in src and ".ailawfirm_india" not in src

    def test_add_then_list_roundtrip(self, tmp_path, monkeypatch):
        # redirect the store to a temp file; impl must expose a redirectable _STORE_PATH
        store = tmp_path / "matters.json"
        monkeypatch.setattr(matter_agent, "_STORE_PATH", store, raising=False)
        matter_agent.handle("add matter Tan Wei Ming v Lee Holdings Pte Ltd")
        listed = matter_agent.handle("list matters")
        assert "Tan Wei Ming" in _flat(listed)

    def test_shape_keys(self):
        r = matter_agent.handle("list matters")
        assert r.get("agent") == "matter_agent"

    def test_no_india_residue(self):
        for q in ["add matter ABC", "list matters", "status of XYZ"]:
            assert not INDIA_RESIDUE.search(_flat(matter_agent.handle(q))), q
