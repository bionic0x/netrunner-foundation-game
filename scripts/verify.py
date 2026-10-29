#!/usr/bin/env python3
"""Run the supplied suite and compare every distributed synthetic dossier."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples" / "netrunner-foundation"


def main() -> int:
    if sys.version_info < (3, 10):
        print("Python 3.10+ is required", file=sys.stderr)
        return 2
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(EXAMPLES),
         "-p", "test_*.py", "-v"], cwd=ROOT,
    )
    if result.returncode:
        return result.returncode
    spec = importlib.util.spec_from_file_location("netrunner_replay", EXAMPLES / "replay.py")
    assert spec and spec.loader
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    expected = engine.replay(json.loads((EXAMPLES / "fixture.json").read_text(encoding="utf-8")))
    saved = json.loads((EXAMPLES / "synthetic-dossier.json").read_text(encoding="utf-8"))
    html = (EXAMPLES / "index.html").read_text(encoding="utf-8")
    match = re.search(r'<script type="application/json" id="dossier-data">(.*?)</script>', html, re.S)
    if not match:
        print("VERIFY_REJECT: embedded dossier is missing", file=sys.stderr)
        return 1
    embedded = json.loads(match.group(1))
    if saved != expected or embedded != expected:
        print("VERIFY_REJECT: saved or embedded dossier differs from replay", file=sys.stderr)
        return 1
    print("Dossier parity: Python replay = JSON export = embedded console data")
    print("SHA-256:", expected["dossier_sha256"])
    node = shutil.which("node")
    if node is None:
        print("VERIFY_REJECT: Node.js 20+ is required for Academy gameplay tests", file=sys.stderr)
        return 2
    return subprocess.run([node, "--test", str(EXAMPLES / "test_academy.cjs")], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
