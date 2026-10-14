from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_many(deck_ids, run_one, *, max_workers=4):
    deck_ids=list(deck_ids)
    if len(deck_ids)!=len(set(deck_ids)):
        raise ValueError("duplicate deck IDs")
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")
    results={}; errors={}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_to_id={pool.submit(run_one,deck_id):deck_id for deck_id in deck_ids}
        for future in as_completed(future_to_id):
            deck_id=future_to_id[future]
            try:
                results[deck_id]=future.result()
            except Exception as exc:
                errors[deck_id]={"type":type(exc).__name__,"message":str(exc)}
    return {"results":results,"errors":errors}
