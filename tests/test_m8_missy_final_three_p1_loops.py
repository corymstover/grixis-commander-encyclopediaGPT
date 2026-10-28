"""Missy's three original deferred P1 W-cases: paid/finite Cyberman traces.

The same source card must move between nonartifact face up and artifact face
down for Missy to keep returning it; a face-down Cyberman cannot recur merely
by being sacrificed again. Repeatedly drawing with Haruspex is NOT an
unbounded safe win when the actual library is finite.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Missy"
SHA = "f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d"
CASES = {"W1", "W2", "W3"}


def ripper_morph_death_trace(*, cycles, missy=True, ripper=True,
                             black_card_to_reveal=True, seer=True,
                             bombardment=False, altar=False, haruspex=False,
                             library=65, starting_opponent_life=40):
    """One REAL Ripper, repeated face-up/sac/death/face-down returns.

    The reveal-only morph cost reuses one black hand card (not discarded).
    Ripper's turn-up triggered life-loss occurs each round, and paid/free
    sacrifice effects are separate. Missy only returns a nonartifact creature
    that just died; the returned *artifact* Cyberman must be turned face up
    before the NEXT qualifying death. No token or duplicate card is created.
    """
    if not (missy and ripper and black_card_to_reveal and (seer or bombardment or altar)):
        return {"cycles": 0, "opponent_life": starting_opponent_life,
                "mana": 0, "draws": 0, "lost_to_draw": False, "reusable": False}
    face_down_artifact = True  # after a valid earlier nonartifact death
    done = draws = mana = 0
    life = starting_opponent_life
    for _ in range(cycles):
        if not face_down_artifact:
            break
        face_down_artifact = False  # reveal an actual black card to morph
        life -= 2                 # Ripper turns up: target opponent loses 2
        if bombardment:
            life -= 1             # Bombardment sac-death damage (targeted)
        mana += int(altar)        # Phyrexian Altar: sac Ripper, add one mana
        draws += int(haruspex)    # another nontoken nonartifact dies
        done += 1
        if haruspex and draws > library:
            return {"cycles": done, "opponent_life": life, "mana": mana,
                    "draws": draws, "lost_to_draw": True, "reusable": False}
        # Sacrificed face-up Ripper was not an artifact; Missy triggers and
        # brings that one card back as a face-down artifact Cyberman.
        face_down_artifact = True
    return {"cycles": done, "opponent_life": life, "mana": mana,
            "draws": draws, "lost_to_draw": False, "reusable": face_down_artifact}


def ixidor_altar_plunderer_trace(*, loops=8, missy=True, ixidor=True,
                                  plunderer=True, ashnod=True,
                                  eligible_face_down_creature=True,
                                  initial_generic=2, initial_blue=1):
    """Each Ixidor activation costs 2U. Ashnod gives CC; one Treasure gives U.

    Requires a previously legally returned face-down nonartifact-original
    creature. Ixidor's activated ability has NO tap cost; sacrifice face up
    and use Plunderer's Treasure to reconstruct the exact next cost.
    """
    mana_generic, mana_blue, completed = initial_generic, initial_blue, 0
    for _ in range(loops):
        if not (missy and ixidor and plunderer and ashnod and eligible_face_down_creature):
            break
        if mana_generic < 2 or mana_blue < 1:
            break
        mana_generic -= 2
        mana_blue -= 1
        # Ixidor turns the one face-down artifact Cyberman face up, making
        # its original nonartifact creature identity the dying source.
        mana_generic += 2  # sacrifice face-up to Ashnod's Altar
        mana_blue += 1     # Plunderer Treasure pays the next U
        # Missy returns the same one creature tapped, face-down artifact.
        completed += 1
    return {"cycles": completed, "generic": mana_generic, "blue": mana_blue}


def villainous_end_step(*, missy_present=True, valeyard_present=False,
                         artifact_creatures=3, choices=None, own_library=30):
    """Choices are explicitly *opponent-selected*, not forced all-damage."""
    if choices is None:
        choices = (("damage",), ("damage",), ("damage",))
    if not missy_present:
        return {"losses": (0,) * len(choices), "draws": 0,
                "draw_loss": False, "choices_executed": 0}
    expected_per_opponent = 1 + int(valeyard_present)
    if any(len(opponent_choices) != expected_per_opponent for opponent_choices in choices):
        raise ValueError("each opponent must receive the exact number of choices")
    damage = [0] * len(choices)
    draws = 0
    for opponent, selections in enumerate(choices):
        for selected in selections:
            if selected == "damage":
                damage[opponent] += artifact_creatures
            elif selected == "draw":
                draws += 1
            else:
                raise ValueError("not a real villainous choice")
    return {"losses": tuple(damage), "draws": draws,
            "draw_loss": draws > own_library,
            "choices_executed": expected_per_opponent * len(choices)}


class MissyFinalOriginalP1Loops(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        assert raw.decode().splitlines()[0] == "1x Missy [Commander]"
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            quantity, name = line.split("x ", 1)
            cls.cards[name.replace(" [Commander]", "")] += int(quantity)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert cls.deferred.issuperset(CASES)

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W1_one_ripper_recurs_after_each_actual_face_up_nontoken_death(self):
        self.source("W1", "Missy", "Ruthless Ripper", "Dragon's Eye Savants",
                    "Horde Ambusher", "Viscera Seer", "Phyrexian Altar",
                    "Ashnod's Altar", "Goblin Bombardment", "Altar of Dementia",
                    "Blood Artist", "Zulaport Cutthroat", "Mayhem Devil")
        trace = ripper_morph_death_trace(cycles=20)
        self.assertEqual((trace["cycles"], trace["opponent_life"], trace["draws"]),
                         (20, 0, 0))
        self.assertTrue(trace["reusable"])
        self.assertEqual(ripper_morph_death_trace(cycles=20, black_card_to_reveal=False)["cycles"], 0)
        self.assertEqual(ripper_morph_death_trace(cycles=20, missy=False)["cycles"], 0)
        self.assertEqual(ripper_morph_death_trace(cycles=20, seer=False)["cycles"], 0)
        burn = ripper_morph_death_trace(cycles=14, seer=False, bombardment=True)
        self.assertEqual(burn["opponent_life"], -2)

    def test_W2_altar_haruspex_forced_draw_ceiling_and_ixidor_paid_loop(self):
        self.source("W2", "Missy", "Phyrexian Altar", "Grim Haruspex",
                    "Ixidor, Reality Sculptor", "Pitiless Plunderer", "Ashnod's Altar",
                    "Ruthless Ripper")
        draw_and_mana = ripper_morph_death_trace(cycles=8, seer=False,
                                                  altar=True, haruspex=True,
                                                  library=8)
        self.assertEqual((draw_and_mana["mana"], draw_and_mana["draws"],
                          draw_and_mana["lost_to_draw"]), (8, 8, False))
        exhaustion = ripper_morph_death_trace(cycles=9, seer=False,
                                               altar=True, haruspex=True,
                                               library=8)
        self.assertTrue(exhaustion["lost_to_draw"])
        paid = ixidor_altar_plunderer_trace(loops=12)
        self.assertEqual(paid, {"cycles": 12, "generic": 2, "blue": 1})
        self.assertEqual(ixidor_altar_plunderer_trace(plunderer=False)["cycles"], 0)
        self.assertEqual(ixidor_altar_plunderer_trace(ashnod=False)["cycles"], 0)
        self.assertEqual(ixidor_altar_plunderer_trace(initial_blue=0)["cycles"], 0)

    def test_W3_opponent_may_take_draw_branch_valeyard_makes_extra_choice(self):
        self.source("W3", "Missy", "The Valeyard", "Cyberman Patrol",
                    "The Cyber-Controller")
        self.assertNotIn("Cybermen Squadron", self.cards)
        self.assertNotIn("Ashad, the Lone Cyberman", self.cards)
        damage = villainous_end_step(valeyard_present=True,
                                     choices=(("damage", "damage"),) * 3)
        self.assertEqual(damage, {"losses": (6, 6, 6), "draws": 0,
                                  "draw_loss": False, "choices_executed": 6})
        avoids_damage = villainous_end_step(valeyard_present=True,
                                             choices=(("draw", "draw"),) * 3,
                                             own_library=4)
        self.assertEqual(avoids_damage["losses"], (0, 0, 0))
        self.assertEqual((avoids_damage["draws"], avoids_damage["draw_loss"]), (6, True))
        normal = villainous_end_step(artifact_creatures=3)
        self.assertEqual((normal["losses"], normal["choices_executed"]), ((3, 3, 3), 3))
        no_artifacts = villainous_end_step(artifact_creatures=0)
        self.assertEqual(no_artifacts["losses"], (0, 0, 0))
        self.assertEqual(villainous_end_step(missy_present=False)["choices_executed"], 0)


if __name__ == "__main__":
    unittest.main()
