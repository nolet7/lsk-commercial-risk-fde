# Airflow DAG contract (future pilot)

DAG tasks: sense input → register landing manifest → quality check → Spark job → graph/screening enrichment → output reconcile → gated version promotion → customer notification. Tasks use bounded retries, idempotent run/partition keys, per-tenant concurrency, separate backfill mode and deterministic alert ownership. No actual Airflow DAG is supplied yet; never interpret this design as scheduled production processing.
