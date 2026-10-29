#!/usr/bin/env python3
"""NETRUNNER synthetic-only, no-network MEV evidence rehearsal.

This is not a trade executor, vulnerability oracle, incident attribution engine,
or real-world claim validator. Python 3.10+ standard library only.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any

NETWORKS = frozenset({"solana", "arbitrum_one"})
KINDS = frozenset({
    "ordering_anomaly", "oracle_deviation", "sequencer_down",
    "sequencer_recovered", "insufficient_data",
})
MAX_BYTES = 2_000_000
MAX_EVENTS = 1_000


class ReplayError(ValueError):
    """Invalid or unsuitable synthetic event package."""


def _timestamp(value: Any) -> str:
    if not isinstance(value, str):
        raise ReplayError("observed_at must be an ISO-8601 timezone-aware string")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReplayError("invalid observed_at") from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ReplayError("observed_at must include an explicit UTC offset")
    return dt.isoformat()


def _positive_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ReplayError(f"{field} must be a numeric, positive value")
    if not math.isfinite(value) or value <= 0:
        raise ReplayError(f"{field} must be finite and greater than zero")
    return float(value)


def _bounded_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 256:
        raise ReplayError(f"{field} must be a nonempty string up to 256 characters")
    return value


def validate_fixture(data: Any) -> list[dict[str, Any]]:
    if not isinstance(data, dict) or set(data) != {"schema_version", "dataset_kind", "scope", "events"}:
        raise ReplayError("fixture top-level keys must be schema_version, dataset_kind, scope, events")
    if data["schema_version"] != "0.1" or data["dataset_kind"] != "synthetic":
        raise ReplayError("v0.1 only supports synthetic data, never live or fork datasets")
    _bounded_text(data["scope"], "scope")
    raw = data["events"]
    if not isinstance(raw, list) or len(raw) > MAX_EVENTS:
        raise ReplayError("events must be a list of at most 1000 entries")
    seen: set[str] = set()
    validated = []
    for idx, ev in enumerate(raw):
        if not isinstance(ev, dict) or set(ev) != {"id", "network", "kind", "observed_at", "source_ref", "observed"}:
            raise ReplayError(f"event[{idx}] has missing or forbidden keys")
        eid = _bounded_text(ev["id"], "id")
        if eid in seen:
            raise ReplayError(f"duplicate event id: {eid}")
        seen.add(eid)
        network, kind = ev["network"], ev["kind"]
        if network not in NETWORKS or kind not in KINDS:
            raise ReplayError(f"event {eid}: unsupported network or kind")
        if kind.startswith("sequencer_") and network != "arbitrum_one":
            raise ReplayError(f"event {eid}: sequencer event requires arbitrum_one")
        ts = _timestamp(ev["observed_at"])
        _bounded_text(ev["source_ref"], "source_ref")
        if not isinstance(ev["observed"], dict):
            raise ReplayError(f"event {eid}: observed must be an object")
        observed = ev["observed"]
        if kind == "oracle_deviation":
            if set(observed) != {"reference_price", "consumed_price", "asset"}:
                raise ReplayError(f"event {eid}: oracle fields must be reference_price, consumed_price, asset")
            _positive_number(observed["reference_price"], "reference_price")
            _positive_number(observed["consumed_price"], "consumed_price")
            _bounded_text(observed["asset"], "asset")
        elif kind == "ordering_anomaly":
            if set(observed) != {"pattern_summary"}:
                raise ReplayError(f"event {eid}: only pattern_summary is allowed")
            _bounded_text(observed["pattern_summary"], "pattern_summary")
        elif kind in {"sequencer_down", "sequencer_recovered"}:
            if set(observed) != {"status_note"}:
                raise ReplayError(f"event {eid}: only status_note is allowed")
            _bounded_text(observed["status_note"], "status_note")
        elif kind == "insufficient_data":
            if set(observed) != {"missing"}:
                raise ReplayError(f"event {eid}: only missing is allowed")
            _bounded_text(observed["missing"], "missing")
        validated.append({**ev, "observed_at": ts})
    return sorted(validated, key=lambda x: (x["network"], x["observed_at"], x["id"]))


def classify(ev: dict[str, Any]) -> dict[str, Any]:
    kind, details = ev["kind"], ev["observed"]
    base = {
        "event_id": ev["id"], "network": ev["network"], "observed_at": ev["observed_at"],
        "source_ref": ev["source_ref"], "source_kind": "synthetic_fixture",
        "claim_status": "HYPOTHESIS", "classification": "INSUFFICIENT_DATA",
        "observation": details, "inference": "No conclusion can be supported.",
        "alternative_explanations": [], "missing_evidence": [],
        "prohibited_inferences": [
            "No malicious actor attribution", "No realized harm or profit", "No live execution authority"
        ],
    }
    if kind == "oracle_deviation":
        a = float(details["reference_price"])
        b = float(details["consumed_price"])
        raw_pct = 100 * abs(a-b)/a
        if not math.isfinite(raw_pct):
            raise ReplayError("oracle difference exceeds representable range")
        delta_pct = round(raw_pct, 4)
        base.update({
            "classification": "REVIEW_ORACLE", "synthetic_price_difference_pct": delta_pct,
            "inference": "A price-input discrepancy is present in the synthetic fixture; cause and user harm are unverified.",
            "alternative_explanations": ["Different price source/decimals", "Stale but valid sampling window", "Fixture construction"],
            "missing_evidence": ["Original feed timestamps/decimals", "On-chain consumed value path", "A policy-defined discrepancy threshold"],
        })
    elif kind == "ordering_anomaly":
        base.update({
            "classification": "REVIEW_ORDERING",
            "inference": "The fixture describes a possible ordering anomaly; it does not prove sandwiching or intent.",
            "alternative_explanations": ["Ordinary priority-fee ordering", "Independent transactions", "Incomplete transaction visibility"],
            "missing_evidence": ["Complete relevant transaction sequence", "Block/slot and fee reconstruction", "Counterfactual price impact"],
        })
    elif kind in ("sequencer_down", "sequencer_recovered"):
        base.update({
            "classification": "REVIEW_RECOVERY",
            "inference": "Synthetic sequencer status alone does not establish whether protocol exposure is resolved.",
            "alternative_explanations": ["RPC-only observation failure", "Stale monitor health", "Sequencer status without application recovery"],
            "missing_evidence": ["Independent sequencer verification", "Oracle/feed freshness", "Protocol-level post-recovery state"],
        })
    elif kind == "insufficient_data":
        base.update({
            "claim_status": "UNKNOWN", "classification": "INSUFFICIENT_DATA",
            "inference": "Required fixture inputs were expressly missing; no signal should be inferred.",
            "missing_evidence": [details["missing"]],
        })
    return base


def replay(data: Any) -> dict[str, Any]:
    events = validate_fixture(data)
    findings = [classify(ev) for ev in events]
    counts = {
        net: {"events": sum(f["network"] == net for f in findings),
              "hypotheses": sum(f["network"] == net and f["claim_status"] == "HYPOTHESIS" for f in findings),
              "unknown": sum(f["network"] == net and f["claim_status"] == "UNKNOWN" for f in findings)}
        for net in sorted(NETWORKS)
    }
    dossier = {
        "schema_version": "0.1", "project": "NETRUNNER FOUNDATION", "mode": "OFFLINE_SYNTHETIC",
        "scope": data["scope"], "network_counts": counts, "findings": findings,
        "authority": "NONE: no network calls, signed transactions, orders or production alerts",
    }
    canonical = json.dumps(dossier, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    dossier["dossier_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return dossier


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path, help="local synthetic JSON fixture")
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args(argv)
    try:
        if args.fixture.stat().st_size > MAX_BYTES:
            raise ReplayError("fixture too large")
        data = json.loads(args.fixture.read_text(encoding="utf-8"))
        result = replay(data)
    except (OSError, UnicodeError, json.JSONDecodeError, ReplayError) as exc:
        print(f"NETRUNNER_REJECT: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
