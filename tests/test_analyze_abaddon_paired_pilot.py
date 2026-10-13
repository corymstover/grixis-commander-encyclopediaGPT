import unittest

from scripts.analyze_abaddon_paired_pilot import (
    BASELINE_LABEL,
    VARIANT_LABEL,
    summarize_game_log,
)


class PairedPilotLogSummaryTests(unittest.TestCase):
    def test_baseline_log_extracts_abaddon_cascade_turn_and_outcome(self):
        target = f"Ai(1)-{BASELINE_LABEL}"
        log = "\n".join([
            f"Turn: Turn 1 ({target})",
            f"Add To Stack: {target} cast Sol Ring",
            "Turn: Turn 2 (Ai(2)-Ruthless Regiment fixed opponent)",
            f"Turn: Turn 3 ({target})",
            f"Add To Stack: {target} cast Abaddon the Despoiler",
            f"Resolve Stack: Cascade - Rakdos, Lord of Riots [Card: Rakdos, Lord of Riots (7), Activator: {target}, SpellAbility: Rakdos]",
            "Game Outcome: Turn 9",
            f"Game Result: Game 1 ended in 12345 ms. {target} has won!",
        ])
        result = summarize_game_log(log, BASELINE_LABEL)
        self.assertEqual(result["outcome"], "TARGET_WIN")
        self.assertEqual(result["abaddon_first_cast_own_turn"], 2)
        self.assertEqual(result["abaddon_cascade_resolutions_observed"], 1)
        self.assertEqual(result["abaddon_cascade_resolutions_by_own_turn_6"], 1)
        self.assertEqual(result["game_duration_ms"], 12345)
        self.assertEqual(result["candidate_card"], "Mind's Desire")
        self.assertIsNone(result["candidate_first_cast_own_turn"])

    def test_variant_log_detects_aurora_cast_and_trigger(self):
        target = f"Ai(1)-{VARIANT_LABEL}"
        log = "\n".join([
            f"Turn: Turn 1 ({target})",
            f"Add To Stack: {target} cast Abaddon the Despoiler",
            f"Turn: Turn 3 ({target})",
            f"Add To Stack: {target} cast Aurora Phoenix",
            f"Add To Stack: {target} triggered Aurora Phoenix",
            f"Resolve Stack: Whenever you cast a spell with cascade, return Aurora Phoenix from your graveyard to your hand. [Activator: {target}]",
            f"Game Result: Game 1 ended in 23456 ms. {target} has won!",
        ])
        result = summarize_game_log(log, VARIANT_LABEL)
        self.assertEqual(result["outcome"], "TARGET_WIN")
        self.assertEqual(result["abaddon_first_cast_own_turn"], 1)
        self.assertEqual(result["candidate_first_cast_own_turn"], 2)
        self.assertTrue(result["candidate_cast_by_own_turn_6"])
        self.assertEqual(result["aurora_trigger_line_count"], 1)
        self.assertEqual(result["aurora_return_resolution_line_count"], 1)

    def test_draw_result_is_not_mistaken_for_a_win(self):
        target = f"Ai(1)-{BASELINE_LABEL}"
        log = "\n".join([
            f"Turn: Turn 1 ({target})",
            "Stopping slow match as draw.",
            "Game Result: Game 1 ended in a Draw! Took 20000 ms.",
        ])
        result = summarize_game_log(log, BASELINE_LABEL)
        self.assertEqual(result["outcome"], "DRAW")
        self.assertEqual(result["game_duration_ms"], 20000)
        self.assertTrue(result["runtime_warning_lines"])


if __name__ == "__main__":
    unittest.main()
