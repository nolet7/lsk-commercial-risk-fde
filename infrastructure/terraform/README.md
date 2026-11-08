# Production AWS infrastructure backlog (not deployed)

Plan modules: private multi-AZ VPC, controlled ingress/WAF, EKS, RDS with PITR, S3/KMS lifecycle, SQS/DLQ, Glue, MWAA, identity roles, Secrets Manager, CloudTrail, CloudWatch, security findings and AWS Budgets. Separate account/environment state, least privilege, remote encrypted Terraform backend and policy checks. Network and IAM must be security-reviewed before implementation. No credentials or fake Terraform resources included.
