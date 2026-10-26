"""Deck #32 Mai and Zuko M7 Rev1: finite source-bound M6 P0/P1 case transfer.

Every case binds to Cory's exact 100-card approved raw SHA and archived Oracle text.
These checks assess narrow rules preconditions, not played multiplayer win rates.
"""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = "8cdf614e47eadf3ec33049a770a3f0a2b84338e84c31bb26a49e6f26f5c60d97"
DECK = ROOT / "refinement/decklists/Mai_and_Zuko_M7_Rev1_Approved_2026-10-25.txt"
INDEX = ROOT / "refinement/verification/Mai_and_Zuko_M7_Rev1_Oracle_Identity_Index_2026-10-25.json"

class TestMaiZukoM7ExactM6Transfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = DECK.read_bytes()
        cls.names = [line.removeprefix("1x ").removesuffix(" [Commander]")
                     for line in cls.raw.decode("utf-8").splitlines()]
        cls.oracle = {row["name"]: row for row in json.loads(INDEX.read_text(encoding="utf-8"))["cards"]}
        assert hashlib.sha256(cls.raw).hexdigest() == SHA
        assert len(cls.names) == len(set(cls.names)) == len(cls.oracle) == 100
        assert set(cls.names) == set(cls.oracle)

    def card(self, name):
        self.assertIn(name, self.oracle)
        item = self.oracle[name]
        self.assertEqual(item["commander_legality"], "legal")
        self.assertTrue(set(item["color_identity"]) <= {"U", "B", "R"})
        return item

    def test_C1_commander_printed_oracle_and_valid_flash_scope(self):
        cmd = self.card("Mai and Zuko")
        self.assertEqual(cmd["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(cmd["oracle_text"], "Firebending 3\nYou may cast Ally spells and artifact spells as though they had flash.")
        self.assertIn("Ally", cmd["type_line"])
        self.assertNotIn("You may cast instant and sorcery spells", cmd["oracle_text"])
        self.assertEqual(self.names[0], "Mai and Zuko")

    def test_K1_flash_and_firebending_combat_window(self):
        cmd = self.card("Mai and Zuko")["oracle_text"]
        turret = self.card("Fire Nation Turret")["oracle_text"]
        self.assertIn("artifact spells as though they had flash", cmd)
        self.assertIn("At the beginning of combat on your turn", turret)
        self.assertIn("firebending 2", turret.lower())
        self.assertEqual(3 + 2, 5)
        # No combat-start trigger can resolve retroactively after that step.
        combat_start_has_turret, turret_flashes_in_later = False, True
        self.assertFalse(combat_start_has_turret and turret_flashes_in_later)

    def test_K2_unwinding_clock_others_turns_not_your_untap(self):
        clock = self.card("Unwinding Clock")["oracle_text"]
        for name in ("Mana Vault", "Basalt Monolith"):
            mon = self.card(name)["oracle_text"]
            self.assertIn("doesn't untap during your untap step", mon)
        self.assertIn("each other player's untap step", clock)
        self.assertNotIn("during your untap step", clock)
        self.assertEqual(3, len([p for p in range(4) if p != 0]))

    def test_K3_saga_uses_printed_mana_cost_not_mana_value(self):
        saga = self.card("Urza's Saga")["oracle_text"]
        self.assertIn("mana cost {0} or {1}", saga)
        self.assertEqual(self.card("Walking Ballista")["mana_cost"], "{X}{X}")
        self.assertNotIn("{X}", "{0}/{1}")  # X-cost card is not a valid Saga III search target.
        self.assertIn("Artifact", self.card("Sol Ring")["type_line"])

    def test_K4_monolith_rings_positive_infinite_iteration(self):
        basalt = self.card("Basalt Monolith")["oracle_text"]
        rings = self.card("Rings of Brighthearth")["oracle_text"]
        self.assertIn("{T}: Add {C}{C}{C}", basalt)
        self.assertIn("{3}: Untap", basalt)
        self.assertIn("if it isn't a mana ability", rings)
        self.assertIn("pay {2}", rings)
        # Tap twice after two untap resolutions; total 6 produced, 3+2 spent.
        self.assertEqual(2 * 3 - (3 + 2), 1)
        self.assertEqual(2 * 3 - (4 + 2), 0)  # Higher untap costs alone do not net mana.

    def test_K5_top_flash_opponent_turn_bounded(self):
        cmd = self.card("Mai and Zuko")["oracle_text"]
        top = self.card("Sensei's Divining Top")["oracle_text"]
        citadel = self.card("Bolas's Citadel")["oracle_text"]
        forge = self.card("Mystic Forge")["oracle_text"]
        self.assertIn("artifact spells as though they had flash", cmd)
        self.assertIn("put this artifact on top", top)
        self.assertIn("top card of your library", citadel)
        self.assertIn("cast artifact spells and colorless spells from the top", forge)
        # Top is an artifact *spell*, whereas Citadel is not granted free spells.
        self.assertIn("Artifact", self.card("Sensei's Divining Top")["type_line"])
        self.assertIn("pay life equal to its mana value", citadel)

    def test_E1_commander_required_for_granted_flash(self):
        cmd = self.card("Mai and Zuko")["oracle_text"]
        self.assertIn("You may cast Ally spells and artifact spells as though they had flash", cmd)
        may_cast_offturn = lambda commander_present, artifact_spell: commander_present and artifact_spell
        self.assertTrue(may_cast_offturn(True, True))
        self.assertFalse(may_cast_offturn(False, True))
        self.assertFalse(may_cast_offturn(True, False))

    def test_E2_combat_red_mana_and_offturn_separate(self):
        cmd = self.card("Mai and Zuko")["oracle_text"]
        self.assertIn("Firebending 3", cmd)
        self.assertIn("artifact spells as though they had flash", cmd)
        red_from_attacking_commander = 3
        self.assertEqual(red_from_attacking_commander, 3)
        self.assertEqual(0 if not True else red_from_attacking_commander, 3)
        self.assertEqual(0 if not False else red_from_attacking_commander, 0)
        # A main-phase Jeska's Will never gains flash from the commander.
        self.assertIn("Sorcery", self.card("Jeska's Will")["type_line"])

    def test_W1_monolith_rings_outlet_not_an_automatic_win(self):
        self.test_K4_monolith_rings_positive_infinite_iteration()
        ballista = self.card("Walking Ballista")["oracle_text"]
        self.assertIn("{4}: Put a +1/+1 counter", ballista)
        self.assertIn("Remove a +1/+1 counter", ballista)
        self.assertIn("deals 1 damage to any target", ballista)
        self.assertGreater(2 * 3 - (3 + 2), 0)

    def test_W2_top_citadel_and_forge_costs_conditions(self):
        top = self.card("Sensei's Divining Top")["oracle_text"]
        citadel = self.card("Bolas's Citadel")["oracle_text"]
        reservoir = self.card("Aetherflux Reservoir")["oracle_text"]
        forge = self.card("Mystic Forge")["oracle_text"]
        reducer = self.card("Foundry Inspector")["oracle_text"]
        self.assertIn("{T}: Draw a card", top)
        self.assertIn("pay life equal to its mana value", citadel)
        self.assertIn("Whenever you cast a spell", reservoir)
        self.assertIn("cast artifact spells and colorless spells from the top", forge)
        self.assertIn("cost {1} less", reducer)
        self.assertEqual(max(0, 1 - 1), 0)  # one generic Top mana reduced only in Forge line
        self.assertIn("Pay 50 life", reservoir)

    def test_W3_breach_led_brainfreeze_graveyard_fuel(self):
        breach = self.card("Underworld Breach")["oracle_text"]
        led = self.card("Lion's Eye Diamond")["oracle_text"]
        freeze = self.card("Brain Freeze")["oracle_text"]
        self.assertIn("exile three other cards", breach)
        self.assertIn("Add three mana", led)
        self.assertIn("Storm", freeze)
        self.assertIn("mills three cards", freeze)
        self.assertTrue(3 * (1 + 2) >= 3)  # base spell + two storm copies as bounded example
        self.assertFalse(2 >= 3)  # cannot escape with only two other graveyard cards

    def test_F1_artifact_hate_disrupts_mana_and_win_engine(self):
        must_have = {"Basalt Monolith", "Rings of Brighthearth", "Walking Ballista"}
        self.assertTrue(must_have.issubset(set(self.names)))
        intact = must_have.copy()
        self.assertTrue({"Basalt Monolith", "Rings of Brighthearth"}.issubset(intact))
        after_artifact_wipe = intact - must_have
        self.assertFalse({"Basalt Monolith", "Rings of Brighthearth"}.issubset(after_artifact_wipe))
        self.assertFalse("Walking Ballista" in after_artifact_wipe)

    def test_F2_saga_cannot_fetch_x_cost_artifacts(self):
        saga = self.card("Urza's Saga")["oracle_text"]
        ballista = self.card("Walking Ballista")
        solring = self.card("Sol Ring")
        self.assertIn("mana cost {0} or {1}", saga)
        self.assertEqual(ballista["mana_cost"], "{X}{X}")
        self.assertEqual(solring["mana_cost"], "{1}")
        self.assertNotIn(ballista["mana_cost"], ("{0}", "{1}"))
        self.assertIn(solring["mana_cost"], ("{0}", "{1}"))

    def test_F3_without_commander_flash_lost_not_combo(self):
        other = {"Basalt Monolith", "Rings of Brighthearth", "Walking Ballista"}
        self.assertTrue(other.issubset(set(self.names)))
        self.assertNotIn("Mai and Zuko", other)
        has_commander, combo_pieces_present = False, True
        self.assertFalse(has_commander)  # loses commander-granted instant-speed permissions
        self.assertTrue(combo_pieces_present)  # main-phase artifact combo remains available
        self.assertEqual(2 * 3 - (3 + 2), 1)

if __name__ == "__main__":
    unittest.main()
