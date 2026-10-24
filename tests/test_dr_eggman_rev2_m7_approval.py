"""Exact owner-approved Dr Eggman M7 Rev2 canonical lock and fourteen earlier-lock regression.

Oracle is archived 2026-10-23 primary Scryfall evidence (including Gloomlake source).
This is not a standalone match simulation or new independent third-model pass.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APPROVED=ROOT/"refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"
BASELINE=ROOT/"refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt"
ORACLE=ROOT/"refinement/verification/Dr_Eggman_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Dr_Eggman_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Dr_Eggman_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXACT="3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec"
OLD="ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3"
DECK_ID="Dr__Eggman"
COMMANDER="Dr. Eggman"
SWAPS=[
 ("Possession Engine","Blasphemous Act"),
 ("Skysovereign, Consul Flagship","Cybermen Squadron"),
 ("Interceptor Mechan","Cryptothrall"),
 ("Behemoth of Vault 0","Weapons Manufacturing"),
 ("Gloomlake Verge","Withering Torment"),
]
BASICS={"Island":2,"Mountain":2,"Swamp":2}
ROCKS={"Arcane Signet","Fellwar Stone","Mox Opal","Sol Ring",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
GAME_CHANGERS={"Ancient Tomb","Cyclonic Rift","Fierce Guardianship"}
PRIOR_14={
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
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    cards=Counter()
    for i,line in enumerate(lines):
        m=re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?",line)
        if m is None:
            raise AssertionError("Invalid line "+str(i+1)+": "+line)
        q,n,comm=int(m.group(1)),m.group(2),m.group(3)
        if i==0:
            assert (q,n,bool(comm))==(1,COMMANDER,True)
        else:
            assert comm is None
        cards[n]+=q
    return cards,lines

class EggmanM7Rev2ExactApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck,cls.lines=parse(APPROVED)
        cls.old,_=parse(BASELINE)
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={x["name"]:x for x in cls.oracle["cards"]}
        cls.registry=json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.receipt=RECEIPT.read_text(encoding="utf-8")
        cls.verification=VERIFY.read_text(encoding="utf-8")
        with TRACKER.open(newline="",encoding="utf-8") as f:
            cls.tracker=list(csv.DictReader(f))

    def test_exact_approved_bytes_and_immutable_oct14(self):
        self.assertEqual(sha(APPROVED),EXACT)
        self.assertEqual(sha(BASELINE),OLD)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(self.oracle["candidate_raw_sha256"],EXACT)
        self.assertEqual(self.oracle["owner_approved_exact_sha256"],EXACT)
        self.assertEqual(self.oracle["canonical_baseline_sha256"],OLD)
        self.assertIn("EXACT_OWNER_APPROVED_CANONICAL_LOCKED",self.oracle["status"])

    def test_100_physical_97_names_and_singleton(self):
        self.assertEqual(sum(self.deck.values()),100)
        self.assertEqual(len(self.lines),97)
        self.assertEqual(len(self.deck),97)
        self.assertEqual(self.lines[0],"1x Dr. Eggman [Commander]")
        self.assertEqual(self.deck[COMMANDER],1)
        self.assertEqual({n:q for n,q in self.deck.items() if q>1},BASICS)
        self.assertEqual(self.oracle["physical_cards"],100)
        self.assertEqual(self.oracle["distinct_names"],97)

    def test_only_five_owner_approved_substitutions(self):
        self.assertEqual(len(SWAPS),5)
        self.assertEqual(self.deck-self.old,Counter({a:1 for a,b in SWAPS}))
        self.assertEqual(self.old-self.deck,Counter({b:1 for a,b in SWAPS}))
        self.assertEqual(self.deck["Foundry Inspector"],1)
        self.assertEqual(self.deck["Unwinding Clock"],1)
        self.assertNotIn("Blasphemous Act",self.deck)
        self.assertIn("previously retained",self.receipt)
        self.assertIn("Okay you can approve that deck",self.receipt)

    def test_oracle_eligibility_and_source_chain(self):
        self.assertEqual(set(self.deck),set(self.cards))
        self.assertEqual(len(self.oracle["cards"]),97)
        self.assertTrue(self.oracle["commander_legal_all"])
        self.assertTrue(self.oracle["color_identity_all_ubr"])
        self.assertEqual(self.oracle["project_exceptions"],[])
        for n,q in self.deck.items():
            with self.subTest(card=n):
                c=self.cards[n]
                self.assertEqual(c["quantity"],q)
                self.assertEqual(c["commander_legality"],"legal")
                self.assertTrue(c["oracle_id"] and c["oracle_text"] and c["source"])
                self.assertTrue(set(c["color_identity"]) <= {"U","B","R"})

    def test_32_lands_31_eligible_payloads_7_rocks_3_gcs(self):
        cards=self.cards.values()
        lands=sum(c["quantity"] for c in cards if "Land" in c["type_line"].split(" — ")[0])
        eligible=sum(c["quantity"] for c in cards
                     if " — " in c["type_line"]
                     if re.search(r"\b(?:Robot|Construct|Vehicle)\b",
                                  c["type_line"].split(" — ",1)[1].split(" // ")[0]))
        self.assertEqual(lands,32)
        self.assertEqual(eligible,31)
        self.assertEqual(self.oracle["lands"],32)
        self.assertEqual(self.oracle["payloads"],31)
        self.assertEqual(set(self.deck)&ROCKS,ROCKS)
        self.assertEqual(set(self.oracle["mana_rocks"]),ROCKS)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},GAME_CHANGERS)
        self.assertEqual(set(self.oracle["game_changers"]),GAME_CHANGERS)

    def test_real_commander_and_artifact_mechanics(self):
        o=lambda n:self.cards[n]["oracle_text"]
        self.assertIn("At the beginning of your end step, draw a card",o(COMMANDER))
        self.assertIn("faces a villainous choice",o(COMMANDER))
        self.assertIn("put a Construct, Robot, or Vehicle card",o(COMMANDER))
        self.assertIn("When this Vehicle enters, gain control",o("Possession Engine"))
        self.assertIn("can't attack or block",o("Possession Engine"))
        self.assertIn("Crew 3",o("Skysovereign, Consul Flagship"))
        self.assertIn("enters or attacks",o("Skysovereign, Consul Flagship"))
        self.assertIn("return target artifact or creature card",o("Interceptor Mechan"))
        self.assertIn("When this creature dies",o("Behemoth of Vault 0"))
        self.assertIn("{E}{E}{E}{E}",o("Behemoth of Vault 0"))
        self.assertIn("control an Island or a Swamp",o("Gloomlake Verge"))
        self.assertIn("Artifact spells you cast cost",o("Foundry Inspector"))
        self.assertIn("each other player's untap step",o("Unwinding Clock"))
        for n in ("Master Transmuter","Kuldotha Forgemaster","Scrapyard Recombiner"):
            self.assertIn("{T}",o(n))
            self.assertIn("Artifact Creature",self.cards[n]["type_line"])
        self.assertIn("empty hand",self.verification)
        self.assertIn("Put",self.verification)
        self.assertIn("no gameplay win rate",self.verification)

    def test_registry_tracker_owner_and_original_sources(self):
        self.assertEqual(len(self.registry["decks"]),62)
        d=self.registry["decks"][DECK_ID]
        self.assertEqual((d["approval_status"],d["lock_status"],d["current_stage"]),
                         ("APPROVED","LOCKED","LOCKED"))
        self.assertEqual(d["approved_list_sha256"],EXACT)
        self.assertEqual(d["approved_list_artifact"],APPROVED.relative_to(ROOT).as_posix())
        self.assertEqual(d["previous_approved_list_sha256"],OLD)
        self.assertEqual(d["previous_approved_list_artifact"],BASELINE.relative_to(ROOT).as_posix())
        self.assertEqual(d["m7_archidekt_tags"],["Villainous Choice","Robots","Artifact Cheat"])
        self.assertEqual(d["m7_power_bracket"],"4 — Optimized")
        self.assertTrue(d["m7_verified_100_physical"])
        self.assertEqual(len(self.tracker),62)
        row=self.tracker[14]
        self.assertEqual((row["index"],row["deck_id"]),("14",DECK_ID))
        self.assertEqual(row["final_list_hash"],EXACT)
        self.assertEqual(row["user_approval_date"],"2026-10-23")
        self.assertEqual(row["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",row["refinement_status"])
        self.assertIn(EXACT,self.receipt)

    def test_previous_fourteen_canonical_locks_unchanged(self):
        for k,(expected,path) in PRIOR_14.items():
            with self.subTest(deck=k):
                d=self.registry["decks"][k]
                self.assertEqual(d["approved_list_sha256"],expected)
                self.assertEqual(d["approved_list_artifact"],path)
                self.assertEqual(d["lock_status"],"LOCKED")
                self.assertEqual(sha(ROOT/path),expected)

if __name__=="__main__":
    unittest.main()
