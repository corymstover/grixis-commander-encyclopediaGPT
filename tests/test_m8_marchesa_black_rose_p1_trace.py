"""M8 original P1 Marchesa exact-current mechanical traces.

Unlike catalog-only tests these run finite repeated board/counter/death/endstep
transitions with costs, redraw limits and opposing broken states. Nothing here
is an entire MTG engine; no blanket 'infinite' claim or unmodeled win asserted.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Marchesa__the_Black_Rose"
SOURCE_SHA = "c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02"
TESTED_CASES = {"K4", "K5", "K6", "K7", "E1", "E2", "W1", "W2", "F2", "F3"}


def redcap_persist_cycle(*, redcap_has_minus, mimic_goblin, outlet_live, target_opponent_life):
    """Bombardment sacrifice, then persist return with Mimic +1 and persist -1."""
    if redcap_has_minus or not outlet_live:
        return {"repeatable": False, "opponent_life": target_opponent_life, "counter_delta": -1}
    # Bombardment deals 1; persist resolves and enters with counters +1/-1
    # on the same object. SBA annihilates the pair before Redcap ETB resolves.
    counters_after_return = -1 + int(mimic_goblin)
    # Redcap has base 2 power and an ETB damage trigger after returning.
    damage = 1 + 2 + counters_after_return
    return {"repeatable": counters_after_return == 0,
            "opponent_life": target_opponent_life - damage,
            "counter_delta": counters_after_return}


def play_redcap_bombardment(opponent_life, *, mimic=True, bombardment=True, max_cycles=20):
    life = opponent_life
    has_minus = False
    events = []
    for _ in range(max_cycles):
        step = redcap_persist_cycle(redcap_has_minus=has_minus, mimic_goblin=mimic,
                                    outlet_live=bombardment, target_opponent_life=life)
        if step["opponent_life"] == life:
            break
        events.append(step)
        life = step["opponent_life"]
        has_minus = step["counter_delta"] < 0
        if life <= 0 or not step["repeatable"]:
            break
    return {"opponent_life": life, "cycles": len(events), "repeatable": bool(events and events[-1]["repeatable"])}


def redcap_self_damage_with_artist(*, counter_reset, artist, opponent_previously_lost_life,
                                  life=10, cap=20):
    """No sac outlet: Redcap ETB can target itself for lethal, Artist punishes death."""
    deaths = 0
    current = life
    can_reset = counter_reset and opponent_previously_lost_life
    while deaths < cap:
        # A 2/2 Redcap can deal its own power (two) to itself at ETB.
        deaths += 1
        if artist:
            current -= 1
        # Persist only restarts with no -1/-1 counter; Gev supplies +1/+1
        # on reentry if an opponent already lost life that turn.
        if not can_reset or current <= 0:
            break
    return deaths, current


def yawgmoth_gary_alternation(*, partner_nonhuman, library_cards, life,
                             opponent_life=40, devotion=7, max_activations=30):
    """Finite source-paid trace: Gary and another nonhuman take alternating deaths.

    Yawgmoth costs one life and one other creature per activation, gives -1
    to the still-present other creature and draws one card. Mikaeus undying
    returns the sacrificed creature (only if no +1); Gary ETB drains.
    A +1 and -1 cancel as SBAs. This does NOT assume an infinite library.
    """
    gary_plus = partner_plus = partner_minus = 0
    opponents = [opponent_life] * 3
    drains = 0
    activation_count = 0
    for turn in range(max_activations):
        sacrifice_gary = turn % 2 == 0
        if not partner_nonhuman and not sacrifice_gary:
            break
        if library_cards == 0:
            return {"won": False, "decked": True, "activations": activation_count,
                    "gary_returns": drains, "life": life}
        if life <= 1:
            break  # cannot pay 1 life as a winning line with no remaining life
        if sacrifice_gary and gary_plus:
            break  # cannot undie a +1-countered Gary without an alternating reset
        if not sacrifice_gary and (partner_plus or partner_minus < -1):
            break
        life -= 1
        library_cards -= 1
        activation_count += 1
        if sacrifice_gary:
            gary_plus = 1  # Mikaeus granted undying to non-Human Gary
            opponents = [x - devotion for x in opponents]
            life += devotion * len(opponents)
            drains += 1
            # Yawgmoth's target was the partner, whose +1 cancels if present.
            if partner_plus:
                partner_plus -= 1
            else:
                partner_minus -= 1
        else:
            partner_plus = 1  # nonhuman partner returns via undying
            partner_minus = 0
            gary_plus -= 1  # target Gary's +1 cancels with the -1
        if all(x <= 0 for x in opponents):
            return {"won": True, "decked": False, "activations": activation_count,
                    "gary_returns": drains, "life": life}
    return {"won": False, "decked": False, "activations": activation_count,
            "gary_returns": drains, "life": life}


def next_endstep(events, after_index):
    return next((event for i, event in enumerate(events)
                 if i > after_index and event.endswith("end_begin")), None)


def marchesa_delayed_return(*, marchesa_at_death, died_as_card_with_plus,
                           still_in_grave, marchesa_removed_after_death=False):
    """Marchesa triggers at death; later commander removal cannot erase trigger."""
    return bool(marchesa_at_death and died_as_card_with_plus and still_in_grave)


def flare_alternate_payment(*, blue, nontoken, has_plus, marchesa_at_death):
    paid = bool(blue and nontoken)
    return paid, bool(paid and has_plus and marchesa_at_death)


def outlet_effects(available_creature, option):
    if not available_creature:
        return None
    return {"Phyrexian Altar": (1, "any"),
            "Ashnod's Altar": (2, "colorless"),
            "Goblin Bombardment": (1, "damage")}[option]


class MarchesaOriginalP1Trace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(d for d in index["decks"] if d["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == SOURCE_SHA == row["source_sha256"]
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            num, name = line.split("x ", 1)
            cls.cards[name.replace(" [Commander]", "")] += int(num)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SOURCE_SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SOURCE_SHA
        cls.original = {r["case_id"]: r["status"] for r in receipt["m6_transfer"]["P1"]}

    def guard(self, case, *cards):
        self.assertEqual(self.original[case], "DEFERRED")
        for card in cards:
            self.assertIn(card, self.cards)

    def test_K4_gary_mikaeus_yawgmoth_requires_other_undying_body_and_draws(self):
        self.guard("K4", "Gray Merchant of Asphodel", "Mikaeus, the Unhallowed",
                   "Yawgmoth, Thran Physician", "Mayhem Devil")
        viable = yawgmoth_gary_alternation(partner_nonhuman=True, library_cards=20, life=40)
        self.assertTrue(viable["won"])
        self.assertEqual(viable["gary_returns"], 6)
        self.assertEqual(viable["activations"], 11)
        self.assertGreater(viable["life"], 40)
        missing_partner = yawgmoth_gary_alternation(partner_nonhuman=False, library_cards=20, life=40)
        self.assertFalse(missing_partner["won"])
        self.assertEqual(missing_partner["gary_returns"], 1)
        # This is repeatable payable lethal, not a literal infinite loop:
        # Yawgmoth's draw is mandatory and the library is finite.
        depleted = yawgmoth_gary_alternation(partner_nonhuman=True, library_cards=2, life=40)
        self.assertFalse(depleted["won"])
        self.assertTrue(depleted["decked"])

    def test_K5_redcap_gev_self_damage_can_loop_without_sac_outlet_if_artist(self):
        self.guard("K5", "Murderous Redcap", "Gev, Scaled Scorch", "Metallic Mimic",
                   "Uncivil Unrest", "Blood Artist")
        deaths, remaining = redcap_self_damage_with_artist(counter_reset=True, artist=True,
                                                           opponent_previously_lost_life=True, life=4)
        self.assertEqual(deaths, 4)
        self.assertEqual(remaining, 0)
        no_seed = redcap_self_damage_with_artist(counter_reset=True, artist=True,
                                                opponent_previously_lost_life=False, life=4)
        self.assertEqual(no_seed, (1, 3))
        no_artist = redcap_self_damage_with_artist(counter_reset=True, artist=False,
                                                  opponent_previously_lost_life=True, life=4, cap=3)
        self.assertEqual(no_artist, (3, 4))  # repeating deaths do not themselves drain

    def test_K6_sneak_attack_sacrifice_and_marchesa_are_next_endstep_not_instant(self):
        self.guard("K6", "Sneak Attack", "Marchesa, the Black Rose", "Unspeakable Symbol")
        events = ["our_main", "our_end_begin", "our_end_late", "opponent_end_begin"]
        # Sneak in main: next end step is ours, then Marchesa schedules next.
        self.assertEqual(next_endstep(events, 0), "our_end_begin")
        self.assertEqual(next_endstep(events, 1), "opponent_end_begin")
        self.assertTrue(marchesa_delayed_return(marchesa_at_death=True,
                                               died_as_card_with_plus=True, still_in_grave=True))
        # Sneak after the beginning of our end step: cannot sacrifice at that same beginning.
        self.assertEqual(next_endstep(events, 2), "opponent_end_begin")
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=True,
                                                died_as_card_with_plus=False, still_in_grave=True))

    def test_K7_flare_blue_nontoken_countered_creature_paid_and_return_queued(self):
        self.guard("K7", "Flare of Denial", "Aether Channeler", "Glen Elendra Archmage")
        self.assertEqual(flare_alternate_payment(blue=True, nontoken=True, has_plus=True,
                                                marchesa_at_death=True), (True, True))
        self.assertEqual(flare_alternate_payment(blue=False, nontoken=True, has_plus=True,
                                                marchesa_at_death=True), (False, False))
        self.assertEqual(flare_alternate_payment(blue=True, nontoken=False, has_plus=True,
                                                marchesa_at_death=True), (False, False))
        self.assertEqual(flare_alternate_payment(blue=True, nontoken=True, has_plus=False,
                                                marchesa_at_death=True), (True, False))

    def test_E1_plus_counter_death_trigger_only_returns_card_at_next_endstep(self):
        self.guard("E1", "Marchesa, the Black Rose", "Forge of Heroes")
        self.assertTrue(marchesa_delayed_return(marchesa_at_death=True,
                                               died_as_card_with_plus=True, still_in_grave=True))
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=True,
                                                died_as_card_with_plus=True, still_in_grave=False))
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=True,
                                                died_as_card_with_plus=False, still_in_grave=True))

    def test_E2_creature_sacrifice_outlet_has_distinct_one_time_payoffs(self):
        self.guard("E2", "Phyrexian Altar", "Ashnod's Altar", "Goblin Bombardment")
        self.assertEqual(outlet_effects(True, "Phyrexian Altar"), (1, "any"))
        self.assertEqual(outlet_effects(True, "Ashnod's Altar"), (2, "colorless"))
        self.assertEqual(outlet_effects(True, "Goblin Bombardment"), (1, "damage"))
        self.assertIsNone(outlet_effects(False, "Goblin Bombardment"))

    def test_W1_four_actual_zero_mana_redcap_mimic_bombardment_cycles_lethal(self):
        self.guard("W1", "Murderous Redcap", "Metallic Mimic", "Goblin Bombardment")
        line = play_redcap_bombardment(10, mimic=True, bombardment=True)
        self.assertEqual(line, {"opponent_life": -2, "cycles": 4, "repeatable": True})
        without_mimic = play_redcap_bombardment(10, mimic=False, bombardment=True)
        self.assertEqual(without_mimic, {"opponent_life": 8, "cycles": 1, "repeatable": False})
        without_outlet = play_redcap_bombardment(10, mimic=True, bombardment=False)
        self.assertEqual(without_outlet["cycles"], 0)

    def test_W2_repeated_gary_undying_uses_partner_life_and_library(self):
        self.guard("W2", "Mikaeus, the Unhallowed", "Gray Merchant of Asphodel",
                   "Yawgmoth, Thran Physician", "Mayhem Devil")
        line = yawgmoth_gary_alternation(partner_nonhuman=True, library_cards=20, life=40)
        self.assertTrue(line["won"])
        self.assertEqual((line["activations"], line["gary_returns"]), (11, 6))
        self.assertFalse(yawgmoth_gary_alternation(partner_nonhuman=False,
                                                   library_cards=20, life=40)["won"])
        self.assertTrue(yawgmoth_gary_alternation(partner_nonhuman=True,
                                                  library_cards=1, life=40)["decked"])

    def test_F2_removed_before_death_fails_but_removed_after_trigger_does_not(self):
        self.guard("F2", "Marchesa, the Black Rose")
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=False,
                                                died_as_card_with_plus=True, still_in_grave=True))
        self.assertTrue(marchesa_delayed_return(marchesa_at_death=True,
                                               died_as_card_with_plus=True, still_in_grave=True,
                                               marchesa_removed_after_death=True))

    def test_F3_counter_removal_or_exile_blocks_exact_recursion_precondition(self):
        self.guard("F3", "Marchesa, the Black Rose", "The Ozolith")
        self.assertTrue(marchesa_delayed_return(marchesa_at_death=True,
                                               died_as_card_with_plus=True, still_in_grave=True))
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=True,
                                                died_as_card_with_plus=False, still_in_grave=True))
        self.assertFalse(marchesa_delayed_return(marchesa_at_death=True,
                                                died_as_card_with_plus=True, still_in_grave=False))

    def test_original_remaining_W3_is_not_implicitly_dispositioned(self):
        self.assertEqual({k for k, v in self.original.items() if v == "DEFERRED"},
                         TESTED_CASES | {"W3"})
        self.assertNotIn("River Kelpie", self.cards)  # historical line changed


if __name__ == "__main__":
    unittest.main()
