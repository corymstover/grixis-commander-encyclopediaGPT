#!/usr/bin/env python3
"""Exact hypergeometric baseline consistency analysis for Abaddon the Despoiler.

This is a transparent card-density calculation, not a game simulator. It does not
model mulligans, color requirements, sequencing, tutors, extra draw, or card text
beyond the explicitly declared early-acceleration set.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_PATH = ROOT / "source-package" / "GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
ARCHIVE_SHA256 = "f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20"
BASELINE_TXT_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
DECK_MEMBER_SUFFIX = "TXT/Abaddon_the_Despoiler.txt"
EARLY_ACCELERATION = {
    "arcane signet",
    "cabal ritual",
    "chrome mox",
    "dark ritual",
    "lion's eye diamond",
    "lotus petal",
    "mana vault",
    "rite of flame",
    "sol ring",
    "talisman of creativity",
    "talisman of dominance",
    "talisman of indulgence",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_baseline_from_archive(path: Path = ARCHIVE_PATH) -> bytes:
    raw = path.read_bytes()
    actual = sha256(raw)
    if actual != ARCHIVE_SHA256:
        raise ValueError(f"Baseline archive SHA-256 mismatch: {actual}")
    with tarfile.open(path, "r:gz") as archive:
        matches = [
            member for member in archive.getmembers()
            if member.isfile() and member.name.replace("\\\\", "/").endswith(DECK_MEMBER_SUFFIX)
        ]
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one {DECK_MEMBER_SUFFIX} member; found {len(matches)}")
        stream = archive.extractfile(matches[0])
        if stream is None:
            raise ValueError("Could not read Abaddon baseline TXT member")
        return stream.read()


def parse_deck_text(text: str) -> tuple[Counter[str], Counter[str], Counter[str]]:
    """Return card counts, role-tag copy counts, and commander copy counts."""
    cards: Counter[str] = Counter()
    roles: Counter[str] = Counter()
    commanders: Counter[str] = Counter()
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        qty_match = re.match(r"^(\d+)x\s+(.+)$", line)
        if not qty_match:
            raise ValueError(f"Line {line_number}: invalid decklist line: {line!r}")
        quantity = int(qty_match.group(1))
        body = qty_match.group(2).strip()
        tag_match = re.search(r"\[([^\]]+)\]\s*$", body)
        if not tag_match:
            raise ValueError(f"Line {line_number}: missing final role tag: {line!r}")
        role = tag_match.group(1).strip()
        body = body[:tag_match.start()].strip()
        card_name = re.sub(r"\s+\([^)]+\)\s+\S+\s*$", "", body).strip()
        if quantity <= 0 or not card_name:
            raise ValueError(f"Line {line_number}: invalid quantity or card name")
        cards[card_name] += quantity
        roles[role] += quantity
        if role.lower().startswith("commander"):
            commanders[card_name] += quantity
    return cards, roles, commanders


def probability_at_least(total: int, category: int, draws: int, minimum: int) -> float:
    if not (0 <= category <= total and 0 <= draws <= total and 0 <= minimum <= draws):
        raise ValueError("Invalid hypergeometric parameters")
    denominator = math.comb(total, draws)
    numerator = sum(
        math.comb(category, k) * math.comb(total - category, draws - k)
        for k in range(minimum, min(category, draws) + 1)
        if 0 <= draws - k <= total - category
    )
    return numerator / denominator


def probability_joint_lands_and_acceleration(
    total: int, lands: int, accelerants: int, draws: int, minimum_lands: int
) -> float:
    """P(at least minimum_lands lands and >=1 early accelerant), disjoint groups."""
    if lands + accelerants > total:
        raise ValueError("Land and acceleration categories must be disjoint")
    other = total - lands - accelerants
    denominator = math.comb(total, draws)
    numerator = 0
    for land_count in range(minimum_lands, min(lands, draws) + 1):
        for accel_count in range(1, min(accelerants, draws - land_count) + 1):
            other_count = draws - land_count - accel_count
            if 0 <= other_count <= other:
                numerator += (
                    math.comb(lands, land_count)
                    * math.comb(accelerants, accel_count)
                    * math.comb(other, other_count)
                )
    return numerator / denominator


def analyze(text_bytes: bytes) -> dict:
    actual_txt_hash = sha256(text_bytes)
    if actual_txt_hash != BASELINE_TXT_SHA256:
        raise ValueError(f"Abaddon baseline TXT SHA-256 mismatch: {actual_txt_hash}")
    text = text_bytes.decode("utf-8-sig")
    cards, roles, commanders = parse_deck_text(text)
    total_copies = sum(cards.values())
    commander_copies = sum(commanders.values())
    if total_copies != 100 or commander_copies != 1:
        raise ValueError(f"Expected 100 total cards including one commander; got {total_copies} and {commander_copies}")
    library_size = total_copies - commander_copies
    land_count = roles["Land"]
    ramp_tag_count = roles["Ramp"]
    early_names_present = {
        name.casefold() for name in cards
        if name.casefold() in EARLY_ACCELERATION
    }
    missing_early = sorted(EARLY_ACCELERATION - early_names_present)
    if missing_early:
        raise ValueError(f"Declared early acceleration cards absent from baseline: {missing_early}")
    for card_name in cards:
        if card_name.casefold() in EARLY_ACCELERATION:
            matching_lines = [
                line for line in text.splitlines()
                if line.strip().startswith("1x ") and card_name.casefold() in line.casefold()
            ]
            if not matching_lines or not any(re.search(r"\[Ramp\]\s*$", line) for line in matching_lines):
                raise ValueError(f"Declared early accelerator is not explicitly tagged Ramp: {card_name}")
    early_count = len(early_names_present)
    if land_count != 34 or ramp_tag_count != 19 or early_count != 12:
        raise ValueError(
            f"Unexpected category counts: lands={land_count}, Ramp-tagged={ramp_tag_count}, "
            f"early accelerants={early_count}"
        )
    metrics = {}
    for draws in (7, 10, 12):
        metrics[str(draws)] = {
            "at_least_2_lands": probability_at_least(library_size, land_count, draws, 2),
            "at_least_3_lands": probability_at_least(library_size, land_count, draws, 3),
            "at_least_4_lands": probability_at_least(library_size, land_count, draws, 4),
            "at_least_1_early_accelerant": probability_at_least(library_size, early_count, draws, 1),
            "at_least_2_lands_and_1_early_accelerant": probability_joint_lands_and_acceleration(
                library_size, land_count, early_count, draws, 2
            ),
            "at_least_3_lands_and_1_early_accelerant": probability_joint_lands_and_acceleration(
                library_size, land_count, early_count, draws, 3
            ),
            "at_least_4_lands_and_1_early_accelerant": probability_joint_lands_and_acceleration(
                library_size, land_count, early_count, draws, 4
            ),
        }
    opening_land_distribution = {
        str(k): math.comb(land_count, k) * math.comb(library_size - land_count, 7 - k)
        / math.comb(library_size, 7)
        for k in range(0, 5)
    }
    opening_land_distribution["5+"] = sum(
        math.comb(land_count, k) * math.comb(library_size - land_count, 7 - k)
        / math.comb(library_size, 7)
        for k in range(5, min(land_count, 7) + 1)
    )
    return {
        "deck_id": "Abaddon_the_Despoiler",
        "baseline_txt_sha256": actual_txt_hash,
        "total_cards_including_commander": total_copies,
        "library_size_excluding_commander": library_size,
        "land_copies": land_count,
        "ramp_tagged_copies": ramp_tag_count,
        "explicit_early_acceleration_copies": early_count,
        "explicit_early_acceleration_names": sorted(early_names_present),
        "opening_7_land_count_distribution": opening_land_distribution,
        "metrics_by_cards_seen": metrics,
        "method": "Exact hypergeometric probabilities without replacement from the 99-card library.",
        "limitations": [
            "No mulligan policy or keep decisions modeled.",
            "No mana-color, tapped-land, sequencing, cost-reduction, or acceleration usability model.",
            "No tutors, extra draw, or card-specific draw triggers modeled.",
            "Early acceleration is a declared 12-card set; Cabal Ritual is conditional on available mana/graveyard state and Chrome Mox/Lion's Eye Diamond have meaningful costs.",
            "This is a descriptive baseline consistency benchmark, not a deck-quality score, gameplay result, or pass/fail threshold."
        ],
    }


def render_markdown(result: dict) -> str:
    metrics = result["metrics_by_cards_seen"]
    def pct(value: float) -> str:
        return f"{value * 100:.2f}%"
    lines = [
        "# Abaddon the Despoiler — Baseline Consistency Analysis",
        "",
        "**Snapshot:** 2026-10-13 UTC  ",
        "**Status:** DESCRIPTIVE BASELINE ONLY — not a gameplay simulation or finalization gate  ",
        f"**Frozen baseline TXT SHA-256:** {result['baseline_txt_sha256']}",
        "",
        "## Verified deck composition",
        "",
        f"- Main deck plus commander: **{result['total_cards_including_commander']} cards**.",
        f"- Library after setting commander aside: **{result['library_size_excluding_commander']} cards**.",
        f"- Lands: **{result['land_copies']}**.",
        f"- Cards tagged Ramp in the source list: **{result['ramp_tagged_copies']}**.",
        f"- Explicit early-acceleration set: **{result['explicit_early_acceleration_copies']} cards**.",
        "",
        "The early-acceleration set is Arcane Signet, Cabal Ritual, Chrome Mox, Dark Ritual, Lion's Eye Diamond, Lotus Petal, Mana Vault, Rite of Flame, Sol Ring, and the three Talismans. This is a transparent classification for a first-pass density check, not a claim that all twelve are equally reliable or always usable.",
        "",
        "## Exact draw-density probabilities",
        "",
        "These probabilities sample cards without replacement from the 99-card library. Seven cards means the un-mulliganed opening hand; ten cards means opening seven plus three draw steps; twelve means opening seven plus five draw steps. Extra draw, tutors, mulligans, sequencing, and mana colors are not modeled.",
        "",
        "| Cards seen | At least 2 lands | At least 3 lands | At least 1 early accelerator | At least 2 lands + 1 accelerator | At least 3 lands + 1 accelerator | At least 4 lands + 1 accelerator |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for n in (7, 10, 12):
        m = metrics[str(n)]
        lines.append(
            f"| {n} | {pct(m['at_least_2_lands'])} | {pct(m['at_least_3_lands'])} | "
            f"{pct(m['at_least_1_early_accelerant'])} | "
            f"{pct(m['at_least_2_lands_and_1_early_accelerant'])} | "
            f"{pct(m['at_least_3_lands_and_1_early_accelerant'])} | "
            f"{pct(m['at_least_4_lands_and_1_early_accelerant'])} |"
        )
    lines += [
        "",
        "## Opening-hand land distribution",
        "",
        "| Lands in opening seven | Exact probability |",
        "|---:|---:|",
    ]
    dist = result["opening_7_land_count_distribution"]
    for key, value in dist.items():
        label = f"{key} lands" if key != "5+" else "5 or more lands"
        lines.append(f"| {label} | {pct(value)} |")
    lines += [
        "",
        "## Interpretation",
        "",
        "- The raw opening seven has at least two lands **76.46%** of the time and at least three lands **45.33%** of the time.",
        "- The opening seven contains at least two lands and at least one card from the declared early-acceleration set **43.49%** of the time.",
        "- By ten cards seen, the probability of at least three lands and at least one declared early accelerator is **52.30%**.",
        "- These are card-density probabilities, not the probability of casting Abaddon on a particular turn. The latter depends on colored sources, tapped lands, mulligans, sequencing, and the actual function of each accelerator.",
        "",
        "## Decision use",
        "",
        "Use this as a frozen-baseline reference for later deck-specific comparisons. Do not infer that the deck fails a target, that more lands are required, or that a candidate is an upgrade without a predeclared metric and a commander-specific reason. No decklist change is implied by this report.",
        "",
        "## Limitations",
        "",
    ]
    lines.extend(f"- {item}" for item in result["limitations"])
    lines += [
        "",
        "## Reproducibility",
        "",
        "Run python scripts/analyze_abaddon_baseline_consistency.py --report-output refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md in the repository. In archive mode, the script verifies the pinned compact-archive SHA-256 and the exact Abaddon TXT SHA-256 before calculating the probabilities.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--decklist", type=Path, help="Optional direct TXT input; exact frozen TXT hash is still required.")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--report-output", type=Path)
    args = parser.parse_args()
    raw = args.decklist.read_bytes() if args.decklist else read_baseline_from_archive()
    result = analyze(raw)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(encoded, encoding="utf-8")
    if args.report_output:
        args.report_output.parent.mkdir(parents=True, exist_ok=True)
        args.report_output.write_text(render_markdown(result), encoding="utf-8")
    if not args.json_output and not args.report_output:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
