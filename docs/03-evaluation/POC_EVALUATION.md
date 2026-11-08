# Evaluation plan | G1 → G2

## Hypothesis
Entity resolution plus explainable ownership traversal reduces analyst preparation time without unacceptable missed risks, privacy risk or unexplained output.

## Golden sets
Create synthetic positives, negatives, ambiguous transliterations, aliases, missing IDs, circular graphs, partial ownership percentages, time-varying edges, jurisdictions and contradictory sources. Keep labels independent from the implementation.

## Metrics and proposed thresholds
- Precision and recall per cohort, with numerator/denominator and uncertainty intervals; no single accuracy-only target.
- Proposed >=99% recall on unambiguous *synthetic* high-risk fixtures; zero unsupported automatic clearance of ambiguous records.
- 100% evidence source IDs for surfaced graph findings.
- A complete provider timeout, 429, duplicate and failed export test.
- Performance measured separately for cached lookup, live upstream calls, graph traversal and bulk jobs.
- Human adjudication and compliance signoff required; actual customer thresholds set in discovery.

## Evaluation decision
GO / CONDITIONAL GO / NO-GO signed by business, security and technical owners. Record coverage gaps, expected cost, provider terms, performance envelope and mitigations. Never extrapolate synthetic fixture success into live-world screening effectiveness.
