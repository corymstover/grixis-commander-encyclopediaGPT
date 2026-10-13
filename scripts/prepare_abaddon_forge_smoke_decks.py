#!/usr/bin/env python3
"""Prepare reproducible Forge deck-load smoke inputs from frozen Abaddon sources.

The generated decks are for simulator compatibility smoke tests only; they are
not evidence that one list is better or that Forge's AI estimates real-world win rate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
from pathlib import Path, PurePosixPath
from typing import Any


EXPECTED_BASELINE_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
COMMANDER = "Abaddon the Despoiler"


def parse_deck_text(text: str, source_label: str) -> tuple[dict[str, int], dict[str, Any]]:
    counts: dict[str, int] = {}
    commander_names: list[str] = []
    commander_copy_total = 0

    for line_number, raw in enumerate(text.lstrip("\ufeff").splitlines(), 1):
        line = raw.strip()
        match = re.match(r"^(\d+)x\s+(.+?)\s*$", line)
        if not match:
            continue
        qty = int(match.group(1))
        raw_name = match.group(2).strip()
        marked_commander = bool(re.search(r"\[Commander(?:\{[^}]*\})?\]", raw_name, re.I))
        name = re.sub(r"\s+\[.*\]\s*$", "", raw_name).strip()
        # Source exports encode printings as "Card Name (set) collector-number [Role]".
        name = re.sub(r"\s+\([^)]+\)\s+\S+\s*$", "", name).strip()
        # Forge's DCK resolver expects the primary/front-face name for transforming cards.
        name = name.split("//", 1)[0].strip()
        if not name:
            raise ValueError(f"{source_label}:{line_number}: empty parsed card name")
        counts[name] = counts.get(name, 0) + qty
        if marked_commander or name == COMMANDER:
            commander_names.append(name)
            commander_copy_total += qty

    if not counts:
        raise ValueError(f"No quantity-prefixed deck cards found in {source_label}")
    if list(counts).count(COMMANDER) != 1 or counts.get(COMMANDER) != 1:
        raise ValueError(f"{source_label}: expected exactly one Abaddon the Despoiler")
    if sum(counts.values()) != 100:
        raise ValueError(f"{source_label}: expected 100 cards including commander, got {sum(counts.values())}")
    if commander_copy_total > 1:
        raise ValueError(f"{source_label}: multiple commander markings found")

    meta = {
        "line_copy_count": sum(counts.values()),
        "unique_front_face_names": len(counts),
        "commander": COMMANDER,
        "commander_copy_count": 1,
    }
    return counts, meta


def read_frozen_baseline(archive_path: Path) -> tuple[bytes, str]:
    with tarfile.open(archive_path, mode="r:gz") as archive:
        members = [
            member
            for member in archive.getmembers()
            if member.isfile() and PurePosixPath(member.name).name == "Abaddon_the_Despoiler.txt"
        ]
        if len(members) != 1:
            raise ValueError(
                f"Expected exactly one Abaddon_the_Despoiler.txt in {archive_path}; found {len(members)}"
            )
        stream = archive.extractfile(members[0])
        if stream is None:
            raise ValueError(f"Could not read {members[0].name} from {archive_path}")
        data = stream.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != EXPECTED_BASELINE_SHA256:
        raise ValueError(
            f"Frozen Abaddon baseline hash mismatch: expected {EXPECTED_BASELINE_SHA256}, got {actual}"
        )
    return data, actual


def write_dck(path: Path, display_name: str, counts: dict[str, int]) -> None:
    if counts.get(COMMANDER) != 1:
        raise ValueError(f"{display_name}: commander must occur exactly once")
    main_cards = {name: qty for name, qty in counts.items() if name != COMMANDER}
    lines = [
        "[metadata]",
        f"Name={display_name}",
        "[Commander]",
        f"1 {COMMANDER}",
        "[Main]",
    ]
    lines.extend(f"{qty} {name}" for name, qty in main_cards.items())
    lines.extend(["[Sideboard]", ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def prepare(archive: Path, variant_path: Path, output_dir: Path) -> dict[str, Any]:
    baseline_bytes, baseline_hash = read_frozen_baseline(archive)
    baseline_counts, baseline_meta = parse_deck_text(
        baseline_bytes.decode("utf-8-sig"), "frozen Abaddon baseline"
    )
    variant_bytes = variant_path.read_bytes()
    variant_hash = hashlib.sha256(variant_bytes).hexdigest()
    variant_counts, variant_meta = parse_deck_text(
        variant_bytes.decode("utf-8-sig"), str(variant_path)
    )

    # Guard the test fixture: exactly Aurora Phoenix in, Mind's Desire out.
    baseline_minus = {n: q for n, q in baseline_counts.items() if n not in variant_counts}
    variant_minus = {n: q for n, q in variant_counts.items() if n not in baseline_counts}
    if baseline_minus != {"Mind's Desire": 1} or variant_minus != {"Aurora Phoenix": 1}:
        raise ValueError(
            "Expected one exact comparison only: Mind's Desire OUT / Aurora Phoenix IN; "
            f"baseline-only={baseline_minus!r}, variant-only={variant_minus!r}"
        )
    common = set(baseline_counts) & set(variant_counts)
    if any(baseline_counts[n] != variant_counts[n] for n in common):
        raise ValueError("Test variant changed a common card quantity")

    # Preserve the frozen baseline's main-deck order in both decks. Put Aurora Phoenix
    # in Mind's Desire's exact slot so identical RNG seeds operate on aligned deck positions.
    # Forge may still consume randomness differently during a game; this only controls input order.
    ordered_variant_counts: dict[str, int] = {}
    for name in baseline_counts:
        if name == "Mind's Desire":
            ordered_variant_counts["Aurora Phoenix"] = variant_counts["Aurora Phoenix"]
        elif name in variant_counts:
            ordered_variant_counts[name] = variant_counts[name]
    if set(ordered_variant_counts) != set(variant_counts):
        raise ValueError(
            "Could not align variant order to baseline; unplaced names: "
            f"{set(variant_counts) - set(ordered_variant_counts)!r}"
        )
    baseline_order = [name for name in baseline_counts if name != COMMANDER]
    variant_order = [name for name in ordered_variant_counts if name != COMMANDER]
    expected_order = [
        "Aurora Phoenix" if name == "Mind's Desire" else name
        for name in baseline_order
    ]
    if variant_order != expected_order:
        raise ValueError("Paired-input card order mismatch beyond the registered one-card substitution")

    write_dck(output_dir / "Abaddon baseline.dck", "Abaddon frozen baseline", baseline_counts)
    write_dck(output_dir / "Abaddon Aurora Phoenix variant.dck", "Abaddon Aurora Phoenix test variant", ordered_variant_counts)

    report = {
        "purpose": "one-game Forge deck-load/runtime smoke test only; no comparative performance claim",
        "frozen_baseline_archive": str(archive),
        "frozen_baseline_sha256": baseline_hash,
        "variant_file": str(variant_path),
        "variant_sha256": variant_hash,
        "comparison": {"removed": baseline_minus, "added": variant_minus},
        "paired_input_order": {
            "baseline_main_card_order": baseline_order,
            "variant_main_card_order": variant_order,
            "differences": [
                {"slot": baseline_order.index("Mind's Desire"), "baseline": "Mind's Desire", "variant": "Aurora Phoenix"}
            ],
            "all_other_slots_aligned": True,
            "limitation": "Input order is aligned for equal seeds, but runtime RNG-stream equivalence and identical opening hands are not yet independently verified."
        },
        "baseline": baseline_meta,
        "variant": variant_meta,
        "dck_files": ["Abaddon baseline.dck", "Abaddon Aurora Phoenix variant.dck"],
    }
    (output_dir / "smoke-deck-manifest.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--variant", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    report = prepare(args.archive, args.variant, args.output_dir)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
