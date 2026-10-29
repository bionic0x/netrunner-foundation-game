"""Local-only, non-executing NETRUNNER v0.2 documentation and contract checks."""
import hashlib
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DOCS = ROOT / 'strategy' / 'netrunner-foundation'


class ConsolidatedContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads((DOCS / 'contracts.v0.2.json').read_text(encoding='utf-8'))

    def test_explicit_no_live_authority(self):
        self.assertFalse(self.spec['live_authority'])
        self.assertEqual(self.spec['gate0'], 'HOLD')
        self.assertEqual(self.spec['mode'], 'DOCUMENTARY_AND_OFFLINE_SYNTHETIC')

    def test_networks_are_independent(self):
        self.assertEqual(set(self.spec['network_scopes']), {'solana', 'arbitrum_one'})
        sol = set(self.spec['channels']['solana']['signal_types'])
        arb = set(self.spec['channels']['arbitrum_one']['signal_types'])
        self.assertTrue(sol.isdisjoint(arb))
        self.assertEqual(sol, {'SOL-ORD', 'SOL-ORC'})
        self.assertEqual(arb, {'ARB-ORC', 'ARB-RES'})

    def test_material_actions_explicitly_excluded(self):
        actions = set(self.spec['excluded_actions'])
        for action in ['transaction_signing', 'transaction_submission', 'custody',
                       'market_manipulation', 'unauthorized_intrusion',
                       'evidence_destruction', 'token_sale']:
            self.assertIn(action, actions)

    def test_docs_are_present(self):
        for name in ['MASTER-BLUEPRINT.md', 'SOURCE-CROSSWALK.md',
                     'CLAIM-ADJUDICATION.md', 'DECISION-RECORD.md', 'DESIGN-BRIEF.md']:
            with self.subTest(name=name):
                self.assertGreater((DOCS / name).stat().st_size, 500)

    def test_no_status_masquerading(self):
        self.assertIn('SOURCE_ASSERTION', self.spec['claim_states'])
        self.assertIn('UNKNOWN', self.spec['epistemic_states'])
        self.assertIn('MEASURED', self.spec['quantitative_classes'])
        self.assertNotIn('PRODUCTION_APPROVED', self.spec['claim_states'])

    def test_local_manifest_size_and_hashes_if_available(self):
        p = ROOT / 'source-manifest.internal.json'
        if not p.is_file():
            self.skipTest('Private source manifest intentionally absent from public repo')
        manifest = json.loads(p.read_text(encoding='utf-8'))
        self.assertEqual(manifest['file_count'], self.spec['source_count'])
        self.assertEqual(len(manifest['sources']), 27)
        # If source files are mounted here, ensure hashes match. Public CI may omit originals.
        for item in manifest['sources']:
            candidate = ROOT.parent / item['filename']
            if candidate.is_file():
                self.assertEqual(hashlib.sha256(candidate.read_bytes()).hexdigest(), item['sha256'])


if __name__ == '__main__':
    unittest.main()
