#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,urllib.parse
from datetime import datetime,timezone
from pathlib import Path
from build_current_cycle_oracle_cache import http_json,canonical_from_live
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=ROOT/'refinement/decklists/Tetsuo_Umezawa_Approval_Ready_2026-10-15.txt'
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
SUMMARY=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json'
LINE_RE=re.compile(r'^\s*(\d+)x\s+(.+?)\s*$'); ROLE_RE=re.compile(r'\s+\[[^\]]+\]\s*$')
def norm(s): return re.sub(r'[^a-z0-9]+','',(s or '').casefold().replace('’',"'"))
def names():
    out=[]
    for line in CANDIDATE.read_text(encoding='utf-8-sig').splitlines():
        if not line.strip(): continue
        m=LINE_RE.match(line)
        if not m: raise RuntimeError(f'malformed candidate line: {line}')
        out.append(ROLE_RE.sub('',m.group(2)).strip())
    return sorted(set(out),key=str.casefold)
def load():
    rows=[]; by={}
    for line in CACHE.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        r=json.loads(line); rows.append(r)
        for k in {r.get('query_name'),r.get('canonical_name')}:
            if k: by[norm(k)]=r
    return rows,by
def main():
    summary=json.loads(SUMMARY.read_text())
    if summary.get('overall_result')!='PASS' or summary.get('unresolved'): raise RuntimeError('existing cache not clean PASS')
    generated=datetime.fromisoformat(summary['generated_at_utc'].replace('Z','+00:00'))
    age=(datetime.now(timezone.utc)-generated.astimezone(timezone.utc)).total_seconds()/3600
    if age>24: raise RuntimeError(f'cache too old: {age:.2f}h')
    rows,by=load(); missing=[n for n in names() if norm(n) not in by]; now=datetime.now(timezone.utc).isoformat(); added=[]
    for name in missing:
        card=http_json('https://api.scryfall.com/cards/named?exact='+urllib.parse.quote(name),attempts=5)
        if card.get('object')=='error': raise RuntimeError(f'Scryfall unresolved {name}: {card.get("details")}')
        rec=canonical_from_live(card,now); rec['query_name']=name
        if not rec.get('oracle_id') or not rec.get('scryfall_id') or not rec.get('oracle_text'): raise RuntimeError(f'incomplete record: {name}')
        if rec.get('commander_legality')!='legal': raise RuntimeError(f'unexpected Commander legality {name}: {rec.get("commander_legality")}')
        rows.append(rec); by[norm(name)]=rec; added.append(name)
    unresolved=[n for n in names() if norm(n) not in by]
    if unresolved: raise RuntimeError('unresolved candidate names: '+', '.join(unresolved))
    rows.sort(key=lambda r:(r.get('canonical_name') or r.get('query_name') or '').casefold())
    text=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows); CACHE.write_text(text,encoding='utf-8')
    summary['generated_at_utc']=now; summary['records_written']=len(rows); summary['unresolved']=[]; summary['overall_result']='PASS'; summary['cache_sha256']=hashlib.sha256(text.encode()).hexdigest()
    summary['targeted_candidate_refresh']={'deck':'Tetsuo Umezawa','candidate_path':str(CANDIDATE.relative_to(ROOT)),'missing_names_resolved_live':added,'prior_cache_age_hours':round(age,3),'method':'reuse clean same-day cache; exact live Scryfall lookup for candidate names absent from cache'}
    SUMMARY.write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','missing_resolved':added,'records':len(rows),'cache_sha256':summary['cache_sha256']},indent=2))
if __name__=='__main__': main()
