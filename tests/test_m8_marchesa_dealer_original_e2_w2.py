"""Exact-current Marchesa, Dealer of Death original P1 E2/W2 bounded traces.

Includes real seven-card hands, costs, physical one-card LED recurrence and
finite library/grave limits. No unbounded loop or unopposed win is asserted.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = "Marchesa__Dealer_of_Death"
SHA = "931baa2762738ab32cd274ae8e128d0e3cd1aa85e81e51c2faa4934c1c70f363"
PLAN_BLOB = "03736d6379f1d8f55299118f8dac2e9ff2515e25"


def opening_mox_mana(hand, spell):
    """A real seven-card hand and once-per-turn land play, no free imprints.

    City of Brass supplies one U or B, an imprinted Dark Ritual supplies B,
    and Diamond discards Badlands to supply one additional color. These
    cannot all pay multiple different spells on the same turn.
    """
    h = Counter(hand)
    if sum(h.values()) != 7 or any(h[card] != 1 for card in (
        "City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond", "Badlands", spell
    )):
        return {"cast": False, "reason": "missing exact hand/land/imprint/diamond card"}
    for card in ("City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond", "Badlands"):
        h[card] -= 1
    # The land is played (one land play), Ritual is EXILED, Badlands DISCARDED.
    cost = {"Mystic Remora": (1, 0), "Rhystic Study": (1, 2),
            "Necropotence": (0, 3)}.get(spell)
    if cost is None:
        return {"cast": False, "reason": "unsupported named draw permanent"}
    # City one any-color + Chrome B + Diamond any-color; all one-use taps.
    if spell == "Necropotence":
        paid = ("B", "B", "B")
    elif spell == "Rhystic Study":
        paid = ("U", "B", "B")
    else:
        paid = ("U",)
    return {"cast": True, "mana_paid": paid, "city_life_loss": 1,
            "land_plays": 1, "imprinted_exiled": "Dark Ritual",
            "diamond_land_discarded": "Badlands",
            "hand_after": sum(h.values()) - 1,  # spell cast, not in hand
            "spell": spell}


def vault_ad_nauseam_opening(hand, reveal_mana_values=(2, 1)):
    """Ad Nauseam on turn one from exactly seven committed physical cards.

    City B pays {1} to cast Vault, then Vault C C C plus Chrome B and
    Diamond B pay full {3}{B}{B}. Imprinting/discarding are real card losses.
    """
    required = ("City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond",
                "Badlands", "Mana Vault", "Ad Nauseam")
    h = Counter(hand)
    if sum(h.values()) != 7 or any(h[c] != 1 for c in required):
        return {"cast": False}
    life = 40 - 1  # City of Brass tapping to pay Vault's generic mana.
    library_draws = []
    for mv in reveal_mana_values:
        life -= mv
        library_draws.append(mv)
    return {"cast": True, "spent": ("City generic 1 for Mana Vault",
                                    "Mana Vault CCC", "Chrome B", "Diamond B"),
            "imprint_exiled": "Dark Ritual", "diamond_discarded": "Badlands",
            "one_land_play": True, "life_after_reveals": life,
            "revealed_mana_values": library_draws}


def enchantment_opponent_draw(*, spell, qualifying_cast=True, opponent_pays=False):
    """Actual conditional trigger choice, with no promised card draw."""
    if spell not in {"Rhystic Study", "Mystic Remora"}:
        return 0
    if spell == "Mystic Remora" and not qualifying_cast:
        return 0  # creature spell is not a Remora trigger
    return int(not opponent_pays)


def petal_only_can_pay_brain_freeze(*, other_generic=0, other_blue=0):
    """Petal supplies either U or one generic, never both for {1}{U}."""
    return bool((other_generic >= 1) or (other_blue >= 1))


def marchesa_crimes_for_freeze(*, original_targets_opponent, storm_copies):
    """One targeted cast, not a new crime per uncast storm copy."""
    assert storm_copies >= 0
    return int(bool(original_targets_opponent))


def breach_led_brain_freeze(*, own_library=84, other_grave_cards=9,
                            opponents=(90, 90, 90), iterations=11,
                            breach=True, led=True, freeze=True,
                            opponent_removes_breach=False):
    """One LED/one Freeze physical loop with paid three-*other*-card escapes.

    Starting 100 physical cards: 84 library, nine distinct other grave cards,
    one Freeze (grave), one Oracle (grave), one LED (battlefield), one Breach
    (battlefield), two tapped lands and one command-zone Marchesa = 100.
    Breach's 1R was paid by those two lands; initial prior spell count is one.
    """
    assert 84 + 9 + 1 + 1 + 1 + 1 + 2 + 1 == 100
    op = list(opponents)
    mana_blue = 0
    prior_spells = 1  # Breach cast in this turn; LED was already in play.
    led_zone = "battlefield"
    freeze_zone = "graveyard"
    history = []
    for step in range(iterations):
        if not (breach and led and freeze) or opponent_removes_breach:
            break
        if step:
            if led_zone != "graveyard" or other_grave_cards < 3:
                break
            other_grave_cards -= 3  # One physical LED escaped, exiling others.
            led_zone = "battlefield"
            prior_spells += 1
        if led_zone != "battlefield" or freeze_zone != "graveyard":
            break
        led_zone = "graveyard"  # LED sac/discard hand; three blue, not 3 of each.
        mana_blue += 3
        if mana_blue < 2 or other_grave_cards < 3:
            break
        mana_blue -= 2  # Brain Freeze costs actual 1U, paid with blue.
        other_grave_cards -= 3  # Freeze's *other* card escape cost.
        freeze_zone = "stack"
        freeze_objects = prior_spells + 1  # Original plus actual storm copies.
        for _ in range(freeze_objects):
            if step < 5:
                mill = min(3, own_library)
                own_library -= mill
                other_grave_cards += mill  # Physical own cards enter our gy.
            else:
                target = max(range(len(op)), key=lambda idx: op[idx])
                mill = min(3, op[target])
                op[target] -= mill  # Opponent grave, NOT our escape fuel.
        freeze_zone = "graveyard"
        prior_spells += 1
        history.append({"storm_objects": freeze_objects,
                        "own_library": own_library, "opponents": tuple(op),
                        "other_grave_cards": other_grave_cards,
                        "blue": mana_blue, "led_zone": led_zone})
    return {"history": history, "own_library": own_library,
            "opponents": tuple(op), "other_grave_cards": other_grave_cards,
            "blue": mana_blue, "led_zone": led_zone}


def escape_oracle_after_self_mill(*, own_library=0, other_grave_cards=30,
                                  oracle_in_grave=True, led_in_grave=True,
                                  breach_present=True, oracle_trigger_resolves=True):
    """A real single Oracle from grave with 2U payment and six other exiles."""
    payable = (own_library == 0 and other_grave_cards >= 6 and oracle_in_grave
               and led_in_grave and breach_present)
    # Escape one real LED: exile 3, sacrifice for UUU; pay UU and exile 3
    # more distinct grave cards to escape Oracle. One blue remains floating.
    return {"payable": payable, "blue_remaining": 1 if payable else 0,
            "other_grave_remaining": other_grave_cards - 6 if payable else other_grave_cards,
            "oracle_win": bool(payable and oracle_trigger_resolves)}


class MarchesaDealerOriginalE2W2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in idx["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        assert raw.decode().splitlines()[0] == "1x Marchesa, Dealer of Death [Commander]"
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            count, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(count)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        assert receipt["m6_transfer"]["plan_blob_sha"] == PLAN_BLOB
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert {"E2", "W2"}.issubset(cls.deferred)
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as stream:
            for line in stream:
                oracle_row = json.loads(line)
                cls.oracle[oracle_row["canonical_name"]] = oracle_row["oracle_text"]

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_E2_seven_card_fast_mana_draw_has_real_imprint_land_and_payments(self):
        self.source("E2", "Mana Vault", "Chrome Mox", "Mox Diamond", "Lotus Petal",
                    "Dark Ritual", "Rhystic Study", "Mystic Remora", "Necropotence",
                    "Ad Nauseam", "City of Brass", "Badlands")
        self.assertIn("exile a nonartifact, nonland card", self.oracle["Chrome Mox"])
        self.assertIn("discard a land card", self.oracle["Mox Diamond"])
        self.assertIn("doesn't untap during your untap step", self.oracle["Mana Vault"])
        self.assertIn("Skip your draw step", self.oracle["Necropotence"])
        hand = ["City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond",
                "Badlands", "Mana Vault", "Ad Nauseam"]
        cast = vault_ad_nauseam_opening(hand)
        self.assertTrue(cast["cast"])
        self.assertEqual(cast["life_after_reveals"], 36)  # City 1 + reveal 2,1.
        self.assertEqual(cast["spent"][-2:], ("Chrome B", "Diamond B"))
        self.assertFalse(vault_ad_nauseam_opening(hand[:-1] + ["Lotus Petal"])["cast"])
        self.assertFalse(vault_ad_nauseam_opening(hand[:-2] + ["Brain Freeze", "Ad Nauseam"])["cast"])
        for permanent, paid in (("Mystic Remora", ("U",)),
                                ("Rhystic Study", ("U", "B", "B")),
                                ("Necropotence", ("B", "B", "B"))):
            h = ["City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond",
                 "Badlands", permanent, "Lotus Petal"]
            result = opening_mox_mana(h, permanent)
            self.assertTrue(result["cast"], permanent)
            self.assertEqual(result["mana_paid"], paid)
            self.assertEqual(result["land_plays"], 1)
            self.assertEqual(result["imprinted_exiled"], "Dark Ritual")
            self.assertEqual(result["diamond_land_discarded"], "Badlands")
        # Study/Remora depend on actual opponent choices; Remora only sees
        # opposing noncreature spells, and has cumulative upkeep later.
        self.assertEqual(enchantment_opponent_draw(spell="Rhystic Study"), 1)
        self.assertEqual(enchantment_opponent_draw(spell="Rhystic Study",
                                                  opponent_pays=True), 0)
        self.assertEqual(enchantment_opponent_draw(spell="Mystic Remora",
                                                  opponent_pays=True), 0)
        self.assertEqual(enchantment_opponent_draw(spell="Mystic Remora",
                                                  qualifying_cast=False), 0)
        invalid = ["City of Brass", "Chrome Mox", "Lion's Eye Diamond",
                   "Mox Diamond", "Badlands", "Necropotence", "Lotus Petal"]
        self.assertFalse(opening_mox_mana(invalid, "Necropotence")["cast"])
        invalid = ["City of Brass", "Chrome Mox", "Dark Ritual", "Mox Diamond",
                   "Brain Freeze", "Necropotence", "Lotus Petal"]
        self.assertFalse(opening_mox_mana(invalid, "Necropotence")["cast"])

    def test_W2_paid_led_breach_brain_freeze_and_oracle_conversion(self):
        self.source("W2", "Underworld Breach", "Lion's Eye Diamond",
                    "Lotus Petal", "Brain Freeze", "Thassa's Oracle")
        self.assertIn("exile three other cards", self.oracle["Underworld Breach"])
        self.assertIn("Storm", self.oracle["Brain Freeze"])
        self.assertIn("Discard your hand, Sacrifice", self.oracle["Lion's Eye Diamond"])
        self.assertIn("pay {1}", self.oracle["Marchesa, Dealer of Death"])
        trace = breach_led_brain_freeze()
        self.assertEqual(len(trace["history"]), 11)
        self.assertEqual([x["storm_objects"] for x in trace["history"]],
                         [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
        self.assertEqual(trace["own_library"], 0)
        self.assertEqual(trace["opponents"], (0, 0, 0))
        self.assertGreaterEqual(trace["other_grave_cards"], 6)
        self.assertEqual(trace["led_zone"], "graveyard")
        # Emptying opponent libraries alone does not make them lose right now.
        oracle = escape_oracle_after_self_mill(
            own_library=trace["own_library"],
            other_grave_cards=trace["other_grave_cards"])
        self.assertTrue(oracle["payable"])
        self.assertTrue(oracle["oracle_win"])
        self.assertEqual(oracle["blue_remaining"], 1)
        self.assertEqual(breach_led_brain_freeze(breach=False)["history"], [])
        self.assertEqual(breach_led_brain_freeze(led=False)["history"], [])
        self.assertEqual(breach_led_brain_freeze(freeze=False)["history"], [])
        self.assertEqual(breach_led_brain_freeze(other_grave_cards=2)["history"], [])
        self.assertEqual(breach_led_brain_freeze(opponent_removes_breach=True)["history"], [])
        self.assertFalse(escape_oracle_after_self_mill(own_library=1)["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(other_grave_cards=5)["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(oracle_trigger_resolves=False)["oracle_win"])
        # Re-escaping Petal alone gives only one mana per one-card escape; it
        # cannot source Brain Freeze's full {1}{U} without other real mana.
        self.assertFalse(petal_only_can_pay_brain_freeze())
        self.assertTrue(petal_only_can_pay_brain_freeze(other_generic=1))
        self.assertTrue(petal_only_can_pay_brain_freeze(other_blue=1))
        self.assertEqual(marchesa_crimes_for_freeze(
            original_targets_opponent=True, storm_copies=21), 1)
        self.assertEqual(marchesa_crimes_for_freeze(
            original_targets_opponent=False, storm_copies=21), 0)


if __name__ == "__main__":
    unittest.main()
