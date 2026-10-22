#!/usr/bin/env python3
"""scripts/validate_repo.py — repo-integrity validator for py-dropship-ai.

CI gate (GitHub Actions) + local runnable. Stdlib only.

Validates:
  1. Every docs/ link in README.md exists
  2. data/oss/*.json parse + schema (query/items/required fields)
  3. data/cde-snapshots/*.json parse + price sanity (price_gs int > 0,
     captured date present, no future dates)
  4. Snapshot freshness: at least one snapshot within the last 14 days
     (warn-only — does not fail — so an idle period doesn't block docs PRs)
  5. Secret-pattern scan

Exit 0 = pass; non-zero with itemized failures = fail.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures: list[str] = []
warns: list[str] = []
checks = 0


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"  ✗ {msg}")


def check(cond: bool, good: str, bad: str) -> None:
    global checks
    checks += 1
    ok(good) if cond else fail(bad)


print("== 1. README doc links")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
doc_links = re.findall(r"\]\((docs/[^)#]+)", readme)
check(bool(doc_links), f"{len(doc_links)} doc links found", "no doc links in README")
for link in doc_links:
    check((ROOT / link).is_file(), f"exists: {link}", f"MISSING: {link}")

print("== 2. data/oss/*.json schema")
oss_files = sorted(f for f in (ROOT / "data" / "oss").glob("*.json") if not f.name.startswith("_"))
check(bool(oss_files), f"{len(oss_files)} oss data files", "no oss data files")
total = 0
for jf in oss_files:
    try:
        data = json.loads(jf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{jf.name}: invalid JSON ({e})")
        continue
    if "items" not in data:
        fail(f"{jf.name}: missing 'items'")
        continue
    bad = [i for i in data["items"] if not all(k in i for k in ("full_name", "url", "stars"))]
    if bad:
        fail(f"{jf.name}: {len(bad)} items missing fields")
    else:
        total += len(data["items"])
ok(f"{total} items pass schema across {len(oss_files)} files")

print("== 3. CDE snapshot integrity")
snap_files = sorted((ROOT / "data" / "cde-snapshots").glob("*.json"))
check(bool(snap_files), f"{len(snap_files)} snapshot files", "no snapshots captured yet")
today = date.today()
newest = None
for sf in snap_files:
    try:
        rows = json.loads(sf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{sf.name}: invalid JSON ({e})")
        continue
    bad_price = [r for r in rows if not isinstance(r.get("price_gs"), int) or r["price_gs"] <= 0]
    if bad_price:
        fail(f"{sf.name}: {len(bad_price)} rows with invalid price_gs")
    for r in rows:
        cap = r.get("captured", "")
        try:
            d = datetime.strptime(cap, "%Y-%m-%d").date()
        except ValueError:
            fail(f"{sf.name}: row with bad captured date {cap!r}")
            continue
        if d > today:
            fail(f"{sf.name}: future capture date {cap}")
        if newest is None or d > newest:
            newest = d
if newest and (today - newest) > timedelta(days=14):
    warns.append(f"newest snapshot {newest} is {(today - newest).days} days old — refresh crawl due")
if newest:
    ok(f"newest snapshot {newest}")

print("== 4. secret scan")
SECRET_PAT = re.compile(r"(ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})")
hits = []
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".json", ".csv", ".yml", ".yaml", ".txt", ".py"}:
        try:
            m = SECRET_PAT.search(f.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
        if m:
            hits.append(f"{f.relative_to(ROOT)}: {m.group(0)[:12]}…")
check(not hits, "no secret patterns found", f"secrets detected: {hits[:3]}")

for w in warns:
    print(f"  ⚠ {w}")
print(f"\n{checks} checks run, {len(failures)} failures, {len(warns)} warnings")
if failures:
    print("VALIDATION FAILED")
    sys.exit(1)
print("VALIDATION PASSED ✓")
