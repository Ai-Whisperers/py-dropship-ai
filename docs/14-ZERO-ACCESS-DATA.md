# Zero-Access Data Gathering — What We Can Collect Starting Today

*2026-10-22. Both operations have a "before any credentials" phase. This doc enumerates everything collectable now — and ships the first captures.*

## 1. DONE today: first CDE price snapshot (Shopping China)

**`data/cde-snapshots/shoppingchina-niche-2026-10-22.json` — 113 unique products with prices**, across the exact niche-finalist categories:

| Category | Products | Notes |
|---|---|---|
| Celulares | 21 | High-ticket anchor category |
| Accesorios para celulares | 20 | Apple-accessory finalist territory |
| Gamer | 19 | Audio+gaming finalist territory |
| Auriculares | 12 | Audio finalist core |
| Accesorios p/ tablet | 17 | WiseTab-adjacent |
| Mochilas/capas | 10 | Bag/case segment |
| Reloj | 9 | Smartwatch-adjacent |
| Notebook acc / almacenamiento / iPad acc | 5 | Thin but present |

**Price stats: Gs. 19,000 – 12,915,000, median Gs. 195,000.** That median sits exactly in our target ticket band (Gs. 150-500k) — the niche hypothesis holds on real data.

**How it was done (repeatable nightly):** plain urllib + regex card-parser against category pages (584 nav paths discovered from the homepage), 1.2s politeness delay, no auth, no bot-wall hit. Tupi's sitemap redirects to a stub domain (tupisa.com.py) — Tupi needs the changedetection.io path instead. Fastrax renders products client-side (Next.js without SSR data in HTML) — needs the Scrapling/browser path. Cellshop/Nissei stay 403 (browser stealth queue).

## 2. The full zero-access collection list

### PY operation:

| # | Dataset | Method | Status |
|---|---|---|---|
| 1 | Shopping China category snapshots (niche) | urllib regex parser (this doc) | ✅ **captured today, 113 SKUs** |
| 2 | Shopping China FULL catalog (584 categories) | same parser, nightly cron | queued — ~3-5k SKUs est. |
| 3 | Fastrax full catalog | Scrapling stealth (Next.js CSR) | queued |
| 4 | Tupi price benchmark | changedetection.io watches on category URLs | queued |
| 5 | Cellshop + Nissei | browser-stealth queue (403 today) | queued |
| 6 | FB Marketplace Asunción niche velocity | browser session, weekly manual-agent pass | designed (doc 07 hat 28) |
| 7 | USD/Gs rate history | BCP endpoints, daily cron | queued |
| 8 | Couriers rate cards (3A, Chilat, ParaguayCourier) | one-shot manual capture to canonical table | queued |
| 9 | Instagram CDE sellers (top 20) | profile + price scrape watch | queued |
| 10 | MELI-PY category prices | public listing pages | queued |

### WiseQ engagement:

| # | Dataset | Method | Status |
|---|---|---|---|
| 1 | WiseQ Shopify catalog (230) | products.json (public) | ✅ captured earlier (data/research-lanes) |
| 2 | Bundle spine (114+25) | derived (doc 07) | ✅ shipped |
| 3 | bol brand-page listings (312 drift) | public brand page scrape | queued — needs IP rotation (blocked from this IP) |
| 4 | BuddyPhones/Puro/iClever bol+Amazon price positions | public listing pages, weekly | queued |
| 5 | educatheek wholesale prices (their products!) | public site parse | queued |
| 6 | koptelefoon-onderwijs.nl (Alpine Muffy school prices) | public site parse | queued |
| 7 | NL school calendar + budget cycles | public DUO/agenda data | partially (lead-gen data) |
| 8 | Trustpilot review stream (WiseQ + competitors) | public pages, weekly | queued |
| 9 | Google Trends NL: kids-audio queries | public API-lite | queued |
| 10 | Amazon.nl search positions for niche terms | public search pages | queued |

## 3. New insights from the first capture

1. **The niche-median validation:** Gs. 195k median across captured SKUs sits in-band; audio+gaming categories are well-stocked at CDE (31 gamer+auriculares SKUs from ONE wholesaler) — supply side confirmed.
2. **Shopping China's catalog is deep** (584 categories discovered) — a single wholesaler gives us the first price-map skeleton; two more sources (Fastrax, Tupi) create the dispersion index (doc 07 hat 1).
3. **Parse fragility is manageable:** the card regex survived 10 categories with zero misses; nightly cron + weekly diff = changedetection redundancy.
4. **Tech-category depth asymmetry:** iPad/almacenamiento thin (1 SKU each) at this wholesaler — Apple-accessory niche needs Fastrax/Cellshop sources before validation concludes.
5. **WiseQ competitive monitoring (their value):** items 4-6 in their table are the "competitor price watch" pilot we can demo to Rob with zero access — the Monday-report format from doc 04.

## 4. Cron plan (the moment infra lands)

```
nightly 02:00  shoppingchina full-catalog snapshot + diff vs yesterday -> alerts on >5% moves
nightly 02:30  fastrax stealth crawl (when built) + same diff
daily   06:00  USD/Gs rate -> canonical table
weekly  Mon 06  bol/Amazon competitor positions -> Monday report (WiseQ)
weekly  Fri 06  FB Marketplace niche velocity count -> niche decision data
```

All snapshots append to `data/cde-snapshots/` (dated files) → the price-history table starts accumulating the moment the first cron runs. **The dispersion index (hat 1) needs ≥2 sources; today we have 1 live + 2 queued — the map is one build away.**
