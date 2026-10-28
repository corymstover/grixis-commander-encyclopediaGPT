"""Deck #3 exact-current Rev3: original five P0/eight P1 bounded cases.

Separate from the historical M6 DESIGN_ONLY blueprint and the earlier Rev2
research. These finite states model their applicable current-card propositions,
including the explicit removal of Pitiless Plunderer and Wonder; no full game
stack engine, independent historical J transfer or win-rate assertion.
"""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"
REPORT = ROOT / "refinement/verification/m8_quality_scope/Admiral_Brass__Unsinkable_dfa192cce0d92562.md"
EXPECTED_SHA = "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7"


def enter_brass(graveyard, source_on_battlefield=True):
    """On ETB mill four from a real library (fixture supplies top cards)."""
    return graveyard[:4] if source_on_battlefield else []


def combat_return(pirate_grave, combat_yours, commander_present, selected):
    """One targeted Pirate returns 4/4 hasty, with finality; cannot fake target."""
    if not (combat_yours and commander_present and selected in pirate_grave):
        return None
    return {"name": selected, "power": 4, "toughness": 4,
            "haste": True, "finality": True, "zone": "battlefield"}


def death_destination(finality):
    return "exile" if finality else "graveyard"


def conduit_reassign_counter(permanent_controlled, finality_present, conduit_untapped, target_legal):
    """Cost tap conduit and remove a counter, then add a counter to legal target."""
    return permanent_controlled and finality_present and conduit_untapped and target_legal


def living_death_resolution(own_grave, opponent_grave):
    """The exiled creature cards from both graveyards return; not one-sided."""
    return {"you": list(own_grave), "opponent": list(opponent_grave)}


def throne_brass_triggers(brass_is_pirate, throne_chose_pirate, throne_active):
    return 1 + int(brass_is_pirate and throne_chose_pirate and throne_active)


def thassa_blink_permanent_steal(controlled_creature, controlled_until_eot, nontoken, thassa_active):
    """New object under our control may escape delayed old-object return.

    Ownership need *not* be ours; that is the point for a stolen nontoken.
    """
    return controlled_creature and controlled_until_eot and nontoken and thassa_active


class BrassRev3CurrentCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = SOURCE.read_bytes()
        if sha256(raw).hexdigest() != EXPECTED_SHA:
            raise AssertionError("Admiral Brass Rev3 source SHA changed")
        rows = raw.decode("utf-8").splitlines()
        if rows[0] != "1x Admiral Brass, Unsinkable [Commander]":
            raise AssertionError("Wrong commander identity")
        cls.cards = Counter()
        for row in rows:
            qty, name = row.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(qty)
        if sum(cls.cards.values()) != 100 or cls.cards["Admiral Brass, Unsinkable"] != 1:
            raise AssertionError("Invalid current 100")
        cls.report = REPORT.read_text(encoding="utf-8")
        cls.must_be_present = {
            "Roaming Throne", "Power Conduit", "Changeling Outcast", "Living Death",
            "Patriarch's Bidding", "Faithless Looting", "Entomb", "Buried Alive",
            "Shared Animosity", "Port Razer", "Angrath's Marauders", "Siren's Ruse",
            "Kitesail Larcenist", "Thassa, Deep-Dwelling", "Coercive Recruiter",
            "Zara, Renegade Recruiter", "Skeleton Crew", "Gemcutter Buccaneer",
            "Hostage Taker", "Ripples of Undeath", "Jhoira, Weatherlight Corsair",
        }
        assert all(cls.cards[name] == 1 for name in cls.must_be_present)
        assert cls.cards["Pitiless Plunderer"] == 0
        assert cls.cards["Wonder"] == 0

    def test_C01_commander_etb_and_graveyard_permission_p0(self):
        self.assertEqual(len(enter_brass(["A", "B", "C", "D", "E"])), 4)
        self.assertEqual(enter_brass(["A", "B"], False), [])
        self.assertEqual(len(enter_brass(["A", "B"])), 2)  # no fake cards past library end
        self.assertEqual(self.cards["Admiral Brass, Unsinkable"], 1)

    def test_K01_beginning_of_our_combat_pirate_return_p0(self):
        state = combat_return(["Changeling Outcast"], True, True, "Changeling Outcast")
        self.assertEqual((state["power"], state["toughness"], state["finality"], state["haste"]),
                         (4, 4, True, True))
        self.assertIsNone(combat_return(["Changeling Outcast"], False, True, "Changeling Outcast"))
        self.assertIsNone(combat_return([], True, True, "Changeling Outcast"))
        self.assertIsNone(combat_return(["Changeling Outcast"], True, False, "Changeling Outcast"))

    def test_K02_finality_replaces_death_not_plunderer_treasure_p0(self):
        self.assertEqual(death_destination(True), "exile")
        self.assertEqual(death_destination(False), "graveyard")
        self.assertEqual(self.cards["Pitiless Plunderer"], 0)
        # Historical Plunderer-on-natural-death source is ABSENT; we credit only
        # surviving finality/replace-not-die rules, not its old Treasure branch.

    def test_K03_power_conduit_removes_finality_counter_p0(self):
        self.assertTrue(conduit_reassign_counter(True, True, True, True))
        for flags in ((False, True, True, True), (True, False, True, True),
                      (True, True, False, True), (True, True, True, False)):
            self.assertFalse(conduit_reassign_counter(*flags))
        state = combat_return(["Skeleton Crew"], True, True, "Skeleton Crew")
        self.assertEqual((state["power"], state["toughness"]), (4, 4))
        state["finality"] = False  # pay Conduit's independent counter-removal cost
        self.assertEqual(death_destination(state["finality"]), "graveyard")
        self.assertEqual((state["power"], state["toughness"]), (4, 4))

    def test_F01_graveyard_hate_or_no_target_breaks_brass_p0(self):
        grave = ["Warkite Marauder"]
        self.assertIsNotNone(combat_return(grave, True, True, "Warkite Marauder"))
        grave.clear()  # opposing exile before target/ability resolves
        self.assertIsNone(combat_return(grave, True, True, "Warkite Marauder"))
        self.assertIsNone(combat_return(["non-Pirate Sorcery"], True, True,
                                        "Warkite Marauder"))

    def test_K04_changeling_yes_cut_wonder_not_current_flying_p1(self):
        self.assertEqual(self.cards["Changeling Outcast"], 1)
        self.assertEqual(self.cards["Wonder"], 0)
        self.assertIsNotNone(combat_return(["Changeling Outcast"], True, True,
                                           "Changeling Outcast"))
        # No global Wonder-in-graveyard flyer claim on Rev3. Thassa is a blink
        # engine, not an automatic team-wide flying permission.
        self.assertEqual(self.cards["Thassa, Deep-Dwelling"], 1)

    def test_K05_living_death_and_bidding_are_symmetric_p1(self):
        outcome = living_death_resolution(["Changeling Outcast"], ["opponent creature"])
        self.assertEqual(outcome["you"], ["Changeling Outcast"])
        self.assertEqual(outcome["opponent"], ["opponent creature"])
        self.assertEqual(living_death_resolution([], ["opponent creature"])["you"], [])
        self.assertEqual(self.cards["Patriarch's Bidding"], 1)
        # Bidding lets each player choose a type; no automatic unilateral effect.

    def test_E01_roaming_throne_adds_second_paid_pirate_trigger_p1(self):
        self.assertEqual(throne_brass_triggers(True, True, True), 2)
        self.assertEqual(throne_brass_triggers(True, False, True), 1)
        self.assertEqual(throne_brass_triggers(True, True, False), 1)
        targets = ["Changeling Outcast", "Warkite Marauder"]
        self.assertEqual(len(set(targets)), 2)
        self.assertTrue(all(combat_return(targets, True, True, target) for target in targets))
        self.assertIsNone(combat_return(targets, True, True, "absent third card"))

    def test_E02_real_pirate_etbs_and_thassa_stolen_new_object_p1(self):
        for card in ("Skeleton Crew", "Gemcutter Buccaneer", "Coercive Recruiter",
                     "Hostage Taker", "Zara, Renegade Recruiter"):
            self.assertEqual(self.cards[card], 1)
        self.assertTrue(thassa_blink_permanent_steal(True, True, True, True))
        # The creature can be opponent-owned and merely temporarily controlled.
        self.assertFalse(thassa_blink_permanent_steal(True, True, False, True))
        self.assertFalse(thassa_blink_permanent_steal(True, False, True, True))
        self.assertFalse(thassa_blink_permanent_steal(True, True, True, False))
        # Ruse explicitly returns under *owner* control; it is NOT Thassa's
        # separate under-our-control return for stolen non-token creatures.
        self.assertEqual(self.cards["Siren's Ruse"], 1)

    def test_W01_conditional_pirate_beats_and_port_razer_p1(self):
        for name in ("Shared Animosity", "Port Razer", "Angrath's Marauders",
                     "Entomb", "Buried Alive"):
            self.assertEqual(self.cards[name], 1)
        def can_repeat_combat(hits_player, legal_distinct_target, raider_alive):
            return hits_player and legal_distinct_target and raider_alive
        self.assertTrue(can_repeat_combat(True, True, True))
        self.assertFalse(can_repeat_combat(False, True, True))
        self.assertFalse(can_repeat_combat(True, False, True))
        self.assertFalse(can_repeat_combat(True, True, False))
        # Neither Shared Animosity nor Marauders creates a guaranteed hit.

    def test_W02_mass_reanimation_requires_actual_yard_and_cost_p1(self):
        self.assertEqual(self.cards["Living Death"], 1)
        self.assertEqual(self.cards["Patriarch's Bidding"], 1)
        self.assertEqual(self.cards["Faithless Looting"], 1)
        self.assertEqual(len(living_death_resolution(["pirate A", "pirate B"], [] )["you"]), 2)
        self.assertEqual(living_death_resolution([], ["opponent creature"])["you"], [])
        # Looting's controlled 2-discard flashback is real setup, unlike random
        # Ripples mill; both fail if no relevant Pirate is physically available.

    def test_F02_finality_one_shot_unless_new_object_or_counter_removed_p1(self):
        self.assertEqual(death_destination(True), "exile")
        self.assertEqual(death_destination(False), "graveyard")
        self.assertTrue(thassa_blink_permanent_steal(True, True, True, True))
        self.assertFalse(thassa_blink_permanent_steal(True, True, False, True))
        self.assertEqual(self.cards["Power Conduit"], 1)

    def test_F03_ripples_random_mill_can_miss_pirates_p1(self):
        self.assertEqual(self.cards["Ripples of Undeath"], 1)
        self.assertEqual(self.cards["Faithless Looting"], 1)
        mill_three = ["land", "counterspell", "mana rock"]
        self.assertEqual(len(mill_three), 3)
        self.assertFalse(any(name in ("Changeling Outcast", "Warkite Marauder")
                             for name in mill_three))
        controlled_discard = ["Warkite Marauder", "land"]
        self.assertIn("Warkite Marauder", controlled_discard)
        # Neither branch assumes an always-hit random self-mill line.

    def test_complete_current_99_role_ledger(self):
        counted = Counter()
        for qty, name in re.findall(r"^- (\d+)x (.+)$", self.report, re.MULTILINE):
            counted[name] += int(qty)
        live = self.cards.copy()
        live.subtract({"Admiral Brass, Unsinkable": 1})
        self.assertIn(EXPECTED_SHA, self.report)
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, live)
        self.assertEqual({name: qty for name, qty in self.cards.items() if qty > 1},
                         {"Island": 2, "Mountain": 2, "Swamp": 2})


if __name__ == "__main__":
    unittest.main()
