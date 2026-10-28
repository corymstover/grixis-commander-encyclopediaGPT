"""PR-base preservation checks that recognize separately certified owner approvals.

An older deck's lock test must not prohibit a later, independently owner-approved
revision of a different deck. It must, however, fail for unapproved or
unattested changes to that other deck's source or authority metadata.
"""

import csv
import hashlib
import json
from pathlib import Path
import subprocess

from scripts import verify_m7_certification_transfer as transfer


def _from_base(root: Path, base: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{base}:{path}"], cwd=root, text=True
    )


def assert_other_decks_preserved(testcase, root: Path, base: str,
                                 protected_key: str, check_tracker: bool = False):
    testcase.assertRegex(base, r"^[0-9a-f]{40}$")
    registry_path = "state/current_deck_overrides.json"
    old = json.loads(_from_base(root, base, registry_path))["decks"]
    new = json.loads((root / registry_path).read_text(encoding="utf-8"))["decks"]
    testcase.assertEqual(set(old), set(new))
    plans = transfer.load_json(root, transfer.PLANS)["decks"]

    superseded = set()
    for key, prior in old.items():
        if key == protected_key:
            continue  # The calling deck-specific test handles its own lock.
        current = new[key]
        if current == prior:
            continue
        previous_sha = prior["approved_list_sha256"]
        current_sha = current["approved_list_sha256"]
        testcase.assertEqual(current.get("approval_status"), "APPROVED", key)
        testcase.assertEqual(current.get("lock_status"), "LOCKED", key)
        testcase.assertEqual(prior.get("approval_status"), "APPROVED", key)
        testcase.assertEqual(prior.get("lock_status"), "LOCKED", key)
        if current_sha == previous_sha:
            # Certification metadata/receipt pointer repairs can occur, but
            # never change the approved bytes or material owner decision.
            for field in ("approval_status", "lock_status", "approval_basis",
                          "user_approval_date", "m7_final_candidate_sha256"):
                testcase.assertEqual(current.get(field), prior.get(field), (key, field))
        else:
            superseded.add(key)
            testcase.assertEqual(current.get("previous_approved_list_sha256"),
                                 previous_sha, key)
            testcase.assertEqual(current.get("m7_final_candidate_sha256"),
                                 current_sha, key)
            testcase.assertIn(current_sha, current.get("approval_basis", ""), key)
            testcase.assertGreaterEqual(current["user_approval_date"],
                                        prior["user_approval_date"], key)
            previous_path = root / current["previous_approved_list_artifact"]
            testcase.assertTrue(previous_path.is_file(), key)
            testcase.assertEqual(hashlib.sha256(previous_path.read_bytes()).hexdigest(),
                                 previous_sha, key)
            receipt = (root / current["approval_record_artifact"]).read_text(encoding="utf-8")
            testcase.assertIn(current_sha, receipt, key)
            testcase.assertIn(previous_sha, receipt, key)
            plan_key = transfer.certified_plan_key(root, key, current)
            attestation = transfer.load_json(
                root, transfer.ATTESTATIONS / f"{key}_{current_sha[:16]}.json"
            )
            transfer.validate_attestation(root, key, current,
                                          plans.get(plan_key), attestation)
        source = root / current["approved_list_artifact"]
        testcase.assertTrue(source.is_file(), key)
        testcase.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                             current_sha, key)

    if check_tracker:
        tracker_path = "refinement/Deck_Refinement_Tracker_2026-10-12.csv"

        def keyed(body):
            return {row["deck_id"]: row for row in csv.DictReader(body.splitlines())}

        before = keyed(_from_base(root, base, tracker_path))
        after = keyed((root / tracker_path).read_text(encoding="utf-8"))
        testcase.assertEqual(set(before), set(after))
        for key in superseded:
            testcase.assertEqual(before[key]["final_list_hash"],
                                 old[key]["approved_list_sha256"], key)
            testcase.assertEqual(after[key]["final_list_hash"],
                                 new[key]["approved_list_sha256"], key)
            testcase.assertEqual(after[key]["final_gate_passed"], "YES", key)
            testcase.assertEqual(after[key]["user_approval_date"],
                                 new[key]["user_approval_date"], key)
        for key in before:
            if key == protected_key or before[key] == after[key]:
                continue
            testcase.assertIn(key, superseded, f"Unapproved tracker drift for {key}")
