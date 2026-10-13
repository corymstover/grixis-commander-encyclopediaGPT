#!/usr/bin/env python3
"""Refresh exact-printing card metadata from Scryfall default_cards bulk data."""
# One controlled refresh run requested for the 2026-10-12 campaign.
import csv, hashlib, io, json, re, tarfile, tempfile, urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import ijson

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/"source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OUT=ROOT/"refinement/metadata_audit"
UA="GrixisCommanderEncyclopedia/1.0 (github.com/corymstover/grixis-commander-encyclopediaGPT)"
PAT=re.compile(r"^\s*(\d+)x\s+(.+?)\s+\(([^()]*)\)\s+(\S+)\s+(?:\*[^*]+\*\s+)?\[([^\]]*)\]\s*$")
BANNED_EXCEPTIONS={
 ("Cecily__Bjorna__Lutri","Lutri, the Spellchaser","Companion"),
 ("Cecily__Bjorna__Lutri","Trade Secrets","Main"),
 ("Cecily__Bjorna__Lutri","Yawgmoth's Bargain","Main")}
FUTURE={"The Madcap Jester","Dragon's Smile","Tresserhorn's Lord, Returned"}
def norm(s): return re.sub(r"[^a-z0-9]+","",(s or "").casefold().replace("’","'"))
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def request(url,accept="application/json"):
 r=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":accept})
 return urllib.request.urlopen(r,timeout=180)
def main():
 if not ARCHIVE.is_file(): raise RuntimeError("Frozen 124-file decklist archive missing")
 decks=defaultdict(list); keys=set()
 with tarfile.open(ARCHIVE,"r:gz") as tf:
  members={m.name:m for m in tf.getmembers() if m.isfile()}
  txts=sorted(p for p in members if p.startswith("TXT/") and p.endswith(".txt"))
  if len(members)!=124 or len(txts)!=62: raise RuntimeError("Expected 124 archive files and 62 TXT files")
  for p in txts:
   did=Path(p).stem
   for line in tf.extractfile(members[p]).read().decode("utf-8-sig").splitlines():
    if not line.strip(): continue
    m=PAT.match(line)
    if not m: raise RuntimeError(f"Malformed entry {p}: {line}")
    q,name,setcode,cn,role=m.groups()
    row={"deck_id":did,"card_name_export":name.strip(),"quantity":int(q),"set_code":setcode.lower(),"collector_number":cn,"role":role}
    decks[did].append(row); keys.add((setcode.lower(),cn))
 with request("https://api.scryfall.com/bulk-data") as r: api=json.load(r)
 bulk=next(x for x in api["data"] if x["type"]=="default_cards")
 found=defaultdict(list)
 with tempfile.NamedTemporaryFile(suffix=".json") as tmp:
  download_uri=bulk.get("download_uri") or bulk.get("download_url")\n if not download_uri: raise RuntimeError("Scryfall bulk entry has no download URI; keys="+",".join(sorted(bulk.keys())))\n with request(download_uri) as src:
   while True:
    b=src.read(1024*1024)
    if not b: break
    tmp.write(b)
  tmp.flush()
  with open(tmp.name,"rb") as src:
   for card in ijson.items(src,"item"):
    key=(str(card.get("set","")).lower(),str(card.get("collector_number","")))
    if key in keys: found[key].append(card)
 def choose(row):
  cand=found.get((row["set_code"],row["collector_number"]),[])
  exact=[x for x in cand if norm(x.get("name"))==norm(row["card_name_export"])]
  if len(exact)==1: return exact[0],"EXACT_SET_COLLECTOR_AND_NAME"
  if len(exact)>1 and len({x.get("oracle_id") for x in exact})==1: return exact[0],"DUPLICATE_RECORDS_SAME_ORACLE_ID"
  if len(exact)>1: return None,"AMBIGUOUS_EXACT_PRINTING"
  if len(cand)==1: return cand[0],"NAME_VARIANT_REVIEW"
  return None,"NOT_FOUND" if not cand else "AMBIGUOUS_SET_COLLECTOR"
 commanders={}
 for did,entries in decks.items():
  ci=set()
  for row in entries:
   if "Commander" in row["role"]:
    card,_=choose(row)
    if card: ci.update(card.get("color_identity") or [])
  commanders[did]=sorted(ci)
 rows=[]; summary={"generated_at_utc":datetime.now(timezone.utc).isoformat(),"bulk_type":"default_cards","bulk_updated_at":bulk.get("updated_at"),"deck_count":len(decks),"decklist_rows":sum(map(len,decks.values())),"distinct_printing_keys":len(keys),"exact_matches":0,"name_variant_reviews":0,"not_found":0,"ambiguous":0,"missing_oracle_text":0,"missing_oracle_id":0,"color_identity_mismatches":[],"official_illegal_rows":[],"known_project_banned_exception_rows":[],"unresolved_project_exception_rows":[],"unresolved_printing_rows":[],"note":"Metadata overlay only; does not certify relevant rules interactions or replace the separate project exception registry."}
 for did,entries in decks.items():
  dci=commanders[did]
  for row in entries:
   card,status=choose(row)
   out={**row,"bulk_updated_at":bulk.get("updated_at"),"scryfall_id":"","oracle_id":"","scryfall_name":"","type_line":"","oracle_text":"","oracle_text_sha256":"","color_identity":"","commander_color_identity":",".join(dci),"color_identity_check":"REVIEW","commander_legality":"UNKNOWN","project_exception_status":"REGISTRY_CHECK_REQUIRED","released_at":"","printing_match_status":status}
   if card is None:
    summary["not_found" if status=="NOT_FOUND" else "ambiguous"]+=1
    out["project_exception_status"]="KNOWN_FUTURE_RELEASE_EXCEPTION — official status not inferred" if row["card_name_export"] in FUTURE else "REVIEW — consult current exception registry"
    summary["unresolved_printing_rows"].append({"deck_id":did,"card_name":row["card_name_export"],"set":row["set_code"],"collector":row["collector_number"],"status":status})
   else:
    summary["exact_matches" if status.startswith("EXACT") or status.startswith("DUPLICATE") else "name_variant_reviews"]+=1
    text=card.get("oracle_text") or ""; oracle_id=card.get("oracle_id") or ""
    if not text: summary["missing_oracle_text"]+=1
    if not oracle_id: summary["missing_oracle_id"]+=1
    ci=sorted(card.get("color_identity") or [])
    out.update({"scryfall_id":card.get("id",""),"oracle_id":oracle_id,"scryfall_name":card.get("name",""),"type_line":card.get("type_line",""),"oracle_text":text,"oracle_text_sha256":sha(text),"color_identity":",".join(ci),"released_at":card.get("released_at",""),"commander_legality":(card.get("legalities") or {}).get("commander","unknown")})
    if "Commander" in row["role"] and not dci: out["color_identity_check"]="REVIEW — commander identity unresolved"
    elif set(ci).issubset(set(dci)): out["color_identity_check"]="PASS"
    else:
     out["color_identity_check"]="FAIL"; summary["color_identity_mismatches"].append({"deck_id":did,"card_name":row["card_name_export"],"card_identity":ci,"commander_identity":dci})
    zone="Companion" if "Companion" in row["role"] else "Main"
    if row["card_name_export"]=="Lutri, the Spellchaser" and zone=="Companion": out["commander_legality"]="banned_as_companion"
    key=(did,row["card_name_export"],zone)
    if key in BANNED_EXCEPTIONS:
     out["project_exception_status"]="KNOWN PROJECT-AUTHORIZED EXCEPTION — official status retained separately"
     summary["known_project_banned_exception_rows"].append({"deck_id":did,"card_name":row["card_name_export"],"zone":zone,"official_status":out["commander_legality"]})
    elif row["card_name_export"] in FUTURE:
     out["project_exception_status"]="KNOWN FUTURE-RELEASE PROJECT EXCEPTION — confirm exact registry row"
     summary["unresolved_project_exception_rows"].append({"deck_id":did,"card_name":row["card_name_export"],"reason":"future-release status should be cross-checked against the current exception registry"})
    if out["commander_legality"] in ("banned","not_legal","banned_as_companion"):
     summary["official_illegal_rows"].append({"deck_id":did,"card_name":row["card_name_export"],"zone":zone,"official_status":out["commander_legality"],"project_exception_status":out["project_exception_status"]})
   rows.append(out)
 OUT.mkdir(parents=True,exist_ok=True)
 with (OUT/"Current_Scryfall_Metadata_Overlay_2026-10-12.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary["rows_written"]=len(rows);summary["decks_with_unresolved_commander_identity"]=sorted(d for d,ci in commanders.items() if not ci)
 summary["unexpected_official_illegal_rows"]=[x for x in summary["official_illegal_rows"] if not str(x["project_exception_status"]).startswith("KNOWN PROJECT-AUTHORIZED EXCEPTION")]
 summary["overall_result"]="REVIEW_REQUIRED" if (summary["not_found"] or summary["ambiguous"] or summary["name_variant_reviews"] or summary["missing_oracle_text"] or summary["missing_oracle_id"] or summary["color_identity_mismatches"] or summary["unresolved_printing_rows"] or summary["unresolved_project_exception_rows"] or summary["unexpected_official_illegal_rows"]) else "METADATA_REFRESH_PASS — exception/rules review remains separate"
 (OUT/"Current_Scryfall_Metadata_Audit_Summary_2026-10-12.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps({k:v for k,v in summary.items() if k not in ("color_identity_mismatches","official_illegal_rows","known_project_banned_exception_rows","unresolved_printing_rows")},indent=2))
if __name__=="__main__": main()
