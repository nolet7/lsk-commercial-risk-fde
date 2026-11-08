from enum import Enum
from pydantic import BaseModel, Field

class ReviewState(str, Enum):
    clear_for_demo = "no_synthetic_indicator"
    manual_review = "manual_review_required"

class Company(BaseModel):
    entity_id: str
    legal_name: str
    jurisdiction: str
    source: str = "fictional-fixture-v1"

class Ownership(BaseModel):
    owner_id: str
    subject_id: str
    percentage: float = Field(ge=0, le=100)
    evidence_id: str

class ScreeningRequest(BaseModel):
    entity_id: str = Field(min_length=1, max_length=100)

class ScreeningResult(BaseModel):
    job_id: str
    entity_id: str
    review_state: ReviewState
    signals: list[str]
    evidence_ids: list[str]
    explanation: str
    policy_version: str = "synthetic-demo-v1"
