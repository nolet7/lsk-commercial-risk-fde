# Delivery governance and evidence gates

G0 Discovery: sponsor, RACI, charter, permission for synthetic-only evaluation.
G1 POC: requirements and workflow acceptance, schema inventory, licensing, golden set, stop/go criteria.
G2 Pilot: benchmarked POC, model limitations, threat model, provider dependency and documented residual risk.
G3 Production: human UAT, data reconciliation, pen test, access isolation, tested failover/restore, on-call, SLO review and approved change ticket.
G4 Handover: independent operator follows SOP, customer sign-off, owned backlog, uptime and business reporting cadence.

Each gate requires named approvers and links to real evidence. Mark all gates **NOT APPROVED** until explicitly signed. A GitHub check passing does not satisfy a security or legal signoff.
