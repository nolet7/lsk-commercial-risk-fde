# Observability and SLO plan

Customer SLI: API successful availability (target 99.9% monthly); batch completion within window (proposed 99%); acknowledged-job persistence; freshness relative to available source; export reconciliation (100% pass before promotion). Record customer usage without PII or unrestricted entity IDs as labels. Grafana dashboards: API p95/5xx, provider quotas, queue oldest age/DLQ, Airflow lateness, Spark output, data drift and business-case backlog. Pager alerts need thresholds and runbook URLs, not just colorful panels.
