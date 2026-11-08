-- PROPOSED schema; not applied to the local in-memory demo.
CREATE TABLE entity (
  tenant_id UUID NOT NULL,
  entity_id UUID NOT NULL,
  legal_name TEXT NOT NULL,
  jurisdiction_code VARCHAR(8),
  source_system TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  observed_at TIMESTAMPTZ NOT NULL,
  ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (tenant_id, entity_id),
  UNIQUE (tenant_id, source_system, source_record_id)
);
CREATE TABLE ownership_edge (
  tenant_id UUID NOT NULL,
  edge_id UUID NOT NULL,
  owner_entity_id UUID NOT NULL,
  subject_entity_id UUID NOT NULL,
  ownership_pct NUMERIC(7,4),
  control_type TEXT,
  valid_from DATE,
  valid_to DATE,
  evidence_source_id TEXT NOT NULL,
  PRIMARY KEY (tenant_id, edge_id),
  FOREIGN KEY (tenant_id, owner_entity_id) REFERENCES entity(tenant_id, entity_id),
  FOREIGN KEY (tenant_id, subject_entity_id) REFERENCES entity(tenant_id, entity_id),
  CHECK (ownership_pct IS NULL OR ownership_pct BETWEEN 0 AND 100),
  CHECK (valid_to IS NULL OR valid_from IS NULL OR valid_to >= valid_from)
);
CREATE INDEX idx_ownership_subject ON ownership_edge (tenant_id, subject_entity_id);
CREATE INDEX idx_ownership_owner ON ownership_edge (tenant_id, owner_entity_id);
-- Production additionally needs evaluated tenant RLS, migration/versioning, immutable evidence
-- and reviewed constraints on cyclic paths and contradictory source records.
