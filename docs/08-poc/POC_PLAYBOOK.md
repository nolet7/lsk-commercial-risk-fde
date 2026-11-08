# POC implementation and evidence

## Step 1
Start synthetic fixture API and verify `GET /v1/entities`, `GET /v1/graphs/meridian-trading`, `POST /v1/screenings`, `GET /v1/screenings/{id}`.

## Step 2
Run entity-resolution quality experiment on independently labeled fictional identity aliases; verify ambiguity is not resolved by string normalization alone.

## Step 3
Run bounded graph traversal and preserve edge evidence. Test cycles, invalid dates, missing ownership fractions, source disagreement and complex paths.

## Step 4
Capture accuracy/error rate/latency, zero silent dropped accepted jobs (production target), incidents and customer comments. Publish evaluation for signed G2 review.

## Present implementation
Pure fixture API with synchronous in-memory screening, no real identity matching and no legal rule engine. All other items in this playbook are acceptance backlog, not completed features.
