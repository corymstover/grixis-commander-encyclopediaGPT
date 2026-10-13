#!/usr/bin/env python3
"""Summarize unpaired same-seed Forge logs; pilot outcomes cannot decide card choice."""
from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
from collections import Counter
from pathlib import Path
from typing import Any


BASELINE_LABEL = "Abaddon frozen baseline"
VARIANT_LABEL = "Abaddon Aurora Phoenix test variant"
OPPONENT_LABEL = "Ruthless Regiment fixed opponent"
PLAYER_LABELS = (
    "Ai(1)-Abaddon frozen baseline",
    "Ai(2)-Abaddon Aurora Phoenix test variant",
    "Ai(2)-Ruthless Regiment fixed opponent",
)


def strip_player_labels(line: str) -> str:
    """Remove player display names so a name embedded in a label is not a card event."""
    for player_label in PLAYER_LABELS:
        line = line.replace(player_label, "PLAYER")
    return line
ERROR_PATTERNS = (
    "Could not load deck",
    "No deck found",
    "Unknown card",
    "StackOverflowError",
    "Exception in thread",
)


def summarize_game_log(log_text: str, target_label: str) -> dict[str, Any]:
    target_name = f"Ai(1)-{target_label}"
    target_turn = 0
    current_is_target_turn = False
    all_turn_count = 0
    target_turn_count = 0
    cast_events: list[dict[str, Any]] = []
    cascade_turns: list[int | None] = []
    aurora_trigger_lines: list[str] = []
    aurora_return_lines: list[str] = []
    mind_desire_copy_lines: list[str] = []
    life_loss_lines: list[str] = []
    land_play_count = 0
    outcome = "UNKNOWN"
    duration_ms: int | None = None
    round_turn: int | None = None

    for raw_line in log_text.splitlines():
        line = re.sub(r"\x1b\[[0-9;]*m", "", raw_line).strip()
        # Forge CLI logs prefix engine events with a wall-clock timestamp and [INFO].
        # Strip those prefixes before matching, while retaining untouched raw logs in artifacts.
        line = re.sub(r"^\d{4}-\d\d-\d\dT[^\s]+Z\s*", "", line)
        line = re.sub(r"^\d{2}:\d{2}:\d{2}\s+\[INFO\s*\]\s*", "", line)
        turn_match = re.match(r"^Turn:\s+Turn\s+(\d+)\s+\((.+)\)$", line)
        if turn_match:
            all_turn_count += 1
            current_is_target_turn = turn_match.group(2) == target_name
            if current_is_target_turn:
                target_turn += 1
                target_turn_count += 1
            continue

        if line.startswith(f"Add To Stack: {target_name} cast "):
            card_text = line.split(f"Add To Stack: {target_name} cast ", 1)[1]
            card_name = re.split(r"\s+targeting\s+", card_text, maxsplit=1)[0].strip()
            cast_events.append({
                "card": card_name,
                "target_own_turn": target_turn if current_is_target_turn else None,
                "on_target_own_turn": current_is_target_turn,
                "line": line,
            })

        if line.startswith("Resolve Stack: Cascade - ") and f"Activator: {target_name}" in line:
            cascade_turns.append(target_turn if current_is_target_turn else None)

        event_line = strip_player_labels(line)
        if "triggered Aurora Phoenix" in event_line:
            aurora_trigger_lines.append(line)
        if "Aurora Phoenix" in event_line and "Resolve Stack:" in line and (
            "graveyard" in event_line.casefold() or "hand" in event_line.casefold()
        ):
            aurora_return_lines.append(line)
        if "Mind's Desire" in line and re.search(r"\b(copy|copies|copied|storm)\b", line, re.I):
            mind_desire_copy_lines.append(line)
        if line.startswith("Life: Life: ") and " > " in line:
            life_loss_lines.append(line)

        if line.startswith(f"Land: {target_name} played "):
            land_play_count += 1

        if line.startswith("Game Outcome: Turn "):
            match = re.search(r"Game Outcome: Turn\s+(\d+)", line)
            if match:
                round_turn = int(match.group(1))

        if "Game Result: Game 1 ended in a Draw" in line:
            outcome = "DRAW"
            match = re.search(r"Took\s+([\d,]+)\s+ms", line)
            if match:
                duration_ms = int(match.group(1).replace(",", ""))
        elif "Game Result: Game 1 ended in " in line and " has won!" in line:
            outcome = "TARGET_WIN" if target_name + " has won!" in line else "OPPONENT_WIN"
            match = re.search(r"ended in\s+([\d,]+)\s+ms", line)
            if match:
                duration_ms = int(match.group(1).replace(",", ""))

    # Forge can print a nominal winner after its simulation clock stopped the match as a draw.
    # The explicit timeout marker is authoritative for this diagnostic report.
    if any("Stopping slow match as draw" in line for line in log_text.splitlines()):
        outcome = "DRAW"

    cast_names = [event["card"] for event in cast_events]

    def first_cast(card_name: str) -> int | None:
        for event in cast_events:
            if event["card"].casefold() == card_name.casefold():
                return event["target_own_turn"]
        return None

    target_candidate = "Aurora Phoenix" if target_label == VARIANT_LABEL else "Mind's Desire"
    own_turn_spell_counts = Counter(
        event["target_own_turn"] for event in cast_events
        if event["on_target_own_turn"] and event["target_own_turn"] is not None
    )
    own_turn_spell_counts_by_turn = {int(k): v for k, v in own_turn_spell_counts.items()}
    nonland_cast_count = len(cast_events)
    combo_cards = ["Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"]
    combo_cards_seen = [card for card in combo_cards if any(
        cast.casefold() == card.casefold() for cast in cast_names
    )]

    return {
        "target_label": target_label,
        "opponent": OPPONENT_LABEL,
        "outcome": outcome,
        "game_duration_ms": duration_ms,
        "game_outcome_turn_value": round_turn,
        "target_own_turns_played": target_turn_count,
        "all_player_turn_segments": all_turn_count,
        "land_plays": land_play_count,
        "target_nonland_spell_cast_count": nonland_cast_count,
        "abaddon_first_cast_own_turn": first_cast("Abaddon the Despoiler"),
        "candidate_card": target_candidate,
        "candidate_first_cast_own_turn": first_cast(target_candidate),
        "candidate_cast_by_own_turn_6": (
            first_cast(target_candidate) is not None and first_cast(target_candidate) <= 6
        ),
        "candidate_cast_by_own_turn_8": (
            first_cast(target_candidate) is not None and first_cast(target_candidate) <= 8
        ),
        "abaddon_cascade_resolutions_observed": len(cascade_turns),
        "abaddon_cascade_resolutions_by_own_turn_6": sum(
            turn is not None and turn <= 6 for turn in cascade_turns
        ),
        "abaddon_cascade_resolutions_by_own_turn_8": sum(
            turn is not None and turn <= 8 for turn in cascade_turns
        ),
        "aurora_trigger_line_count": len(aurora_trigger_lines),
        "aurora_return_resolution_line_count": len(aurora_return_lines),
        "mind_desire_copy_or_storm_line_count": len(mind_desire_copy_lines),
        "underworld_breach_led_brain_freeze_cast_set": combo_cards_seen,
        "all_three_breach_combo_cards_cast": len(combo_cards_seen) == 3,
        "target_own_turns_without_logged_nonland_cast": [
            turn for turn in range(1, target_turn_count + 1)
            if own_turn_spell_counts_by_turn.get(turn, 0) == 0
        ],
        "life_change_event_line_count": len(life_loss_lines),
        "runtime_warning_lines": [
            line for line in log_text.splitlines()
            if any(pattern.casefold() in line.casefold() for pattern in ERROR_PATTERNS)
            or "Stopping slow match as draw" in line
        ],
        "raw_relevant_lines": {
            "abaddon_cast": [line for line in log_text.splitlines() if "cast Abaddon the Despoiler" in line],
            "cascade_resolutions": [line for line in log_text.splitlines() if "Resolve Stack: Cascade -" in line],
            "aurora": [line for line in log_text.splitlines() if "Aurora Phoenix" in strip_player_labels(line)],
            "mind_desire": [line for line in log_text.splitlines() if "Mind's Desire" in line],
            "breach_combo": [line for line in log_text.splitlines() if any(card in line for card in combo_cards)],
        },
    }


def _mean_if_values(values: list[float]) -> float | None:
    return round(statistics.mean(values), 3) if values else None


def _median_if_values(values: list[float]) -> float | None:
    return round(statistics.median(values), 3) if values else None


def summarize_group(games: list[dict[str, Any]]) -> dict[str, Any]:
    outcomes = Counter(game["outcome"] for game in games)
    abaddon_turns = [
        game["abaddon_first_cast_own_turn"] for game in games
        if game["abaddon_first_cast_own_turn"] is not None
    ]
    candidate_turns = [
        game["candidate_first_cast_own_turn"] for game in games
        if game["candidate_first_cast_own_turn"] is not None
    ]
    return {
        "games": len(games),
        "outcomes": dict(outcomes),
        "target_win_rate": round(outcomes.get("TARGET_WIN", 0) / len(games), 3) if games else None,
        "draw_rate": round(outcomes.get("DRAW", 0) / len(games), 3) if games else None,
        "abaddon_cast_games": len(abaddon_turns),
        "abaddon_mean_own_turn_when_cast": _mean_if_values(abaddon_turns),
        "abaddon_median_own_turn_when_cast": _median_if_values(abaddon_turns),
        "candidate_cast_games": len(candidate_turns),
        "candidate_cast_fraction": round(len(candidate_turns) / len(games), 3) if games else None,
        "candidate_mean_own_turn_when_cast": _mean_if_values(candidate_turns),
        "candidate_median_own_turn_when_cast": _median_if_values(candidate_turns),
        "mean_cascade_resolutions": _mean_if_values([
            float(game["abaddon_cascade_resolutions_observed"]) for game in games
        ]),
        "games_with_aurora_trigger": sum(game["aurora_trigger_line_count"] > 0 for game in games),
        "games_with_mind_desire_copy_or_storm_line": sum(
            game["mind_desire_copy_or_storm_line_count"] > 0 for game in games
        ),
        "games_with_all_three_breach_combo_cards_cast": sum(
            game["all_three_breach_combo_cards_cast"] for game in games
        ),
        "games_with_runtime_warnings": sum(bool(game["runtime_warning_lines"]) for game in games),
    }


def analyze(pilot_dir: Path) -> dict[str, Any]:
    manifest_path = pilot_dir / "same-seed-run-manifest.csv"
    with manifest_path.open(newline="", encoding="utf-8-sig") as handle:
        trials = list(csv.DictReader(handle))
    if not trials:
        raise ValueError("Same-seed run manifest is empty")

    baseline_games: list[dict[str, Any]] = []
    variant_games: list[dict[str, Any]] = []
    paired_rows: list[dict[str, Any]] = []

    for trial in trials:
        seed = int(trial["seed"])
        baseline_text = (pilot_dir / trial["baseline_log"]).read_text(encoding="utf-8", errors="replace")
        variant_text = (pilot_dir / trial["variant_log"]).read_text(encoding="utf-8", errors="replace")
        baseline_result = summarize_game_log(baseline_text, BASELINE_LABEL)
        variant_result = summarize_game_log(variant_text, VARIANT_LABEL)
        baseline_result["seed"] = seed
        variant_result["seed"] = seed
        baseline_games.append(baseline_result)
        variant_games.append(variant_result)
        paired_rows.append({
            "trial_index": int(trial["trial_index"]),
            "seed": seed,
            "baseline_outcome": baseline_result["outcome"],
            "variant_outcome": variant_result["outcome"],
            "baseline_abaddon_cast_turn": baseline_result["abaddon_first_cast_own_turn"],
            "variant_abaddon_cast_turn": variant_result["abaddon_first_cast_own_turn"],
            "baseline_candidate_cast_turn": baseline_result["candidate_first_cast_own_turn"],
            "variant_candidate_cast_turn": variant_result["candidate_first_cast_own_turn"],
            "baseline_cascade_resolutions": baseline_result["abaddon_cascade_resolutions_observed"],
            "variant_cascade_resolutions": variant_result["abaddon_cascade_resolutions_observed"],
            "baseline_aurora_return_lines": baseline_result["aurora_return_resolution_line_count"],
            "variant_aurora_return_lines": variant_result["aurora_return_resolution_line_count"],
            "baseline_mind_desire_copy_or_storm_lines": baseline_result["mind_desire_copy_or_storm_line_count"],
            "variant_mind_desire_copy_or_storm_lines": variant_result["mind_desire_copy_or_storm_line_count"],
            "baseline_all_breach_pieces_cast": baseline_result["all_three_breach_combo_cards_cast"],
            "variant_all_breach_pieces_cast": variant_result["all_three_breach_combo_cards_cast"],
        })

    outcomes_match = sum(row["baseline_outcome"] == row["variant_outcome"] for row in paired_rows)
    report = {
        "status": "SAME-SEED PILOT COMPLETE — UNPAIRED DESCRIPTIVE ONLY; DO NOT USE TO APPROVE A CARD SWAP",
        "engine": "Forge forge-2.0.15",
        "opponent": OPPONENT_LABEL,
        "comparison_design": "same numeric seed values and same fixed opponent/seat order, but UNPAIRED by initial library order; Forge Deck/CardPool iteration is not order-preserving",
        "trials_per_list": len(trials),
        "baseline": summarize_group(baseline_games),
        "variant": summarize_group(variant_games),
        "same_seed_outcomes": {
            "same_outcome_seed_labels": outcomes_match,
            "different_outcome_seed_labels": len(paired_rows) - outcomes_match,
            "interpretation": "Baseline and variant use the same numeric seed values, but their starting libraries are not proven aligned. Descriptive AI-play only, not real-world win-rate evidence or a paired confirmatory test."
        },
        "decision_use_allowed": False,
        "limitations": [
            "Forge AI has documented limitations on combo decks.",
            "The pilot may not exercise Aurora Phoenix or Mind's Desire often enough to compare their value; candidate cast frequency is reported explicitly.",
            "The event parser is a first-pass text-log summary; raw per-game logs are preserved for manual audit.",
            "The pilot tests one fixed opponent in two-player Commander, not a representative multiplayer pod.",
            "No card substitution is approved or applied by this report."
        ],
        "games": {"baseline": baseline_games, "variant": variant_games},
        "same_seed_comparison_rows": paired_rows,
    }

    (pilot_dir / "pilot-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    with (pilot_dir / "same-seed-results-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(paired_rows[0].keys()))
        writer.writeheader()
        writer.writerows(paired_rows)

    md = [
        "# Abaddon Same-Seed Forge Pilot — Unpaired, Descriptive Only",
        "",
        f"- Same-seed trials per list: {len(trials)}",
        f"- Opponent: {OPPONENT_LABEL}",
        "- Same numeric seeds and seat order per trial; starting hands/library order are NOT guaranteed matched by Forge.",
        "- This does not decide the Aurora Phoenix vs Mind's Desire slot.",
        "",
        "## Baseline summary",
        "",
        "~~~json",
        json.dumps(report["baseline"], indent=2),
        "~~~",
        "",
        "## Aurora Phoenix variant summary",
        "",
        "~~~json",
        json.dumps(report["variant"], indent=2),
        "~~~",
        "",
        "## Same-seed outcome labels (not matched-start pairs)",
        "",
        f"- Same-outcome seed labels: {outcomes_match}/{len(trials)}",
        f"- Different-outcome seed labels: {len(trials) - outcomes_match}/{len(trials)}",
        "",
        "## Interpretation control",
        "",
        "This is a pilot used to assess instrumentation and estimate variability only. Forge AI results are conditional on its heuristics. Do not use this report to approve or reject the card swap; the exact Oracle/rules interactions and final decision gate remain separate.",
        "",
    ]
    (pilot_dir / "pilot-summary.md").write_text("\n".join(md), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot-dir", type=Path, required=True)
    args = parser.parse_args()
    report = analyze(args.pilot_dir)
    print(json.dumps({
        "status": report["status"],
        "trials_per_list": report["trials_per_list"],
        "baseline": report["baseline"],
        "variant": report["variant"],
        "same_seed_outcomes": report["same_seed_outcomes"],
        "decision_use_allowed": report["decision_use_allowed"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
