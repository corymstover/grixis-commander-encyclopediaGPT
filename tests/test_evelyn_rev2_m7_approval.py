"""Exact Evelyn M7 Rev2 owner-approved canonical list with seventeen prior locks.

Archived Oct23 live Scryfall evidence; no live Oct24 retrieval, match win rate,
third-model independence or complete unrelated historical test suite claim.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT / "refinement/decklists/Evelyn_the_Covetous_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Evelyn_the_Covetous_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.md"
VERIFY = ROOT / "refinement/verification/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac"
OLD = "1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a"
DECK_ID = "Evelyn__the_Covetous"
SWAPS = [
    ("Marsh Flats", "Thundering Falls"),
    ("Insolent Neonate", "Spellskite"),
    ("Brainstorm", "Redirect Lightning"),
    ("Burnt Offering", "Wan Shi Tong, Librarian"),
    ("Verdant Catacombs", "Blazemire Verge"),
]
KEEPS = {"Vexing Bauble", "Ripples of Undeath", "Saw in Half",
         "Windfall", "Notion Thief", "Stifle", "Mistrise Village",
         "Leyline of Anticipation", "Thassa's Oracle", "Underworld Breach",
         "Worldgorger Dragon", "Animate Dead", "Dance of the Dead", "Necromancy"}
GAME_CHANGERS = {
    "Ad Nauseam", "Ancient Tomb", "Chrome Mox", "Demonic Tutor",
    "Force of Will", "Gamble", "Imperial Seal", "Lion's Eye Diamond",
    "Mana Vault", "Mox Diamond", "Mystical Tutor", "Necropotence",
    "Notion Thief", "Opposition Agent", "Orcish Bowmasters",
    "Rhystic Study", "Thassa's Oracle", "Underworld Breach", "Vampiric Tutor"
}
PRIOR_17 = {
    "Abaddon_the_Despoiler": ("5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24", "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"),
    "Admiral_Beckett_Brass": ("ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000", "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"),
    "Admiral_Brass__Unsinkable": ("dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7", "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"),
    "Anhelo_the_Painter": ("865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77", "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"),
    "Ashad_the_Lone_Cyberman": ("352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267", "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"),
    "Ashnod_the_Uncaring": ("a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761", "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"),
    "Be_lakor_the_Dark_Master": ("2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4", "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"),
    "Cecily__Bjorna__Lutri": ("e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d", "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"),
    "Cormela__Glamour_Thief": ("d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd", "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"),
    "Crosis__the_Purger": ("a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a", "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"),
    "Cult_of_Skaro": ("e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d", "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"),
    "Davros__Dalek_Creator": ("96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc", "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"),
    "Doctor_Doom__King_of_Latveria": ("7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20", "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"),
    "Don_Andres__the_Renegade": ("59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f", "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"),
    "Dr__Eggman": ("3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec", "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"),
    "Edea__Possessed_Sorceress": ("a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54", "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"),
    "Edward_Kenway": ("8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1", "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt"),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (i+1, line)
        qty,name,commander=int(m[1]),m[2],m[3]
        if i==0:
            assert (qty,name,bool(commander))==(1,"Evelyn, the Covetous",True)
        else:
            assert commander is None
        cards[name]+=qty
    return cards,lines

class EvelynM7Rev2ExactApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards,cls.lines=parse(APPROVED)
        cls.old,_=parse(BASELINE)
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.ev={x["name"]:x for x in cls.oracle["cards"]}
        cls.registry=json.loads(REGISTRY.read_text(encoding="utf-8"))
        with TRACKER.open(newline="",encoding="utf-8") as f:
            cls.tracker=list(csv.DictReader(f))

    def test_exact_raw_sha_and_preserved_historical_file(self):
        self.assertEqual(digest(APPROVED),SHA)
        self.assertEqual(digest(BASELINE),OLD)
        self.assertEqual(self.oracle["candidate_raw_sha256"],SHA)
        self.assertEqual(self.oracle["baseline_raw_sha256"],OLD)
        self.assertIn(SHA,RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(SHA,VERIFY.read_text(encoding="utf-8"))

    def test_exact_100_singleton_and_five_owner_swaps(self):
        self.assertEqual(len(self.lines),100)
        self.assertEqual(sum(self.cards.values()),100)
        self.assertEqual(len(self.cards),100)
        self.assertTrue(all(q==1 for q in self.cards.values()))
        self.assertEqual(set(self.cards)-set(self.old),{x for x,_ in SWAPS})
        self.assertEqual(set(self.old)-set(self.cards),{x for _,x in SWAPS})
        self.assertTrue(KEEPS <= self.cards.keys())

    def test_archived_oracle_legality_identity_and_count(self):
        self.assertEqual(set(self.cards),set(self.ev))
        self.assertEqual(sum(q for name,q in self.cards.items()
                             if "Land" in self.ev[name]["type_line"]),26)
        self.assertEqual({name for name in self.cards
                          if self.ev[name].get("game_changer")},GAME_CHANGERS)
        self.assertEqual({name for name in self.cards
                          if "Vampire" in self.ev[name]["type_line"]},
                         {"Evelyn, the Covetous","Insolent Neonate"})
        for name,q in self.cards.items():
            c=self.ev[name]
            self.assertEqual(c["quantity"],q)
            self.assertEqual(c["commander_legality"],"legal",name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"),name)
            self.assertTrue(c["oracle_id"],name)
        self.assertEqual(self.oracle["project_exceptions"],[])

    def test_commander_and_combo_oracle_boundaries(self):
        txt=lambda n:self.ev[n]["oracle_text"]
        self.assertIn("Whenever Evelyn or another Vampire you control enters",
                      txt("Evelyn, the Covetous"))
        self.assertIn("Once each turn, you may play a card",
                      txt("Evelyn, the Covetous"))
        self.assertIn("Discard a card, Sacrifice this creature: Draw a card",
                      txt("Insolent Neonate"))
        self.assertIn("As an additional cost to cast this spell, sacrifice a creature",
                      txt("Burnt Offering"))
        self.assertIn("Draw three cards, then put two cards",txt("Brainstorm"))
        self.assertIn("if no mana was spent to cast it, counter that spell",
                      txt("Vexing Bauble"))
        self.assertIn("exile all other permanents you control",
                      txt("Worldgorger Dragon"))

    def test_owner_registry_and_tracker_record(self):
        self.assertEqual(len(self.registry["decks"]),62)
        state=self.registry["decks"][DECK_ID]
        self.assertEqual((state["approval_status"],state["lock_status"],
                          state["current_stage"]),("APPROVED","LOCKED","LOCKED"))
        self.assertTrue(state["final_gate_passed"])
        self.assertEqual(state["approved_list_sha256"],SHA)
        self.assertEqual(state["m7_final_candidate_sha256"],SHA)
        self.assertEqual(state["previous_approved_source_raw_sha256"],OLD)
        self.assertEqual(state["previous_approved_list_artifact"],str(BASELINE.relative_to(ROOT)))
        self.assertEqual(state["approved_list_artifact"],str(APPROVED.relative_to(ROOT)))
        self.assertEqual(state["user_approval_date"],"2026-10-23")
        self.assertEqual(state["m7_power_bracket"],"5 — cEDH")
        self.assertEqual(state["m7_archidekt_tags"],["cEDH","Worldgorger Combo","Thassa's Oracle"])
        self.assertEqual(state["m7_project_exceptions"],[])
        self.assertEqual(len(self.tracker),62)
        entry=self.tracker[17]
        self.assertEqual(entry["deck_id"],DECK_ID)
        self.assertEqual(entry["final_list_hash"],SHA)
        self.assertEqual(entry["user_approval_date"],"2026-10-23")
        self.assertEqual(entry["final_gate_passed"],"YES")
        self.assertIn("M7 Rev2",entry["refinement_status"])

    def test_earlier_seventeen_m7_locks_untouched(self):
        for deck_id,(expected_sha,path) in PRIOR_17.items():
            r=self.registry["decks"][deck_id]
            self.assertEqual(r["approved_list_sha256"],expected_sha,deck_id)
            self.assertEqual(r["approved_list_artifact"],path,deck_id)
            self.assertEqual(r["approval_status"],"APPROVED",deck_id)
            self.assertEqual(r["lock_status"],"LOCKED",deck_id)
            self.assertEqual(digest(ROOT/path),expected_sha,deck_id)

if __name__=="__main__":
    unittest.main()
