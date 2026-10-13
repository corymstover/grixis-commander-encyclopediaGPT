import subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class AutomationContractTests(unittest.TestCase):
    def test_refresh_workflow_contract(self):
        result = subprocess.run([sys.executable, "scripts/check_workflow_contracts.py"], cwd=ROOT,
                                text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS:", result.stdout)

if __name__ == "__main__":
    unittest.main()
