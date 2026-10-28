"""Catch omitted M7 Archidekt presentation metadata without touching decks."""

import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "state" / "current_deck_overrides.json"

# Source: existing whole-deck commander-first deep reviews, each independently
# stating optimized/Bracket 4. Tags are concise role labels, not certifications.
HISTORICALLY_MISSING = {
    "Abaddon_the_Despoiler",
    "Admiral_Beckett_Brass",
    "Admiral_Brass__Unsinkable",
    "Anhelo_the_Painter",
    "Parnesse__the_Subtle_Brush",
    "The_Rani",
}


class M7MetadataCompleteness(unittest.TestCase):
    def test_exact_62_metadata_and_lock_integrity(self):
        decks = json.loads(REGISTRY.read_text())["decks"]
        self.assertEqual(len(decks), 62)
        for deck_id, record in decks.items():
            with self.subTest(deck_id=deck_id):
                self.assertEqual(record["approval_status"], "APPROVED")
                self.assertEqual(record["lock_status"], "LOCKED")
                tags = record.get("m7_archidekt_tags", [])
                self.assertEqual(len(tags), 3)
                self.assertEqual(len(set(tags)), 3)
                self.assertTrue(all(isinstance(t, str) and t.strip() == t and t for t in tags))
                self.assertTrue(record.get("m7_power_bracket", "").startswith(("4 —", "5 —")))
                raw = (ROOT / record["approved_list_artifact"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), record["approved_list_sha256"])
                if deck_id in HISTORICALLY_MISSING:
                    self.assertEqual(record["m7_power_bracket"], "4 — Optimized")


if __name__ == "__main__":
    unittest.main()
