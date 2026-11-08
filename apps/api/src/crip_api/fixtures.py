from .models import Company, Ownership

COMPANIES = {
    "meridian-trading": Company(entity_id="meridian-trading", legal_name="Meridian Trading (FICTIONAL)", jurisdiction="US"),
    "harbor-holdings": Company(entity_id="harbor-holdings", legal_name="Harbor Holdings (FICTIONAL)", jurisdiction="GB"),
    "northstar-capital": Company(entity_id="northstar-capital", legal_name="Northstar Capital (FICTIONAL)", jurisdiction="CA"),
    "restricted-x": Company(entity_id="restricted-x", legal_name="Synthetic Restricted Entity X (FICTIONAL)", jurisdiction="XX"),
    "unrestricted-y": Company(entity_id="unrestricted-y", legal_name="Unrestricted Owner Y (FICTIONAL)", jurisdiction="US"),
}
# Owner -> subject, not a statement of actual control or a regulatory ownership calculation.
EDGES = [
    Ownership(owner_id="harbor-holdings", subject_id="meridian-trading", percentage=60, evidence_id="fictional-edge-1"),
    Ownership(owner_id="northstar-capital", subject_id="meridian-trading", percentage=40, evidence_id="fictional-edge-2"),
    Ownership(owner_id="restricted-x", subject_id="harbor-holdings", percentage=80, evidence_id="fictional-edge-3"),
    Ownership(owner_id="unrestricted-y", subject_id="northstar-capital", percentage=100, evidence_id="fictional-edge-4"),
]
FICTIONAL_INDICATOR_SET = {"restricted-x"}
