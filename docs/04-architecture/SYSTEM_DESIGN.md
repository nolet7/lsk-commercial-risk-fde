# System design | production target, not implemented state

## C4 context
Customer banking/KYC systems → LSK ingestion/API → licensed commercial intelligence provider or synthetic test adapter → normalized identity/ownership graph → screening rules → human case review → customer export / BI. Platform observability and access governance span the flow.

## Containers and control plane
- **API:** FastAPI on EKS behind authenticated gateway/WAF; asynchronous long jobs use a queue and durable state machine. Request-level policy enforces tenant/resource scopes.
- **Connectors:** provider interface, typed DTOs, per-tenant entitlement enforcement, schema contract tests, explicit upstream quotas, bounded retry and egress restrictions.
- **Data plane:** S3 raw/quarantine/validated/curated partitions, AWS Glue PySpark transforms, Athena for analytics and MWAA for orchestrated ingestion with freshness metrics.
- **System of record:** RDS PostgreSQL for cases, outbox, screening state and audit metadata; production storage segregated by tenant/authorized workload.
- **Graph:** Neptune or Neo4j only after graph POC validates traversal cost, freshness and auditability; temporal edges with direction, controls, percentages, validity window and provenance.
- **Messaging:** SQS with DLQ, request-id keyed idempotency, outbox/inbox for durable enqueue; bounded retries, poison-message isolation, replay by authorized operator.
- **BI:** Grafana for SLOs, Metabase for authorized business views, telemetry redaction and label cardinality control.
- **LLM:** optional evidence-grounded draft only; human review, egress/data processor approval and prompt-injection assessment.

## Data contracts
`tenant_id`, `source_system`, `source_record_id`, `record_version`, `effective_at`, `observed_at`, `ingested_at`, `classification`, `schema_version`, `provenance`, `checksum`. Event updates require immutable source versions; corrections supersede rather than silently erase evidence.

## Graph correctness
Ownership economic percentages are NOT a substitute for legal sanctions tests. Graph traversal must handle multiple paths without double counting, cycles, invalid dates, direct vs indirect ownership, control, aggregation and jurisdiction-specific interpretation. Policy version and counsel approval required.

## Critical request sequence
Caller auth → tenant authorization → validate → durable job ID/outbox transaction → queue → resolve/provider calls → evidence snapshot → evaluate rules → case triage → result status; downstream export only when quality & consent gates pass.

## ADRs required
ADR-001 AWS primary; ADR-002 demo/local vs production identity; ADR-003 graph store selection; ADR-004 async job outbox; ADR-005 tenant isolation; ADR-006 provider data rights; ADR-007 LLM boundary; ADR-008 recovery/retention.

## Performance budgets
Cached lookup p95 <500ms proposed; live calls budgeted separately. Bulk 100k synthetic entities benchmarked to agreed run window. Define tenant concurrency, graph depth, IO/CPU caps and cost ceilings before pilot.
