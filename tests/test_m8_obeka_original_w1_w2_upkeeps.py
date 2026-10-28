"""Source-bound Obeka W1/W2: real upkeep count, artifact cost and alt-win."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = "Obeka__Splitter_of_Seconds"
SHA = "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859"
PLAN = "e3d991092b39c957fe9114fb0ed34f3db4556e61"


def sieve_extra_turns(*, iterations=6, damage=4, spy=True, sieve=True,
                      obeka=True, spy_has_artifact=True,
                      damaged_each_turn=True, initial_thopters=0):
    """One normal upkeep + actual combat-damage additional upkeeps.

    Spy Network produces one physical Thopter on each upkeep if an artifact
    survives; Time Sieve consumes five distinct tokens and taps for one extra
    turn. The next turn untaps Sieve and must repeat an actual Obeka combat hit.
    """
    thopters = initial_thopters
    records = []
    for turn in range(iterations):
        extra_upkeeps = damage if obeka and damaged_each_turn else 0
        upkeeps = 1 + extra_upkeeps
        generated = upkeeps if spy and spy_has_artifact else 0
        thopters += generated
        paid = bool(sieve and thopters >= 5)
        if paid:
            thopters -= 5
        records.append({"turn": turn + 1, "upkeeps": upkeeps,
                        "tokens_created": generated, "sacrificed": 5 if paid else 0,
                        "thopters_remaining": thopters, "extra_turn": paid})
        if not paid:
            break
    return records


def production_upkeeps(*, starting_same_name=1, combat_damage=6,
                       obeka=True, production=True, enchanted_artifact=True,
                       survives=True, additional_upkeeps_resolve=True):
    """Each upkeep adds *one* same-name artifact, then checks eight total."""
    same_name = starting_same_name
    history = []
    n = 1 + (combat_damage if obeka and additional_upkeeps_resolve else 0)
    for _ in range(n):
        if not production or not enchanted_artifact or not survives:
            break
        same_name += 1
        history.append({"same_name": same_name, "won": same_name >= 8})
        if same_name >= 8:
            break
    return {"history": history, "same_name": same_name,
            "won": bool(history and history[-1]["won"])}


class ObekaOriginalW1W2Upkeeps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        item = next(r for r in idx["decks"] if r["deck_id"] == DECK)
        raw = (ROOT / item["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == item["source_sha256"] == SHA
        assert raw.decode().splitlines()[0] == "1x Obeka, Splitter of Seconds [Commander]"
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            n, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(n)
        assert sum(cls.cards.values()) == 100
        rec = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                          / f"{DECK}_{SHA[:16]}.json").read_text())
        assert rec["approved_raw_sha256"] == SHA
        assert rec["m6_transfer"]["plan_blob_sha"] == PLAN
        cls.deferred = {c["case_id"] for c in rec["m6_transfer"]["P1"]
                        if c["status"] == "DEFERRED"}
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as f:
            for line in f:
                row = json.loads(line)
                cls.oracle[row["canonical_name"]] = row["oracle_text"]

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W1_sieve_five_actual_thopters_per_turn_no_free_upkeep(self):
        self.source("W1", "Obeka, Splitter of Seconds", "Time Sieve",
                    "Thopter Spy Network", "Replicating Ring", "Court of Vantress",
                    "Smaug the Magnificent", "Roaming Throne")
        self.assertIn("that many additional upkeep steps", self.oracle["Obeka, Splitter of Seconds"])
        self.assertIn("Sacrifice five artifacts", self.oracle["Time Sieve"])
        self.assertIn("if you control an artifact", self.oracle["Thopter Spy Network"])
        result = sieve_extra_turns()
        self.assertEqual(len(result), 6)
        self.assertTrue(all(r["extra_turn"] for r in result))
        self.assertEqual([r["sacrificed"] for r in result], [5] * 6)
        self.assertTrue(all(r["thopters_remaining"] == 0 for r in result))
        # Reusable board invariant: untap Sieve next extra turn, hit for four,
        # receive four bonus upkeeps plus the ordinary one, generate five.
        self.assertEqual(len(sieve_extra_turns(damage=2)), 1)
        self.assertFalse(sieve_extra_turns(damage=2)[0]["extra_turn"])
        self.assertFalse(sieve_extra_turns(spy=False)[0]["extra_turn"])
        self.assertFalse(sieve_extra_turns(sieve=False)[0]["extra_turn"])
        self.assertFalse(sieve_extra_turns(obeka=False)[0]["extra_turn"])
        self.assertFalse(sieve_extra_turns(spy_has_artifact=False)[0]["extra_turn"])
        self.assertFalse(sieve_extra_turns(damaged_each_turn=False)[0]["extra_turn"])
        # Source's unmodified Obeka is not declared to naturally deal four;
        # a genuine power buff, unblocked combat and survivors are required.

    def test_W2_mechanized_eighth_name_not_absent_reactor(self):
        self.source("W2", "Obeka, Splitter of Seconds", "Mechanized Production")
        self.assertEqual(self.cards["Darksteel Reactor"], 0)
        self.assertIn("eight or more artifacts with the same name",
                      self.oracle["Mechanized Production"])
        winning = production_upkeeps()
        self.assertEqual(len(winning["history"]), 7)
        self.assertEqual(winning["same_name"], 8)
        self.assertTrue(winning["won"])
        self.assertFalse(production_upkeeps(combat_damage=4)["won"])
        self.assertFalse(production_upkeeps(production=False)["won"])
        self.assertFalse(production_upkeeps(enchanted_artifact=False)["won"])
        self.assertFalse(production_upkeeps(survives=False)["won"])
        self.assertFalse(production_upkeeps(additional_upkeeps_resolve=False)["won"])
        # No existing Reactor branch, magic artifact duplication, or instant
        # victory before the actual eighth same-name artifact check.


if __name__ == "__main__":
    unittest.main()
