import pytest
from crip_api.engine import upstream_owners, screen
from crip_api.models import ReviewState

def test_indirect_risk_indicator_and_provenance():
    result = screen("meridian-trading", "j1")
    assert result.review_state == ReviewState.manual_review
    assert "FICTIONAL_INDIRECT_RELATIONSHIP" in result.signals
    assert "fictional-edge-3" in result.evidence_ids

def test_no_signal_does_not_claim_clearance():
    result = screen("unrestricted-y", "j2")
    assert result.review_state == ReviewState.clear_for_demo
    assert "legal determination" in result.explanation

def test_graph_bounded_and_acyclic():
    paths = upstream_owners("meridian-trading", 2)
    assert len(paths) == 4
    assert all(p["depth"] <= 2 for p in paths)
    with pytest.raises(ValueError):
        upstream_owners("meridian-trading", 100)
