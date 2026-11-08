# LSK Commercial Risk Intelligence Platform (CRIP)

**Status: portfolio reference implementation / synthetic data only. Not an actual Sayari deployment or production-certified financial crime control.**

An end-to-end Forward Deployed Engineering customer engagement: CTO mandate → discovery → evaluation → POC → pilot → security review → production readiness → handover and field-to-product feedback.

## What is implemented
- Typed FastAPI service with versioned API, synthetic entity lookup, bounded ownership graph traversal, and in-memory screening results.
- Deterministic fictional corporate network and simple, explicitly non-regulatory risk signals; shared-key header authentication **local demo only**.
- Unit and API tests, CI workflow, container packaging, sample SQL and Spark/Airflow designs.
- Extensive architecture, threat model, requirements, phased workplan, customer acceptance, and operating playbooks.

## Important limitations
- All companies, persons, and risk references are **fictional**; data is not Sayari's Commercial World Model.
- The API uses an in-memory fixture and demonstration API-key authentication; **never deploy the demo authentication or in-memory state to production**.
- Sanctions signals are *investigation indicators*, not legal determinations. Legal interpretation, aggregation and control rules are not implemented.
- No customer data, sanctioned-name lists, or credentials are bundled.
- AWS Terraform, real Sayari API credentials, graph database, persistent case store, orchestrated Spark execution, security approvals, and production deployment remain explicit future milestones.

## Quick start
```bash
python -m venv .venv
# Windows Git Bash: source .venv/Scripts/activate
# Linux/macOS: source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
uvicorn crip_api.main:app --reload
```

Local-only demo header: `X-Demo-Key: local-synthetic-demo-key` (change or disable before exposing externally). Open `http://127.0.0.1:8000/docs`.

```bash
curl -H 'X-Demo-Key: local-synthetic-demo-key' http://127.0.0.1:8000/v1/entities
curl -H 'X-Demo-Key: local-synthetic-demo-key' http://127.0.0.1:8000/v1/graphs/meridian-trading
curl -X POST http://127.0.0.1:8000/v1/screenings -H 'X-Demo-Key: local-synthetic-demo-key' -H 'Content-Type: application/json' -H 'Idempotency-Key: demo-001' -d '{"entity_id":"meridian-trading"}'
```

## Delivery navigator
Start with [`docs/01-mandate/CTO_MANDATE.md`](docs/01-mandate/CTO_MANDATE.md), then [`planning/ROADMAP.md`](planning/ROADMAP.md), [`docs/04-architecture/SYSTEM_DESIGN.md`](docs/04-architecture/SYSTEM_DESIGN.md), and [`docs/07-security/THREAT_MODEL.md`](docs/07-security/THREAT_MODEL.md).

## Scope guardrails
1. Only approved/licensed APIs and data rights may be used with a real provider.
2. No fully automated adverse compliance decisions. Ambiguity → human review.
3. Customer PII and investigation evidence remain in approved access domains.
4. Deployment claims require objective proof; a passing unit suite is not a production sign-off.
