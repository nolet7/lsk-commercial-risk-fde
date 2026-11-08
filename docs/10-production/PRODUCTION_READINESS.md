# Production release checklist | all initially unchecked

- [ ] Approved data processing and provider licenses
- [ ] Owner-approved governance rules; human escalation and no automated legal disposition
- [ ] Customer UAT: happy path, ambiguous, erroneous and unavailable-provider scenarios
- [ ] OIDC, machine identities, resource-level tenant isolation, export RBAC
- [ ] Encryption, egress control, retention rules, data deletion/legal hold procedures
- [ ] Threat model, pen test, secret scan, dependency scan, SBOM, artifact provenance
- [ ] Durable jobs, outbox, DLQ and safe replay validated
- [ ] Performance/load testing and SLO/error budget signoff
- [ ] Backup restore, RPO/RTO and outage drills performed
- [ ] Audit trail and independent reconciliation validated
- [ ] Observability, alerts, paging and runbooks accepted by operators
- [ ] Rollout/rollback plans and release signatories recorded
- [ ] Budget, quota, billing alerts and support contract approved

Proposed rollout: shadow → limited users → expanding tenant-approved volume → full supported workload. Abort if critical data mismatch, false clearance, security exposure, provider license violation or untracked accepted jobs.
