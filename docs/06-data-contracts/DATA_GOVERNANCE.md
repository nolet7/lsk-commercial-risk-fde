# Data contracts, provenance and governance

## Source schema
Require owner, contractual right, data classification, data subject category, permitted use, refresh rate, effective and ingestion timestamps, allowed destinations, expiration and deletion obligations.

## Data product manifest
Product name/version, tenant, source identifiers and timestamps, schema fingerprint, partition set, exported record count, rejected count/reasons, SHA-256 checksum, policy version, operator/automated actor, access grant and retention deadline.

## Pipeline publication
Raw immutable landing → malware/file sanity checks → schema validation → quarantined bad rows → normalized curated staged version → count/checksum reconciliation → approval controls → atomic version pointer promotion. Failed quality checks must NOT update customer-visible current version.

## Privacy and retention
Classify PII; encrypt in transit and rest; avoid names, addresses and investigations in traces; enforce per-tenant encryption/access and retention/delete policy. Deny export unless entitlement and contract permit it. Maintain auditable revocation and legal hold paths.
