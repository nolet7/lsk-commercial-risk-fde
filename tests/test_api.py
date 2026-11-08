import os
from fastapi.testclient import TestClient
from crip_api.main import app

os.environ["CRIP_ENV"] = "local"
client = TestClient(app)
AUTH = {"X-Demo-Key": "local-synthetic-demo-key"}

def test_requires_demo_auth():
    assert client.get("/v1/entities").status_code == 401

def test_graph_evidence():
    response = client.get("/v1/graphs/meridian-trading", headers=AUTH)
    assert response.status_code == 200
    assert len(response.json()["relationships"]) == 4

def test_idempotency_and_conflict():
    headers = {**AUTH, "Idempotency-Key": "api-test-unique"}
    a = client.post("/v1/screenings", json={"entity_id": "meridian-trading"}, headers=headers)
    b = client.post("/v1/screenings", json={"entity_id": "meridian-trading"}, headers=headers)
    c = client.post("/v1/screenings", json={"entity_id": "northstar-capital"}, headers=headers)
    assert a.status_code == 201
    assert a.json()["job_id"] == b.json()["job_id"]
    assert c.status_code == 409

def test_demo_fails_closed_outside_local(monkeypatch):
    monkeypatch.setenv("CRIP_ENV", "production")
    assert client.get("/v1/entities", headers=AUTH).status_code == 503
