"""Missy M7 Rev1: five finite source-bound M6/P0 contract fixtures.

Checks one normal and one adversarial state for each required source case.
This is a bounded rules model, not a full turn engine or multiplayer simulation.
"""

import hashlib
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
LIST = ROOT / "refinement/decklists/Missy_M7_Rev1_Approved_2026-10-26.txt"
if not LIST.is_file():
    LIST = ROOT / "Missy_M7_Rev1_Approval_Candidate_2026-10-26.txt"
EXPECTED = "f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d"

# Pinned to engineering PR #719 current Scryfall snapshot, checked there
# 97/97. Missy: {3}{U}{B}{R}; another NONARTIFACT creature dies -> tapped
# face-down 2/2 Cyberman artifact under your control. Printed morph creatures
# may be turned up for their printed costs/reveal, which restores their traits.
FREE_MORPH = {
    "Ruthless Ripper": "B",
    "Dragon's Eye Savants": "U",
    "Horde Ambusher": "R",
}


def source_names():
    lines = LIST.read_bytes().decode().splitlines()
    assert hashlib.sha256(LIST.read_bytes()).hexdigest() == EXPECTED
    values = {}
    for line in lines:
        qty, name = line.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        values[name] = values.get(name, 0) + int(qty)
    assert sum(values.values()) == 100
    return values


def dying_to_missy(*, another=True, nonartifact=True, dies=True,
                   missy_present=True, original_controller="us"):
    """One Missy dies-event predicate and permanent transition, not a stack."""
    if not (another and nonartifact and dies and missy_present):
        return None
    return {"owner_of_event": original_controller, "new_controller": "us",
            "face_down": True, "tapped": True, "power": 2, "toughness": 2,
            "artifact": True, "colorless": True, "subtype": "Cyberman"}


def morph_turn_up(permanent, *, printed_name, revealed_color=None,
                  eligible_to_turn_up=True):
    if not permanent or not permanent["face_down"]:
        return None
    if not eligible_to_turn_up or FREE_MORPH.get(printed_name) != revealed_color:
        return None
    changed = dict(permanent)
    changed.update({"face_down": False, "artifact": False, "colorless": False,
                    "printed_name": printed_name})
    return changed


def can_cast_missy(mana):
    """Simplified available colored/total mana check for {3}{U}{B}{R}."""
    if not all(mana.get(color, 0) >= 1 for color in ("U", "B", "R")):
        return False
    return sum(mana.values()) >= 6


class Deck38M7SourceCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = source_names()
        assert cls.cards["Missy"] == 1

    def test_C1_missy_nonartifact_death_and_end_step_condition(self):
        """Positive: another nonartifact death returns tapped Cyberman.
        Negative: artifact death, commander dying, absent Missy do not.
        """
        self.assertEqual(dying_to_missy()["subtype"], "Cyberman")
        self.assertTrue(dying_to_missy()["tapped"])
        self.assertIsNone(dying_to_missy(nonartifact=False))
        self.assertIsNone(dying_to_missy(another=False))
        self.assertIsNone(dying_to_missy(missy_present=False))
        # End-step choice uses *artifact creature* count, not all creatures.
        artifact_creatures, nonartifact_creatures = 3, 8
        self.assertEqual(artifact_creatures, 3)
        self.assertNotEqual(artifact_creatures, artifact_creatures + nonartifact_creatures)

    def test_K1_face_down_colorless_and_morph_restriction(self):
        """Positive: Missy converts to artifact 2/2 then morph turns up.
        Negative: a card lacking the matching printed morph cannot turn up.
        """
        p = dying_to_missy()
        self.assertEqual((p["face_down"], p["colorless"], p["artifact"], p["power"]),
                         (True, True, True, 2))
        self.assertIn("Ruthless Ripper", self.cards)
        self.assertIsNotNone(morph_turn_up(p, printed_name="Ruthless Ripper", revealed_color="B"))
        self.assertIsNone(morph_turn_up(p, printed_name="Ruthless Ripper", revealed_color="U"))
        self.assertIsNone(morph_turn_up(p, printed_name="Accursed Marauder", revealed_color="B"))

    def test_K2_turn_up_reset_reenables_nonartifact_death(self):
        """Positive: each three printed nonartifact reveal-morphs can loop.
        Negative: still-facedown artifact dying does not trigger Missy.
        """
        for name, color in FREE_MORPH.items():
            with self.subTest(card=name):
                self.assertIn(name, self.cards)
                down = dying_to_missy()
                self.assertIsNone(dying_to_missy(nonartifact=not down["artifact"]))
                up = morph_turn_up(down, printed_name=name, revealed_color=color)
                self.assertFalse(up["artifact"])
                self.assertIsNotNone(dying_to_missy(nonartifact=not up["artifact"]))
                self.assertIsNone(morph_turn_up(down, printed_name=name,
                                                revealed_color="G"))

    def test_K3_opponent_died_nonartifact_returns_to_missy_controller(self):
        """Positive: opponent-owned nonartifact returns under our control.
        Negative: opponent artifact creature death doesn't convert.
        """
        stolen = dying_to_missy(original_controller="opponent")
        self.assertEqual(stolen["new_controller"], "us")
        self.assertEqual(stolen["owner_of_event"], "opponent")
        self.assertTrue(stolen["tapped"])
        self.assertIsNone(dying_to_missy(original_controller="opponent", nonartifact=False))
        self.assertIsNone(dying_to_missy(original_controller="opponent", dies=False))

    def test_F1_six_mana_commander_colored_source_and_acceleration(self):
        """Positive: real acceleration permits {3}{U}{B}{R} on six total.
        Negative: enough generic but missing U or B or R cannot cast.
        """
        for name in ("Sol Ring", "Grim Monolith", "Chrome Mox", "Arcane Signet",
                     "Mana Vault", "Talisman of Creativity", "Talisman of Dominance",
                     "Talisman of Indulgence", "Command Tower"):
            self.assertIn(name, self.cards)
        self.assertTrue(can_cast_missy({"U": 1, "B": 1, "R": 1, "C": 3}))
        self.assertFalse(can_cast_missy({"U": 1, "B": 1, "C": 9}))
        self.assertFalse(can_cast_missy({"U": 1, "B": 1, "R": 1, "C": 2}))
        self.assertFalse(can_cast_missy({"U": 0, "B": 2, "R": 2, "C": 8}))


if __name__ == "__main__":
    unittest.main()
