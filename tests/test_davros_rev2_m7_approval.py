"""Cory-approved canonical Davros M7 Rev2 nine-swap exact source and previous-lock regression."""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT/"refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT/"refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt"
ORACLE = ROOT/"refinement/verification/Davros_Dalek_Creator_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT/"refinement/approvals/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.md"
VERIFICATION = ROOT/"refinement/verification/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT/"state/current_deck_overrides.json"
TRACKER = ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXACT = "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc"
OLD = "aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc"
ADD_CUT = [
    ("Bloodletter of Aclazotz", "Death in Heaven"),
    ("Tergrid, God of Fright", "The Cyber-Controller"),
    ("Purphoros, God of the Forge", "Blasphemous Act"),
    ("Fiery Confluence", "This Is How It Ends"),
    ("Flame Rift", "Cyberman Patrol"),
    ("Spark Double", "Cybermen Squadron"),
    ("Irenicus's Vile Duplication", "Weeping Angel"),
    ("Quantum Misalignment", "Ashad, the Lone Cyberman"),
    ("Mechanized Warfare", "Labyrinth Raptor"),
]
GCS = {"Ancient Tomb","Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Jeska's Will","Tergrid, God of Fright"}
ROCKS = {"Sol Ring","Mox Opal","Arcane Signet","Fellwar Stone","Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_list(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    names=Counter()
    for i,l in enumerate(lines):
        match=re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?",l)
        if not match: raise AssertionError(f"Bad line {i+1}: {l}")
        count,name,commander=int(match.group(1)),match.group(2),match.group(3)
        if i==0: assert name=="Davros, Dalek Creator" and count==1 and commander
        else: assert commander is None
        assert count > 0
        names[name]+=count
    return names,lines

class DavrosM7Rev2ExactApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck,cls.lines=read_list(APPROVED)
        cls.old,cls.old_lines=read_list(BASELINE)
        cls.source=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.source["cards"]}
        cls.reg=json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.receipt=RECEIPT.read_text(encoding="utf-8")
        cls.verification=VERIFICATION.read_text(encoding="utf-8")
        with TRACKER.open(encoding="utf-8",newline="") as f:
            cls.rows=list(csv.DictReader(f))

    def test_approved_and_historical_exact_byte_hash(self):
        self.assertEqual(sha(APPROVED),EXACT)
        self.assertEqual(sha(BASELINE),OLD)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(self.source["candidate_sha256"],EXACT)
        self.assertEqual(self.source["owner_approved_exact_sha256"],EXACT)
        self.assertEqual(self.source["baseline_sha256"],OLD)

    def test_physical_100_singleton_first_commander(self):
        self.assertEqual(sum(self.deck.values()),100)
        self.assertEqual(len(self.lines),95)
        self.assertEqual(len(self.deck),95)
        self.assertEqual(self.deck["Davros, Dalek Creator"],1)
        self.assertEqual({n:q for n,q in self.deck.items() if q>1},{"Island":2,"Mountain":3,"Swamp":3})
        self.assertEqual(self.source["physical_cards"],100)
        self.assertEqual(self.source["distinct_names"],95)
        self.assertEqual(sum(self.old.values()),100)

    def test_nine_and_only_nine_owner_approved_substitutions(self):
        self.assertEqual(len(ADD_CUT),9)
        self.assertEqual(self.deck-self.old,Counter({a:1 for a,_ in ADD_CUT}))
        self.assertEqual(self.old-self.deck,Counter({b:1 for _,b in ADD_CUT}))
        for name in ("Swan Song","Vandalblast","Sycorax Commander"):
            self.assertEqual(self.deck[name],1)

    def test_selected_oracle_legality_identity_and_sources(self):
        self.assertEqual(set(self.deck),set(self.cards))
        self.assertEqual(len(self.cards),95)
        self.assertTrue(self.source["commander_legal_all"])
        self.assertTrue(self.source["color_identity_all_ubr"])
        self.assertEqual(self.source["project_exceptions"],[])
        for name,qty in self.deck.items():
            with self.subTest(name=name):
                x=self.cards[name]
                self.assertEqual(x["quantity"],qty)
                self.assertEqual(x["commander_legality"],"legal")
                self.assertTrue(x["oracle_id"] and x["oracle_text"])
                self.assertTrue(set(x["color_identity"]) <= {"U","B","R"})
                self.assertTrue(x["source"])
        self.assertIn("Wizards",self.cards["Mechanized Warfare"]["source"])
        self.assertIn("Scryfall",self.cards["Spark Double"]["source"])
        self.assertIn("Scryfall",self.cards["Irenicus's Vile Duplication"]["source"])
        self.assertIn("Scryfall",self.cards["Quantum Misalignment"]["source"])

    def test_mana_game_changers_and_bracket(self):
        land=sum(v["quantity"] for v in self.cards.values() if "Land" in v["type_line"])
        self.assertEqual(land,34)
        self.assertEqual(self.source["land_count"],34)
        self.assertEqual({name for name,v in self.cards.items() if v.get("game_changer")},GCS)
        self.assertEqual(set(self.source["game_changers"]),GCS)
        self.assertTrue(ROCKS <= set(self.deck))
        self.assertEqual(self.reg["decks"]["Davros__Dalek_Creator"]["m7_power_bracket"],"4 — Optimized")

    def test_real_commander_copy_and_end_step_interactions(self):
        x=lambda n:self.cards[n]["oracle_text"]
        self.assertIn("At the beginning of your end step",x("Davros, Dalek Creator"))
        self.assertIn("if an opponent lost 3 or more life this turn",x("Davros, Dalek Creator"))
        self.assertIn("it isn't legendary",x("Spark Double"))
        self.assertIn("it isn't legendary",x("Irenicus's Vile Duplication"))
        self.assertIn("it isn't legendary",x("Quantum Misalignment"))
        self.assertIn("Rebound",x("Quantum Misalignment"))
        self.assertIn("Whenever another creature you control enters",x("Purphoros, God of the Forge"))
        self.assertIn("red or artifact source",x("Mechanized Warfare"))
        self.assertIn("that much damage plus 1",x("Mechanized Warfare"))
        self.assertIn("lose twice that much life",x("Bloodletter of Aclazotz"))
        self.assertIn("from a graveyard",x("Tergrid, God of Fright"))
        self.assertIn("nontoken permanent",x("Tergrid, God of Fright"))

    def test_finite_trigger_qualification_cases(self):
        # Only second Davros resolution can see a Purphoros ping from the first.
        starting={"A":3,"B":0,"C":0}
        def after_ping(ping):
            return {name for name,v in starting.items() if v+ping>=3}
        self.assertEqual(after_ping(2),{"A"})
        self.assertEqual(after_ping(3),{"A","B","C"}) # Mechanized red damage replacement
        self.assertEqual(after_ping(4),{"A","B","C"}) # Bloodletter replacement on our turn
        self.assertIn("the *second* trigger can benefit",self.verification.lower().replace("only the *second*","the *second*"))

    def test_registry_only_named_deck_approved_and_old_source_pinned(self):
        self.assertEqual(len(self.reg["decks"]),62)
        d=self.reg["decks"]["Davros__Dalek_Creator"]
        self.assertEqual(d["approval_status"],"APPROVED")
        self.assertEqual(d["lock_status"],"LOCKED")
        self.assertTrue(d["final_gate_passed"])
        self.assertEqual(d["approved_list_sha256"],EXACT)
        self.assertEqual(d["m7_final_candidate_sha256"],EXACT)
        self.assertEqual(d["previous_approved_source_raw_sha256"],OLD)
        self.assertEqual(d["previous_approved_list_artifact"],"refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt")
        self.assertEqual(d["m7_archidekt_tags"],["Daleks","Villainous Choice","Group Slug"])
        self.assertTrue(d["m7_verified_100_physical"])
        self.assertEqual(d["m7_project_exceptions"],[])

    def test_tracker_one_row_exact_hash_no_other_new_m7_lock(self):
        self.assertEqual(len(self.rows),62)
        matches=[r for r in self.rows if r["deck_id"]=="Davros__Dalek_Creator"]
        self.assertEqual(len(matches),1)
        row=matches[0]
        self.assertEqual(row["index"],"11")
        self.assertEqual(row["final_list_hash"],EXACT)
        self.assertEqual(row["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",row["refinement_status"])
        self.assertIn("M7 CANONICAL REVISION",row["notes"])

    def test_owner_receipt_scope_and_no_j_or_multiplayer_overclaim(self):
        self.assertIn("> Approve",self.receipt)
        self.assertIn(EXACT,self.receipt)
        self.assertIn("only this exact 100-card raw list",self.receipt)
        self.assertIn("not re-sealed",self.receipt.lower())
        self.assertIn("not** re-sealed",self.verification.lower())
        self.assertIn("No measured multiplayer win-rate",self.receipt)
        self.assertIn("no invented win rate",self.verification.lower())
        self.assertIn("Deck #13",self.receipt)
        self.assertIn("40056636170",self.receipt)

if __name__=="__main__":
    unittest.main()
