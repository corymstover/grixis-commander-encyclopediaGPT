#!/usr/bin/env python3
"""Run same-seed, explicitly unpaired Forge Commander trials via Forge's supported CLI."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


FORGE_RELEASE = "forge-2.0.15"
FORGE_COMMIT = "4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676"
BASELINE_NAME = "Abaddon baseline.dck"
VARIANT_NAME = "Abaddon Aurora Phoenix variant.dck"
OPPONENT_NAME = "Ruthless Regiment.dck"
OPPONENT_LABEL = "Ruthless Regiment fixed opponent"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_command(
    java: str,
    jar: Path,
    deck_dir: Path,
    target_name: str,
    seed: int,
    timeout_seconds: int,
) -> list[str]:
    return [
        java, "-Djava.awt.headless=true", "-jar", str(jar), "sim",
        "-D", str(deck_dir.resolve()),
        "-d", target_name, OPPONENT_NAME,
        "-f", "Commander",
        "-n", "1",
        "-s", str(seed),
        "-c", str(timeout_seconds),
    ]


def run_game(
    command: list[str],
    output_path: Path,
    *,
    timeout_seconds: int,
    target_display_name: str,
) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        text = exc.stdout or ""
        if isinstance(text, bytes):
            text = text.decode("utf-8", errors="replace")
        output_path.write_text(text, encoding="utf-8")
        raise RuntimeError(f"Forge CLI process exceeded {timeout_seconds}s; see {output_path}") from exc

    output_path.write_text(proc.stdout, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError(
            f"Forge CLI returned exit code {proc.returncode}; see {output_path}"
        )
    if "Game Result: Game 1 ended" not in proc.stdout:
        raise RuntimeError(f"Forge CLI did not emit a completed Game Result; see {output_path}")

    if "Stopping slow match as draw" in proc.stdout:
        outcome = "DRAW"
    elif f"{target_display_name} has won!" in proc.stdout:
        outcome = "TARGET_WIN"
    elif " has won!" in proc.stdout:
        outcome = "OPPONENT_WIN"
    elif "Game Result: Game 1 ended in a Draw" in proc.stdout:
        outcome = "DRAW"
    else:
        outcome = "UNKNOWN"

    return {
        "outcome_detected_by_runner": outcome,
        "return_code": proc.returncode,
        "log_path": str(output_path),
        "log_sha256": sha256(output_path),
        "game_result_line": next(
            (line.strip() for line in proc.stdout.splitlines()
             if "Game Result: Game 1 ended" in line),
            None,
        ),
    }


def run_pilot(
    *,
    jar: Path,
    deck_dir: Path,
    output_dir: Path,
    java: str = "java",
    trials: int = 3,
    base_seed: int = 2026101300,
    timeout_seconds: int = 30,
) -> dict[str, Any]:
    if not jar.is_file():
        raise FileNotFoundError(f"Pinned Forge JAR not found: {jar}")
    if not 1 <= trials <= 25:
        raise ValueError("--trials must be between 1 and 25 for this exploratory workflow")
    if not 10 <= timeout_seconds <= 120:
        raise ValueError("--timeout-seconds must be between 10 and 120")

    required = [
        deck_dir / BASELINE_NAME,
        deck_dir / VARIANT_NAME,
        deck_dir / OPPONENT_NAME,
    ]
    for path in required:
        if not path.is_file():
            raise FileNotFoundError(f"Required DCK file not found: {path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    baseline_hash = sha256(deck_dir / BASELINE_NAME)
    variant_hash = sha256(deck_dir / VARIANT_NAME)
    opponent_hash = sha256(deck_dir / OPPONENT_NAME)

    rows: list[dict[str, Any]] = []
    baseline_results: list[dict[str, Any]] = []
    variant_results: list[dict[str, Any]] = []

    for trial_index in range(1, trials + 1):
        seed = base_seed + trial_index - 1
        baseline_log_name = f"seed-{seed}-baseline.log"
        variant_log_name = f"seed-{seed}-variant.log"
        baseline_display_name = "Ai(1)-Abaddon frozen baseline"
        variant_display_name = "Ai(1)-Abaddon Aurora Phoenix test variant"

        baseline_result = run_game(
            build_command(java, jar, deck_dir, BASELINE_NAME, seed, timeout_seconds),
            output_dir / baseline_log_name,
            timeout_seconds=timeout_seconds * 5 + 120,
            target_display_name=baseline_display_name,
        )
        variant_result = run_game(
            build_command(java, jar, deck_dir, VARIANT_NAME, seed, timeout_seconds),
            output_dir / variant_log_name,
            timeout_seconds=timeout_seconds * 5 + 120,
            target_display_name=variant_display_name,
        )

        baseline_results.append(baseline_result)
        variant_results.append(variant_result)
        rows.append({
            "trial_index": trial_index,
            "seed": seed,
            "baseline_log": baseline_log_name,
            "variant_log": variant_log_name,
            "opponent_label": OPPONENT_LABEL,
            "baseline_sha256": baseline_hash,
            "variant_sha256": variant_hash,
            "opponent_sha256": opponent_hash,
        })
        print(
            f"TRIAL {trial_index}/{trials} seed={seed} "
            f"baseline={baseline_result['outcome_detected_by_runner']} "
            f"variant={variant_result['outcome_detected_by_runner']}"
        )

    manifest_path = output_dir / "same-seed-run-manifest.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    manifest = {
        "forge_release": FORGE_RELEASE,
        "forge_source_commit": FORGE_COMMIT,
        "purpose": "same-seed but UNPAIRED exploratory CLI pilot; not a real-world win-rate estimate",
        "trials_per_list": trials,
        "base_seed": base_seed,
        "timeout_seconds_per_game": timeout_seconds,
        "baseline_dck_sha256": baseline_hash,
        "variant_dck_sha256": variant_hash,
        "opponent_dck_sha256": opponent_hash,
        "opponent": OPPONENT_LABEL,
        "same_numeric_seed_values_used_for_each_trial": True,
        "same_seat_order": True,
        "starting_hand_pairing": (
            "NOT GUARANTEED: pinned Forge Deck.normalizeDeferredSections converts deck text through "
            "CardPool.fromCardList and iterates ItemPool's unordered ConcurrentHashMap. Equal seed "
            "values therefore do not prove aligned opening hands or initial library order."
        ),
        "baseline_run_summaries": baseline_results,
        "variant_run_summaries": variant_results,
        "decision_use_allowed": False,
        "limitations": [
            "Only one fixed opponent deck and two-player Commander are used.",
            "Forge AI performance is conditional on its heuristics and is not real-world win-rate evidence.",
            "Same seed values are run in separate processes but starting libraries are not guaranteed matched.",
            "A pilot can validate instrumentation and reveal obvious engine/log issues only.",
            "No card substitution is approved or applied by this report.",
        ],
    }
    (output_dir / "same-seed-run-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--deck-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--java", default="java")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--base-seed", type=int, default=2026101300)
    parser.add_argument("--timeout-seconds", type=int, default=30)
    args = parser.parse_args()
    report = run_pilot(
        jar=args.jar,
        deck_dir=args.deck_dir,
        output_dir=args.output_dir,
        java=args.java,
        trials=args.trials,
        base_seed=args.base_seed,
        timeout_seconds=args.timeout_seconds,
    )
    print(json.dumps({
        "forge_release": report["forge_release"],
        "trials_per_list": report["trials_per_list"],
        "opponent": report["opponent"],
        "starting_hand_pairing": report["starting_hand_pairing"],
        "decision_use_allowed": report["decision_use_allowed"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
