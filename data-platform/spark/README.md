# Spark implementation contract (future pilot)

Glue PySpark jobs: read immutable S3 raw partitions, validate schema, quarantine rejected records, normalize identifiers, enrich against source snapshots, write partitioned Parquet to unique staging prefix, and publish version pointer only after reconciliation passes. Output manifest includes row counts, checksum, source IDs, timestamps and tenant/classification. Never blindly overwrite current.

Tests: duplicate/replayed inputs, schema drift, zero records, partial partitions, executor loss, oversized partitions, late arrivals, failed manifest, encryption/permission denial.
