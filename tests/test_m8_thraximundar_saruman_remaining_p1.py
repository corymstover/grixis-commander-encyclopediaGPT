"""Five remaining original P1 cases with finite physical combat/death traces."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Thraximundar": ("f3e71b71fc10fbe6d8a1afde29b5291e9e32d4e83db44c2dcb7aab0773f18da2",
                     "ee410cdca6d22af61e6e1603b941cc3e7204b89c"),
    "Saruman__the_White_Hand": (
        "dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b",
        "4b0910b7ab8366f4851d877f53e73b1d3aacb621"),
}


def crawler_altar_drain(*, opponent_life=20, steps=25, zombie=True,
                        altar=True, crawler=True, artist=True,
                        grave_exile=False, opponent_target_legal=True):
    """One physical Gravecrawler: Altar sacrifice pays exactly its B recast.

    Carrion Feeder stays to satisfy control-another-Zombie continuously.
    The Gravecrawler object alternates battlefield→graveyard→battlefield;
    Artist triggers from each death, not from casting itself.
    """
    events = []
    zone = "battlefield" if crawler else "absent"
    for _ in range(steps):
        if zone != "battlefield" or not altar:
            break
        zone = "exile" if grave_exile else "graveyard"
        loss = int(bool(artist and opponent_target_legal))
        opponent_life -= loss
        recast = bool(zone == "graveyard" and zombie)
        if recast:
            zone = "battlefield"  # Altar produces B; Gravecrawler costs B.
        events.append({"altar_black": 1, "crawler_recast": recast,
                       "artist_life_loss": loss, "opponent_life": opponent_life,
                       "crawler_zone": zone})
        if opponent_life <= 0:
            break
    return {"events": tuple(events), "opponent_life": opponent_life,
            "opponent_lost": opponent_life <= 0, "crawler_zone": zone}


def thraxi_attack_sequence(*, opposing_creatures=3, cultist=True,
                           hits=(True, True, True), upkeep_sacrifice_paid=True,
                           commander_present=True):
    """Thraxi 6/6 haste; each attack sacrifices exactly one opposing creature.

    Cultist +3/+3 is conditional on its compulsory own-upkeep sacrifice.
    Shizo fear is never converted into guaranteed unblocked combat damage.
    """
    counters = 0
    damage = 0
    events = []
    if not commander_present or (cultist and not upkeep_sacrifice_paid):
        return events
    for hit in hits:
        sacrificed = int(opposing_creatures > 0)
        opposing_creatures -= sacrificed
        counters += sacrificed  # Thraxi may choose to add a counter; yes here.
        power = 6 + (3 if cultist else 0) + counters
        combat = power if hit else 0
        damage += combat
        events.append({"opponent_sacrificed": sacrificed, "power": power,
                       "hit": hit, "combat_damage": combat,
                       "commander_damage": damage,
                       "commander_loss": damage >= 21})
        if damage >= 21:
            break
    return events


def counterspell_capacity(*, threats=2, counterspells_in_hand=1,
                          mana_for_counters=1, both_counterable=True):
    """Each real Counterspell/Mana Drain object pays for only one target."""
    answer = min(threats, counterspells_in_hand, mana_for_counters) if both_counterable else 0
    return {"countered": answer, "unanswered": threats - answer}


def cair_andros_blasphemous(*, opponents_toughness=(2, 2, 2),
                            saruman=True, fall=True, all_will_be_one=True,
                            act_resolves=True, initial_army=0):
    """Act MV nine amasses on cast, then deals thirteen to all creatures.

    Fall's actual X is *excess damage* for each opposing creature, not two.
    Old Army power nine is killed by Act unless already boosted above thirteen;
    Fall's triggers then rebuild an Army with the sum of real excesses. Each
    individual amass counter event can make one All Will Be One trigger.
    """
    if not act_resolves:
        return {"act_resolved": False, "army_after": initial_army,
                "fall_events": (), "all_will_be_one_damage": 0}
    before = initial_army + (9 if saruman else 0)
    old_army_survives = before > 13
    army = before if old_army_survives else 0
    excesses = tuple(max(0, 13 - toughness) for toughness in opponents_toughness)
    trigger_excess = tuple(x for x in excesses if x and fall)
    for x in trigger_excess:
        army += x
    return {"act_resolved": True, "saruman_cast_amass": 9 if saruman else 0,
            "old_army_survives": old_army_survives,
            "fall_events": trigger_excess, "army_after": army,
            "all_will_be_one_damage": ((9 if saruman else 0) + sum(trigger_excess))
                                       if all_will_be_one else 0}


def army_projected_damage(*, army_power=41, opponents=(40, 40, 40),
                          soul_fire=False, ignition=False,
                          saruman_cast_trigger=False,
                          soul_target=0, paid_soul_mana=3,
                          paid_ignition_mana=5, paid_red_for_ignition=2,
                          army_target_survives=True):
    """One creature source hits one target by Soul's Fire or all by Ignition.

    Spells' single creature target must stay legal through resolution; the
    noncombat damage is not commander damage.
    """
    life = list(opponents)
    if not army_target_survives:
        return {"opponents": tuple(life), "damage": (0,) * len(life)}
    dealt = [0] * len(life)
    # A living Saruman's cast trigger resolves first and amasses the *mana
    # value* of these noncreature spells, not their discounted paid cost.
    final_power = army_power + ((3 if soul_fire else 0) + (5 if ignition else 0)
                                if saruman_cast_trigger else 0)
    if soul_fire and paid_soul_mana >= 3 and 0 <= soul_target < len(life):
        dealt[soul_target] += final_power
    if ignition and paid_ignition_mana >= 5 and paid_red_for_ignition >= 2:
        dealt = [d + final_power for d in dealt]
    for i, d in enumerate(dealt):
        life[i] -= d
    return {"opponents": tuple(life), "damage": tuple(dealt),
            "eliminated": tuple(i for i, value in enumerate(life) if value <= 0)}


class ThraxiSarumanRemainingP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.cards = {}
        cls.deferred = {}
        for deck, (raw_sha, plan_sha) in SOURCES.items():
            row = next(x for x in idx["decks"] if x["deck_id"] == deck)
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == row["source_sha256"] == raw_sha
            assert raw.decode().splitlines()[0].endswith(" [Commander]")
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

    def test_thraxi_W1_crawler_altar_real_black_and_live_zombie_death_drain(self):
        deck = "Thraximundar"
        self.source(deck, "W1", "Gravecrawler", "Phyrexian Altar", "Carrion Feeder",
                    "Rooftop Storm", "Pitiless Plunderer", "Reassembling Skeleton",
                    "Ashnod's Altar", "Blood Artist", "Zulaport Cutthroat",
                    "Warren Soultrader", "Diabolic Intent", "Demonic Tutor", "Vampiric Tutor")
        self.assertIn("as long as you control a Zombie", self.oracle["Gravecrawler"])
        self.assertIn("Add one mana of any color", self.oracle["Phyrexian Altar"])
        self.assertIn("target player loses 1 life", self.oracle["Blood Artist"])
        trace = crawler_altar_drain(opponent_life=20)
        self.assertEqual(len(trace["events"]), 20)
        self.assertTrue(trace["opponent_lost"])
        self.assertEqual(sum(e["altar_black"] for e in trace["events"]), 20)
        self.assertTrue(all(e["crawler_recast"] for e in trace["events"]))
        self.assertEqual(trace["crawler_zone"], "battlefield")
        self.assertEqual(len(crawler_altar_drain(zombie=False)["events"]), 1)
        self.assertEqual(len(crawler_altar_drain(grave_exile=True)["events"]), 1)
        self.assertEqual(len(crawler_altar_drain(altar=False)["events"]), 0)
        self.assertFalse(crawler_altar_drain(artist=False)["opponent_lost"])
        self.assertFalse(crawler_altar_drain(opponent_target_legal=False)["opponent_lost"])
        # The independently surviving Carrion Feeder is the necessary Zombie,
        # not the Gravecrawler being sacrificed during its own recast window.

    def test_thraxi_W2_actual_attack_sacrifice_growth_and_combat_only_damage(self):
        deck = "Thraximundar"
        self.source(deck, "W2", "Thraximundar", "Cultist of the Absolute",
                    "Shizo, Death's Storehouse", "Accursed Marauder",
                    "Fleshbag Marauder", "Innocent Blood", "Plaguecrafter")
        self.assertIn("Whenever Thraximundar attacks", self.oracle["Thraximundar"])
        self.assertIn("+3/+3", self.oracle["Cultist of the Absolute"])
        self.assertIn("artifact creatures and/or black creatures", self.oracle["Shizo, Death's Storehouse"])
        buffed = thraxi_attack_sequence()
        self.assertEqual([r["power"] for r in buffed], [10, 11])
        self.assertEqual([r["commander_damage"] for r in buffed], [10, 21])
        self.assertTrue(buffed[-1]["commander_loss"])
        no_cultist = thraxi_attack_sequence(cultist=False)
        self.assertEqual([r["commander_damage"] for r in no_cultist], [7, 15, 24])
        blocked = thraxi_attack_sequence(hits=(False, False, True))
        self.assertEqual(blocked[0]["commander_damage"], 0)
        self.assertFalse(blocked[-1]["commander_loss"])
        self.assertEqual(thraxi_attack_sequence(upkeep_sacrifice_paid=False), [])
        self.assertEqual(thraxi_attack_sequence(commander_present=False), [])
        # Fear still permits opposing artifact/black blockers, so each hit is
        # explicitly staged, not assumed from Shizo. Sacrifice is a choice.

    def test_thraxi_F2_limited_counter_capacity_after_force_cut(self):
        deck = "Thraximundar"
        self.source(deck, "F2", "Mana Drain", "Fierce Guardianship",
                    "Deflecting Swat")
        self.assertEqual(self.cards[deck]["Force of Will"], 0)
        self.assertEqual(self.cards[deck]["Counterspell"], 0)
        self.assertEqual(self.cards[deck]["Deadly Rollick"], 0)
        self.assertIn("Counter target spell", self.oracle["Mana Drain"])
        self.assertIn("Counter target noncreature spell", self.oracle["Fierce Guardianship"])
        shortage = counterspell_capacity(threats=2, counterspells_in_hand=1)
        self.assertEqual(shortage, {"countered": 1, "unanswered": 1})
        covered = counterspell_capacity(threats=2, counterspells_in_hand=2,
                                        mana_for_counters=2)
        self.assertEqual(covered, {"countered": 2, "unanswered": 0})
        self.assertEqual(counterspell_capacity(threats=2, mana_for_counters=0)
                         ["unanswered"], 2)
        self.assertEqual(counterspell_capacity(threats=2, both_counterable=False)
                         ["countered"], 0)
        # This is a bounded two-threat stress test, not a metagame win-rate,
        # probability-of-drawing-counters or proof the deck has zero answers.

    def test_saruman_W1_act_mv9_fall_excess_not_self_fueling_loop(self):
        deck = "Saruman__the_White_Hand"
        self.source(deck, "W1", "Fall of Cair Andros", "Blasphemous Act",
                    "Saruman, the White Hand", "All Will Be One", "The Great Goblin")
        self.assertIn("excess noncombat damage", self.oracle["Fall of Cair Andros"])
        self.assertIn("amass Orcs X", self.oracle["Saruman, the White Hand"])
        self.assertIn("13 damage", self.oracle["Blasphemous Act"])
        trace = cair_andros_blasphemous()
        self.assertEqual(trace["saruman_cast_amass"], 9)  # MV, not reduced cost.
        self.assertFalse(trace["old_army_survives"])
        self.assertEqual(trace["fall_events"], (11, 11, 11))
        self.assertEqual(trace["army_after"], 33)
        self.assertEqual(trace["all_will_be_one_damage"], 42)
        self.assertEqual(cair_andros_blasphemous(fall=False)["army_after"], 0)
        self.assertEqual(cair_andros_blasphemous(
                         opponents_toughness=(14, 14)) ["fall_events"], ())
        self.assertEqual(cair_andros_blasphemous(
                         all_will_be_one=False)["all_will_be_one_damage"], 0)
        self.assertFalse(cair_andros_blasphemous(act_resolves=False)["act_resolved"])
        # Act also kills an ordinary unprotected Saruman/Great Goblin; the
        # after-Act Fall counters cannot claim a surviving Goblin ping.

    def test_saruman_W2_one_target_soul_fire_multi_ignition_paid(self):
        deck = "Saruman__the_White_Hand"
        self.source(deck, "W2", "Saruman, the White Hand", "Soul's Fire",
                    "Chandra's Ignition", "The Great Goblin", "All Will Be One",
                    "Widespread Brutality", "Mauhúr, Uruk-hai Captain",
                    "Harmonic Prodigy", "Wizard's Staff", "Veyran, Voice of Duality")
        self.assertIn("to any target", self.oracle["Soul's Fire"])
        self.assertIn("each other creature and each opponent", self.oracle["Chandra's Ignition"])
        self.assertIn("one or more counters", self.oracle["The Great Goblin"])
        one = army_projected_damage(soul_fire=True, army_power=38,
                                    saruman_cast_trigger=True)
        self.assertEqual(one["damage"], (41, 0, 0))
        self.assertEqual(one["eliminated"], (0,))
        table = army_projected_damage(ignition=True, army_power=36,
                                     saruman_cast_trigger=True)
        self.assertEqual(table["damage"], (41, 41, 41))
        self.assertEqual(table["eliminated"], (0, 1, 2))
        self.assertEqual(army_projected_damage(ignition=True,
                         paid_red_for_ignition=1)["damage"], (0, 0, 0))
        self.assertEqual(army_projected_damage(soul_fire=True,
                         paid_soul_mana=2)["damage"], (0, 0, 0))
        self.assertEqual(army_projected_damage(ignition=True,
                         army_target_survives=False)["damage"], (0, 0, 0))
        self.assertEqual(army_projected_damage(army_power=33,
                         ignition=True)["eliminated"], ())
        # Goblin pings TWO per counter-placement event, not per +1/+1 counter.
        # All Will Be One can do counter count damage, but those are separate
        # triggered abilities, not free copied Soul's Fires or lethal attacks.


if __name__ == "__main__":
    unittest.main()
