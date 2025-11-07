# UGFT Chapter‑0 DSL (Python‑only bundle)
This folder contains the canonical Chapter‑0 implementation and tests.
## Quick start
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```
## Files
- `ugft_forms.py` – Chapter‑0 DSL and physics helpers
- `test_ch0.py` – main correctness tests
- `test_ch0_edges.py` – edge cases (IBP, *^2, Wick, BRST, etc.)
- `test_ch0_curved_perf.py` – FRW curvature/Bianchi + projector checks
- `test_ch0_perf_curved.py` – compatibility test (name/order the user used)
