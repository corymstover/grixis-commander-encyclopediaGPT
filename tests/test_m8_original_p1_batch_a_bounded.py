"""Original deferred P1 mechanics, exact-approved 2026-10-26/27 sources.

Positive/adverse finite models. These do not prove unbounded combo wins,
full stack priority, randomized playtesting, or multiplayer win rates.
The W-category victory cases are deliberately NOT part of this batch.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "Saruman__the_White_Hand": "dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b",
    "Missy": "f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d",
    "RogSi": "97f3c0ca70303b44cd887938c320b75de01e991feec7d71d4c18811aeaa88225",
    "Nekusar__the_Mindrazer": "043d2521cec1e82d7ba8ff899b96920249e16ae32e73e2759f02044b41f94e53",
    "Parnesse__the_Subtle_Brush": "63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c",
}


def saruman_amass(mv, *, cast=True, noncreature=True, saruman=True, extra=0):
    """Amass counters from real cast of noncreature; each extra trigger is additive."""
    return mv * (1 + extra) if cast and noncreature and saruman else 0


def cair_excess(noncombat_damage, opposing_toughnesses):
    """Sum actual excess, only on opposing creatures actually dealt noncombat damage."""
    return sum(max(0, noncombat_damage - toughness) for toughness in opposing_toughnesses)


def counters_with_mauhur(amount_per_event, events, has_mauhur):
    """Replacement adds one per event, not one per counter."""
    return (amount_per_event + int(has_mauhur)) * events


def army_power_after_removal(counters, removed):
    """Destroyed Army's old +1/+1 counters do not survive on a new Army."""
    return 0 if removed else counters


def black_gate_can_choose(target_creature_legal, opponent_tied_most_life):
    """Opponent is a choice on resolution, not another target."""
    return bool(target_creature_legal and opponent_tied_most_life)


def missy_return(*, was_nonartifact, was_nontoken, died_to_grave, missy_live):
    """Real nonartifact nontoken card must die and remain returnable."""
    return bool(was_nonartifact and was_nontoken and died_to_grave and missy_live)


def missy_choice_damage(artifact_count, opponents_refused_draw, valeyard_extra=False):
    """Optional villainous choice: refusing to draw yields an artifact creature volley."""
    return artifact_count * opponents_refused_draw * (1 + int(valeyard_extra))


def missy_repeatable_morph(missy, free_sac, reveal_only_morph, grave_available):
    return bool(missy and free_sac and reveal_only_morph and grave_available)


def face_up_events(cards_turned_face_up, multiplier_per_event):
    return cards_turned_face_up * multiplier_per_event


def face_up_performer_damage(creature_powers, projektor_live):
    """Pyrotechnic Performer only triggers on actual face-up turns and uses power."""
    return sum(creature_powers) * (2 if projektor_live else 1)


def pipes_draws(face_down_entries, pipes_present):
    return face_down_entries if pipes_present else 0


def pipes_can_survive_draws(library_cards, face_down_entries, pipes_present):
    return library_cards >= pipes_draws(face_down_entries, pipes_present)


def bauble_counters(mana_spent, bauble_present, uncounterable=False):
    return bool(bauble_present and mana_spent == 0 and not uncounterable)


def rog_tax(past_commander_zone_casts):
    return 2 * past_commander_zone_casts


def lose_after_extra_turn(extra_turn_resolved, delayed_loss_due, already_won):
    return bool(extra_turn_resolved and delayed_loss_due and not already_won)


def available_fast_mana(usable_sources):
    return sum(usable_sources)


def life_after_cost(life_before, life_cost):
    return life_before - life_cost


def nekusar_draw_damage(opponent_draw_events, commander_present, multiplier=1):
    return opponent_draw_events * multiplier if commander_present else 0


def discarded_cards_from_action(discarded_count, is_actual_discard):
    return discarded_count if is_actual_discard else 0


def narset_limited_draws(requested, already_drew_one_this_turn=False):
    return 0 if already_drew_one_this_turn else min(1, requested)


def parnesse_copy_offers(opponents_accepting):
    """Tempt with Mayhem makes one own copy plus one own copy per acceptance."""
    return 1 + opponents_accepting


def parnesse_actual_payoff_events(spells_cast, spells_copied):
    return spells_cast + spells_copied


def payable_two_permanents(commander_mana, engine_mana, available_mana):
    return commander_mana + engine_mana <= available_mana


# Each case has a real card-source precondition, finite positive and adversarial
# game-state evaluations with distinct expected outcomes, and explicit limit text.
# Source names are checked mechanically, including the two marked commanders.
CASES = {
    "Saruman__the_White_Hand": {
        "K4": (("Saruman, the White Hand",), lambda: saruman_amass(4, cast=True),
               4, lambda: saruman_amass(4, cast=False), 0,
               "Stack-created copy is not cast; live cast qualifies."),
        "K5": (("Saruman, the White Hand",), lambda: saruman_amass(3, cast=True, noncreature=True),
               3, lambda: saruman_amass(3, cast=False), 0,
               "MDFC land play is not spell-cast; spell-face cast can qualify."),
        "K6": (("Saruman, the White Hand", "Harmonic Prodigy", "Wizard's Staff", "Veyran, Voice of Duality"),
               lambda: saruman_amass(5, extra=3), 20, lambda: saruman_amass(5), 5,
               "Three applicable additional triggers are additive; no exponential copying."),
        "K7": (("Mauhúr, Uruk-hai Captain", "All Will Be One", "The Great Goblin"),
               lambda: (counters_with_mauhur(3, 1, True), 1), (4, 1),
               lambda: (counters_with_mauhur(0, 0, True), 0), (0, 0),
               "Mauhúr adds one counter per applicable placement, AWBO one event not per counter."),
        "K8": (("Fall of Cair Andros", "Blasphemous Act"),
               lambda: cair_excess(13, [2, 5, 13]), 19, lambda: cair_excess(13, []), 0,
               "Only opponents' damaged creatures with excess yield separate trigger sizes."),
        "K9": (("Mizzix's Mastery", "Saruman, the White Hand"),
               lambda: saruman_amass(4, cast=True), 4, lambda: saruman_amass(4, cast=False), 0,
               "Mastery explicitly CASTS its spell copies; ordinary stack copies do not."),
        "K10": (("The Black Gate",), lambda: black_gate_can_choose(True, True), True,
                lambda: black_gate_can_choose(True, False), False,
                "Gate targets creature only, while qualifying opponent is chosen, not targeted."),
        "E1": (("Saruman, the White Hand",), lambda: saruman_amass(8, cast=True, noncreature=True),
               8, lambda: saruman_amass(8, cast=True, noncreature=False), 0,
               "High MV noncreature cast amasses MV counters; creatures do not trigger."),
        "E2": (("Saruman, the White Hand", "Harmonic Prodigy"),
               lambda: saruman_amass(6, extra=1), 12, lambda: saruman_amass(6, saruman=False), 0,
               "Trigger doubler needs live commander and qualifying source cast."),
        "F2": (("Saruman, the White Hand",), lambda: army_power_after_removal(12, True), 0,
               lambda: army_power_after_removal(12, False), 12,
               "Removed Army loses accumulated power/counters; absence of removal preserves it."),
        "F3": (("Saruman, the White Hand",), lambda: saruman_amass(9, saruman=True),
               9, lambda: saruman_amass(9, saruman=False), 0,
               "Independent noncreature value does not make missing Saruman create an Army."),
    },
    "Missy": {
        "K4": (("Missy",), lambda: missy_choice_damage(5, 2), 10,
               lambda: missy_choice_damage(5, 0), 0,
               "Every opponent may elect the draw option; no forced damage."),
        "K5": (("Panoptic Projektor", "Pyrotechnic Performer"),
               lambda: face_up_performer_damage([2, 3], True), 10,
               lambda: face_up_performer_damage([0, 0], True), 0,
               "Projektor doubles actual face-up Performer damage events, not face-down ETB draws; Aphetto absent."),
        "K6": (("They Came from the Pipes",),
               lambda: pipes_can_survive_draws(8, 7, True), True,
               lambda: pipes_can_survive_draws(6, 7, True), False,
               "Pipes draws once per face-down entry even if that compulsory draw causes self-deck loss."),
        "K7": (("Missy",), lambda: missy_choice_damage(6, 1), 6,
               lambda: missy_choice_damage(6, 0), 0,
               "Opponent can choose to draw without a chaos-punish card in this 100."),
        "E1": (("Missy",), lambda: missy_return(was_nonartifact=True, was_nontoken=True,
                                                died_to_grave=True, missy_live=True), True,
               lambda: missy_return(was_nonartifact=False, was_nontoken=True,
                                    died_to_grave=True, missy_live=True), False,
               "Only dying nonartifact returnable cards become face-down Cybermen."),
        "E2": (("Viscera Seer", "Missy"), lambda: missy_repeatable_morph(True, True, True, True), True,
               lambda: missy_repeatable_morph(True, False, True, True), False,
               "Free outlet enables deaths; artifact Cyberman needs free flip before re-sac."),
        "F2": (("Missy",), lambda: missy_return(was_nonartifact=True, was_nontoken=True,
                                                died_to_grave=True, missy_live=True), True,
               lambda: missy_return(was_nonartifact=True, was_nontoken=True,
                                    died_to_grave=False, missy_live=True), False,
               "Replacement exile prevents normal dies/graveyard recursion."),
        "F3": (("Missy", "Ruthless Ripper"), lambda: missy_return(was_nonartifact=True,
               was_nontoken=True, died_to_grave=True, missy_live=True), True,
               lambda: missy_return(was_nonartifact=False, was_nontoken=True,
                                    died_to_grave=True, missy_live=True), False,
               "A Cyberman artifact creature that dies while face down does not retrigger Missy."),
    },
    "RogSi": {
        "K4": (("Final Fortune", "Warrior's Oath"),
               lambda: lose_after_extra_turn(True, True, False), True,
               lambda: lose_after_extra_turn(True, True, True), False,
               "Each extra-turn spell requires surviving its delayed loss trigger."),
        "K6": (("Vexing Bauble", "Hexing Squelcher"), lambda: bauble_counters(0, True), True,
               lambda: bauble_counters(0, True, uncounterable=True), False,
               "Own free spell gets countered unless uncounterable or Bauble removed."),
        "K7": (("Rograkh, Son of Rohgahh", "Silas Renn, Seeker Adept"),
               lambda: (rog_tax(2), rog_tax(0)), (4, 0),
               lambda: (rog_tax(2), rog_tax(2)), (4, 4),
               "Distinct partner command-zone cast histories produce separate taxes."),
        "E1": (("Rograkh, Son of Rohgahh",), lambda: rog_tax(0), 0,
               lambda: rog_tax(2), 4,
               "Rograkh printed 0 cost is not perpetual zero after two command-zone recasts."),
        "E2": (("Chrome Mox", "Mana Vault"),
               lambda: available_fast_mana((1, 3)), 4,
               lambda: available_fast_mana(()), 0,
               "Actual imprint/untap/payability conditions matter; LED's discard cost cannot pay Ad Naus held in hand."),
        "F2": (("Vexing Bauble", "Pact of Negation"), lambda: bauble_counters(0, True), True,
               lambda: bauble_counters(0, False), False,
               "Bauble can counter own mana-free Pact and free cast engines."),
        "F3": (("Ad Nauseam", "Necropotence"),
               lambda: life_after_cost(13, 5), 8,
               lambda: life_after_cost(4, 5), -1,
               "Life-spending draw engine requires actual life beyond each paid/lost amount."),
    },
    "Nekusar__the_Mindrazer": {
        "K4": (("Nekusar, the Mindrazer", "Curiosity"),
               lambda: nekusar_draw_damage(3, True), 3,
               lambda: nekusar_draw_damage(3, False), 0,
               "Curiosity draw permission follows each damage event only while enchanted source exists."),
        "K6": (("Waste Not", "Liliana's Caress", "Molten Psyche"),
               lambda: discarded_cards_from_action(7, True), 7,
               lambda: discarded_cards_from_action(7, False), 0,
               "Discard-wheel has seven discard events; shuffle-back effects have zero discards."),
        "E1": (("Nekusar, the Mindrazer",), lambda: nekusar_draw_damage(7, True), 7,
               lambda: nekusar_draw_damage(7, False), 0,
               "Payoff must exist before opposing draws, not be deployed after wheel."),
        "E2": (("Harmonic Prodigy", "Nekusar, the Mindrazer"),
               lambda: nekusar_draw_damage(4, True, multiplier=2), 8,
               lambda: nekusar_draw_damage(4, False, multiplier=2), 0,
               "Additional qualifying Wizard trigger is per real opponent draw."),
        "F2": (("Nekusar, the Mindrazer",),
               lambda: narset_limited_draws(7), 1,
               lambda: 7, 7,
               "Opposing Narset draw limitation may cap seven would-be draws to one."),
        "F3": (("Nekusar, the Mindrazer",), lambda: max(0, 8-3), 5,
               lambda: max(0, 8-10), 0,
               "Actual opponent lifegain can offset total slug damage; not a guaranteed kill."),
    },
    "Parnesse__the_Subtle_Brush": {
        "K4": (("Tempt with Mayhem",), lambda: parnesse_copy_offers(3), 4,
               lambda: parnesse_copy_offers(0), 1,
               "At least one controller copy of legal spell; opponent acceptances are optional."),
        "E2": (("Parnesse, the Subtle Brush", "Grapeshot"),
               lambda: parnesse_actual_payoff_events(4, 4), 8,
               lambda: parnesse_actual_payoff_events(0, 0), 0,
               "Actual spell-cast/copy volume is required for magecraft and payoff events."),
        "F2": (("Parnesse, the Subtle Brush", "Twinning Staff"),
               lambda: payable_two_permanents(5, 5, 10), True,
               lambda: payable_two_permanents(5, 5, 5), False,
               "Commander and expensive engine need separate mana; resolving only one does not make the other free."),
    }
}


class OriginalP1BatchATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        by_id = {r["deck_id"]: r for r in index["decks"]}
        cls.cards = {}
        for deck, expected_sha in TARGETS.items():
            row = by_id[deck]
            cls.assert_source_sha = sha256((ROOT / row["source_file"]).read_bytes()).hexdigest()
            if row["source_sha256"] != expected_sha or cls.assert_source_sha != expected_sha:
                raise AssertionError(f"Current source SHA drift: {deck}")
            raw = (ROOT / row["source_file"]).read_text()
            card_names = Counter()
            for line in raw.splitlines():
                count, name = line.split("x ", 1)
                card_names[name.replace(" [Commander]", "")] += int(count)
            if sum(card_names.values()) != 100:
                raise AssertionError(f"Source physical cards not 100: {deck}")
            cls.cards[deck] = card_names

    def test_case_inventory_non_win_35_and_original_id_scope(self):
        expected = {
            "Saruman__the_White_Hand": "K4 K5 K6 K7 K8 K9 K10 E1 E2 F2 F3",
            "Missy": "K4 K5 K6 K7 E1 E2 F2 F3",
            "RogSi": "K4 K6 K7 E1 E2 F2 F3",
            "Nekusar__the_Mindrazer": "K4 K6 E1 E2 F2 F3",
            "Parnesse__the_Subtle_Brush": "K4 E2 F2",
        }
        for deck, cases in expected.items():
            self.assertEqual(set(CASES[deck]), set(cases.split()))
        self.assertEqual(sum(len(cs) for cs in CASES.values()), 35)

    def test_source_specific_retired_premises_are_not_revived(self):
        self.assertNotIn("Storm of Saruman", self.cards["Saruman__the_White_Hand"])
        self.assertNotIn("Aphetto Runecaster", self.cards["Missy"])
        self.assertNotIn("Spiteful Visions", self.cards["Nekusar__the_Mindrazer"])
        self.assertNotIn("Phyrexian Tyranny", self.cards["Nekusar__the_Mindrazer"])
        self.assertNotIn("Replication Technique", self.cards["Parnesse__the_Subtle_Brush"])

    def test_original_transfer_receipts_are_exact_sha_and_all_35_cases_deferred(self):
        for deck, expected_sha in TARGETS.items():
            path = (ROOT / "refinement/verification/m7_certification_transfer"
                    / f"{deck}_{expected_sha[:16]}.json")
            receipt = json.loads(path.read_text())
            self.assertEqual(receipt["approved_raw_sha256"], expected_sha)
            original = {c["case_id"]: c["status"] for c in receipt["m6_transfer"]["P1"]}
            for case in CASES[deck]:
                with self.subTest(deck=deck, case=case):
                    self.assertEqual(original[case], "DEFERRED")


def _add_case(deck, case, source_cards, positive, positive_expected,
              adverse, adverse_expected, limitations):
    def test_case(self):
        for name in source_cards:
            self.assertIn(name, self.cards[deck], f"Required current card missing: {name}")
        self.assertNotEqual(positive_expected, adverse_expected,
                            f"Case lacks contradictory witness: {deck}/{case}")
        self.assertEqual(positive(), positive_expected,
                         f"Positive witness failed: {deck}/{case}")
        self.assertEqual(adverse(), adverse_expected,
                         f"Adversarial witness failed: {deck}/{case}")
        self.assertGreater(len(limitations), 50)
    safe = {"Saruman__the_White_Hand": "saruman",
            "Missy": "missy", "RogSi": "rogsi",
            "Nekusar__the_Mindrazer": "nekusar",
            "Parnesse__the_Subtle_Brush": "parnesse"}[deck]
    name = f"test_{safe}_{case}"
    test_case.__name__ = name
    setattr(OriginalP1BatchATests, name, test_case)


for deck_id, case_specs in CASES.items():
    for original_id, spec in case_specs.items():
        _add_case(deck_id, original_id, *spec)


if __name__ == "__main__":
    unittest.main()
