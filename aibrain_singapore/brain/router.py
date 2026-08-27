"""Brain router."""

import importlib
from aibrain_singapore.brain.intents import Intent, AGENT_FOR_INTENT


def route(intent: Intent, payload: str) -> dict:
    agent_module_name = AGENT_FOR_INTENT.get(intent, "matter_agent")
    full_module = f"aibrain_singapore.agents.{agent_module_name}"
    try:
        mod = importlib.import_module(full_module)
        handler = getattr(mod, "handle", None)
        if handler is None:
            return {
                "ok": False,
                "intent": intent.value,
                "agent": agent_module_name,
                "error": f"agent module {full_module} has no handle()",
            }
        result = handler(payload)
        return {"ok": True, "intent": intent.value, "agent": agent_module_name, "result": result}
    except ImportError as e:
        return {
            "ok": False,
            "intent": intent.value,
            "agent": agent_module_name,
            "error": f"agent module import failed: {e}",
        }


def think(text: str) -> dict:
    from aibrain_singapore.brain.classifier import classify

    intent = classify(text)
    response = route(intent, text)

    # AI-backed specialist answer when a host LLM is available (Claude / GLM / Codex / AGY).
    # Offline-safe: specialists.answer() returns None when no ANTHROPIC_* env is present,
    # so the structured result is returned unchanged and deterministic tests still pass.
    try:
        from aibrain_singapore.brain import specialists

        grounding = response.get("result", {}) if isinstance(response, dict) else {}
        ai = specialists.answer(intent.value, text, grounding)
        if ai:
            response["answer"] = ai
    except Exception:
        pass

    return response
