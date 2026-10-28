"""The final five original P1 cases: source-bound finite conditional witnesses.

Qualitative W/F assertions remain bounded matchup observations, not universal
proof that a 100-card Commander deck must win or lose every possible game.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Mishra__Artificer_Prodigy": (
        "45c0d559f0aa859b84e2fb52baf31fdbb683de3e7bc7f211821b50420dee9761",
        "7528365f27f59d296b0426e5c45e7d247005fbdd"),
    "Nathan_Drake__Treasure_Hunter": (
        "e461d3e89828c7d4950f33301eb5ce658818014304de3771664ec19ce608ef57",
        "b16c6a340de8a638eec0cdc4e838663e6de5931a"),
    "Obeka__Splitter_of_Seconds": (
        "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859",
        "e3d991092b39c957fe9114fb0ed34f3db4556e61"),
    "The_Rani": (
        "924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27",
        "65b91c7eec13c7fc4494662576b5ebf16c8a8c9e"),
}


def mishra_artifact_hate(*, stony=False, ouphe=False, artifacts=4,
                        top=True, kci=True, forge=True, sculptor=True,
                        reservoir=True, force_in_hand=False,
                        force_blue_pitch=False, remove_hate=False):
    """Opposing Stony/Ouphe forbids artifact activations, not static/triggered.

    This exercises permission at an activation window, not a claim that an
    entire game with four distinct artifact objects can be captured here.
    """
    blocked = (stony or ouphe) and not remove_hate
    artifact_present = artifacts > 0
    return {"top_activation": artifact_present and top and not blocked,
            "kci_mana": 2 if artifact_present and kci and not blocked else 0,
            "forge_top_exile": artifact_present and forge and not blocked,
            "reservoir_pay_50": artifact_present and reservoir and not blocked,
            "forge_static_cast_permission": artifact_present and forge,
            "sculptor_static_discount": bool(artifact_present and sculptor),
            "reservoir_cast_trigger": bool(artifact_present and reservoir),
            "force_counter_available": bool(force_in_hand and force_blue_pitch)}


def nathan_attack_reveal(*, opponent_top=("spell", 3, "green"),
                         self_top=("land", 0, ""), other_tops=(),
                         nathan_attacks=True, mana=3,
                         cast_selected_opponent=True, opposing_counter=False):
    """Exile one real top card per player and allow ONE spell during trigger.

    Opposing spell color can be paid with any-color mana thanks to Nathan;
    generic mana quantity still must be spent, and exiled lands cannot cast.
    No unchosen exile card is returned to a library or put into a hand.
    """
    if not nathan_attacks:
        return {"exiled": 0, "cast": False, "stolen": False,
                "resolved": False, "unused_exiled": 0}
    tops = (self_top, opponent_top) + tuple(other_tops)
    chosen = opponent_top if cast_selected_opponent else self_top
    is_spell = chosen[0] == "spell"
    legal_cost = mana >= chosen[1] and (cast_selected_opponent or
                                         chosen[2] in {"", "blue", "black", "red"})
    cast = is_spell and legal_cost
    return {"exiled": len(tops), "cast": cast,
            "stolen": cast and cast_selected_opponent,
            "resolved": cast and not opposing_counter,
            "unused_exiled": len(tops) - int(cast),
            "mana_paid": chosen[1] if cast else 0,
            "trigger_cast_window": cast}


def nathan_interactive_game(*, turns=3, attack_reveals=("land", "spell", "land"),
                            stolen_spells_answered=True,
                            force_in_hand=False, blue_pitch=False,
                            opponent_combo_at_turn=3):
    """Bounded adversarial table: card access is not a guaranteed finisher."""
    casts = sum(1 for x in attack_reveals[:turns] if x == "spell")
    resolutions = 0 if stolen_spells_answered else casts
    can_stop_combo = force_in_hand and blue_pitch
    return {"casts": casts, "resolutions": resolutions,
            "opponent_finishes": opponent_combo_at_turn <= turns and not can_stop_combo,
            "guaranteed_lethal": False}


def obeka_smaug_journal(*, obeka_connects=True, combat_damage=2,
                        smaug_attacks=True, treasures_initial=0,
                        smaug_upkeep_trigger=True, journal=True,
                        journal_untapped=True, opponent_blocks=False):
    """Bonus upkeep steps happen AFTER the combat phase, not before attack.

    One normal upkeep supplies one Treasure/Clue. Smaug's same-combat attack
    trigger counts ONLY precombat Treasures. Obeka then earns damage-number
    extra upkeeps, triggering one more Treasure and Clue per upkeep.
    """
    precombat_treasures = treasures_initial + int(smaug_upkeep_trigger)
    attack_damage = precombat_treasures if smaug_attacks else 0
    additional = combat_damage if obeka_connects and not opponent_blocks else 0
    total_upkeeps = 1 + additional
    treasures_after = treasures_initial + (total_upkeeps if smaug_upkeep_trigger else 0)
    clues = total_upkeeps if journal else 0
    tutor = bool(journal and journal_untapped and clues >= 3)
    return {"smaug_same_combat_damage": attack_damage,
            "additional_upkeeps_after_combat": additional,
            "total_upkeeps": total_upkeeps,
            "treasures_after_combat_upkeeps": treasures_after,
            "clues_created": clues,
            "journal_tutor": tutor,
            "clues_after_tutor": clues - (3 if tutor else 0),
            "unconditional_lethal": False}


def rani_long_combat(*, goaded_connects=True, erdwal=True,
                     manufactor=True, bjorna_target_creature=True,
                     sieve_untapped=True, life=40, own_attack_damage=0):
    """Rani gains Clue resources only from real other-opponent goaded hits."""
    investigations = (1 + int(erdwal)) if goaded_connects else 0
    artifacts = investigations * (3 if manufactor else 1)
    bjorna_sacrifice = bool(artifacts and bjorna_target_creature)
    remain = artifacts - int(bjorna_sacrifice)
    sieve = bool(sieve_untapped and remain >= 5)
    remain -= 5 if sieve else 0
    # Bjorna deals to a target CREATURE, not a player; Rani Clues do no damage.
    return {"investigations": investigations, "artifacts_created": artifacts,
            "bjorna_creature_damage": 1 if bjorna_sacrifice else 0,
            "extra_turn": sieve, "artifacts_remaining": remain,
            "opponent_life_after": life - own_attack_damage,
            "lethal": own_attack_damage >= life}


class LastFourQualitativeOriginalP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.cards = {}
        cls.deferred = {}
        for deck, (raw_sha, plan_sha) in SOURCES.items():
            row = next(x for x in idx["decks"] if x["deck_id"] == deck)
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == row["source_sha256"] == raw_sha
            cards = Counter()
            for line in raw.decode().splitlines():
                n, name = line.split("x ", 1)
                cards[name.removesuffix(" [Commander]")] += int(n)
            assert sum(cards.values()) == 100
            cls.cards[deck] = cards
            rec = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{deck}_{raw_sha[:16]}.json").read_text())
            assert rec["approved_raw_sha256"] == raw_sha
            assert rec["m6_transfer"]["plan_blob_sha"] == plan_sha
            cls.deferred[deck] = {r["case_id"] for r in rec["m6_transfer"]["P1"]
                                  if r["status"] == "DEFERRED"}
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as f:
            for line in f:
                row = json.loads(line)
                cls.oracle[row["canonical_name"]] = row["oracle_text"]

    def source(self, deck, case, *cards):
        self.assertIn(case, self.deferred[deck])
        for card in cards:
            self.assertEqual(self.cards[deck][card], 1, (deck, card))

    def test_mishra_artificer_F2_stony_ouphe_activation_lock_and_static_survivors(self):
        deck = "Mishra__Artificer_Prodigy"
        self.source(deck, "F2", "Mishra, Artificer Prodigy", "Sensei's Divining Top",
                    "Krark-Clan Ironworks", "Mystic Forge", "Etherium Sculptor",
                    "Aetherflux Reservoir", "Cyclonic Rift", "Force of Will")
        self.assertIn("Sacrifice an artifact: Add", self.oracle["Krark-Clan Ironworks"])
        self.assertIn("You may cast artifact spells", self.oracle["Mystic Forge"])
        self.assertIn("Whenever you cast a spell", self.oracle["Aetherflux Reservoir"])
        normal = mishra_artifact_hate()
        self.assertTrue(normal["top_activation"])
        self.assertEqual(normal["kci_mana"], 2)
        for hate in ({"stony": True}, {"ouphe": True}, {"stony": True, "ouphe": True}):
            r = mishra_artifact_hate(**hate)
            self.assertFalse(r["top_activation"])
            self.assertEqual(r["kci_mana"], 0)
            self.assertFalse(r["forge_top_exile"])
            self.assertFalse(r["reservoir_pay_50"])
            self.assertTrue(r["forge_static_cast_permission"])
            self.assertTrue(r["sculptor_static_discount"])
            self.assertTrue(r["reservoir_cast_trigger"])
            self.assertTrue(mishra_artifact_hate(**hate, remove_hate=True)["top_activation"])
        self.assertFalse(mishra_artifact_hate(artifacts=0)["top_activation"])
        self.assertFalse(mishra_artifact_hate(stony=True)["force_counter_available"])
        self.assertTrue(mishra_artifact_hate(stony=True, force_in_hand=True,
                                            force_blue_pitch=True)["force_counter_available"])
        # Creature removal or Rift may remove a relevant permanent, but no
        # response is assumed to exist in hand at the adversarial window.

    def test_nathan_W2_one_paid_opponent_stolen_spell_conditional_library(self):
        deck = "Nathan_Drake__Treasure_Hunter"
        self.source(deck, "W2", "Nathan Drake, Treasure Hunter",
                    "Fire Lord Azula", "Karlach, Fury of Avernus")
        self.assertIn("exile the top card of each player's library",
                      self.oracle["Nathan Drake, Treasure Hunter"])
        self.assertIn("mana as though it were mana of any color",
                      self.oracle["Nathan Drake, Treasure Hunter"])
        self.assertIn("Firebending 2", self.oracle["Fire Lord Azula"])
        for absent in ("Gonti, Night Minister", "Thief of Sanity",
                       "Tinybones, the Pickpocket", "Etali, Primal Storm"):
            self.assertEqual(self.cards[deck][absent], 0)
        r = nathan_attack_reveal(other_tops=(("land", 0, ""), ("spell", 8, "white")))
        self.assertEqual(r["exiled"], 4)
        self.assertTrue(r["cast"] and r["stolen"] and r["resolved"])
        self.assertEqual(r["mana_paid"], 3)
        self.assertEqual(r["unused_exiled"], 3)
        self.assertFalse(nathan_attack_reveal(opponent_top=("spell", 5, "green"))["cast"])
        self.assertFalse(nathan_attack_reveal(opponent_top=("land", 0, ""))["cast"])
        self.assertFalse(nathan_attack_reveal(nathan_attacks=False)["cast"])
        self.assertFalse(nathan_attack_reveal(opposing_counter=True)["resolved"])
        self.assertFalse(nathan_attack_reveal(cast_selected_opponent=False)["cast"])
        # 'Whatever opponent libraries provide' is conditional, not a
        # guaranteed deterministic card or extra free spell each attack.

    def test_nathan_F2_interaction_heavy_three_turn_miss_fixture(self):
        deck = "Nathan_Drake__Treasure_Hunter"
        self.source(deck, "F2", "Nathan Drake, Treasure Hunter", "Force of Will",
                    "Fire Lord Azula", "Karlach, Fury of Avernus")
        adversarial = nathan_interactive_game()
        self.assertEqual(adversarial["casts"], 1)
        self.assertEqual(adversarial["resolutions"], 0)
        self.assertTrue(adversarial["opponent_finishes"])
        self.assertFalse(adversarial["guaranteed_lethal"])
        self.assertFalse(nathan_interactive_game(force_in_hand=True,
                         blue_pitch=True)["opponent_finishes"])
        favorable = nathan_interactive_game(attack_reveals=("spell",) * 3,
                                            stolen_spells_answered=False)
        self.assertEqual(favorable["resolutions"], 3)
        self.assertFalse(favorable["guaranteed_lethal"])
        # F2 records a plausible fragile tempo matchup; it cannot prove no
        # possible stolen opponent combo nor an exhaustive 99-card absence.

    def test_obeka_W3_postcombat_upkeep_smaug_and_journal_value_fixture(self):
        deck = "Obeka__Splitter_of_Seconds"
        self.source(deck, "W3", "Obeka, Splitter of Seconds",
                    "Smaug the Magnificent", "Tamiyo's Journal", "Super Intelligence")
        self.assertIn("after this phase", self.oracle["Obeka, Splitter of Seconds"])
        self.assertIn("number of Treasures you control", self.oracle["Smaug the Magnificent"])
        self.assertIn("Sacrifice three Clues", self.oracle["Tamiyo's Journal"])
        self.assertIn("enchanted creature's controller", self.oracle["Super Intelligence"])
        normal = obeka_smaug_journal()
        self.assertEqual(normal["smaug_same_combat_damage"], 1)
        self.assertEqual(normal["additional_upkeeps_after_combat"], 2)
        self.assertEqual(normal["total_upkeeps"], 3)
        self.assertEqual(normal["treasures_after_combat_upkeeps"], 3)
        self.assertEqual(normal["clues_created"], 3)
        self.assertTrue(normal["journal_tutor"])
        self.assertEqual(normal["clues_after_tutor"], 0)
        blocked = obeka_smaug_journal(opponent_blocks=True)
        self.assertEqual(blocked["total_upkeeps"], 1)
        self.assertFalse(blocked["journal_tutor"])
        self.assertEqual(obeka_smaug_journal(smaug_attacks=False)
                         ["smaug_same_combat_damage"], 0)
        self.assertFalse(obeka_smaug_journal(journal_untapped=False)["journal_tutor"])
        self.assertFalse(obeka_smaug_journal(combat_damage=1)["journal_tutor"])
        self.assertFalse(normal["unconditional_lethal"])
        # Future combat can convert Treasures into Smaug trigger damage; the
        # current combat cannot spend bonus upkeeps before they happen.

    def test_rani_F2_nonlethal_token_value_and_conditional_extra_turn(self):
        deck = "The_Rani"
        self.source(deck, "F2", "The Rani", "Bjorna, Nightfall Alchemist",
                    "Time Sieve", "Erdwal Illuminator", "Academy Manufactor",
                    "Ghoulish Impetus", "Disrupt Decorum")
        self.assertIn("deals combat damage to one of your opponents",
                      self.oracle["The Rani"])
        self.assertIn("target creature", self.oracle["Bjorna, Nightfall Alchemist"])
        self.assertIn("Sacrifice five artifacts", self.oracle["Time Sieve"])
        normal = rani_long_combat()
        self.assertEqual(normal["artifacts_created"], 6)
        self.assertEqual(normal["bjorna_creature_damage"], 1)
        self.assertTrue(normal["extra_turn"])
        self.assertEqual(normal["artifacts_remaining"], 0)
        self.assertEqual(normal["opponent_life_after"], 40)
        self.assertFalse(normal["lethal"])
        self.assertFalse(rani_long_combat(goaded_connects=False)["extra_turn"])
        self.assertFalse(rani_long_combat(manufactor=False)["extra_turn"])
        self.assertFalse(rani_long_combat(erdwal=False)["extra_turn"])
        self.assertFalse(rani_long_combat(sieve_untapped=False)["extra_turn"])
        self.assertTrue(rani_long_combat(own_attack_damage=40)["lethal"])
        # It is a conditional creature-combat win plan, not a certified
        # assertion that no unexamined 99-card interaction can go infinite.


if __name__ == "__main__":
    unittest.main()
