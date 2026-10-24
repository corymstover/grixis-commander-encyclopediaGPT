"""Ashad M7 Rev3: owner-approved exact 100, 95-name Oracle, history, registry and tracker."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt"
SOURCE=ROOT/"refinement/verification/Ashad_the_Lone_Cyberman_M7_Rev3_Scryfall_Selected_2026-10-23.json"
APPROVAL=ROOT/"refinement/approvals/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.md"
VERIFICATION=ROOT/"refinement/verification/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23_Verification.md"
EXPECTED="352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267"
PREVIOUS="087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25"
ADD={"Skullclamp","Piggy Bank","Razorlash Transmogrant","Necron Deathmark",
     "Royal Warden","Mishra's Workshop","Ancient Tomb","City of Brass",
     "Mana Confluence","Liberator, Urza's Battlethopter"}
CUT={"Fellwar Stone","Reckless Fireweaver","Thoughtcast","Noxious Gearhulk",
     "Thopter Spy Network","Tezzeret, Master of the Bridge","Delete",
     "Crumbling Necropolis","Shipwreck Marsh","Kappa Cannoneer"}
BASICS={"Island","Mountain","Swamp"}
ROCKS={"Arcane Signet","Rakdos Signet","Sol Ring","Talisman of Creativity",
       "Talisman of Dominance","Talisman of Indulgence","Mox Opal","Cursed Mirror"}
GCS={"Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Ancient Tomb","Mishra's Workshop"}
PREVIOUS_M7={
  "Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
  "Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
  "Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
  "Anhelo_the_Painter":"865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
}

def counts(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    out=Counter()
    for line in lines:
        qty,raw=line.split("x ",1)
        assert qty.isdecimal() and int(qty)>0, line
        out[raw.removesuffix(" [Commander]")]+=int(qty)
    return lines,out

class AshadRev3CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=json.loads(SOURCE.read_text(encoding="utf-8"))
        cls.oracle={c["name"]:c for c in cls.source["cards"]}

    def test_approved_exact_bytes_100_count_singleton_and_mana(self):
        self.assertEqual(hashlib.sha256(NEW.read_bytes()).hexdigest(),EXPECTED)
        lines,c=counts(NEW)
        self.assertEqual(lines[0],"1x Ashad, the Lone Cyberman [Commander]")
        self.assertEqual((len(lines),len(c),sum(c.values())),(95,95,100))
        self.assertEqual(sum("[Commander]" in line for line in lines),1)
        self.assertEqual(c["Ashad, the Lone Cyberman"],1)
        self.assertEqual({n:q for n,q in c.items() if q>1},
                         {"Island":3,"Mountain":2,"Swamp":3})
        self.assertTrue(all(q==1 or n in BASICS for n,q in c.items()))
        self.assertEqual(sum(q for n,q in c.items() if "Land" in self.oracle[n]["type_line"]),32)
        self.assertEqual(sum(c[n] for n in ROCKS),8)
        for name in ("Marionette Master","Unwinding Clock","Ichor Wellspring","Shimmer Myr",
                     "Liberator, Urza's Battlethopter"):
            self.assertIn(name,c)

    def test_immutable_older_source_ten_exact_replacements(self):
        self.assertEqual(hashlib.sha256(OLD.read_bytes()).hexdigest(),PREVIOUS)
        _,before=counts(OLD)
        _,after=counts(NEW)
        self.assertEqual(set((after-before).elements()),ADD)
        self.assertEqual(set((before-after).elements()),CUT)
        self.assertEqual(sum((after-before).values()),10)
        self.assertEqual(sum((before-after).values()),10)

    def test_all_95_primary_oracle_legal_and_no_exceptions(self):
        _,c=counts(NEW)
        s=self.source
        self.assertEqual((s["candidate_raw_sha256"],s["physical_cards"],s["exact_selected_unique_names"]),
                         (EXPECTED,100,95))
        self.assertEqual((len(self.oracle),set(self.oracle)),(95,set(c)))
        self.assertTrue(s["all_selected_commander_legal"])
        self.assertTrue(s["all_selected_grixis_identity"])
        self.assertEqual(s["project_exceptions"],[])
        self.assertEqual(set(s["rejected_research_only"]),{"Bio-Asset Allocator","Golos, Tireless Pilgrim"})
        self.assertTrue(set(s["rejected_research_only"]).isdisjoint(c))
        for name,qty in c.items():
            with self.subTest(card=name):
                o=self.oracle[name]
                self.assertEqual(o["quantity"],qty)
                self.assertEqual(o["commander_legality"],"legal")
                self.assertTrue(set(o["color_identity"]) <= {"U","B","R"})
                self.assertTrue(o["oracle_id"] and o["oracle_text"] is not None)
        self.assertEqual({n for n in c if self.oracle[n]["game_changer"]},GCS)
        self.assertIn("first nonlegendary artifact spell",self.oracle["Ashad, the Lone Cyberman"]["oracle_text"])
        self.assertIn("as though they had flash",self.oracle["Liberator, Urza's Battlethopter"]["oracle_text"])
        self.assertIn("only to cast artifact spells",self.oracle["Mishra's Workshop"]["oracle_text"])

    def test_registry_tracker_explicit_owner_and_prior_four_locks(self):
        state=json.loads((ROOT/"state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(len(state["decks"]),62)
        d=state["decks"]["Ashad_the_Lone_Cyberman"]
        for key,value in {
          "approved_list_sha256":EXPECTED,
          "m7_final_candidate_sha256":EXPECTED,
          "previous_approved_list_sha256":PREVIOUS,
          "previous_approved_source_raw_sha256":PREVIOUS,
          "user_approval_date":"2026-10-23",
          "approved_list_artifact":str(NEW.relative_to(ROOT)),
          "approval_status":"APPROVED","lock_status":"LOCKED","current_stage":"LOCKED",
        }.items():
            self.assertEqual(d[key],value,key)
        self.assertTrue(d["final_gate_passed"])
        self.assertIn("Cory explicitly replied 'Approved'",d["approval_basis"])
        for deck_id,raw in PREVIOUS_M7.items():
            self.assertEqual(state["decks"][deck_id]["approved_list_sha256"],raw,deck_id)
        with (ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            encoding="utf-8",newline=""
        ) as stream:
            records=list(csv.DictReader(stream))
        self.assertEqual(len(records),62)
        self.assertEqual(records[4]["deck_id"],"Ashad__the_Lone_Cyberman")
        self.assertEqual(records[4]["final_list_hash"],EXPECTED)
        self.assertEqual(records[4]["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",records[4]["refinement_status"])
        for i,prior in enumerate(("5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
                                  "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
                                  "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
                                  "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77")):
            self.assertEqual(records[i]["final_list_hash"],prior)

    def test_approval_receipt_exceptions_scope_and_source_pin(self):
        a=APPROVAL.read_text(encoding="utf-8")
        v=VERIFICATION.read_text(encoding="utf-8")
        for d in (a,v):
            for digest in (EXPECTED,PREVIOUS):
                self.assertIn(digest,d)
            self.assertIn("M6.10",d)
            self.assertIn("2026-10-23",d)
            self.assertIn("ef7a1f726f26648886cf9b44069f2c8e205df189",d)
        self.assertIn("> Approved",a)
        self.assertIn("original five-swap I/J",a)
        for name in ADD:
            self.assertIn(name,a)
        self.assertEqual(self.source["engineering_source_raw_sha256"],
                         "1c989cb1f72eea444a02b22084700be260aea92b5935126a8b8fcf33deb8d5a7")
        self.assertIn("original five-swap",v.lower())

if __name__=="__main__":
    unittest.main()
