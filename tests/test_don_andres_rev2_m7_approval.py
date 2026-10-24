"""Exact Cory-approved Don Andres M7 Rev2 100-card canonical lock and 13 earlier-lock regression."""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT / "refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Don_Andres_the_Renegade_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.md"
VERIFICATION = ROOT / "refinement/verification/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXACT = "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f"
OLD = "a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb"
COMMANDER = "Don Andres, the Renegade"
ID = "Don_Andres__the_Renegade"
SWAPS = [
    ("Gríma, Saruman's Footman", "Professional Face-Breaker"),
    ("Fallen Shinobi", "Seize the Spotlight"),
    ("Treachery", "Blasphemous Act"),
    ("Gloomlake Verge", "Shipwreck Marsh"),
    ("Blazemire Verge", "Smoldering Marsh"),
    ("Mind's Dilation", "Stolen Strategy"),
    ("Passionate Archaeologist", "Breeches, Eager Pillager"),
]
ROCKS = {"Arcane Signet","Dimir Signet","Fellwar Stone","Izzet Signet","Rakdos Signet",
         "Sol Ring","Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
GAME_CHANGERS = {"Ancient Tomb","Cyclonic Rift","Fierce Guardianship","Opposition Agent","Vampiric Tutor"}
PRIOR_LOCKS = {
    "Abaddon_the_Despoiler": "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
    "Admiral_Beckett_Brass": "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
    "Admiral_Brass__Unsinkable": "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
    "Anhelo_the_Painter": "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    "Ashad_the_Lone_Cyberman": "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "Ashnod_the_Uncaring": "a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
    "Be_lakor_the_Dark_Master": "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
    "Cecily__Bjorna__Lutri": "e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
    "Cormela__Glamour_Thief": "d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd",
    "Crosis__the_Purger": "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a",
    "Cult_of_Skaro": "e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d",
    "Davros__Dalek_Creator": "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc",
    "Doctor_Doom__King_of_Latveria": "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20"
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    cards=Counter()
    lines=path.read_text(encoding="utf-8").splitlines()
    for i,line in enumerate(lines):
        m=re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?",line)
        if not m: raise AssertionError("Unparseable row %s: %s" % (i+1,line))
        qty,name,tag=int(m.group(1)),m.group(2),m.group(3)
        if i==0:
            assert name==COMMANDER and qty==1 and tag
        else:
            assert tag is None
        cards[name]+=qty
    return cards,lines

class DonAndresM7Rev2ExactOwnerApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck,cls.lines=parse(APPROVED)
        cls.old,_=parse(BASELINE)
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.oracle["cards"]}
        cls.adversarial={c["name"]:c for c in cls.oracle["adversarial_source_cards"]}
        cls.reg=json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.receipt=RECEIPT.read_text(encoding="utf-8")
        cls.verification=VERIFICATION.read_text(encoding="utf-8")
        with TRACKER.open(encoding="utf-8",newline="") as f:
            cls.rows=list(csv.DictReader(f))

    def test_exact_raw_sha_and_historical_preservation(self):
        self.assertEqual(sha(APPROVED),EXACT)
        self.assertEqual(sha(BASELINE),OLD)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(self.oracle["candidate_sha256"],EXACT)
        self.assertEqual(self.oracle["owner_approved_exact_sha256"],EXACT)
        self.assertEqual(self.oracle["baseline_sha256"],OLD)
        self.assertIn("EXACT_OWNER_APPROVED_CANONICAL_LOCKED",self.oracle["status"])

    def test_100_physical_only_island_repeated(self):
        self.assertEqual(sum(self.deck.values()),100)
        self.assertEqual(len(self.lines),99)
        self.assertEqual(len(self.deck),99)
        self.assertEqual(self.deck[COMMANDER],1)
        self.assertEqual(self.lines[0],"1x Don Andres, the Renegade [Commander]")
        self.assertEqual({n:q for n,q in self.deck.items() if q>1},{"Island":2})
        self.assertEqual(self.oracle["physical_cards"],100)
        self.assertEqual(self.oracle["distinct_names"],99)

    def test_seven_owner_approved_changes_exact(self):
        self.assertEqual(len(SWAPS),7)
        self.assertEqual(self.deck-self.old,Counter({a:1 for a,_ in SWAPS}))
        self.assertEqual(self.old-self.deck,Counter({b:1 for _,b in SWAPS}))
        for name in ("Thieving Amalgam","Jhoira, Weatherlight Corsair","Insurrection",
                     "Gonti, Night Minister","Roaming Throne","Wand of Wonder","Kindred Discovery"):
            self.assertEqual(self.deck[name],1)

    def test_oracle_commander_color_identity_and_legality(self):
        self.assertEqual(set(self.deck),set(self.cards))
        self.assertEqual(len(self.cards),99)
        self.assertTrue(self.oracle["commander_legal_all"])
        self.assertTrue(self.oracle["color_identity_all_ubr"])
        self.assertEqual(self.oracle["project_exceptions"],[])
        for n,q in self.deck.items():
            with self.subTest(card=n):
                c=self.cards[n]
                self.assertEqual(c["quantity"],q)
                self.assertTrue(c["oracle_id"] and c["oracle_text"] and c["source"])
                self.assertEqual(c["commander_legality"],"legal")
                self.assertTrue(set(c["color_identity"]) <= {"U","B","R"})

    def test_lands_rocks_game_changers_and_bracket(self):
        lands=sum(c["quantity"] for c in self.cards.values() if "Land" in c["type_line"])
        self.assertEqual(lands,35)
        self.assertEqual(self.oracle["land_count"],35)
        self.assertEqual(set(self.deck)&ROCKS,ROCKS)
        self.assertEqual(set(self.oracle["mana_rocks"]),ROCKS)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},GAME_CHANGERS)
        self.assertEqual(set(self.oracle["game_changers"]),GAME_CHANGERS)
        self.assertEqual(self.reg["decks"][ID]["m7_power_bracket"],"4 — Optimized")

    def test_land_conditions_and_legitimate_trades(self):
        self.assertIn("two or more other lands",self.adversarial["Shipwreck Marsh"]["oracle_text"])
        self.assertNotIn("two or more basic lands",self.adversarial["Shipwreck Marsh"]["oracle_text"])
        self.assertIn("two or more basic lands",self.adversarial["Smoldering Marsh"]["oracle_text"])
        self.assertIn("control an Island or a Swamp",self.cards["Gloomlake Verge"]["oracle_text"])
        self.assertIn("control a Swamp or a Mountain",self.cards["Blazemire Verge"]["oracle_text"])
        self.assertIn("two **other** lands",self.verification)
        self.assertIn("two **basic** lands",self.verification)

    def test_actual_theft_background_treasure_and_untap_rules(self):
        text=lambda n:self.cards[n]["oracle_text"]
        self.assertIn("control but don't own",text(COMMANDER))
        self.assertIn("a noncreature spell you don't own",text(COMMANDER))
        self.assertIn("two tapped Treasure tokens",text(COMMANDER))
        self.assertIn("Commander creatures you own",text("Passionate Archaeologist"))
        self.assertIn("Whenever you cast a spell from exile",text("Passionate Archaeologist"))
        self.assertIn("their first spell each turn",text("Mind's Dilation"))
        self.assertIn("without paying its mana cost",text("Mind's Dilation"))
        self.assertIn("Gríma can't be blocked",text("Gríma, Saruman's Footman"))
        self.assertIn("Ninjutsu",text("Fallen Shinobi"))
        self.assertIn("untap up to five lands",text("Treachery"))
        self.assertIn("triggers an additional time",text("Roaming Throne"))

    def test_bounded_three_opponent_cast_trace_not_game_simulation(self):
        spells=[("opponent","Sorcery",2,True),
                ("opponent","Creature",4,True),
                ("opponent","Instant",6,True)]
        treas=sum(2 for owner,typ,mv,exile in spells if owner=="opponent" and typ!="Creature")
        damage=sum(mv for owner,typ,mv,exile in spells if exile)
        self.assertEqual(treas,4)
        self.assertEqual(damage,12)
        self.assertIn("conditional source-bound trace",self.verification)
        self.assertIn("not a simulated game result",self.verification.lower())

    def test_registry_only_don_changed_and_all_thirteen_locks_pinned(self):
        self.assertEqual(len(self.reg["decks"]),62)
        d=self.reg["decks"][ID]
        self.assertEqual(d["approved_list_sha256"],EXACT)
        self.assertEqual(d["m7_final_candidate_sha256"],EXACT)
        self.assertEqual(d["previous_approved_source_raw_sha256"],OLD)
        self.assertEqual(d["previous_approved_list_artifact"],
                         "refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt")
        self.assertEqual(d["approval_status"],"APPROVED")
        self.assertEqual(d["lock_status"],"LOCKED")
        self.assertEqual(d["user_approval_date"],"2026-10-23")
        self.assertEqual(d["m7_archidekt_tags"],["Theft","Pirates","Treasure"])
        self.assertTrue(d["m7_verified_100_physical"])
        self.assertEqual(d["m7_project_exceptions"],[])
        for key,expected in PRIOR_LOCKS.items():
            with self.subTest(previous=key):
                p=self.reg["decks"][key]
                self.assertEqual(p["approved_list_sha256"],expected)
                self.assertEqual(sha(ROOT/p["approved_list_artifact"]),expected)

    def test_tracker_scope_and_owner_receipt(self):
        self.assertEqual(len(self.rows),62)
        matched=[r for r in self.rows if r["deck_id"]==ID]
        self.assertEqual(len(matched),1)
        row=matched[0]
        self.assertEqual(row["index"],"13")
        self.assertEqual(row["final_list_hash"],EXACT)
        self.assertEqual(row["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",row["refinement_status"])
        self.assertIn("M7 CANONICAL REVISION",row["notes"])
        self.assertIn("> Approve",self.receipt)
        self.assertIn(EXACT,self.receipt)
        self.assertIn("only this exact 100-card",self.receipt)
        self.assertIn("Deck #15 Dr. Eggman",self.receipt)
        self.assertIn("40058523937",self.receipt)
        self.assertIn("no measured multiplayer win-rate",self.receipt.lower())

if __name__=="__main__":
    unittest.main()
