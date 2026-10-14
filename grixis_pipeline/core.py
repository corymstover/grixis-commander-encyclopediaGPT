from __future__ import annotations
import hashlib, json, time
from dataclasses import dataclass, asdict
from pathlib import Path

STAGES=("UNREFINED","INTAKE","BLUEPRINT","CANDIDATE_TRIAGE","RULES_REVIEW","VERIFY","TEST","FINALIZE","LOCKED")

@dataclass
class StageResult:
    deck_id: str
    stage: str
    input_hash: str
    result: str
    cache_hit: bool
    duration_s: float
    retry_count: int = 0
    blocker_code: str | None = None

def stable_hash(payload)->str:
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"),default=str).encode()
    return hashlib.sha256(raw).hexdigest()

def atomic_json(path: Path, payload):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(payload,indent=2,sort_keys=True,default=str)+"\n",encoding="utf-8")
    tmp.replace(path)

def append_telemetry(path: Path, result: StageResult):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("a",encoding="utf-8") as out:
        out.write(json.dumps(asdict(result),sort_keys=True)+"\n")

def run_cached_stage(*, deck_id, stage, inputs, work, root=Path(".grixis"), max_retries=2,
                     retry_exceptions=(TimeoutError, ConnectionError), retry_delay_s=0.25, sleep=time.sleep):
    if stage not in STAGES:
        raise ValueError(f"unknown stage: {stage}")
    if max_retries < 0:
        raise ValueError("max_retries must be >= 0")
    key=stable_hash({"stage_version":2,"stage":stage,"inputs":inputs})
    cache=root/"cache"/stage.lower()/f"{key}.json"
    started=time.monotonic()
    if cache.exists():
        result=StageResult(deck_id,stage,key,"PASS",True,time.monotonic()-started)
        append_telemetry(root/"telemetry.jsonl",result)
        return json.loads(cache.read_text(encoding="utf-8"))

    attempt=0
    while True:
        try:
            payload=work()
            atomic_json(cache,payload)
            atomic_json(root/"checkpoints"/f"{deck_id}.json",{
                "deck_id":deck_id,"stage":stage,"input_hash":key,"result":"PASS","retry_count":attempt
            })
            result=StageResult(deck_id,stage,key,"PASS",False,time.monotonic()-started,retry_count=attempt)
            append_telemetry(root/"telemetry.jsonl",result)
            return payload
        except retry_exceptions as exc:
            if attempt >= max_retries:
                result=StageResult(deck_id,stage,key,"BLOCKED",False,time.monotonic()-started,
                                   retry_count=attempt,blocker_code=type(exc).__name__)
                append_telemetry(root/"telemetry.jsonl",result)
                atomic_json(root/"checkpoints"/f"{deck_id}.json",{
                    "deck_id":deck_id,"stage":stage,"input_hash":key,"result":"BLOCKED",
                    "retry_count":attempt,"blocker_code":type(exc).__name__
                })
                raise
            attempt += 1
            sleep(retry_delay_s * (2 ** (attempt-1)))
        except Exception as exc:
            result=StageResult(deck_id,stage,key,"BLOCKED",False,time.monotonic()-started,
                               retry_count=attempt,blocker_code=type(exc).__name__)
            append_telemetry(root/"telemetry.jsonl",result)
            atomic_json(root/"checkpoints"/f"{deck_id}.json",{
                "deck_id":deck_id,"stage":stage,"input_hash":key,"result":"BLOCKED",
                "retry_count":attempt,"blocker_code":type(exc).__name__
            })
            raise
