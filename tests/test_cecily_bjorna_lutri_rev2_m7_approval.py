"""Canonical Cory-approved Cecily/Bjorna/Lutri M7 Rev2, special legality exceptions and seven prior locks."""
import csv, hashlib, json, unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt"
ORACLE=ROOT/"refinement/verification/Cecily__Bjorna__Lutri_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d"
PREVIOUS="553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28"
SWAPS=(
 ("Emry, Lurker of the Loch","Strionic Resonator"),
 ("Goblin Engineer","Echo, Perceptive Prodigy"),
 ("Sai, Master Thopterist","Twenty-Toed Toad"),
 ("Dark Deal","Sea Gate Restoration // Sea Gate, Reborn"),
 ("Mana Geyser","Deflecting Swat"),
 ("Seething Song","Mana Drain"),
 ("Cruel Ultimatum","Fevered Suspicion"),
 ("Wheel of Misfortune","Aminatou's Augury"),
 ("Crumbling Necropolis","City of Brass"),
 ("Fabled Passage","Mana Confluence"),
)
ROCKS={"Sol Ring","Arcane Signet","Dimir Signet","Izzet Signet","Rakdos Signet",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence","Thought Vessel"}
GCS={"Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Jeska's Will","Mystical Tutor",
     "Notion Thief","Rhystic Study","The One Ring","Underworld Breach","Vampiric Tutor"}
PREVIOUS_M7={
 "Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
 "Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
 "Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
 "Anhelo_the_Painter":"865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
 "Ashad_the_Lone_Cyberman":"352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
 "Ashnod_the_Uncaring":"a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
 "Be_lakor_the_Dark_Master":"2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    rows=[]
    for line in lines:
        q,n=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        zone="main"
        for label in ("Commander","Companion"):
            if n.endswith(" ["+label+"]"):
                n=n.removesuffix(" ["+label+"]");zone=label
        rows.append((int(q),n,zone))
    return rows

class CecilyBjornaLutriRev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=parse(NEW)
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.o["cards"]}
        cls.counts=Counter({n:q for q,n,z in cls.rows if z!="Companion"})
        cls.prior=Counter({n:q for q,n,z in parse(OLD)})
        cls.registry=json.loads(STATE.read_text(encoding="utf-8"))["decks"]

    def test_exact_sha_and_october_source_preserved(self):
        self.assertEqual(sha(NEW),RAW)
        self.assertEqual(sha(OLD),PREVIOUS)
        self.assertTrue(NEW.read_bytes().endswith(bytes([10])))

    def test_two_commanders_100_and_companion_outside(self):
        self.assertEqual(len(self.rows),100)
        self.assertEqual(len({n for q,n,z in self.rows}),100)
        self.assertEqual(sum(q for q,n,z in self.rows if z!="Companion"),100)
        self.assertEqual(sum(q for q,n,z in self.rows),101)
        self.assertEqual(self.rows[:3],[
            (1,"Bjorna, Nightfall Alchemist","Commander"),
            (1,"Cecily, Haunted Mage","Commander"),
            (1,"Lutri, the Spellchaser","Companion")])
        self.assertEqual(sum(z=="Commander" for q,n,z in self.rows),2)
        self.assertEqual(sum(z=="Companion" for q,n,z in self.rows),1)
        self.assertEqual({n:q for n,q in self.counts.items() if q>1},{"Island":2})
        self.assertEqual(len(self.counts),99)

    def test_exact_ten_swaps_vs_old_canonical_100(self):
        self.assertEqual(sum(self.prior.values()),100)
        self.assertEqual(len(SWAPS),10)
        self.assertEqual(self.counts-self.prior,Counter({add:1 for cut,add in SWAPS}))
        self.assertEqual(self.prior-self.counts,Counter({cut:1 for cut,add in SWAPS}))
        self.assertIn("In Garruk's Wake",self.counts)
        self.assertIn("Wheel of Fortune",self.counts)

    def test_selected_current_oracle_and_named_ban_exceptions(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["historical_raw_100_sha256"],PREVIOUS)
        self.assertEqual(self.o["physical_cards_in_100"],100)
        self.assertEqual(self.o["total_physical_including_companion"],101)
        self.assertEqual(len(self.cards),100)
        self.assertEqual(set(self.cards),{n for q,n,z in self.rows})
        self.assertEqual(set(self.o["official_commander_banned_cards_in_100"]),{"Trade Secrets","Yawgmoth's Bargain"})
        self.assertTrue(self.o["companion_officially_banned"])
        self.assertEqual(len(self.o["ban_exceptions"]),3)
        for q,n,z in self.rows:
            with self.subTest(name=n):
                c=self.cards[n]
                self.assertEqual((c["quantity"],c["zone"]),(q,z))
                self.assertLessEqual(set(c["color_identity"]),{"U","B","R"})
                self.assertTrue(c["oracle_id"])
                self.assertIsNotNone(c["oracle_text"])
                self.assertTrue(c["source"])
                if n in {"Trade Secrets","Yawgmoth's Bargain"}:
                    self.assertEqual(c["commander_legality"],"banned")
                    self.assertIn("exception",c["project_exception"].lower())
                else:
                    self.assertEqual(c["commander_legality"],"legal")
        self.assertIn("companion",self.cards["Lutri, the Spellchaser"]["project_exception"])

    def test_lands_mana_rocks_game_changers(self):
        self.assertEqual((self.o["printed_land_slots"],self.o["modal_land_options"]),(33,1))
        self.assertEqual(self.o["static_rocks"],9)
        self.assertEqual(ROCKS & set(self.counts),ROCKS)
        self.assertEqual({n for n in self.counts if self.cards[n]["game_changer"]},GCS)

    def test_copied_trigger_hand_size_and_rebound_rules(self):
        self.assertIn("Then if you have eleven or more cards",self.cards["Cecily, Haunted Mage"]["oracle_text"])
        self.assertIn("Copy target activated or triggered ability",self.cards["Echo, Perceptive Prodigy"]["oracle_text"])
        self.assertIn("Copy target triggered ability",self.cards["Strionic Resonator"]["oracle_text"])
        self.assertIn("you win the game",self.cards["Twenty-Toed Toad"]["oracle_text"])
        self.assertIn("Rebound",self.cards["Fevered Suspicion"]["oracle_text"])
        self.assertIn("Exile the top eight cards",self.cards["Aminatou's Augury"]["oracle_text"])
        self.assertIn("Companion",self.cards["Lutri, the Spellchaser"]["oracle_text"])

    def test_exact_approval_receipt_and_limits(self):
        s=RECEIPT.read_text(encoding="utf-8")
        t=VERIFY.read_text(encoding="utf-8")
        self.assertIn("> Approve",s)
        self.assertIn(RAW,s)
        self.assertIn("not a blanket authorization",s)
        self.assertIn("non-independent",s)
        self.assertIn("project-only",s)
        self.assertIn("first-pass",t)
        self.assertIn("new formal M6 I/J",t)
        self.assertIn("100 physical",t)
        self.assertIn("101 physical",t)

    def test_registry_exact_lock_and_previous_source(self):
        r=self.registry["Cecily__Bjorna__Lutri"]
        self.assertEqual((r["approval_status"],r["lock_status"]),( "APPROVED","LOCKED"))
        self.assertTrue(r["final_gate_passed"])
        self.assertEqual(r["approved_list_sha256"],RAW)
        self.assertEqual(r["m7_final_candidate_sha256"],RAW)
        self.assertEqual(r["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(r["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(r["previous_approved_list_artifact"],str(OLD.relative_to(ROOT)))
        self.assertEqual(r["m7_power_bracket"],"4 — Optimized")
        self.assertEqual(r["m7_archidekt_tags"],["Spellslinger","Wheels","Hand Size Matters"])
        self.assertEqual(len(r["m7_designated_project_exceptions"]),3)
        self.assertIn("Lutri",r["m7_companion_physical_convention"])

    def test_tracker_exact_hash_date_and_exceptions(self):
        with TRACKER.open(encoding="utf-8",newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        r=next(x for x in rows if x["index"]=="7")
        self.assertEqual(r["deck_id"],"Cecily__Bjorna__Lutri")
        self.assertEqual(r["final_list_hash"],RAW)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertEqual(r["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("ten",r["swap_decision_ledger_complete"])
        self.assertIn("Lutri",r["official_named_ban_list_checkpoint"])
        self.assertIn("PROJECT ONLY",r["fresh_official_legality_check"])

    def test_previous_seven_m7_locks_remain_immutable(self):
        for key,expected in PREVIOUS_M7.items():
            with self.subTest(deck=key):
                r=self.registry[key]
                self.assertEqual((r["approval_status"],r["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(r["approved_list_sha256"],expected)

if __name__=="__main__": unittest.main()
