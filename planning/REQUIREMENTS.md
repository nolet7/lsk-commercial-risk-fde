# Traceable engineering requirements

| ID | Priority | Requirement | Acceptance test |
|---|---|---|---|
| FR-01 | P0 | Screen requested synthetic entity | API unit/integration test |
| FR-02 | P0 | Bounded graph paths with evidence | graph fixture test |
| FR-03 | P0 | Ambiguous match demands review | future adjudicated goldens |
| FR-04 | P0 | Durable idempotent jobs | future crash/restart integration |
| FR-05 | P0 | Tenant isolation at data/resource layer | future cross-tenant attack tests |
| FR-06 | P0 | Licensed provider entitlements respected | future provider contract tests |
| FR-07 | P1 | Parquet export with manifest | future reconciliation tests |
| FR-08 | P1 | Pipeline quality gating | future Airflow failure drills |
| FR-09 | P1 | Case approvals audited | future role/state machine tests |
| NFR-01 | P0 | API 99.9% monthly proposed | future SLO instrumentation |
| NFR-02 | P0 | Recovery RPO 1h/RTO 4h proposed | future restore drill |
| NFR-03 | P0 | No automatic legal determination | security/policy review |
| NFR-04 | P1 | Documented independent handover | future operator exercise |

All future tests and gates remain NOT IMPLEMENTED until validated.
