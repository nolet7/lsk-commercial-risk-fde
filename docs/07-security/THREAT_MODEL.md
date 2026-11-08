# Security threat model and production hardening

## Trust boundaries
1. Bank → API ingress; 2. API → service/database; 3. worker → licensed external provider; 4. pipeline → S3/warehouse; 5. analyst → cases/exports; 6. optional LLM egress. Each requires separate identity, classification and audit controls.

## Priority threats and mitigations
| Threat | Control | Required verification |
|---|---|---|
| Tenant IDOR / cross-tenant graph joins | Authenticated identity + policy enforcement at every resource / query | adversarial isolation tests |
| Credential exfiltration | AWS IRSA / Pod Identity, Secrets Manager, egress deny-by-default | secrets scan, IAM review, simulated leakage |
| Malicious provider payload or prompt injection | strictly typed parser, output encoding, LLM untrusted context, no autonomous tools | injection evals |
| Replay, duplicates, lost acknowledged jobs | idempotency scope + durable outbox / inbox, unique constraints | crash/retry tests |
| Overbroad data product export | contractual entitlement, RBAC, TTL signed URLs, immutable audit | access review and export audit |
| Unbounded graph/query costs | traversal caps, query budgets, resource limits, query timeouts | load tests |
| Sanctions policy drift | versioned, counsel-approved rule and effective-date governance | golden set and policy approval |
| CI/CD compromise | branch protection, pinned reviewed actions, SBOM, signed artifacts, scanning | release evidence |
| LLM leaks or hallucinations | approved endpoint, grounding, abstention, human disposition | scenario eval + privacy review |
| Source tampering / stale feeds | signed/checksummed manifests, quality quarantine, freshness alarms | corrupted/late input drills |

## Must-fix before any non-local exposure
Replace demo header with enterprise OIDC/JWT validation (issuer/audience/JWKS), workload IAM, tenant policy engine, real persistent database, TLS, audit log, WAF, signed builds, secret rotation, secure tracing and approved pen test. Demo startup intentionally refuses `CRIP_ENV != local`.

## Security release gate
No critical/high unmitigated issues without formally approved documented exception; verify OWASP ASVS/API Security requirements and applicable bank standards. Never describe this repository as compliance certified.
