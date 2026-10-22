#!/usr/bin/env python3
"""scripts/crawl_shoppingchina.py — nightly CDE price snapshot crawler.

Crawls Shopping China (shoppingchina.com.py) niche category pages with a
polite plain-HTTP parser (no auth, 1.2s delay) and writes a dated snapshot
to data/cde-snapshots/shoppingchina-niche-YYYY-MM-DD.json.

Used by .github/workflows/snapshot.yml (nightly) and runnable locally.
Category list mirrors docs/14-ZERO-ACCESS-DATA.md §1 (the 10 niche-finalist
categories). Extend targets as more categories are validated.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data" / "cde-snapshots"
BASE = "https://www.shoppingchina.com.py"

TARGETS = [
    "/electronicos/auriculares",
    "/electronicos/accesorios-para-celulares",
    "/electronicos/celulares",
    "/informatica/gamer",
    "/informatica/accesorios-p-notebook",
    "/informatica/accesorios-p-tablet",
    "/casa-y-decoracion/reloj",
    "/informatica/almacenamientos",
    "/informatica/ipad-acc-apple",
    "/informatica/maletas-mochilas-capas",
]

CARD_RE = re.compile(
    r'<a[^>]+href="(/producto/[^"]+)"[^>]*>(?:\s*<[^>]+>)*\s*([^<]{8,90}?)\s*(?:<[^>]+>)*.{0,600}?Gs\.?\s?([\d.]{5,12})',
    re.S,
)


def fetch(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot: dict[tuple[str, int], dict] = {}
    for cat in TARGETS:
        try:
            html = fetch(BASE + cat)
        except Exception as e:  # noqa: BLE001 — log and continue with other cats
            print(f"  ! {cat}: {e}")
            continue
        added = 0
        for link, title, price in CARD_RE.findall(html):
            title = re.sub(r"\s+", " ", title).strip()
            if not title:
                continue
            key = (title, int(price.replace(".", "")))
            if key in snapshot:
                continue
            snapshot[key] = {
                "source": "shoppingchina",
                "category": cat,
                "title": title,
                "price_gs": key[1],
                "url": BASE + link,
                "captured": str(date.today()),
            }
            added += 1
        print(f"  {cat}: +{added}")
        time.sleep(1.2)

    out = OUT_DIR / f"shoppingchina-niche-{date.today()}.json"
    out.write_text(json.dumps(list(snapshot.values()), ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nTOTAL unique products: {len(snapshot)} -> {out.relative_to(ROOT)}")
    if not snapshot:
        print("ERROR: zero products captured — site structure may have changed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
