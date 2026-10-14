#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,sys
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl'
CACHE_SUMMARY=ROOT/'refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json'
EXCEPTIONS=ROOT/'source-package/research/Project_Exceptions_Current_2026-10-12.csv'
BASICS={'Plains','Island','Swamp','Mountain','Forest','Wastes','Snow-Covered Plains','Snow-Covered Island','Snow-Covered Swamp','Snow-Covered Mountain','Snow-Covered Forest'}
LINE_RE=re.compile(r'^\s*(\d+)x\s+(.+?)(?:\s+\[([^\]]+)\])?\s*$')
def norm(s): return re.sub(r'[^a-z0-9]+','',(s or '').casefold().replace('’',"'"))
def sha(b): return hashlib.sha256(b).hexdigest()
def ts(v):
 d=datetime.fromisoformat(v.replace('Z','+00:00')); return d.astimezone(timezone.utc)
def read_json(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def parse(path):
 raw=path.read_bytes(); out=[]
 for n,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
  if not line.strip(): continue
  m=LINE_RE.match(line)
  if not m: raise RuntimeError(f'malformed line {n}: {line}')
  out.append({'quantity':int(m.group(1)),'name':m.group(2).strip(),'role':m.group(3) or ''})
 return raw,out
def cache_load():
 c={}
 for line in CACHE.read_text(encoding='utf-8').splitlines():
  if not line.strip(): continue
  r=json.loads(line)
  for k in {r.get('query_name'),r.get('canonical_name')}:
   if k: c[norm(k)]=r
 return c
def exceptions_load():
 out={}
 if not EXCEPTIONS.exists(): return out
 with EXCEPTIONS.open(newline='',encoding='utf-8-sig') as f:
  for r in csv.DictReader(f): out[(r['deck_id'],norm(r['card_name']))]=r
 return out
def copy_exception(name,rec):
 if name in BASICS:return True
 t=(rec.get('oracle_text') or '').casefold()
 return 'a deck can have' in t and 'cards named' in t
def require_attestation(path,deck_sha,kind):
 x=read_json(path); errs=[]
 if x.get('status')!='PASS':errs.append(f'{kind} status != PASS')
 if x.get('deck_sha256')!=deck_sha:errs.append(f'{kind} deck_sha256 mismatch')
 if not x.get('checked_at_utc'):errs.append(f'{kind} missing checked_at_utc')
 if not x.get('sources'):errs.append(f'{kind} missing sources')
 if kind=='rules':
  its=x.get('interactions') or []
  if not its:errs.append('rules interactions empty')
  for i in its:
   if i.get('status')!='PASS':errs.append(f"rules interaction failed: {i.get('name')}")
 if kind=='official_legality' and x.get('unexpected_banned_cards'):
  errs.append(f"unexpected banned cards: {x.get('unexpected_banned_cards')}")
 return x,errs

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--config',required=True);a=ap.parse_args()
 cfg=read_json(a.config); deck_id=cfg['deck_id']; deck_path=ROOT/cfg['decklist_path']; outdir=ROOT/cfg['output_dir'];outdir.mkdir(parents=True,exist_ok=True)
 errors=[]
 if not deck_path.exists(): errors.append('decklist missing')
 if not CACHE.exists() or not CACHE_SUMMARY.exists(): errors.append('current-cycle cache missing')
 if errors: raise RuntimeError('; '.join(errors))
 summary=json.loads(CACHE_SUMMARY.read_text(encoding='utf-8'))
 if summary.get('overall_result')!='PASS' or summary.get('unresolved'): errors.append('Oracle cache is not clean PASS')
 age=(datetime.now(timezone.utc)-ts(summary['generated_at_utc'])).total_seconds()/3600
 if age>float(cfg.get('max_cache_age_hours',72)): errors.append(f'Oracle cache stale: {age:.1f}h')
 raw,entries=parse(deck_path); deck_sha=sha(raw)
 exp=cfg.get('expected_deck_sha256')
 if exp and exp!=deck_sha: errors.append(f'deck SHA mismatch expected {exp} actual {deck_sha}')
 if cfg.get('baseline_path'):
  bp=ROOT/cfg['baseline_path']; bsha=sha(bp.read_bytes())
  if cfg.get('expected_baseline_sha256') and bsha!=cfg['expected_baseline_sha256']: errors.append('baseline SHA mismatch')
 cache=cache_load(); excs=exceptions_load(); total=sum(x['quantity'] for x in entries)
 if total!=100: errors.append(f'count={total}, expected 100')
 commanders=[x for x in entries if 'Commander' in x['role']]
 if not commanders: errors.append('no [Commander] marker')
 cci=set(); unresolved=[]
 for e in commanders:
  r=cache.get(norm(e['name']))
  if not r: unresolved.append(e['name'])
  else: cci.update(r.get('color_identity') or [])
 counts=Counter(); rows=[]; project_ex=[]
 for e in entries:
  r=cache.get(norm(e['name']))
  if not r: unresolved.append(e['name']); continue
  counts[e['name']]+=e['quantity']; ci=set(r.get('color_identity') or []); color_ok=ci.issubset(cci)
  leg=r.get('commander_legality','unknown'); ex=excs.get((deck_id,norm(e['name'])))
  if leg=='legal': result='PASS'
  elif ex and str(ex.get('project_status','')).startswith('INTENTIONAL'):
   result='PROJECT_EXCEPTION';project_ex.append({'card':e['name'],'official_status':leg,'type':ex.get('exception_type')})
  else: result='FAIL';errors.append(f"unexpected Commander legality {leg}: {e['name']}")
  if not color_ok: result='FAIL';errors.append(f"color identity mismatch: {e['name']}")
  if not r.get('oracle_id') or not r.get('scryfall_id') or not r.get('oracle_text'): errors.append(f"incomplete Oracle record: {e['name']}")
  rows.append({'card_name':e['name'],'quantity':e['quantity'],'role':e['role'],'canonical_name':r.get('canonical_name',''),'scryfall_id':r.get('scryfall_id',''),'oracle_id':r.get('oracle_id',''),'type_line':r.get('type_line',''),'mana_cost':r.get('mana_cost',''),'color_identity':','.join(r.get('color_identity') or []),'commander_color_identity':','.join(sorted(cci)),'commander_legality':leg,'project_exception':ex.get('exception_type','') if ex else '','result':result,'oracle_text':r.get('oracle_text',''),'source':r.get('scryfall_uri','')})
 if unresolved: errors.append('unresolved cache records: '+', '.join(sorted(set(unresolved))))
 for n,q in counts.items():
  if q>1 and not copy_exception(n,cache.get(norm(n),{})): errors.append(f'singleton violation {q}x {n}')
 rules,rerrs=require_attestation(cfg['rules_attestation_path'],deck_sha,'rules');errors+=rerrs
 legal,lerrs=require_attestation(cfg['official_legality_attestation_path'],deck_sha,'official_legality');errors+=lerrs
 status='APPROVAL_READY' if not errors else 'FAIL'
 report={'generated_at_utc':datetime.now(timezone.utc).isoformat(),'deck_id':deck_id,'decklist_path':cfg['decklist_path'],'deck_sha256':deck_sha,'baseline_path':cfg.get('baseline_path'),'baseline_source_sha256':cfg.get('baseline_source_sha256'),'count':total,'distinct_names':len(counts),'commander_color_identity':sorted(cci),'cache_generated_at_utc':summary.get('generated_at_utc'),'cache_sha256':summary.get('cache_sha256'),'project_exceptions':project_ex,'rules_gate':'PASS' if not rerrs else 'FAIL','official_legality_gate':'PASS' if not lerrs else 'FAIL','errors':errors,'overall_result':status,'approval_state':'NOT_APPROVED — explicit user approval still required'}
 stem=cfg.get('output_stem',deck_id)
 with (outdir/f'{stem}_Card_Verification.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (outdir/f'{stem}_Complete_Gate.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 md=f"# {cfg.get('display_name',deck_id)} — complete approval gate\n\n**Result:** {status}\n\n- Deck SHA-256: `{deck_sha}`\n- Count: **{total}**\n- Distinct names: **{len(counts)}**\n- Oracle/cache: **{'PASS' if not unresolved else 'FAIL'}**\n- Color identity / Commander legality: **{'PASS' if not any('color identity' in x or 'Commander legality' in x for x in errors) else 'FAIL'}**\n- Official banned-list attestation: **{'PASS' if not lerrs else 'FAIL'}**\n- Rules-interaction attestation: **{'PASS' if not rerrs else 'FAIL'}**\n- Explicit user approval: **REQUIRED**\n"
 if errors: md+='\n## Errors\n'+'\n'.join('- '+x for x in errors)+'\n'
 (outdir/f'{stem}_Complete_Gate.md').write_text(md,encoding='utf-8')
 print(json.dumps(report,indent=2)); return 0 if status=='APPROVAL_READY' else 1
if __name__=='__main__': sys.exit(main())
