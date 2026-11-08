from collections import deque
from .fixtures import COMPANIES, EDGES, FICTIONAL_INDICATOR_SET
from .models import ReviewState, ScreeningResult

MAX_DEPTH = 6

def upstream_owners(subject_id: str, max_depth: int = MAX_DEPTH) -> list[dict]:
    """Bounded BFS. Return relationship paths; do not collapse paths into legal ownership."""
    if subject_id not in COMPANIES:
        raise KeyError(subject_id)
    if not 0 <= max_depth <= MAX_DEPTH:
        raise ValueError("Graph depth outside bounded demo range")
    queue = deque([(subject_id, (), frozenset({subject_id}))])
    result = []
    while queue:
        current, path, visited = queue.popleft()
        if len(path) >= max_depth:
            continue
        for edge in EDGES:
            if edge.subject_id != current or edge.owner_id in visited:
                continue
            new_path = (*path, edge)
            result.append({"owner_id": edge.owner_id,
                           "path": [e.model_dump() for e in new_path],
                           "depth": len(new_path)})
            queue.append((edge.owner_id, new_path, visited | {edge.owner_id}))
    return result

def screen(entity_id: str, job_id: str) -> ScreeningResult:
    paths = upstream_owners(entity_id)
    direct = entity_id in FICTIONAL_INDICATOR_SET
    indirect = [p for p in paths if p["owner_id"] in FICTIONAL_INDICATOR_SET]
    signals = (["FICTIONAL_DIRECT_INDICATOR"] if direct else []) + (
        ["FICTIONAL_INDIRECT_RELATIONSHIP"] if indirect else [])
    evidence = [e["evidence_id"] for p in indirect for e in p["path"]]
    review = ReviewState.manual_review if signals else ReviewState.clear_for_demo
    return ScreeningResult(
        job_id=job_id, entity_id=entity_id, review_state=review,
        signals=signals, evidence_ids=sorted(set(evidence)),
        explanation="Synthetic review indicator only; not a sanctions legal determination."
    )
