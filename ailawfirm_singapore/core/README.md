# core/ — Shared Domain Logic

Used by BOTH solo and firm modes:
- `ontology.py` — MatterType · SingaporeCourt · SingaporeStatute · SingaporeBarRule + Matter and Citation dataclasses
- `courts/` — court hierarchy + jurisdiction
- `citations/` — Singapore citation format parsers (SLR · SGCA · SGHC)
- `statutes/` — PDPA · CPC · PC · LPA · ROC etc. (v0.2+ adds real text)
- `calendar/` — ICS writer + publishers (ADR-002 D4)

Anything that depends on Singapore jurisdiction lives here. Anything that depends on practice size lives in solo/ or firm/.
