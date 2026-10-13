# Abaddon Forge Qualification Update — 2026-10-13

## New verified evidence

GitHub Actions workflow [Probe Forge CLI distribution](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38331076831) completed successfully. It downloaded the official Forge `forge-2.0.15` desktop distribution archive, checked its SHA-256, and listed its entries without installing the engine or running games.

| Evidence | Result |
|---|---|
| Release archive | `forge-installer-2.0.15.tar.bz2` |
| Download size | 297,081,149 bytes |
| SHA-256 | `4468f182b60f6ca62d89697baa208981085af744f116781af751c611826db600` — matched |
| Archive member count | 22,241 |
| Runnable application entry | `forge-gui-desktop-2.0.15-jar-with-dependencies.jar` |
| Other jar entry | `forge-gui-mobile-dev-2.0.15-jar-with-dependencies.jar` |
| Engine launched | No |
| Exact Abaddon list loaded | No |
| Gameplay runs | 0 |

Workflow log: https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38331076831

## What this establishes

There is a reproducible, checksum-verified path to obtain the pinned Forge distribution on a GitHub-hosted Ubuntu runner. The archive contains the desktop runnable JAR and a substantial distribution tree. This is more than source-code browsing, but it is still only a distribution probe.

It does **not** establish that Forge has been installed or launched, that the exact deck can be imported, that all 94 unique card names resolve, that the target interactions work at runtime, or that seeded paired games and usable event logs can be collected.

## Revised next technical action

The next highest-value reversible step is a separate, explicitly scoped CI workflow that downloads the pinned archive with the verified checksum, extracts it in a temporary runner workspace, invokes the desktop JAR's documented headless/CLI entry point for a harmless version/help probe, then scans the extracted `res/cardsfolder` tree for all 94 deck names. The script audit should normalize split-face/DFC names and distinguish “script file found” from “expected Oracle behavior tested.” It should publish a machine-readable coverage report and fail on missing/ambiguous names, while preserving raw logs as an artifact. This step must not yet run Commander self-play or change any decklist.

Only after the CLI starts cleanly and card support coverage is reviewed should we attempt small runtime smoke tests for Abaddon-given cascade, Aurora's graveyard trigger/stack ordering, cascade-from-exile, storm-copy/cast distinctions, and the Breach/LED/Brain Freeze line. The paired-start protocol gate must be evaluated separately: documented repeat counts alone do not prove reproducible matching seeds or structured events.

## Status and invariants

- Forge remains **NOT QUALIFIED** for registered confirmatory gameplay testing.
- Aurora Phoenix remains **proposed for testing only**.
- The frozen Abaddon baseline and all approved decks remain unchanged.
- No gameplay simulations were run by this probe.
