"""Deterministic synthetic evidence separation and negative-path tests."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("netrunner_replay", ROOT / "replay.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(mod)


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((ROOT / "fixture.json").read_text(encoding="utf-8"))

    def test_schema_and_isolation(self):
        out = mod.replay(self.fixture)
        self.assertEqual(out["mode"], "OFFLINE_SYNTHETIC")
        self.assertEqual(out["network_counts"]["solana"], {"events":3, "hypotheses":2, "unknown":1})
        self.assertEqual(out["network_counts"]["arbitrum_one"], {"events":3, "hypotheses":3, "unknown":0})

    def test_determinism_reordering(self):
        a = mod.replay(self.fixture)
        b = copy.deepcopy(self.fixture)
        b["events"].reverse()
        self.assertEqual(a, mod.replay(b))
        self.assertEqual(len(a["dossier_sha256"]), 64)

    def test_flags_remain_hypotheses(self):
        out = mod.replay(self.fixture)
        self.assertTrue(all(f["claim_status"] != "EVIDENCE" for f in out["findings"]))
        self.assertTrue(all(f["source_kind"] == "synthetic_fixture" for f in out["findings"]))
        self.assertTrue(all(f["prohibited_inferences"] for f in out["findings"]))

    def test_confident_attribution_absent(self):
        out = mod.replay(self.fixture)
        text = json.dumps(out).lower()
        self.assertNotIn("attacker_identity", text)
        self.assertNotIn("profit_usd", text)

    def test_wrong_dataset_kind(self):
        bad = copy.deepcopy(self.fixture)
        bad["dataset_kind"] = "live"
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_invalid_network(self):
        bad = copy.deepcopy(self.fixture)
        bad["events"][0]["network"] = "ethereum"
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_sequencer_cannot_transfer_to_solana(self):
        bad = copy.deepcopy(self.fixture)
        ev = next(e for e in bad["events"] if e["kind"] == "sequencer_down")
        ev["network"] = "solana"
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_duplicate_event(self):
        bad = copy.deepcopy(self.fixture)
        bad["events"][1]["id"] = bad["events"][0]["id"]
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_rejects_execution_fields(self):
        bad = copy.deepcopy(self.fixture)
        bad["events"][0]["private_key"] = "not permitted"
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_rejects_naive_timestamp(self):
        bad = copy.deepcopy(self.fixture)
        bad["events"][0]["observed_at"] = "2026-10-01T10:00:00"
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_oracle_invalid_numbers(self):
        for invalid in (-1, 0, float("nan"), float("inf"), True, "123"):
            bad = copy.deepcopy(self.fixture)
            ev = next(e for e in bad["events"] if e["kind"] == "oracle_deviation")
            ev["observed"]["reference_price"] = invalid
            with self.subTest(invalid=str(invalid)), self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_oracle_extreme_ratio_rejected(self):
        bad = copy.deepcopy(self.fixture)
        ev = next(e for e in bad["events"] if e["kind"] == "oracle_deviation")
        ev["observed"]["reference_price"] = 1e-200
        ev["observed"]["consumed_price"] = 1e200
        with self.assertRaises(mod.ReplayError): mod.replay(bad)

    def test_ui_dossier_matches_fixture(self):
        dossier = mod.replay(self.fixture)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(dossier["dossier_sha256"], html)
        self.assertIn("NO TRADING", html)
        self.assertNotIn("XMLHttpRequest(", html)
        self.assertNotIn("fetch(", html)

    def test_oracle_math(self):
        out = mod.replay(self.fixture)
        solarb = {(f["network"], f["event_id"]): f for f in out["findings"]}
        self.assertEqual(solarb[("solana", "SOL-SYN-002")]["synthetic_price_difference_pct"], 4.0)
        self.assertEqual(solarb[("arbitrum_one", "ARB-SYN-001")]["synthetic_price_difference_pct"], 1.0)

    def test_command_line(self):
        run = subprocess.run([sys.executable, str(ROOT/"replay.py"), str(ROOT/"fixture.json"), "--compact"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        self.assertEqual(json.loads(run.stdout)["project"], "NETRUNNER FOUNDATION")

    def test_missing_fixture_rejected(self):
        run = subprocess.run([sys.executable, str(ROOT/"replay.py"), str(ROOT/"missing.json")], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2)
        self.assertIn("NETRUNNER_REJECT", run.stderr)

    def test_max_events(self):
        bad = copy.deepcopy(self.fixture)
        bad["events"] = [dict(bad["events"][0], id=f"e{i}") for i in range(1001)]
        with self.assertRaises(mod.ReplayError): mod.replay(bad)


if __name__ == "__main__":
    unittest.main()
