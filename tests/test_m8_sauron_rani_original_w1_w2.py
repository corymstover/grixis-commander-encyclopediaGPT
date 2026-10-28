"""Current approved Sauron and Rani original W1/W2 finite/payable witnesses."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Sauron__Lord_of_the_Rings": (
        "c427805f78f7aca7384db56022868a2e7cb7d01eeeabbb280a18e77e538a8159",
        "f156344c744b0448f3e91e69552d8f0ffd37393f"),
    "The_Rani": (
        "924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27",
        "65b91c7eec13c7fc4494662576b5ebf16c8a8c9e"),
}


def sauron_archon_reanimation(*, from_commander=True, spell_paid=True,
                              creature_in_grave=True, target_mv=8, life=40,
                              target_etb_resolves=True, anger_grave=True,
                              mountain=True, wonder_grave=True, island=True,
                              opponent_life=40, opponent_hand=3,
                              opponent_creatures=2):
    """Sauron cast trigger mills five and reanimates; Reanimate pays life.

    Both routes require a real creature card in graveyard, possibly one just
    milled by Sauron; neither grants haste or flying unless grave/land gates.
    """
    if not creature_in_grave or (not from_commander and not spell_paid):
        return {"reanimated": False, "opponent_life": opponent_life}
    life -= 0 if from_commander else target_mv
    if life <= 0:
        return {"reanimated": False, "died_from_reanimate": True}
    if target_etb_resolves:
        opponent_life -= 3
        opponent_hand -= int(opponent_hand > 0)
        opponent_creatures -= int(opponent_creatures > 0)
        life += 3
    return {"reanimated": True, "amassed_on_cast": 5 if from_commander else 0,
            "milled_on_cast": 5 if from_commander else 0,
            "hasty": bool(anger_grave and mountain),
            "flying": bool(wonder_grave and island),
            "opponent_life": opponent_life, "opponent_hand": opponent_hand,
            "opponent_creatures": opponent_creatures, "our_life": life,
            "archon_draws": int(target_etb_resolves)}


def nazgul_ring_trigger(*, wraiths=4, temptations=1,
                        ring_effect=True, call_of_ring=True,
                        bearer_available=True, pay_two_life=True,
                        our_life=40):
    """Each Nazgul is a real Wraith with one trigger per temptation.

    The one Call upkeep temptation can optionally cost two life and draw one
    card after choosing a Ring-bearer. Each of four Nazgul triggers adds one
    counter to *each* controlled Wraith, not four fresh temptations.
    """
    n = temptations if ring_effect and call_of_ring else 0
    counters_each = wraiths * n
    paid = bool(n and bearer_available and pay_two_life and our_life > 2)
    return {"temptations": n, "nazgul_triggers": counters_each,
            "counters_each_wraith": counters_each,
            "total_counters": counters_each * wraiths,
            "life": our_life - (2 if paid else 0), "draws": int(paid)}


def rani_goaded_combat(*, opponents=3, goaded_creature=True,
                        attack_other_opponent=True, blocked=False,
                        defender_can_be_attacked=True,
                        erdwal=True, manufactor=True):
    """One marked/goaded opposing creature deals one player damage event.

    Rani investigates only for combat damage to one *of your opponents*.
    Erdwal adds one investigation on first investigate in the turn; Academy
    Manufactor converts each Clue into Clue+Food+Treasure token trio.
    """
    hit = (opponents >= 2 and goaded_creature and attack_other_opponent
           and defender_can_be_attacked and not blocked)
    investigations = (1 + int(erdwal)) if hit else 0
    token_trios = investigations if manufactor else 0
    return {"goaded_hit": hit, "investigations": investigations,
            "clues": investigations, "foods": token_trios,
            "treasures": token_trios,
            "total_artifacts": investigations * (3 if manufactor else 1)}


def rani_bjorna_sieve(*, investigations=2, manufactor=True,
                      bjorna_present=True, creature_target=True,
                      sieve=True, sieve_untapped=True):
    """One Rani/Erdwal clue batch and real Bjorna+Sieve sacrifice costs.

    Bjorna's one damage hits a target *creature*, not a player. Its activation
    sacrifices one physical artifact. Sieve then consumes five distinct
    remaining artifacts and taps for exactly one extra turn.
    """
    artifacts = investigations * (3 if manufactor else 1)
    ping = bool(bjorna_present and creature_target and artifacts >= 1)
    artifacts -= int(ping)
    turn = bool(sieve and sieve_untapped and artifacts >= 5)
    if turn:
        artifacts -= 5
    return {"bjorna_creature_damage": int(ping), "bjorna_goad": ping,
            "sieve_sacrificed": 5 if turn else 0, "extra_turn": turn,
            "artifacts_remaining": artifacts}


class SauronRaniOriginalW1W2(unittest.TestCase):
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
            receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                                  / f"{deck}_{raw_sha[:16]}.json").read_text())
            assert receipt["approved_raw_sha256"] == raw_sha
            assert receipt["m6_transfer"]["plan_blob_sha"] == plan_sha
            cls.deferred[deck] = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
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

    def test_sauron_W1_paid_reanimate_and_archon_exact_life_grave_gates(self):
        deck = "Sauron__Lord_of_the_Rings"
        self.source(deck, "W1", "Sauron, Lord of the Rings", "Archon of Cruelty",
                    "Valgavoth, Terror Eater", "Sheoldred, Whispering One",
                    "Anger", "Wonder", "Reanimate", "Animate Dead", "Necromancy",
                    "Dance of the Dead", "Victimize")
        self.assertEqual(self.cards[deck]["Jin-Gitaxias, Core Augur"], 0)
        self.assertIn("amass Orcs 5, mill five cards", self.oracle["Sauron, Lord of the Rings"])
        self.assertIn("lose life equal to that card's mana value", self.oracle["Reanimate"])
        self.assertIn("Whenever this creature enters or attacks", self.oracle["Archon of Cruelty"])
        cast = sauron_archon_reanimation()
        self.assertTrue(cast["reanimated"])
        self.assertEqual((cast["amassed_on_cast"], cast["milled_on_cast"]), (5, 5))
        self.assertEqual((cast["opponent_life"], cast["our_life"]), (37, 43))
        self.assertTrue(cast["hasty"] and cast["flying"])
        spell = sauron_archon_reanimation(from_commander=False)
        self.assertEqual(spell["our_life"], 35)  # 40 - 8 Reanimate + 3 Archon.
        self.assertFalse(sauron_archon_reanimation(creature_in_grave=False)["reanimated"])
        self.assertFalse(sauron_archon_reanimation(from_commander=False,
                         spell_paid=False)["reanimated"])
        self.assertFalse(sauron_archon_reanimation(from_commander=False,
                         life=8)["reanimated"])
        self.assertFalse(sauron_archon_reanimation(mountain=False)["hasty"])
        self.assertFalse(sauron_archon_reanimation(island=False)["flying"])
        self.assertEqual(sauron_archon_reanimation(target_etb_resolves=False)
                         ["opponent_life"], 40)
        # One Archon ETB attack-style drain is three life, not a promised
        # one-shot win. The cut Jin-Gitaxias branch is not relabelled tested.

    def test_sauron_W2_four_nazgul_one_real_tempt_four_triggers_each(self):
        deck = "Sauron__Lord_of_the_Rings"
        self.source(deck, "W2", "Call of the Ring", "The Black Gate",
                    "Sauron, Lord of the Rings")
        self.assertEqual(self.cards[deck]["Nazgûl"], 4)
        self.assertIn("Whenever the Ring tempts you", self.oracle["Nazgûl"])
        self.assertIn("you may pay 2 life", self.oracle["Call of the Ring"])
        r = nazgul_ring_trigger()
        self.assertEqual(r, {"temptations": 1, "nazgul_triggers": 4,
                             "counters_each_wraith": 4, "total_counters": 16,
                             "life": 38, "draws": 1})
        self.assertEqual(nazgul_ring_trigger(call_of_ring=False)["total_counters"], 0)
        self.assertEqual(nazgul_ring_trigger(wraiths=1)["total_counters"], 1)
        self.assertEqual(nazgul_ring_trigger(pay_two_life=False)["draws"], 0)
        self.assertEqual(nazgul_ring_trigger(bearer_available=False)["draws"], 0)
        self.assertEqual(nazgul_ring_trigger(our_life=2)["draws"], 0)
        # Four approved Nazgul are an actual special singleton exception; no
        # ninth copy, phantom temptation or immediate commander damage.

    def test_rani_W1_actual_other_opponent_goad_hit_and_investigate_tokens(self):
        deck = "The_Rani"
        self.source(deck, "W1", "The Rani", "Ghoulish Impetus", "Psychic Impetus",
                    "Shiny Impetus", "Coercive Impetus", "Incriminating Impetus",
                    "Eye of Nidhogg", "Disrupt Decorum", "Kardur, Doomscourge",
                    "Erdwal Illuminator", "Academy Manufactor")
        self.assertIn("Whenever a goaded creature deals combat damage to one of your opponents",
                      self.oracle["The Rani"])
        self.assertIn("investigate an additional time", self.oracle["Erdwal Illuminator"])
        hit = rani_goaded_combat()
        self.assertEqual(hit, {"goaded_hit": True, "investigations": 2,
                               "clues": 2, "foods": 2, "treasures": 2,
                               "total_artifacts": 6})
        self.assertEqual(rani_goaded_combat(blocked=True)["total_artifacts"], 0)
        self.assertEqual(rani_goaded_combat(opponents=1)["total_artifacts"], 0)
        self.assertEqual(rani_goaded_combat(manufactor=False)["total_artifacts"], 2)
        self.assertEqual(rani_goaded_combat(erdwal=False)["total_artifacts"], 3)
        self.assertEqual(rani_goaded_combat(goaded_creature=False)["total_artifacts"], 0)
        # Goad forces attacks only if able; never promises combat damage,
        # opponents left available to attack, or unlimited Clues.

    def test_rani_W2_bjorna_only_creature_ping_one_sieve_five_distinct_artifacts(self):
        deck = "The_Rani"
        self.source(deck, "W2", "Bjorna, Nightfall Alchemist", "Time Sieve",
                    "Academy Manufactor", "Erdwal Illuminator")
        self.assertIn("deals 1 damage to target creature", self.oracle["Bjorna, Nightfall Alchemist"])
        self.assertIn("Sacrifice five artifacts", self.oracle["Time Sieve"])
        r = rani_bjorna_sieve()
        self.assertEqual(r, {"bjorna_creature_damage": 1, "bjorna_goad": True,
                             "sieve_sacrificed": 5, "extra_turn": True,
                             "artifacts_remaining": 0})
        self.assertFalse(rani_bjorna_sieve(manufactor=False)["extra_turn"])
        self.assertFalse(rani_bjorna_sieve(investigations=1)["extra_turn"])
        self.assertFalse(rani_bjorna_sieve(sieve_untapped=False)["extra_turn"])
        self.assertFalse(rani_bjorna_sieve(sieve=False)["extra_turn"])
        self.assertFalse(rani_bjorna_sieve(creature_target=False)["bjorna_goad"])
        # One earned extra turn is not an unbounded repeatable engine without
        # fresh goaded combat hits generating two further investigations.


if __name__ == "__main__":
    unittest.main()
