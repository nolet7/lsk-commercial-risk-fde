# Customer discovery and technical scoping

Hold four structured sessions: business compliance workflow, data engineering/integrations, security/privacy/legal, and platform/SRE/CTO. Observe real work (subject to approval) and record before/after process maps, data entitlements and baseline measurements.

## Interview prompts
1. Which workflows trigger screening? What regulatory regimes and policy owners apply?
2. What identity attributes are available, and what is the acceptable ambiguous-match disposition?
3. Which upstream feeds exist? Who owns schema, freshness, incident communication and backfills?
4. Which customers, territories and data classes are permitted under provider license?
5. What percentiles, rate limits, volume spikes, analyst staffing and service windows matter?
6. Which actions are advisory and which trigger legally consequential decisions?
7. What manual control will continue if the system/provider is unavailable?

## Record for each requirement
ID, business rationale, owner, priority, source, measurable acceptance, data dependency, security classification, change log and test case ID.

## Gate G1
Signed workflow, data inventory, provider entitlement matrix, bounded test population, hypotheses, golden labels and stop conditions.
