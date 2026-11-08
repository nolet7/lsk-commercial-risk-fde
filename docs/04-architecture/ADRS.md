# Architecture decision register

| ID | Decision | Status | Rationale / approval needed |
|---|---|---|---|
| ADR-001 | AWS primary cloud | Proposed | Existing customer IAM/S3 integration; cost verification |
| ADR-002 | Local demo API key must never ship to production | Accepted guardrail | OIDC JWT, scoped identity, authorization and audit required |
| ADR-003 | Choose Neo4j vs Neptune after workload-specific benchmarks | Open | Query semantics, operations, cost and export restrictions |
| ADR-004 | SQS + transactional outbox for async jobs | Proposed | Avoid acknowledging jobs without durable persistence |
| ADR-005 | Tenant isolation with explicit data-level enforcement | Required | No cross-tenant reads, writes, caches or exports |
| ADR-006 | Licensed provider contract and allowed use only | Required | Proprietary data and sanctioned export rights |
| ADR-007 | LLM draft is never automatic compliance adjudication | Required | Evidentiary, privacy and model limitations |
| ADR-008 | Recovery targets RPO 1h, RTO 4h initial proposal | Open | Must be tested and approved by customer |
