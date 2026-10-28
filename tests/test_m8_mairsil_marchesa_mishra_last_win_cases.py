"""Original M6 remaining Mairsil W3, Marchesa W3 and Mishra Eminent W3/F3.

Each fixture is source/plan exact, uses one physical card per permanent and
executes bounded normal/adversarial state transitions without deck mutation.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Mairsil__the_Pretender": (
        "fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad",
        "e696c3c125ec11578a32b17e6859750d82a1845f"),
    "Marchesa__the_Black_Rose": (
        "c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02",
        "7d8c894c23bbcf7a6cd5adc361023ba2014ec9ad"),
    "Mishra__Eminent_One": (
        "0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0",
        "ce67d40eb242741e235f6366caa438053683e8de"),
}


def caged_tree_hateflayer(*, opponent_life=40, mairsil_toughness=4,
                          mairsil_power=4, tree_caged=True, hateflayer_caged=True,
                          mairsil_untapped=True, controlled_since_turn_start=True,
                          haste_from_anger=False, pay_two_generic_one_red=True,
                          tree_target_legal=True, damage_target_legal=True,
                          prevent_hateflayer_damage=False):
    """Tree {T} exchanges life and toughness; Hateflayer 2R,{Q} deals power.

    A caged ability is usable only once per turn. Q requires a tapped source
    and a creature controlled since turn start or genuine haste. Tree's
    exchange changes toughness, not power; this is not infinite untapping.
    """
    can_act = controlled_since_turn_start or haste_from_anger
    if not (tree_caged and mairsil_untapped and can_act and tree_target_legal):
        return {"tree_used": False, "opponent_life": opponent_life, "won": False}
    opponent_life, mairsil_toughness = mairsil_toughness, opponent_life
    can_flayer = (hateflayer_caged and pay_two_generic_one_red and can_act
                  and damage_target_legal)
    damage = mairsil_power if can_flayer and not prevent_hateflayer_damage else 0
    opponent_life -= damage
    return {"tree_used": True, "flayer_used": can_flayer,
            "mairsil_toughness": mairsil_toughness,
            "damage": damage, "mairsil_untapped": can_flayer,
            "opponent_life": opponent_life, "won": opponent_life <= 0}


def mairsil_disk_blink(*, disk_caged=True, aetherling_caged=True,
                       pay_one_generic=True, pay_blue=True,
                       mairsil_untapped=True, owner_leaves_in_exile=True,
                       disk_resolves=True):
    """Disk {1},T goes on stack; Aetherling U exiles Mairsil in response.

    The commander can return at the next end step only if its owner declines
    the command-zone move and leaves the same physical card in exile.
    """
    activated = bool(disk_caged and pay_one_generic and mairsil_untapped)
    escaped = bool(activated and aetherling_caged and pay_blue and owner_leaves_in_exile)
    return {"disk_activated": activated, "disk_destroyed_board":
            bool(activated and disk_resolves),
            "mairsil_survives": bool(escaped or not (activated and disk_resolves)),
            "mairsil_return_end_step": escaped}


def spark_redcap_persist(*, opponent_life=20, iterations=20,
                         spark_double=True, redcap_present=True,
                         altar=True, opponent_target_legal=True,
                         graveyard_hate=False, persist_counter_remains=False):
    """One Spark Double enters as a nonlegendary Redcap copy with +1 counter.

    On dying its copied persist triggers. It returns with -1 counter and, if
    Redcap is still present to copy, Spark Double's new +1 counter cancels it.
    Thus the same Spark Double card may die again with no -1 and recur.
    Marchesa's delayed +1-counter return cannot double-return a card that
    has already left the graveyard through persist. Altar sacrifices exactly
    one physical creature per cycle; Redcap ETB deals power two per return.
    """
    if not spark_double or not redcap_present or not altar:
        return {"events": (), "opponent_life": opponent_life, "won": False}
    events = []
    counter = "+1"  # Spark enters with +1; present copied Redcap is 2/2.
    for _ in range(iterations):
        if counter == "-1" or not redcap_present:
            break
        # Real Altar sacrifice: one permanent changes zones once.
        recurs = not graveyard_hate
        if recurs:
            # Persist returns with -1; Spark Double adds +1 on new entry.
            counter = "none" if not persist_counter_remains else "-1"
        else:
            counter = "exile"
        damage = 2 if recurs and opponent_target_legal else 0
        opponent_life -= damage
        events.append({"altar_colorless": 2, "persist_return": recurs,
                       "redcap_etb_damage": damage, "counter_after": counter,
                       "opponent_life": opponent_life})
        if opponent_life <= 0 or not recurs:
            break
    return {"events": tuple(events), "opponent_life": opponent_life,
            "won": opponent_life <= 0, "counter_after": counter}


def mishra_combat_warforms(*, commander_present=True, target_noncreature=True,
                           artifact_present=True, resonator=True, engine=True,
                           pay_resonator_two=True, pay_engine_two=True,
                           both_untapped=True, end_step=True):
    """One Mishra beginning-combat trigger and separately paid ability copies.

    Each Warform copy of a noncreature artifact is a 4/4 haste Construct named
    Mishra's Warform. Copying the trigger creates tokens, not further trigger
    activations; neither Strionic nor Engine can repeat taps unassisted.
    """
    if not commander_present or not target_noncreature or not artifact_present:
        return {"tokens_created": 0, "warforms_remaining": 0, "copied": 0}
    copies = int(bool(resonator and pay_resonator_two and both_untapped))
    copies += int(bool(engine and pay_engine_two and both_untapped))
    n = 1 + copies
    return {"tokens_created": n, "copied": copies,
            "warforms_remaining": 0 if end_step else n,
            "sacrificed_end_step": n if end_step else 0,
            "combat_haste": n}


def reservoir_warform_activation(*, life=51, warform_exists=True,
                                 legal_opponent=True, damage_prevented=False):
    """An Aetherflux-copy Warform inherits pay-50, not free 50 damage."""
    can_pay = life > 50 and warform_exists and legal_opponent
    return {"activated": can_pay, "life_after_cost": life - 50 if can_pay else life,
            "damage": 50 if can_pay and not damage_prevented else 0}


def mishra_five_mana_speed(*, opposing_finish_turn=3, commander_ready_turn=5,
                            first_counter_in_hand=False, blue_pitch=False,
                            opponent_spell_counterable=True, life=40):
    """A staged turn-three opposing combo; Force is conditional, not drawn."""
    countered = bool(first_counter_in_hand and blue_pitch and life > 1
                     and opponent_spell_counterable)
    return {"mishra_started": opposing_finish_turn >= commander_ready_turn,
            "opponent_wins_fixture": opposing_finish_turn < commander_ready_turn
                                     and not countered,
            "countered": countered}


class ThreeLastWinPackages(unittest.TestCase):
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

    def source(self, deck, case, *names):
        self.assertIn(case, self.deferred[deck])
        for name in names:
            self.assertEqual(self.cards[deck][name], 1, (deck, name))

    def test_mairsil_W3_tree_hateflayer_once_each_and_paid_disk_blink(self):
        deck = "Mairsil__the_Pretender"
        self.source(deck, "W3", "Mairsil, the Pretender", "Tree of Perdition",
                    "Hateflayer", "Aetherling", "Anger", "Nevinyrral's Disk")
        self.assertIn("only once each turn", self.oracle["Mairsil, the Pretender"])
        self.assertIn("Exchange target opponent's life total", self.oracle["Tree of Perdition"])
        self.assertIn("{2}{R}, {Q}", self.oracle["Hateflayer"])
        self.assertIn("Return it to the battlefield", self.oracle["Aetherling"])
        result = caged_tree_hateflayer()
        self.assertEqual(result["opponent_life"], 0)
        self.assertEqual(result["mairsil_toughness"], 40)
        self.assertEqual(result["damage"], 4)
        self.assertTrue(result["won"] and result["mairsil_untapped"])
        self.assertFalse(caged_tree_hateflayer(hateflayer_caged=False)["won"])
        self.assertFalse(caged_tree_hateflayer(pay_two_generic_one_red=False)["won"])
        self.assertFalse(caged_tree_hateflayer(damage_target_legal=False)["won"])
        self.assertFalse(caged_tree_hateflayer(prevent_hateflayer_damage=True)["won"])
        self.assertFalse(caged_tree_hateflayer(controlled_since_turn_start=False)["tree_used"])
        self.assertTrue(caged_tree_hateflayer(controlled_since_turn_start=False,
                        haste_from_anger=True)["won"])
        disk = mairsil_disk_blink()
        self.assertEqual(disk, {"disk_activated": True, "disk_destroyed_board": True,
                                "mairsil_survives": True, "mairsil_return_end_step": True})
        self.assertFalse(mairsil_disk_blink(pay_blue=False)["mairsil_survives"])
        self.assertFalse(mairsil_disk_blink(owner_leaves_in_exile=False)["mairsil_survives"])
        self.assertFalse(mairsil_disk_blink(disk_caged=False)["disk_activated"])

    def test_mairsil_F3_mirror_mad_removed_no_unsafe_self_mill_claim(self):
        deck = "Mairsil__the_Pretender"
        self.source(deck, "F3", "Mairsil, the Pretender", "Entomb", "Buried Alive",
                    "Demonic Tutor")
        self.assertEqual(self.cards[deck]["Mirror-Mad Phantasm"], 0)
        self.assertEqual(self.cards[deck]["Entomb"], 1)
        self.assertEqual(self.cards[deck]["Buried Alive"], 1)
        # Original blueprint's unsafe Mirror-Mad self-mill branch has no
        # physical source object. Entomb is one targeted card, Buried Alive
        # up to three; neither is an invented whole-library Mirror-Mad spin.

    def test_marchesa_W3_one_spark_copy_redcap_persist_counter_annihilation(self):
        deck = "Marchesa__the_Black_Rose"
        self.source(deck, "W3", "Marchesa, the Black Rose", "Spark Double",
                    "Murderous Redcap", "Glen Elendra Archmage",
                    "Puppeteer Clique", "Flayer of the Hatebound",
                    "Sage of Fables", "Ashnod's Altar", "Altar of Dementia")
        self.assertEqual(self.cards[deck]["River Kelpie"], 0)
        self.assertIn("additional +1/+1 counter", self.oracle["Spark Double"])
        self.assertIn("Persist", self.oracle["Murderous Redcap"])
        self.assertIn("deals damage equal to its power", self.oracle["Murderous Redcap"])
        trace = spark_redcap_persist(opponent_life=20)
        self.assertEqual(len(trace["events"]), 10)
        self.assertTrue(trace["won"])
        self.assertEqual([r["redcap_etb_damage"] for r in trace["events"]], [2] * 10)
        self.assertEqual([r["counter_after"] for r in trace["events"]], ["none"] * 10)
        self.assertEqual(sum(e["altar_colorless"] for e in trace["events"]), 20)
        self.assertFalse(spark_redcap_persist(redcap_present=False)["won"])
        self.assertFalse(spark_redcap_persist(altar=False)["won"])
        self.assertFalse(spark_redcap_persist(opponent_target_legal=False)["won"])
        self.assertEqual(len(spark_redcap_persist(graveyard_hate=True)["events"]), 1)
        self.assertEqual(len(spark_redcap_persist(persist_counter_remains=True)["events"]), 1)
        # Marchesa's delayed return is not another Spark Double object or an
        # extra copy after persist already moved the same card out of grave.

    def test_mishra_W3_reservoir_warform_paid_not_infinite_kci_resonator(self):
        deck = "Mishra__Eminent_One"
        self.source(deck, "W3", "Mishra, Eminent One", "Aetherflux Reservoir",
                    "Krark-Clan Ironworks", "Strionic Resonator", "Lithoform Engine")
        self.assertIn("beginning of combat on your turn", self.oracle["Mishra, Eminent One"])
        self.assertIn("{2}, {T}", self.oracle["Strionic Resonator"])
        self.assertIn("Sacrifice an artifact", self.oracle["Krark-Clan Ironworks"])
        copy = mishra_combat_warforms()
        self.assertEqual(copy, {"tokens_created": 3, "copied": 2,
                                "warforms_remaining": 0, "sacrificed_end_step": 3,
                                "combat_haste": 3})
        self.assertEqual(mishra_combat_warforms(resonator=False)["tokens_created"], 2)
        self.assertEqual(mishra_combat_warforms(engine=False)["tokens_created"], 2)
        self.assertEqual(mishra_combat_warforms(both_untapped=False)["tokens_created"], 1)
        self.assertEqual(mishra_combat_warforms(target_noncreature=False)["tokens_created"], 0)
        self.assertEqual(reservoir_warform_activation(),
                         {"activated": True, "life_after_cost": 1, "damage": 50})
        self.assertFalse(reservoir_warform_activation(life=50)["activated"])
        self.assertEqual(reservoir_warform_activation(damage_prevented=True)["damage"], 0)
        # KCI can sacrifice a physical Warform for CC, but that mana does not
        # untap either copier or generate new beginning-of-combat triggers.

    def test_mishra_F3_five_mana_combat_timing_and_precommander_response(self):
        deck = "Mishra__Eminent_One"
        self.source(deck, "F3", "Mishra, Eminent One", "Force of Will",
                    "Fierce Guardianship", "Mana Drain", "Deflecting Swat")
        self.assertIn("beginning of combat on your turn", self.oracle["Mishra, Eminent One"])
        lost = mishra_five_mana_speed()
        self.assertFalse(lost["mishra_started"])
        self.assertTrue(lost["opponent_wins_fixture"])
        defended = mishra_five_mana_speed(first_counter_in_hand=True, blue_pitch=True)
        self.assertTrue(defended["countered"])
        self.assertFalse(defended["opponent_wins_fixture"])
        self.assertTrue(mishra_five_mana_speed(first_counter_in_hand=True,
                        blue_pitch=False)["opponent_wins_fixture"])
        self.assertTrue(mishra_five_mana_speed(first_counter_in_hand=True,
                        blue_pitch=True, life=1)["opponent_wins_fixture"])
        self.assertTrue(mishra_five_mana_speed(first_counter_in_hand=True,
                        blue_pitch=True, opponent_spell_counterable=False)
                        ["opponent_wins_fixture"])
        self.assertTrue(mishra_five_mana_speed(opposing_finish_turn=6)
                        ["mishra_started"])
        # No promised T5 arrival: acceleration can make Mishra earlier; the
        # chosen opposing combo and interaction are conditional stress input.


if __name__ == "__main__":
    unittest.main()
