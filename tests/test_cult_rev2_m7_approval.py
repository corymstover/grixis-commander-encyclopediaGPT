"""Canonical Cory-approved Cult of Skaro nine-swap M7 Rev2; exact prior-lock regression."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt"
ORACLE=ROOT/"refinement/verification/Cult_of_Skaro_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d"
PREVIOUS="4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b"
SWAPS=(
 ("Cybermen Squadron","Karlach, Fury of Avernus"),
 ("Canoptek Spyder","Kindred Discovery"),
 ("Adaptive Omnitool","Hammer of Purphoros"),
 ("Thopter Spy Network","Shaun, Father of Synths"),
 ("Anrakyr the Traveller","Quantum Misalignment"),
 ("Baleful Strix","Skorpekh Lord"),
 ("Desynchronization","Reverse the Polarity"),
 ("Island","Otawara, Soaring City"),
 ("Swamp","Takenuma, Abandoned Mire"),
)
ROCKS={"Sol Ring","Mana Vault","Mox Opal","Arcane Signet","Dimir Signet",
       "Fellwar Stone","Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
REDUCERS={"Etherium Sculptor","Enthusiastic Mechanaut","Shuri, Wakandan Inventor"}
PREVIOUS_M7={
  'Abaddon_the_Despoiler': '5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24',
  'Admiral_Beckett_Brass': 'ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000',
  'Admiral_Brass__Unsinkable': 'dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7',
  'Anhelo_the_Painter': '865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77',
  'Ashad_the_Lone_Cyberman': '352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267',
  'Ashnod_the_Uncaring': 'a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761',
  'Be_lakor_the_Dark_Master': '2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4',
  'Cecily__Bjorna__Lutri': 'e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d',
  'Cormela__Glamour_Thief': 'd91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd',
  'Crosis__the_Purger': 'a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a'
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    names=Counter()
    for line in lines:
        q,name=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        names[name.removesuffix(" [Commander]")]+=int(q)
    return lines,names

class CultM7Rev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines,cls.deck=parse(NEW)
        _,cls.baseline=parse(OLD)
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={x["name"]:x for x in cls.o["cards"]}
        cls.reg=json.loads(STATE.read_text(encoding="utf-8"))["decks"]

    def test_exact_approved_bytes_and_immutable_historical_source(self):
        self.assertEqual(sha(NEW),RAW)
        self.assertTrue(NEW.read_bytes().endswith(b"\n"))
        self.assertEqual(sha(OLD),PREVIOUS)

    def test_one_commander_100_singleton_and_basics(self):
        self.assertEqual(self.lines[0],"1x Cult of Skaro [Commander]")
        self.assertEqual(sum("[Commander]" in line for line in self.lines),1)
        self.assertEqual((len(self.lines),len(self.deck),sum(self.deck.values())),(96,96,100))
        self.assertEqual((self.deck["Island"],self.deck["Mountain"],self.deck["Swamp"]),(2,3,2))
        self.assertTrue(all(q==1 for n,q in self.deck.items() if n not in {"Island","Mountain","Swamp"}))

    def test_nine_owner_approved_changes_and_retained_master_reducers(self):
        self.assertEqual(len(SWAPS),9)
        self.assertEqual(self.deck-self.baseline,Counter({a:1 for c,a in SWAPS}))
        self.assertEqual(self.baseline-self.deck,Counter({c:1 for c,a in SWAPS}))
        for n in ("Cult of Skaro","The Master, Multiplied","Etherium Sculptor",
                  "Auton Soldier","Shaun, Father of Synths","Kindred Discovery",
                  "Hammer of Purphoros","Karlach, Fury of Avernus","Aggravated Assault",
                  "Sword of Feast and Famine","Roaming Throne","Scientist Supreme of A.I.M."):
            self.assertEqual(self.deck[n],1,n)

    def test_current_selected_oracle_legality_grixis(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["baseline_raw_sha256"],PREVIOUS)
        self.assertEqual(self.o["physical_cards"],100)
        self.assertEqual(self.o["distinct_names"],96)
        self.assertEqual(self.o["project_exceptions"],[])
        self.assertTrue(self.o["official_commander_legal_all"])
        self.assertTrue(self.o["grixis_color_identity_all"])
        self.assertEqual(set(self.cards),set(self.deck))
        for n,c in self.cards.items():
            with self.subTest(card=n):
                self.assertEqual(c["quantity"],self.deck[n])
                self.assertEqual(c["commander_legality"],"legal",n)
                self.assertLessEqual(set(c["color_identity"]),{"U","B","R"})
                self.assertTrue(c["oracle_id"],n)
                self.assertIsNotNone(c["oracle_text"])
                self.assertTrue(c["source"])

    def test_lands_rocks_reducers_game_changers(self):
        self.assertEqual(self.o["normal_lands"],34)
        self.assertEqual(sum(c["quantity"] for c in self.cards.values() if "Land" in c["type_line"]),34)
        self.assertEqual(self.o["mana_rocks"],9)
        self.assertEqual(ROCKS & set(self.deck),ROCKS)
        self.assertEqual(REDUCERS & set(self.deck),REDUCERS)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},set(self.o["game_changers"]))
        self.assertEqual(set(self.o["game_changers"]),{"Cyclonic Rift","Fierce Guardianship","Mana Vault"})
        for n,color in (("Otawara, Soaring City","U"),("Takenuma, Abandoned Mire","B")):
            self.assertIn("{T}: Add {"+color+"}",self.cards[n]["oracle_text"])
            self.assertIn("Channel —",self.cards[n]["oracle_text"])

    def test_trigger_clone_shaun_master_exile_and_counter_rules(self):
        self.assertIn("Whenever Cult of Skaro attacks, choose one at random",self.cards["Cult of Skaro"]["oracle_text"])
        self.assertIn("Triggered abilities you control can't cause you to sacrifice or exile creature tokens",
                      self.cards["The Master, Multiplied"]["oracle_text"])
        self.assertIn("tapped and attacking token",self.cards["Shaun, Father of Synths"]["oracle_text"])
        self.assertIn("When Shaun leaves the battlefield, exile all Synth tokens",
                      self.cards["Shaun, Father of Synths"]["oracle_text"])
        self.assertIn("Exile the tokens at end of combat",self.cards["Auton Soldier"]["oracle_text"])
        self.assertIn("additional combat phase",self.cards["Karlach, Fury of Avernus"]["oracle_text"])
        self.assertIn("Creatures you control have haste",self.cards["Hammer of Purphoros"]["oracle_text"])
        self.assertIn("Whenever a creature you control of the chosen type enters or attacks",self.cards["Kindred Discovery"]["oracle_text"])
        self.assertEqual(self.cards["Reverse the Polarity"]["mana_cost"],"{1}{U}{U}")
        self.assertIn("Creatures can't be blocked this turn",self.cards["Reverse the Polarity"]["oracle_text"])

    def test_receipt_ownership_source_scope_not_new_j(self):
        a=RECEIPT.read_text(encoding="utf-8")
        b=VERIFY.read_text(encoding="utf-8")
        for t in ("> Approve",RAW,"not a blanket approval","nine expressly approved","not** re-sealed"):
            self.assertIn(t.lower(),a.lower())
        for t in ("100 physical","96 distinct","**not** re-sealed","no deterministic infinite","The Master"):
            self.assertIn(t.lower(),b.lower())

    def test_canonical_registry_tracker_exact_approved_shas(self):
        x=self.reg["Cult_of_Skaro"]
        self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
        self.assertTrue(x["final_gate_passed"])
        self.assertEqual(x["approved_list_sha256"],RAW)
        self.assertEqual(x["m7_final_candidate_sha256"],RAW)
        self.assertEqual(x["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(x["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(x["previous_approved_list_artifact"],str(OLD.relative_to(ROOT)))
        self.assertEqual(x["m7_archidekt_tags"],["Artifacts","Extra Combats","Copies"])
        self.assertEqual(x["m7_power_bracket"],"4 — Optimized")
        self.assertEqual(x["m7_project_exceptions"],[])
        with TRACKER.open(newline="",encoding="utf-8") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        r=next(x for x in rows if x["index"]=="10")
        self.assertEqual(r["deck_id"],"Cult_of_Skaro")
        self.assertEqual(r["final_list_hash"],RAW)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertEqual(r["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("nine",r["swap_decision_ledger_complete"])

    def test_ten_previous_m7_locks_unchanged(self):
        self.assertEqual(len(self.reg),62)
        self.assertEqual(len(PREVIOUS_M7),10)
        for n,h in PREVIOUS_M7.items():
            with self.subTest(deck=n):
                x=self.reg[n]
                self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(x["approved_list_sha256"],h)

if __name__=="__main__":
    unittest.main()
