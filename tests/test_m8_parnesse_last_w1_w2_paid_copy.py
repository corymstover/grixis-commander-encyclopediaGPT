"""Parnesse original W1/W2: real Narset stack copies and paid Reiterate buyback."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = "Parnesse__the_Subtle_Brush"
SHA = "63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c"
PLAN = "d4e18342ded198de1c9faccb21251df2580f387f"


def narset_search_stack(*, own_library=20, mana_available=5,
                        blue_symbols_available=3, search_present=True,
                        reversal_present=True, twinning_staff=True,
                        reversal_resolves=True, target_still_on_stack=True):
    """Pay Frantic Search {2}{U}, then Narset's Reversal {U}{U}.

    Twinning replacement adds a second *copy* of Search, not a second cast.
    The original Search returns to hand; the actual Reversal resolves to its
    graveyard. Two copies draw/discard two each and untap up to three lands
    each. None of these copies is a cast or puts Narset back into hand.
    """
    if not search_present or mana_available < 3 or blue_symbols_available < 1:
        return {"cast": False, "draws": 0, "search_returned": False}
    can_reversal = (reversal_present and mana_available >= 5
                    and blue_symbols_available >= 3)
    if not can_reversal or not reversal_resolves:
        # The original Search can resolve normally, if still on stack.
        copies = 1 if target_still_on_stack else 0
        returned = False
    elif not target_still_on_stack:
        copies = 0
        returned = False
    else:
        copies = 1 + int(twinning_staff)
        returned = True
    draws = min(own_library, 2 * copies)
    return {"cast": True, "search_copies_resolved": copies,
            "draws": draws, "discards": draws,
            "failed_empty_draw": draws < 2 * copies,
            "land_untaps_available": copies * 3,
            "search_returned": returned,
            "narset_returned": False, "narset_zone":
            "graveyard" if can_reversal and reversal_resolves and target_still_on_stack
            else "stack_or_graveyard"}


def reiterate_geyser_loop(*, opponent_tapped_lands=10, initial_red=6,
                          repeats=40, buyback=True,
                          geyser_original_on_stack=True,
                          reiterate_in_hand=True, opponent_stops_loop=False):
    """One Reiterate with buyback 3 plus 1RR = six real red per cast.

    Original Mana Geyser was paid {3}{R}{R} and remains on stack while
    copies add R for each *actually tapped* opponent land. Reiterate comes
    back to hand by its buyback replacement and can target the original
    again. Copies never add storm because they are not cast spells.
    """
    red = initial_red
    n = 0
    snapshots = []
    for _ in range(repeats):
        if (not buyback or not geyser_original_on_stack or
                not reiterate_in_hand or opponent_stops_loop or red < 6):
            break
        red -= 6
        red += opponent_tapped_lands
        n += 1
        snapshots.append({"reiterate_casts": n, "red": red,
                          "geyser_copies": n, "original_on_stack": True,
                          "reiterate_in_hand": True})
    # Earlier original Geyser cast and each *real Reiterate cast* add storm.
    before_grapeshot = 1 + n
    grapeshot_paid = red >= 2
    return {"history": tuple(snapshots), "red": red,
            "reiterate_casts": n, "original_geyser_resolved": False,
            "storm_count_before_grapeshot": before_grapeshot,
            "grapeshot_payable": grapeshot_paid,
            "grapeshot_damage_objects": 1 + before_grapeshot if grapeshot_paid else 0}


class ParnesseLastOriginalW1W2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in idx["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        assert raw.decode().splitlines()[0] == "1x Parnesse, the Subtle Brush [Commander]"
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            n, card = line.split("x ", 1)
            cls.cards[card.removesuffix(" [Commander]")] += int(n)
        assert sum(cls.cards.values()) == 100
        rec = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                          / f"{DECK}_{SHA[:16]}.json").read_text())
        assert rec["approved_raw_sha256"] == SHA
        assert rec["m6_transfer"]["plan_blob_sha"] == PLAN
        cls.deferred = {r["case_id"] for r in rec["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as f:
            for line in f:
                row = json.loads(line)
                cls.oracle[row["canonical_name"]] = row["oracle_text"]

    def source(self, case, *names):
        self.assertIn(case, self.deferred)
        for name in names:
            self.assertEqual(self.cards[name], 1, name)

    def test_W1_paid_narset_twinning_frantic_search_finite_copies_not_infinite(self):
        self.source("W1", "Narset's Reversal", "Twinning Staff",
                    "Reiterate", "Increasing Vengeance", "Reverberate",
                    "Return the Favor", "Primal Amulet // Primal Wellspring",
                    "Frantic Search", "Storm-Kiln Artist", "Bonus Round",
                    "Thousand-Year Storm")
        self.assertIn("return it to its owner's hand", self.oracle["Narset's Reversal"])
        self.assertIn("that many times plus an additional time", self.oracle["Twinning Staff"])
        self.assertIn("Untap up to three lands", self.oracle["Frantic Search"])
        r = narset_search_stack()
        self.assertEqual(r["search_copies_resolved"], 2)
        self.assertEqual((r["draws"], r["discards"]), (4, 4))
        self.assertEqual(r["land_untaps_available"], 6)
        self.assertTrue(r["search_returned"])
        self.assertFalse(r["narset_returned"])
        self.assertEqual(r["narset_zone"], "graveyard")
        self.assertEqual(narset_search_stack(twinning_staff=False)
                         ["search_copies_resolved"], 1)
        self.assertEqual(narset_search_stack(reversal_resolves=False)
                         ["search_copies_resolved"], 1)
        self.assertEqual(narset_search_stack(target_still_on_stack=False)
                         ["search_copies_resolved"], 0)
        self.assertTrue(narset_search_stack(own_library=3)["failed_empty_draw"])
        self.assertFalse(narset_search_stack(mana_available=4)["search_returned"])
        self.assertFalse(narset_search_stack(blue_symbols_available=2)["search_returned"])
        # Search copies draw from a finite library; this does not itself
        # return Narset's Reversal from grave or create unlimited mana.

    def test_W2_paid_reiterate_geyser_buyback_invariant_and_grapeshot_storm(self):
        self.source("W2", "Reiterate", "Increasing Vengeance", "Reverberate",
                    "Return the Favor", "Alania, Divergent Storm",
                    "Prismari, the Inspiration", "Thousand-Year Storm",
                    "Mana Geyser", "Jeska's Will", "Grapeshot")
        self.assertEqual(self.cards["Pyromancer's Goggles"], 0)
        self.assertIn("Buyback {3}", self.oracle["Reiterate"])
        self.assertIn("each tapped land your opponents control", self.oracle["Mana Geyser"])
        self.assertIn("Storm", self.oracle["Grapeshot"])
        result = reiterate_geyser_loop()
        self.assertEqual(result["reiterate_casts"], 40)
        self.assertEqual(result["red"], 166)  # Initial six + 40*(10 - 6).
        self.assertFalse(result["original_geyser_resolved"])
        self.assertEqual(result["storm_count_before_grapeshot"], 41)
        self.assertEqual(result["grapeshot_damage_objects"], 42)
        self.assertTrue(result["grapeshot_payable"])
        self.assertTrue(all(h["reiterate_in_hand"] for h in result["history"]))
        self.assertEqual(reiterate_geyser_loop(opponent_tapped_lands=6,
                         repeats=5)["red"], 6)  # Storm but no net mana.
        self.assertEqual(reiterate_geyser_loop(opponent_tapped_lands=5)
                         ["reiterate_casts"], 1)
        self.assertEqual(reiterate_geyser_loop(buyback=False)["reiterate_casts"], 0)
        self.assertEqual(reiterate_geyser_loop(geyser_original_on_stack=False)
                         ["reiterate_casts"], 0)
        self.assertEqual(reiterate_geyser_loop(initial_red=5)["reiterate_casts"], 0)
        self.assertEqual(reiterate_geyser_loop(opponent_stops_loop=True)
                         ["reiterate_casts"], 0)
        # Only original Geyser plus forty real Reiterate casts count for
        # Grapeshot storm; copied Geysers are NOT cast. Forty-two damage
        # objects may be aimed at a legal 40-life opponent, not at no target.


if __name__ == "__main__":
    unittest.main()
