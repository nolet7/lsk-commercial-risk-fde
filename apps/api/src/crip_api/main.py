import os
from threading import Lock
from uuid import uuid4
from fastapi import FastAPI, Header, HTTPException, Depends, status
from .engine import screen, upstream_owners
from .fixtures import COMPANIES
from .models import ScreeningRequest, ScreeningResult

app = FastAPI(title="LSK CRIP synthetic demo", version="0.1.0")
_jobs: dict[str, ScreeningResult] = {}
_idempotency: dict[str, tuple[str, str]] = {}
_lock = Lock()

def demo_auth(x_demo_key: str | None = Header(default=None)) -> None:
    if os.environ.get("CRIP_ENV", "local") != "local":
        raise HTTPException(503, "Demo API disabled outside local environment")
    if x_demo_key != os.environ.get("CRIP_DEMO_KEY", "local-synthetic-demo-key"):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

@app.get("/health/live")
def live():
    return {"status": "ok", "mode": "synthetic-local-only"}

@app.get("/v1/entities", dependencies=[Depends(demo_auth)])
def entities():
    return list(COMPANIES.values())

@app.get("/v1/entities/{entity_id}", dependencies=[Depends(demo_auth)])
def entity(entity_id: str):
    if entity_id not in COMPANIES:
        raise HTTPException(404, "Unknown synthetic entity")
    return COMPANIES[entity_id]

@app.get("/v1/graphs/{entity_id}", dependencies=[Depends(demo_auth)])
def graph(entity_id: str, max_depth: int = 6):
    try:
        return {"entity_id": entity_id, "relationships": upstream_owners(entity_id, max_depth)}
    except KeyError:
        raise HTTPException(404, "Unknown synthetic entity") from None
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@app.post("/v1/screenings", status_code=201, response_model=ScreeningResult, dependencies=[Depends(demo_auth)])
def create_screening(payload: ScreeningRequest, idempotency_key: str = Header(min_length=1, max_length=128)):
    if payload.entity_id not in COMPANIES:
        raise HTTPException(404, "Unknown synthetic entity")
    with _lock:
        if idempotency_key in _idempotency:
            previous_entity, previous_job = _idempotency[idempotency_key]
            if previous_entity != payload.entity_id:
                raise HTTPException(409, "Idempotency key reused with different payload")
            return _jobs[previous_job]
        job_id = str(uuid4())
        result = screen(payload.entity_id, job_id)
        _jobs[job_id] = result
        _idempotency[idempotency_key] = (payload.entity_id, job_id)
        return result

@app.get("/v1/screenings/{job_id}", response_model=ScreeningResult, dependencies=[Depends(demo_auth)])
def get_screening(job_id: str):
    if job_id not in _jobs:
        raise HTTPException(404, "Unknown job")
    return _jobs[job_id]
