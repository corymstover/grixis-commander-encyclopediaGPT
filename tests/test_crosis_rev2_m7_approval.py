"""Cory-approved Crosis M7 Rev2 exact source, historical baseline and other nine locks."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt"
ORACLE=ROOT/"refinement/verification/Crosis__the_Purger_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Crosis__the_Purger_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Crosis__the_Purger_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a"
PREVIOUS="a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1"
SWAPS=(
 ("Jet Medallion","Megrim"),
 ("Blizzard Specter","Rankle, Master of Pranks"),
 ("Dream Salvage","Aggravated Assault"),
 ("Oppression","Raiders' Wake"),
 ("Fell Specter","Deadly Rollick"),
 ("Bottomless Pit","Bloodchief Ascension"),
 ("Island","Otawara, Soaring City"),
 ("Swamp","Takenuma, Abandoned Mire"),
 ("Mountain","Sokenzan, Crucible of Defiance"),
)
ROCKS={"Sol Ring","Mana Vault","Chrome Mox","Mox Diamond","Lotus Petal",
       "Arcane Signet","Dimir Signet","Izzet Signet","Rakdos Signet",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
PREVIOUS_M7={
  'Abaddon_the_Despoiler': '5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24',
  'Admiral_Beckett_Brass': 'ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000',
  'Admiral_Brass__Unsinkable': 'dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7',
  'Anhelo_the_Painter': '865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77',
  'Ashad_the_Lone_Cyberman': '352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267',
  'Ashnod_the_Uncaring': 'a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761',
  'Be_lakor_the_Dark_Master': '2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4',
  'Cecily__Bjorna__Lutri': 'e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d',
  'Cormela__Glamour_Thief': 'd91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd'
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    counts=Counter()
    for line in lines:
        q,name=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        counts[name.removesuffix(" [Commander]")]+=int(q)
    return lines,counts

class CrosisM7Rev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines,cls.counts=parse(NEW)
        cls.original_lines,cls.previous=parse(OLD)
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.o["cards"]}
        cls.reg=json.loads(STATE.read_text(encoding="utf-8"))["decks"]

    def test_exact_raw_and_preserved_historical_bytes(self):
        self.assertEqual(sha(NEW),RAW)
        self.assertTrue(NEW.read_bytes().endswith(b"\n"))
        self.assertEqual(sha(OLD),PREVIOUS)

    def test_commander_100_singleton_and_basics(self):
        self.assertEqual(self.lines[0],"1x Crosis, the Purger [Commander]")
        self.assertEqual(sum("[Commander]" in l for l in self.lines),1)
        self.assertEqual((len(self.lines),len(self.counts),sum(self.counts.values())),(95,95,100))
        self.assertEqual((self.counts["Island"],self.counts["Mountain"],self.counts["Swamp"]),(3,2,3))
        self.assertEqual(self.counts["Crosis, the Purger"],1)
        self.assertTrue(all(v==1 for k,v in self.counts.items() if k not in {"Island","Mountain","Swamp"}))

    def test_nine_explicit_swaps_from_actual_approved_source(self):
        self.assertEqual(len(SWAPS),9)
        self.assertEqual(self.counts-self.previous,Counter({a:1 for c,a in SWAPS}))
        self.assertEqual(self.previous-self.counts,Counter({c:1 for c,a in SWAPS}))
        for n in ("Izzet Signet","Dark Deal","Painter's Servant","Sword of Feast and Famine",
                  "Brotherhood Regalia","Sedraxis Specter","Lightning Greaves"):
            self.assertEqual(self.counts[n],1,n)

    def test_selected_source_legality_oracle_and_identity(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["baseline_raw_sha256"],PREVIOUS)
        self.assertEqual(self.o["physical_cards"],100)
        self.assertEqual(self.o["distinct_names"],95)
        self.assertEqual(self.o["project_exceptions"],[])
        self.assertTrue(self.o["official_commander_legal_all"])
        self.assertTrue(self.o["grixis_color_identity_all"])
        self.assertEqual(set(self.cards),set(self.counts))
        for n,c in self.cards.items():
            with self.subTest(name=n):
                self.assertEqual(c["quantity"],self.counts[n])
                self.assertEqual(c["commander_legality"],"legal")
                self.assertLessEqual(set(c["color_identity"]),{"U","B","R"})
                self.assertTrue(c["oracle_id"])
                self.assertIsNotNone(c["oracle_text"])
                self.assertTrue(c["source"])

    def test_lands_acceleration_game_changers_and_channel_utility(self):
        self.assertEqual(self.o["normal_lands"],36)
        self.assertEqual(sum(c["quantity"] for c in self.cards.values() if "Land" in c["type_line"]),36)
        self.assertEqual(self.o["acceleration_artifacts"],12)
        self.assertEqual(ROCKS & set(self.counts),ROCKS)
        self.assertEqual(sum(self.counts[x] for x in ROCKS),12)
        self.assertEqual(len(self.o["game_changers"]),14)
        self.assertEqual({x["name"] for x in self.cards.values() if x["game_changer"]},set(self.o["game_changers"]))
        for n,c in (("Otawara, Soaring City","U"),("Takenuma, Abandoned Mire","B"),("Sokenzan, Crucible of Defiance","R")):
            self.assertIn("{T}: Add {"+c+"}",self.cards[n]["oracle_text"])
            self.assertIn("Channel —",self.cards[n]["oracle_text"])

    def test_commander_combo_and_payoffs_conditional(self):
        self.assertIn("combat damage to a player, you may pay {2}{B}",self.cards["Crosis, the Purger"]["oracle_text"])
        self.assertIn("All cards that aren't on the battlefield",self.cards["Painter's Servant"]["oracle_text"])
        self.assertIn("Whenever an opponent discards a card",self.cards["Megrim"]["oracle_text"])
        self.assertIn("Whenever an opponent discards a card",self.cards["Raiders' Wake"]["oracle_text"])
        self.assertIn("three or more quest counters",self.cards["Bloodchief Ascension"]["oracle_text"])
        self.assertIn("At the beginning of each end step",self.cards["Bloodchief Ascension"]["oracle_text"])
        self.assertIn("Activate only as a sorcery",self.cards["Aggravated Assault"]["oracle_text"])
        self.assertIn("untap all lands you control",self.cards["Sword of Feast and Famine"]["oracle_text"])
        self.assertIn("If you control a commander",self.cards["Deadly Rollick"]["oracle_text"])

    def test_approval_receipt_and_no_overclaims(self):
        r=RECEIPT.read_text(encoding="utf-8")
        v=VERIFY.read_text(encoding="utf-8")
        for t in ("> Approve",RAW,"not a blanket approval","not", "nine expressly approved","not** re-sealed"):
            self.assertIn(t.lower(),r.lower())
        for t in ("100 physical","**not** re-sealed","Grok","95 distinct","No source claims statistical"):
            self.assertIn(t.lower(),v.lower())

    def test_registry_and_tracker_exact_status(self):
        rec=self.reg["Crosis__the_Purger"]
        self.assertEqual((rec["approval_status"],rec["lock_status"]),("APPROVED","LOCKED"))
        self.assertTrue(rec["final_gate_passed"])
        self.assertEqual(rec["approved_list_sha256"],RAW)
        self.assertEqual(rec["m7_final_candidate_sha256"],RAW)
        self.assertEqual(rec["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(rec["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(rec["previous_approved_list_artifact"],str(OLD.relative_to(ROOT)))
        self.assertEqual(rec["m7_archidekt_tags"],["Discard","Dragons","Extra Combats"])
        self.assertEqual(rec["m7_power_bracket"],"4 — Optimized")
        self.assertEqual(rec["m7_project_exceptions"],[])
        with TRACKER.open(newline="",encoding="utf-8") as f:
            tracker=list(csv.DictReader(f))
        self.assertEqual(len(tracker),62)
        row=next(x for x in tracker if x["index"]=="9")
        self.assertEqual(row["deck_id"],"Crosis__the_Purger")
        self.assertEqual(row["final_list_hash"],RAW)
        self.assertEqual(row["user_approval_date"],"2026-10-23")
        self.assertEqual(row["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",row["refinement_status"])
        self.assertIn("nine",row["swap_decision_ledger_complete"])

    def test_nine_previous_m7_locks_still_immutable(self):
        self.assertEqual(len(self.reg),62)
        for deck,digest in PREVIOUS_M7.items():
            with self.subTest(deck=deck):
                x=self.reg[deck]
                self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(x["approved_list_sha256"],digest)

if __name__=="__main__":
    unittest.main()
