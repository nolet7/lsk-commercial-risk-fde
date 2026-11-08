# On-call runbook: source/provider errors or stale data

**Trigger:** freshness SLI breached, >=threshold upstream 429/5xx, queue age growth, invalid dataset manifest, or investigation integrity defect.

1. Create incident ID, record start time, affected tenants and source revisions. Do not put PII in public channels.
2. Check API metrics, Airflow run state, SQS oldest message, DLQ count, source feed version and export promotion state.
3. Stop publish/screening if results could be materially wrong or stale. Preserve read access to last known-good version if lawful and clearly labeled.
4. For 429: honor Retry-After, reduce concurrency, apply jitter and document provider limits. Never retry indefinitely.
5. For schema failures: quarantine partition, inform upstream owner, validate corrected sample, bounded replay with same idempotency key.
6. For missing accepted jobs: reconcile API receipts, outbox rows, queue state and terminal statuses; escalate immediately.
7. Notify authorized customer contacts with what is known, scope, next action and update cadence.
8. Restore from verified data state, replay in controlled order, compare manifest counts and obtain responsible approval before publishing.
9. Post-incident: timeline, contributing causes, customer impact, corrective work, owner and due date.

**Escalation:** Primary SRE → FDE → Data owner/Provider → Security/Compliance (if data correctness/privacy impacted) → Executive sponsor for material incidents.
