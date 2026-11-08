# Controlled pilot plan

Cohort: one designated business unit and approved users; data access limited to signed approval and provider entitlement. First run shadow mode to compare with existing manual process. Start with bounded batch volume and expand using objective gates.

## Required work
1. Integrate customer source via typed schemas and controlled credential boundaries.
2. Implement MWAA DAG: source availability, landing, validation, Glue Spark transform, screening jobs, reconciliation, version promotion, notification.
3. Build durable outbox, SQS workers, retries, DLQ, observability, and case workflow.
4. Generate Parquet and CSV data products with authoritative manifests and provenance.
5. Train customer analysts and capture their accept/reject decisions.

## Exit
Documented accuracy by cohort, three representative run cycles including failure recovery, acceptable backlog/latency and signed G2/G3 proposal. Production remains blocked pending security and business approvals.
