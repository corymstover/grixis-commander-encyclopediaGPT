"""Canonical exact Cory-approved Be'lakor M7 Rev2 eight-swap lock and prior preservation."""
import csv, hashlib, json, unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt"
ORACLE=ROOT/"refinement/verification/Be_lakor_the_Dark_Master_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4"
PREVIOUS="3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e"
SWAPS=(
 ("Dream Devourer","Desecration Demon"),
 ("Blasphemous Act","Kindred Dominance"),
 ("Rakdos, Patron of Chaos","Demonlord Belzenlok"),
 ("Bloodthirster","Shadowgrange Archfiend"),
 ("Fellwar Stone","Cursed Mirror"),
 ("Balor","Curse-Marred Demon"),
 ("Crumbling Necropolis","City of Brass"),
 ("Foreboding Ruins","Mana Confluence"),
)
ROCKS={"Sol Ring","Arcane Signet","Rakdos Signet","Talisman of Creativity",
       "Talisman of Dominance","Talisman of Indulgence","Cursed Mirror"}
GCS={"Ancient Tomb","Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Vampiric Tutor"}
PREVIOUS_M7={
 "Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
 "Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
 "Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
 "Anhelo_the_Painter":"865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
 "Ashad_the_Lone_Cyberman":"352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
 "Ashnod_the_Uncaring":"a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    cards=Counter()
    for line in lines:
        q,n=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        cards[n.removesuffix(" [Commander]")]+=int(q)
    return lines,cards

class BeLakorRev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards=json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]
        cls.oracle={x["name"]:x for x in cls.cards}
        cls.registry=json.loads(STATE.read_text(encoding="utf-8"))["decks"]
        cls.lines,cls.counts=parse(NEW)

    def test_exact_raw_sha_100_physical_and_singleton(self):
        self.assertEqual(sha(NEW),RAW)
        self.assertEqual(self.lines[0],"1x Be'lakor, the Dark Master [Commander]")
        self.assertEqual((len(self.lines),len(self.counts),sum(self.counts.values())),(94,94,100))
        self.assertEqual({n:q for n,q in self.counts.items() if q>1},{"Island":3,"Mountain":2,"Swamp":4})
        self.assertEqual(sum("[Commander]" in s for s in self.lines),1)

    def test_exact_eight_swaps_and_historical_bytes(self):
        self.assertEqual(sha(OLD),PREVIOUS)
        _,before=parse(OLD)
        self.assertEqual(sum(before.values()),100)
        self.assertEqual(self.counts-before,Counter({add:1 for cut,add in SWAPS}))
        self.assertEqual(before-self.counts,Counter({cut:1 for cut,add in SWAPS}))

    def test_current_selected_oracle_legality_and_grixis_identity(self):
        o=json.loads(ORACLE.read_text(encoding="utf-8"))
        self.assertEqual(o["candidate_raw_sha256"],RAW)
        self.assertEqual(o["physical_cards"],100)
        self.assertEqual(o["unique_card_names"],94)
        self.assertEqual(o["exceptions"],[])
        self.assertEqual(len(self.cards),94)
        self.assertEqual(set(self.oracle),set(self.counts))
        for n,q in self.counts.items():
            c=self.oracle[n]
            self.assertEqual(c["quantity"],q,n)
            self.assertEqual(c["commander_legality"],"legal",n)
            self.assertLessEqual(set(c["color_identity"]),{"U","B","R"},n)
            self.assertTrue(c["oracle_id"],n)
            self.assertTrue(c["oracle_text"] is not None,n)
            self.assertTrue(c["source"],n)

    def test_lands_demons_ramp_bracket(self):
        self.assertEqual(sum(c["quantity"] for c in self.cards if "Land" in c["type_line"]),36)
        self.assertEqual(sum(c["quantity"] for c in self.cards if "Demon" in c["type_line"]),25)
        self.assertEqual(ROCKS & set(self.counts),ROCKS)
        self.assertEqual({n for n in self.counts if self.oracle[n]["game_changer"]},GCS)
        o=json.loads(ORACLE.read_text(encoding="utf-8"))
        self.assertEqual((o["lands"],o["printed_demons"],o["static_mana_rocks"]),(36,25,7))

    def test_oracle_interactions_and_caveats(self):
        self.assertIn("discard a card at random",self.oracle["Curse-Marred Demon"]["oracle_text"])
        self.assertIn("greatest power among creatures sacrificed",self.oracle["Shadowgrange Archfiend"]["oracle_text"])
        self.assertIn("copy of any creature",self.oracle["Cursed Mirror"]["oracle_text"])
        t=VERIFY.read_text(encoding="utf-8")
        self.assertIn("5+5×4",t)
        self.assertIn("25 finite Lord triggers",t)
        self.assertIn("legend rule",t)
        self.assertIn("not a formal certificate",t)
        self.assertIn("Spellbook",t)

    def test_registry_and_exact_owner_scope(self):
        x=self.registry["Be_lakor_the_Dark_Master"]
        self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
        self.assertEqual(x["approved_list_sha256"],RAW)
        self.assertEqual(x["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(x["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(x["m7_archidekt_tags"],["Demon Tribal","ETB Damage","Reanimator"])
        self.assertEqual(x["m7_power_bracket"],"4 — Optimized")
        s=RECEIPT.read_text(encoding="utf-8")
        self.assertIn("> Approve",s)
        self.assertIn(RAW,s)
        self.assertIn("not a blanket delegation",s)
        self.assertIn("non-independent",s)

    def test_tracker_row_and_alias_preserved(self):
        with TRACKER.open(newline="",encoding="utf-8") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        r=next(x for x in rows if x["index"]=="6")
        self.assertEqual(r["deck_id"],"Be_lakor__the_Dark_Master")
        self.assertEqual(r["final_list_hash"],RAW)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertEqual(r["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("eight",r["swap_decision_ledger_complete"])

    def test_six_preceding_m7_locks_unchanged(self):
        for k,h in PREVIOUS_M7.items():
            with self.subTest(deck=k):
                x=self.registry[k]
                self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(x["approved_list_sha256"],h)

if __name__=="__main__": unittest.main()
