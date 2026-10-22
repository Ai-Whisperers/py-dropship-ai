# Catálogo de Software Open-Source — 25 temas, 1,710 repos únicos

*Investigación 2026-10-22 vía GitHub Search API: top 100 por estrellas por tema (≥20★, sin archivados). Data cruda: `data/oss/<tema>.json` (25 archivos, 1,816 filas). Este doc resume lo actionable.*

## Stack adoptado (decisión)

| Capa | Elección | ★ | Por qué |
|---|---|---|---|
| Orquestación | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | — | Ya operado por AIW; cron, webhooks, MCP, multi-perfil |
| WhatsApp gateway | [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api) | 9.9k | Self-hosted REST; número dedicado; WAHA plan B |
| Inventario | [inventree/InvenTree](https://github.com/inventree/InvenTree) | 7.7k | API-first, MIT |
| Scraping stealth | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 89k | Anti-bot — Cellshop/Nissei 403 |
| Watchdog cambios | [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | 35.2k | Alertas precio/stock sin parser |
| Flujos no-agentes | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 208k | Notificaciones/ETL; Hermes decide, n8n ejecuta |
| Meta Ads | [oliverames/meta-mcp-server](https://github.com/oliverames/meta-mcp-server) | 59 | 200+ tools Meta MCP |

## Reglas de adopción

1. **>1k★ o patrón probado AIW** — si no, script propio ~200 líneas.
2. **Docker + API/CLI completos** — operable por agente sin humano.
3. **Licencia comercial OK** (MIT/Apache; n8n fair-code interno OK).
4. **Un dueño por capa** — elegir, no coleccionar.

## 1. Sourcing y monitoreo de precios

### Monitoreo de precios · `price-tracking` · 98 repos · 28,953 resultados en GitHub

**Shortlist:** [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) · [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) · [getlago/lago](https://github.com/getlago/lago) · [achannarasappa/ticker](https://github.com/achannarasappa/ticker)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | 35,195 | Python | Best and simplest tool for website change detection, web page monitoring, and website change al |
| [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | 20,731 | TypeScript | OpenStock is an open-source alternative to expensive market platforms. Track real-time prices,  |
| [getlago/lago](https://github.com/getlago/lago) | 10,705 | Go | Open Source Metering and Usage Based Billing API ⭐️ Consumption tracking, Subscription manageme |
| [achannarasappa/ticker](https://github.com/achannarasappa/ticker) | 6,248 | Go | Track stocks, crypto, and derivatives prices and positions in real time from your terminal |
| [jez500/pricebuddy](https://github.com/jez500/pricebuddy) | 1,432 | PHP | A self hostable app that tracks prices and sends you notifications when prices match your prefe |
| [techwithtim/Price-Tracking-Web-Scraper](https://github.com/techwithtim/Price-Tracking-Web-Scraper) | 1,294 | Python | An automated price tracker that uses bright data, playwright, react and flask. |
| [clucraft/PriceGhost](https://github.com/clucraft/PriceGhost) | 1,128 | TypeScript | A self-hosted price tracking application that monitors product prices from any website. |
| [Cybrarist/Discount-Bandit](https://github.com/Cybrarist/Discount-Bandit) | 754 | PHP | A Multi-User Selfhosted price tracker for Amazon, Aliexpress, ebay and many more along with cus |
| [adrianhajdin/pricewise](https://github.com/adrianhajdin/pricewise) | 634 | TypeScript | Dive into web scraping and build a Next.js 13 eCommerce price tracker within a single video tha |
| [druv5319/Sneaks-API](https://github.com/druv5319/Sneaks-API) | 498 | JavaScript | A StockX, FlightClub, Goat, and Stadium Goods API all in one. This sneaker API allows users to  |
| [adrianhajdin/signalist_stock-tracker-app](https://github.com/adrianhajdin/signalist_stock-tracker-app) | 486 | TypeScript | Stock Market app built with Next.js, Shadcn, Better Auth, and Inngest. Track prices, set alerts |
| [EthVentures/CryptoTracker](https://github.com/EthVentures/CryptoTracker) | 433 | Python | A complete open source system for tracking and visualizing cryptocurrency price movements on le |
| [elsbrock/hetzner-radar](https://github.com/elsbrock/hetzner-radar) | 403 | TypeScript | 🕵️Track prices of the Hetzner dedicated server auction |
| [walkingddd/CPA-Helper](https://github.com/walkingddd/CPA-Helper) | 311 | Go | CPA-Helper is a local, self-hosted multi-user management panel designed for CLIProxyAPI users.  |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | - | Skip to content github / docs Code Issues 80 Pull requests 35 Discussions Actions Projects 2 Se |
| [ManojKumarPatnaik/Major-project-list](https://github.com/ManojKumarPatnaik/Major-project-list) | 259 | - | A list of practical projects that anyone can solve in any programming language (See solutions). |
| [Crinibus/scraper](https://github.com/Crinibus/scraper) | 249 | Python | Web scraper for scraping, tracking and visualizing prices of products on various websites. |
| [cmoog/traderjoes](https://github.com/cmoog/traderjoes) | 244 | Haskell | Price tracking program and website for Trader Joe's, updated daily. |
| [the-hideout/tarkov-dev](https://github.com/the-hideout/tarkov-dev) | 236 | JavaScript | The official site for tarkov.dev - A web app to track item prices, view trader barters, quests, |
| [uhussain/WebCrawlerForInflation](https://github.com/uhussain/WebCrawlerForInflation) | 206 | Python | Price Crawler - Tracking Price Inflation |
| [martinarva/dynamic_energy_cost](https://github.com/martinarva/dynamic_energy_cost) | 203 | Python | A Home Assistant integration to provide real-time and cumulative energy cost tracking, optimize |
| [polyrabbit/my-token](https://github.com/polyrabbit/my-token) | 193 | Go | 📈Track token prices in your terminal |
| [jeancsil/flight-spy](https://github.com/jeancsil/flight-spy) | 184 | PHP | Looking for the cheapest flights and don't have enough time to track all the prices? |
| [affromero/flight-finder](https://github.com/affromero/flight-finder) | 173 | TypeScript | Self-hosted flight, hotel, and car rental price tracking with alerts, price history, and web an |
| [valmi-io/value](https://github.com/valmi-io/value) | 170 | Python | ⚡ "Value"  - https://value.valmi.io . Valmi Value is Outcome-based billing and payments infrast |
| [brianleect/binance-pump-alerts](https://github.com/brianleect/binance-pump-alerts) | 156 | Python | Tracks prices of pairs on binance and notifies when price movements based on pre-defined parame |
| [duyet/pricetrack](https://github.com/duyet/pricetrack) | 140 | JavaScript | Price tracker monitors of products and alerts you when prices drop. Supported tiki.vn, shopee,  |
| [Bananefre/Stock-Market-app](https://github.com/Bananefre/Stock-Market-app) | 140 | TypeScript | Stock Market app which track prices and automate workflows |
| [adomi-io/listing-lab](https://github.com/adomi-io/listing-lab) | 133 | Python | A simple workspace for keeping track of homes you’re considering. Save listings, add notes, and |
| [dylanleigh/PriceAndNutritionTrackingSystem](https://github.com/dylanleigh/PriceAndNutritionTrackingSystem) | 132 | Python | PANTS is a self-hosted, open-source nutrition tracker and tool for nutritional data analysis of |

### Web scraping · `web-scraping` · 97 repos · 139,663 resultados en GitHub

**Shortlist:** [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) · [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) · [scrapy/scrapy](https://github.com/scrapy/scrapy) · [soimort/you-get](https://github.com/soimort/you-get)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 193,958 | TypeScript | Supercharge your AI agents with data from the web and beyond. Building the library for superint |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 89,054 | Python | 🕷️ A Web Scraping framework that handles everything from a single request to a full-scale crawl |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 64,942 | Python | Scrapy, a fast high-level web crawling & scraping framework for Python. |
| [soimort/you-get](https://github.com/soimort/you-get) | 56,860 | Python | :arrow_double_down: Dumb downloader that scrapes the web |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | 29,117 | Rust | The headless browser for AI agents and web scraping |
| [apify/crawlee](https://github.com/apify/crawlee) | 26,216 | TypeScript | Crawlee—A web scraping and browser automation library for Node.js to build reliable crawlers. I |
| [dzhng/deep-research](https://github.com/dzhng/deep-research) | 19,812 | TypeScript | An AI-powered research assistant that performs iterative, deep research on any topic by combini |
| [seleniumbase/SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | 13,112 | Python | 📊 Python APIs for Web Automation, E2E Testing, and Data Scraping. CDP Mode bypasses bot-detecti |
| [code4craft/webmagic](https://github.com/code4craft/webmagic) | 11,670 | Java | A scalable web crawler framework for Java. |
| [apify/crawlee-python](https://github.com/apify/crawlee-python) | 9,614 | Python | Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Ex |
| [clips/pattern](https://github.com/clips/pattern) | 8,854 | Python | Web mining module for Python, with tools for scraping, natural language processing, machine lea |
| [lorien/awesome-web-scraping](https://github.com/lorien/awesome-web-scraping) | 8,184 | JavaScript | List of libraries, tools and APIs for web scraping and data processing. |
| [alirezamika/autoscraper](https://github.com/alirezamika/autoscraper) | 8,058 | Python | A Smart, Automatic, Fast and Lightweight Web Scraper for Python |
| [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | 7,666 | JavaScript | Official Firecrawl MCP server, the context API for AI agents: search, scrape, and interact with |
| [go-rod/rod](https://github.com/go-rod/rod) | 7,138 | Go | A Chrome DevTools Protocol driver for web automation and scraping. |
| [adbar/trafilatura](https://github.com/adbar/trafilatura) | 7,003 | Python | Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extracti |
| [brightdata/cli](https://github.com/brightdata/cli) | 6,234 | TypeScript | Official Bright Data CLI - scrape, search, and extract structured web data directly from your t |
| [niespodd/browser-fingerprinting](https://github.com/niespodd/browser-fingerprinting) | 5,150 | JavaScript | Analysis of Bot Protection systems with available countermeasures 🚿. How to defeat anti-bot sys |
| [REMitchell/python-scraping](https://github.com/REMitchell/python-scraping) | 4,729 | Jupyter Notebook | Code samples from the book Web Scraping with Python http://shop.oreilly.com/product/06369200343 |
| [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | 4,511 | Go | Open-source web scraping API. Turn any website into clean markdown or structured JSON. Anti-det |
| [sparklemotion/mechanize](https://github.com/sparklemotion/mechanize) | 4,445 | Ruby | Mechanize is a ruby library that makes automated web interaction easy. |
| [dotnetcore/DotnetSpider](https://github.com/dotnetcore/DotnetSpider) | 4,144 | C# | DotnetSpider, a .NET standard web crawling library. It is lightweight, efficient and fast high- |
| [aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE](https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE) | 3,290 | Python | Do you want to LEARN NEW STUFF for FREE? Don't worry, with the power of web-scraping and automa |
| [symfony/panther](https://github.com/symfony/panther) | 3,070 | PHP | A browser testing and web crawling library for PHP and Symfony |
| [TheBlewish/Automated-AI-Web-Researcher-Ollama](https://github.com/TheBlewish/Automated-AI-Web-Researcher-Ollama) | 3,023 | Python | A python program that turns an LLM, running on Ollama, into an automated researcher, which will |
| [spider-rs/spider](https://github.com/spider-rs/spider) | 2,793 | Rust | Foundational low latency web data collecting in Rust |
| [geziyor/geziyor](https://github.com/geziyor/geziyor) | 2,781 | Go | Geziyor, blazing fast web crawling & scraping framework for Go. Supports JS rendering. |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | 2,685 | JavaScript | A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public  |
| [firecrawl/open-agent-builder](https://github.com/firecrawl/open-agent-builder) | 2,641 | TypeScript | 🔥 Visual workflow builder for AI agents powered by Firecrawl - drag-and-drop web scraping pipel |
| [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | 2,503 | Python | Playwright that anti-bots cannot see, so no captchas: same API, anti-detect stealth headless Fi |

### Motores de búsqueda/crawl · `search-crawl` · 22 repos · 1,573 resultados en GitHub

**Shortlist:** [outpoot/vyntr](https://github.com/outpoot/vyntr) · [Norconex/crawler](https://github.com/Norconex/crawler)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [outpoot/vyntr](https://github.com/outpoot/vyntr) | 367 | TypeScript | Independent search engine. Includes web crawling, search indexing, dictionary API, and more. ht |
| [ahmia/ahmia-crawler](https://github.com/ahmia/ahmia-crawler) | 236 | Python | Collection of crawlers used by the ahmia search engine |
| [Norconex/crawler](https://github.com/Norconex/crawler) | 205 | Java | Norconex Crawlers (or spiders) are flexible web and filesystem crawlers for collecting, parsing |
| [Don-No7/Hack-SQL](https://github.com/Don-No7/Hack-SQL) | 149 | - | -- -- File generated with SQLiteStudio v3.2.1 on Sun Feb 7 14:58:28 2021 -- -- Text encoding us |
| [aws-samples/aws-step-functions-kendra-web-crawler-search-engine](https://github.com/aws-samples/aws-step-functions-kendra-web-crawler-search-engine) | 120 | TypeScript | This sample aims to demonstrate how to create a serverless web crawler and search engine, using |
| [Drahflow/crawler](https://github.com/Drahflow/crawler) | 76 | C++ | I needed a serious web crawler for search engine applications. This is it. |
| [mzollin/qr-pirate](https://github.com/mzollin/qr-pirate) | 76 | Python | crawl QR-codes from search engines and look for bitcoin private keys |
| [benkitzelman/google-ajax-crawler](https://github.com/benkitzelman/google-ajax-crawler) | 58 | Ruby | Rack Middleware adhering to the Google Ajax Crawling Scheme, using a headless browser to render |
| [conaticus/search-engine-crawler](https://github.com/conaticus/search-engine-crawler) | 53 | TypeScript | - |
| [andrewjw/celery-crawler](https://github.com/andrewjw/celery-crawler) | 48 | Python | A Django based search engine powered by CouchDB, celery and whoosh. |
| [AshwinAmbal/DarkWeb-Crawling-Indexing](https://github.com/AshwinAmbal/DarkWeb-Crawling-Indexing) | 45 | HTML | A DarkWeb Crawler based off the open-source TorSpider. Indexing with search engine created usin |
| [hackfengJam/ArticleSpider](https://github.com/hackfengJam/ArticleSpider) | 40 | Python | Crawling zhihu, jobbole, lagou by Scrapy, and using Elasticsearch+Django to build a Search Engi |
| [vincenzo-afk/NEXUS-ENGINE](https://github.com/vincenzo-afk/NEXUS-ENGINE) | 38 | Rust | A full-featured search engine in Rust. Local filesystem + web crawl, BM25+PageRank ranking, BPE |
| [johnhuang-cn/AngularSEO](https://github.com/johnhuang-cn/AngularSEO) | 35 | CSS | Java filter make AngularJS + JEE web site to be crawled by search engines |
| [BlockchainLabs/SpreadCoin](https://github.com/BlockchainLabs/SpreadCoin) | 33 | - | SpreadCoin October 5, 2014 Introduction In proof-of-work cryptocurrencies new coins are generat |
| [MultiX0/last-archive](https://github.com/MultiX0/last-archive) | 32 | Go | A local-first RAG engine for web archival and semantic search. Crawl, embed, and query your own |
| [9b/frisbee](https://github.com/9b/frisbee) | 31 | Python | Collect email addresses by crawling search engine results. |
| [udinparla/aa.py](https://github.com/udinparla/aa.py) | 29 | - | #!/usr/bin/env python import re import hashlib import Queue from random import choice import th |
| [p0dalirius/crawlersuseragents](https://github.com/p0dalirius/crawlersuseragents) | 26 | Python | Python script to check if there is any differences in responses of an application when the requ |
| [ProductCrawler/product_crawler](https://github.com/ProductCrawler/product_crawler) | 23 | - | The Open Source Search Engine for Product Components |
| [finnsson/crawlerjs](https://github.com/finnsson/crawlerjs) | 23 | JavaScript | AJAX-crawler that stores escaped fragment snapshots of #!/-sites that search engines can unders |
| [MultiX0/froxy](https://github.com/MultiX0/froxy) | 23 | TypeScript | Open-source web indexing engine built with Go, Node.js, and Next.js. Crawls pages, scores them  |

### Scrapers de producto/marketplace · `product-search` · 93 repos · 30,249 resultados en GitHub

**Shortlist:** [oxylabs/amazon-scraper](https://github.com/oxylabs/amazon-scraper) · [ChenglongChen/kaggle-CrowdFlower](https://github.com/ChenglongChen/kaggle-CrowdFlower) · [C0nw0nk/Nginx-Lua-Anti-DDoS](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS) · [drawrowfly/amazon-product-api](https://github.com/drawrowfly/amazon-product-api)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [oxylabs/amazon-scraper](https://github.com/oxylabs/amazon-scraper) | 3,408 | Python | Free Trial Amazon Scraper API for extracting search, product, offer listing, reviews, question  |
| [ChenglongChen/kaggle-CrowdFlower](https://github.com/ChenglongChen/kaggle-CrowdFlower) | 1,770 | C++ | 1st Place Solution for CrowdFlower Product Search Results Relevance Competition on Kaggle. |
| [C0nw0nk/Nginx-Lua-Anti-DDoS](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS) | 1,664 | Lua | A Anti-DDoS script to protect Nginx web servers using Lua with a HTML Javascript based authenti |
| [drawrowfly/amazon-product-api](https://github.com/drawrowfly/amazon-product-api) | 778 | JavaScript | Amazon Scraper. Scrape products from the amazon search result or reviews from the specific prod |
| [druv5319/Sneaks-API](https://github.com/druv5319/Sneaks-API) | 498 | JavaScript | A StockX, FlightClub, Goat, and Stadium Goods API all in one. This sneaker API allows users to  |
| [ChenglongChen/kaggle-HomeDepot](https://github.com/ChenglongChen/kaggle-HomeDepot) | 469 | Python | 3rd Place Solution for HomeDepot Product Search Results Relevance Competition on Kaggle. |
| [projectdiscovery/awesome-search-queries](https://github.com/projectdiscovery/awesome-search-queries) | 416 | Go | Community curated list of search queries for various products across multiple search engines. |
| [amazon-science/esci-data](https://github.com/amazon-science/esci-data) | 404 | Python | Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search |
| [kkapuria3/FREE-Amazon-BUY-Bot](https://github.com/kkapuria3/FREE-Amazon-BUY-Bot) | 389 | JavaScript | FREE Amazon BUY Bot is an Add to Cart and Auto Checkout Bot. This auto buying bot can search mu |
| [s87343472/backlink-pilot](https://github.com/s87343472/backlink-pilot) | 373 | JavaScript | Automated backlink submission toolkit for indie hackers — submit your product to directory site |
| [matsui528/nanopq](https://github.com/matsui528/nanopq) | 362 | Python | Pure python implementation of product quantization for nearest neighbor search |
| [askaitools/askaitools-community-edition](https://github.com/askaitools/askaitools-community-edition) | 354 | TypeScript | A cutting-edge search engine project tailored specifically for the AI product |
| [ivorpad/mercadona-cli](https://github.com/ivorpad/mercadona-cli) | 331 | Go | Unofficial, agent-friendly Mercadona shopping CLI (Go) — search products, read prices, build a  |
| [dwyl/learn-elasticsearch](https://github.com/dwyl/learn-elasticsearch) | 268 | Elixir | :mag: Learn how to use ElasticSearch to power a great search experience for your project/produc |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | - | Skip to content github / docs Code Issues 80 Pull requests 35 Discussions Actions Projects 2 Se |
| [ManojKumarPatnaik/Major-project-list](https://github.com/ManojKumarPatnaik/Major-project-list) | 259 | - | A list of practical projects that anyone can solve in any programming language (See solutions). |
| [DeMoriarty/TorchPQ](https://github.com/DeMoriarty/TorchPQ) | 236 | Cuda | Approximate nearest neighbor search with product quantization on GPU in pytorch and cuda |
| [zach22-1999/amazon-skills](https://github.com/zach22-1999/amazon-skills) | 232 | Python | Open-source Agent Skills for Amazon sellers: product research, feature validation, listing audi |
| [apiguru-app/amazon-scraper-v2](https://github.com/apiguru-app/amazon-scraper-v2) | 221 | Python | Agent-ready Amazon Scraper API: real-time product details (batch ASIN), offers & stock, reviews |
| [piyushpathak03/Recommendation-systems](https://github.com/piyushpathak03/Recommendation-systems) | 219 | Jupyter Notebook | Recommendation Systems This is a workshop on using Machine Learning and Deep Learning Technique |
| [Carmenliukang/1688_crawler-image_search_products](https://github.com/Carmenliukang/1688_crawler-image_search_products) | 201 | Python | 通过 1688 PC 端网址，上传图片查询类似的商品 |
| [sublay-io/monorepo](https://github.com/sublay-io/monorepo) | 182 | TypeScript | Infrastructure for user-powered products — pre-modeled bundles for comments, notifications, fil |
| [redis-developer/redis-product-search](https://github.com/redis-developer/redis-product-search) | 177 | TypeScript | Visual and semantic vector similarity with Redis Stack, FastAPI, PyTorch and Huggingface. |
| [mmdju/digikala-mcp](https://github.com/mmdju/digikala-mcp) | 160 | JavaScript | MCP server for Digikala: search, compare and price-check products on Iran's largest marketplace |
| [JahidHasanCO/BuyNow.-The-E-commerce-App](https://github.com/JahidHasanCO/BuyNow.-The-E-commerce-App) | 148 | Kotlin | Buy Now is an e-commerce app. In this app I use Machine Learning Algorithm for users can search |
| [Shashank02051997/Shotang-App](https://github.com/Shashank02051997/Shotang-App) | 144 | Java | The New Home Screen is designed in a modular way with the core focus on product discovery. Sear |
| [sulasoft/Amacapy-Bot-Telegram-Amazon-Affiliates](https://github.com/sulasoft/Amacapy-Bot-Telegram-Amazon-Affiliates) | 134 | Python | Amacapy is a software that does web scraping to the Amazon website and publishes them on Telegr |
| [lewpgs/migros-mcp](https://github.com/lewpgs/migros-mcp) | 133 | TypeScript | MCP server for Migros Switzerland product data - search products, nutrition info, store locatio |
| [LauraAddams/skincareAPI](https://github.com/LauraAddams/skincareAPI) | 132 | Ruby | An api of over 2,000 popular skincare products in the US, Korea, and Japan. Users can search by |
| [hoangsonww/MERN-Stack-Ecommerce-App](https://github.com/hoangsonww/MERN-Stack-Ecommerce-App) | 127 | JavaScript | 🛒 Welcome to Fusion Electronics -  a sample full-stack, lightweight, and modern online e-commer |

## 2. Catálogo y tienda

### Plataformas e-commerce · `ecommerce-platform` · 93 repos · 27,443 resultados en GitHub

**Shortlist:** [medusajs/medusa](https://github.com/medusajs/medusa) · [bagisto/bagisto](https://github.com/bagisto/bagisto) · [bagisto/opensource-ecommerce-mobile-app](https://github.com/bagisto/opensource-ecommerce-mobile-app) · [spree/spree](https://github.com/spree/spree)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [medusajs/medusa](https://github.com/medusajs/medusa) | 36,845 | TypeScript | The world's most flexible commerce platform for agents and developers |
| [bagisto/bagisto](https://github.com/bagisto/bagisto) | 28,270 | PHP | Open Source eCommerce & Multi-Vendor Marketplace Platform Built with Laravel for Enterprise-Sca |
| [bagisto/opensource-ecommerce-mobile-app](https://github.com/bagisto/opensource-ecommerce-mobile-app) | 16,074 | Dart | This open-source mobile ecommerce app seamlessly transforms your Bagisto store into a powerful  |
| [spree/spree](https://github.com/spree/spree) | 15,769 | Ruby | Open Source Platform for DTC, B2B Commerce, Marketplaces & Omnichannel. REST APIs, TypeScript S |
| [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) | 12,399 | JavaScript | Project has been discontinued ////// Mailchimp Open Commerce is an API-first, headless commerce |
| [woocommerce/woocommerce](https://github.com/woocommerce/woocommerce) | 10,561 | PHP | A customizable, open-source ecommerce platform built on WordPress. Build any commerce solution  |
| [evershopcommerce/evershop](https://github.com/evershopcommerce/evershop) | 10,519 | TypeScript | 🛍️ Typescript E-commerce Platform |
| [PrestaShop/PrestaShop](https://github.com/PrestaShop/PrestaShop) | 9,229 | PHP | PrestaShop is the universal open-source software platform to build your e-commerce solution. |
| [Sylius/Sylius](https://github.com/Sylius/Sylius) | 8,560 | PHP | Headless open-source eCommerce platform on top of PHP/Symfony/API Platform |
| [vendurehq/vendure](https://github.com/vendurehq/vendure) | 8,529 | TypeScript | Open-source headless commerce platform built with TypeScript, NestJS, React, and GraphQL |
| [simplcommerce/SimplCommerce](https://github.com/simplcommerce/SimplCommerce) | 4,413 | C# | A simple, cross platform, modulith ecommerce system built on .NET |
| [pimcore/pimcore](https://github.com/pimcore/pimcore) | 3,879 | PHP | Core Framework for the Open Core Data & Experience Management Platform (PIM, MDM, CDP, DAM, DXP |
| [shopware/shopware](https://github.com/shopware/shopware) | 3,453 | PHP | Shopware 6 is an open commerce platform based on Symfony Framework and Vue and supported by a w |
| [shuup/shuup](https://github.com/shuup/shuup) | 2,404 | Python | E-Commerce Platform |
| [beikeshop/beikeshop](https://github.com/beikeshop/beikeshop) | 1,980 | PHP | Free and Open-Source, Easy-to-Use Laravel eCommerce Platform,It supports multiple languages and |
| [ever-co/ever-demand](https://github.com/ever-co/ever-demand) | 1,867 | TypeScript | Ever® Demand™ - Open Commerce Platform - https://everdemand.co |
| [mercurjs/mercur](https://github.com/mercurjs/mercur) | 1,861 | TypeScript | The complete open source platform to run your entire marketplace. Storefront, vendor panel, adm |
| [smartstore/Smartstore](https://github.com/smartstore/Smartstore) | 1,736 | C# | A modular, scalable and ultra-fast open-source all-in-one eCommerce platform built on ASP.NET C |
| [netlify/gocommerce](https://github.com/netlify/gocommerce) | 1,616 | Go | A headless e-commerce for JAMstack sites. |
| [kirilkirkov/Ecommerce-CodeIgniter-Bootstrap](https://github.com/kirilkirkov/Ecommerce-CodeIgniter-Bootstrap) | 1,436 | PHP | Responsive, Multi-Vendor, MultiLanguage Online Store Platform (shopping cart solution) |
| [grandnode/grandnode2](https://github.com/grandnode/grandnode2) | 1,336 | C# | Open-source eCommerce platform for C# and ASP.NET Core 10 with MongoDB. Build multi-store shops |
| [VirtoCommerce/vc-platform](https://github.com/VirtoCommerce/vc-platform) | 1,314 | C# | Virto's Commerce Innovation Platform. Source-available, modular .NET commerce backend built on  |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | 1,215 | Python | E-commerce skills for AI agents — product research, marketing automation, supply chain optimiza |
| [drhenner/ror_ecommerce](https://github.com/drhenner/ror_ecommerce) | 1,208 | Ruby | Ruby on Rails Ecommerce platform, perfect for your small business solution. |
| [thelia/thelia](https://github.com/thelia/thelia) | 882 | PHP | Thelia is an open-source e-commerce CMS and framework built on Symfony 7 and API Platform. |
| [storefront-foundation/react-storefront](https://github.com/storefront-foundation/react-storefront) | 839 | JavaScript | React Storefront - PWA for eCommerce. 100% offline, platform agnostic, headless, Magento 2 supp |
| [olivrg/Awesome-Open-Source-eCommerce-Platforms](https://github.com/olivrg/Awesome-Open-Source-eCommerce-Platforms) | 545 | - | Awesome list of open source e-commerce platforms |
| [strangerstudios/paid-memberships-pro](https://github.com/strangerstudios/paid-memberships-pro) | 532 | PHP | The Trusted Membership Platform That Grows with You: Restrict access to content and charge recu |
| [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) | 425 | Shell | E-commerce product image generator skill — 39 scenario templates, GPT-Image-2/2.5 (Flare/Sunbur |
| [dennisivy/proshop_django](https://github.com/dennisivy/proshop_django) | 422 | JavaScript | Full-stack eCommerce platform built with Django REST Framework and React/Redux |

### Storefronts headless · `headless-storefront` · 36 repos · 724 resultados en GitHub

**Shortlist:** [spree/spree](https://github.com/spree/spree) · [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) · [vuestorefront/vue-storefront](https://github.com/vuestorefront/vue-storefront) · [bagisto/nextjs-commerce](https://github.com/bagisto/nextjs-commerce)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [spree/spree](https://github.com/spree/spree) | 15,769 | Ruby | Open Source Platform for DTC, B2B Commerce, Marketplaces & Omnichannel. REST APIs, TypeScript S |
| [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) | 12,399 | JavaScript | Project has been discontinued ////// Mailchimp Open Commerce is an API-first, headless commerce |
| [vuestorefront/vue-storefront](https://github.com/vuestorefront/vue-storefront) | 10,959 | - | Alokai is a Frontend as a Service solution that simplifies composable commerce. It connects all |
| [bagisto/nextjs-commerce](https://github.com/bagisto/nextjs-commerce) | 6,430 | TypeScript | Open source headless commerce that’s fast, flexible, and built to scale,launch stunning storefr |
| [itswadesh/svelte-commerce](https://github.com/itswadesh/svelte-commerce) | 1,821 | Svelte | Open-source headless SvelteKit storefront for 26 commerce backends — Medusa, Shopify, Saleor, V |
| [saleor/storefront](https://github.com/saleor/storefront) | 1,634 | TypeScript | Saleor Storefront built using React, Next.js with App Router, TypeScript, GraphQL, and Tailwind |
| [storefront-foundation/react-storefront](https://github.com/storefront-foundation/react-storefront) | 839 | JavaScript | React Storefront - PWA for eCommerce. 100% offline, platform agnostic, headless, Magento 2 supp |
| [CromwellCMS/Cromwell](https://github.com/CromwellCMS/Cromwell) | 753 | TypeScript | WordPress-like CMS for Next.js websites |
| [reactioncommerce/example-storefront](https://github.com/reactioncommerce/example-storefront) | 612 | JavaScript | Example Storefront is Reaction Commerce’s headless ecommerce storefront - Next.js, GraphQL, Rea |
| [thomasKn/astro-shopify](https://github.com/thomasKn/astro-shopify) | 505 | Astro | A lightweight and powerful ecommerce starter theme to build headless Shopify storefronts with A |
| [instantcommerce/shopify-headless-theme](https://github.com/instantcommerce/shopify-headless-theme) | 414 | CSS | Liquid theme that automatically redirects customers to your custom storefront. |
| [Weaverse/pilot](https://github.com/Weaverse/pilot) | 388 | TypeScript | A fully-featured Shopify Hydrogen theme crafted to help you launch modern, high-performing head |
| [graphcommerce-org/graphcommerce](https://github.com/graphcommerce-org/graphcommerce) | 362 | TypeScript | GraphCommerce® is a headless storefront replacement for Magento 2 (PWA), that delivers a faster |
| [frontvibe/fluid](https://github.com/frontvibe/fluid) | 290 | TypeScript | Fluid is a Hydrogen theme that lets you easily build Shopify headless storefronts by organizing |
| [vendurehq/storefront-qwik-starter](https://github.com/vendurehq/storefront-qwik-starter) | 265 | TypeScript | An e-commerce storefront starter built with Qwik and Vendure |
| [zackha/nuxtcommerce](https://github.com/zackha/nuxtcommerce) | 247 | Vue | An open-source, dynamic e-commerce solution powered by Nuxt 4 and GraphQL, headless storefront  |
| [shopware/frontends](https://github.com/shopware/frontends) | 230 | TypeScript | Shopware Frontends is a framework for building custom, headless storefronts with Shopware 6. |
| [vendurehq/storefront-remix-starter](https://github.com/vendurehq/storefront-remix-starter) | 227 | TypeScript | A storefront starter kit for Vendure built with Remix |
| [mirumee/nimara-ecommerce](https://github.com/mirumee/nimara-ecommerce) | 131 | TypeScript | Headless, composable ecommerce storefront built with Next.js, Typescript, and shadcn/ui. |
| [bagisto/headless-ecommerce](https://github.com/bagisto/headless-ecommerce) | 111 | PHP | Laravel Headless eCommerce APIs allow you to experience seamless and easily scalable storefront |
| [ecomplus/storefront](https://github.com/ecomplus/storefront) | 102 | JavaScript | Modern and high performant headless eCommerce Storefront. PWA & JAMstack architecture ready for |
| [swellstores/origin-theme](https://github.com/swellstores/origin-theme) | 100 | Vue | Headless NuxtJS 2 storefront starter powered by Swell |
| [swellstores/horizon](https://github.com/swellstores/horizon) | 72 | TypeScript | Headless NextJS storefront starter powered by Swell |
| [spree/storefront](https://github.com/spree/storefront) | 68 | TypeScript | Open-source Next.js eCommerce storefront for @spree. DTC & B2B, Stripe/Adyen/PayPal payments, m |
| [perryraskin/nextjs-tailwind-shopify-storefront](https://github.com/perryraskin/nextjs-tailwind-shopify-storefront) | 62 | TypeScript | Starter template for a Shopify Headless React Storefront using TailwindCSS |
| [hubblecommerce/hubble-frontend-pwa](https://github.com/hubblecommerce/hubble-frontend-pwa) | 60 | TypeScript | E-Commerce PWA Storefront - Shopware 6 Nuxt.JS Storefront |
| [ecomplus/cloud-commerce](https://github.com/ecomplus/cloud-commerce) | 54 | TypeScript | Complete platform on top of headless commerce APIs. High performant Astro + Vue storefront with |
| [DivanteLtd/spartacus-capybara](https://github.com/DivanteLtd/spartacus-capybara) | 45 | TypeScript | SAP Spartacus Theme based on https://storefrontui.io look and feel and design system. Headless  |
| [GatsbyStorefront/gatsby-starter-storefront-shopify](https://github.com/GatsbyStorefront/gatsby-starter-storefront-shopify) | 44 | JavaScript | Starter package for faster setup process of Gatsby Storefront. |
| [Agilo/medusawp](https://github.com/Agilo/medusawp) | 40 | PHP | MedusaWP enables you to use WordPress as a headless CMS or as a storefront for your Medusa shop |

### Software de marketplace · `marketplace-software` · 98 repos · 15,704 resultados en GitHub

**Shortlist:** [bagisto/bagisto](https://github.com/bagisto/bagisto) · [spree/spree](https://github.com/spree/spree) · [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) · [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [bagisto/bagisto](https://github.com/bagisto/bagisto) | 28,270 | PHP | Open Source eCommerce & Multi-Vendor Marketplace Platform Built with Laravel for Enterprise-Sca |
| [spree/spree](https://github.com/spree/spree) | 15,769 | Ruby | Open Source Platform for DTC, B2B Commerce, Marketplaces & Omnichannel. REST APIs, TypeScript S |
| [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) | 12,399 | JavaScript | Project has been discontinued ////// Mailchimp Open Commerce is an API-first, headless commerce |
| [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | 9,626 | TypeScript | A Web3 wallet and agent platform for the Unicity network - crypto wallet, DMs, group chat, and  |
| [jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace) | 2,858 | Python | Model-agnostic agent-skills platform with a harness-free canonical layer, verified adapters, an |
| [sharetribe/sharetribe](https://github.com/sharetribe/sharetribe) | 2,448 | Ruby | Sharetribe Go is Sharetribe's old source-available marketplace software, which was also availab |
| [FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform) | 2,407 | Python | Build tested agent skills and govern their lifecycle through a user-defined marketplace: eviden |
| [Websoft9/websoft9](https://github.com/Websoft9/websoft9) | 2,131 | TypeScript | Applications self-hosting and DevOps platform for running open source, web-based linux Panel of |
| [beikeshop/beikeshop](https://github.com/beikeshop/beikeshop) | 1,980 | PHP | Free and Open-Source, Easy-to-Use Laravel eCommerce Platform,It supports multiple languages and |
| [yint-tech/sekiro-open](https://github.com/yint-tech/sekiro-open) | 1,912 | Java | SEKIRO is a multi-language, distributed, network topology-independent service publishing platfo |
| [ever-co/ever-demand](https://github.com/ever-co/ever-demand) | 1,867 | TypeScript | Ever® Demand™ - Open Commerce Platform - https://everdemand.co |
| [mercurjs/mercur](https://github.com/mercurjs/mercur) | 1,861 | TypeScript | The complete open source platform to run your entire marketplace. Storefront, vendor panel, adm |
| [openilink/openilink-hub](https://github.com/openilink/openilink-hub) | 1,594 | Go | 开源微信 Bot 管理平台 + App 应用市场 / Self-hosted WeChat Bot Platform with App Marketplace / Lark · Slack  |
| [enatega/food-delivery-multivendor](https://github.com/enatega/food-delivery-multivendor) | 1,404 | TypeScript | Enatega is a fully customizable and scalable delivery management system that supports multiple  |
| [moyangzhan/langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin) | 1,383 | Java | AI 应用平台（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） / AI application platform (Chat,Draw,RAG,Workflow,M |
| [grandnode/grandnode2](https://github.com/grandnode/grandnode2) | 1,336 | C# | Open-source eCommerce platform for C# and ASP.NET Core 10 with MongoDB. Build multi-store shops |
| [higress-group/himarket](https://github.com/higress-group/himarket) | 1,313 | Java | HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is  |
| [tanshuai/alphabiz](https://github.com/tanshuai/alphabiz) | 1,215 | JavaScript | Web3 YouTube Alternative - fully decentralized media platform and blockchain-based marketplace |
| [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) | 1,042 | JavaScript | A plugin marketplace for GitHub Copilot and other AI agents that provides Power Platform develo |
| [Cocolabs-SAS/cocorico](https://github.com/Cocolabs-SAS/cocorico) | 873 | PHP | 🚀 Cocorico has evolved into Second (www.scnd.com) - a powerful, scalable, and enterprise-ready  |
| [marketplacekit/marketplacekit](https://github.com/marketplacekit/marketplacekit) | 822 | PHP | A platform to create an online marketplace |
| [stripe/stripe-connect-rocketrides](https://github.com/stripe/stripe-connect-rocketrides) | 653 | Swift | Sample on-demand platform built on Stripe: Connect onboarding for pilots, iOS app for passenger |
| [coopcycle/coopcycle-web](https://github.com/coopcycle/coopcycle-web) | 605 | PHP | Logistics & marketplace platform. Only for worker-owned business. |
| [nft-api/nft-api](https://github.com/nft-api/nft-api) | 544 | - | The Moralis NFT API: Your ultimate ally for top-tier NFT dApps. Build gaming platforms, secure  |
| [open-condo-software/condo](https://github.com/open-condo-software/condo) | 424 | JavaScript | Condo is an Open Source property management SaaS that allows users to manage tickets, resident  |
| [Kooboo/Kooboo](https://github.com/Kooboo/Kooboo) | 345 | JavaScript | High-performance platform for building websites, e-commerce, and web applications—with Native A |
| [stelace/stelace](https://github.com/stelace/stelace) | 317 | JavaScript | Open-source marketplace backend in Node.js, empowering Web platforms with Search API, Automatio |
| [xiaodou-official/xiaodou-market](https://github.com/xiaodou-official/xiaodou-market) | 307 | - | 小豆集市｜数字商品交易平台：发卡寄售、卡密平台、虚拟发卡、寄售网。24 小时发卡平台、卡密自动发货；虚拟商品寄售免费开店，买家免注册，支付宝、微信收款（支付宝内可选花呗/信用卡，微信内可选信 |
| [getdokan/dokan](https://github.com/getdokan/dokan) | 287 | TypeScript | Multivendor marketplace platform for WordPress |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | - | Skip to content github / docs Code Issues 80 Pull requests 35 Discussions Actions Projects 2 Se |

### PIM (info de producto) · `pim` · 34 repos · 1,690 resultados en GitHub

**Shortlist:** [unopim/unopim](https://github.com/unopim/unopim) · [akeneo/pim-community-dev](https://github.com/akeneo/pim-community-dev) · [atrocore/atropim](https://github.com/atrocore/atropim)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [unopim/unopim](https://github.com/unopim/unopim) | 11,042 | PHP | Open source Product Information Management (PIM) and Digital Asset Management (DAM) platform bu |
| [akeneo/pim-community-dev](https://github.com/akeneo/pim-community-dev) | 1,046 | PHP | [Community Development Repository] The open source Product Information Management (PIM) |
| [akeneo/pim-community-standard](https://github.com/akeneo/pim-community-standard) | 436 | - | [Community Standard Edition] The open source Product Information Management (PIM) - please rais |
| [sajxraj/InventoryManagementSystem](https://github.com/sajxraj/InventoryManagementSystem) | 344 | Java | A software developed using Java SE which provides as easy way to track the products, suppliers, |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | - | Skip to content github / docs Code Issues 80 Pull requests 35 Discussions Actions Projects 2 Se |
| [ManojKumarPatnaik/Major-project-list](https://github.com/ManojKumarPatnaik/Major-project-list) | 259 | - | A list of practical projects that anyone can solve in any programming language (See solutions). |
| [atrocore/atrocore](https://github.com/atrocore/atrocore) | 240 | JavaScript | AtroCore is an enterprise-ready, highly configurable Business Application Platform for managing |
| [atrocore/atropim](https://github.com/atrocore/atropim) | 210 | PHP | AtroPIM is a flexible, highly configurable, modular, open-source product information management |
| [justdoinc/justdo](https://github.com/justdoinc/justdo) | 171 | - | Enterprise project and portfolio management. Official product information, demos and resources. |
| [jettbrains/-L-](https://github.com/jettbrains/-L-) | 166 | - | W3C Strategic Highlights  September 2019  This report was prepared for the September 2019 W3C A |
| [Rastaman4e/-1](https://github.com/Rastaman4e/-1) | 78 | - | NICEHASH PLATFORM TERMS OF USE AND NICEHASH MINING TERMS OF SERVICE   PLEASE READ THESE NICEHAS |
| [akeneo/pim-docs](https://github.com/akeneo/pim-docs) | 62 | CSS | [Community Documentation Repository] The open source Product Information Management (PIM) |
| [tmjeee/fuyuko](https://github.com/tmjeee/fuyuko) | 54 | TypeScript | An open source Master Data Management / Product Information Management application. Contributio |
| [Abhishekkt15/Pharmacy-Management-System](https://github.com/Abhishekkt15/Pharmacy-Management-System) | 53 | CSS | The main aim of the project is the management of the database of the pharmaceutical shop. This  |
| [hector-jewell/react-native-based-food-delivery-app](https://github.com/hector-jewell/react-native-based-food-delivery-app) | 46 | JavaScript | React Native based food delivery app is a fully realized and customizable food delivery applica |
| [projectworldsofficial/Jwellary-shop-PHP-MYSQL-](https://github.com/projectworldsofficial/Jwellary-shop-PHP-MYSQL-) | 43 | - | Free Download Online Jewellery Shopping System Php Project with source code. Online Jewellery S |
| [Mdshobu/Liberty-House-Club-Whitepaper](https://github.com/Mdshobu/Liberty-House-Club-Whitepaper) | 35 | - | # Liberty House Club **A Parallel Binance Chain to Enable Smart Contracts**  _NOTE: This docume |
| [VirtoCommerce/vc-module-catalog](https://github.com/VirtoCommerce/vc-module-catalog) | 34 | C# | Product information management module |
| [3scale-labs/3scale_ws_api_for_php](https://github.com/3scale-labs/3scale_ws_api_for_php) | 32 | PHP | 3scale integration plugin for PHP applications. 3scale is an API Infrastructure service which h |
| [marthaegrimaldi/food-ordering-app-react-native](https://github.com/marthaegrimaldi/food-ordering-app-react-native) | 31 | JavaScript | Food ordering app react native is a fully realized and customizable food delivery application t |
| [3scale-labs/3scale_ws_api_for_java](https://github.com/3scale-labs/3scale_ws_api_for_java) | 28 | Java | 3scale integration plugin for Java applications. 3scale is an API Infrastructure service which  |
| [yqmark/agreement](https://github.com/yqmark/agreement) | 27 | - | Privacy Policy introduction We understand the importance of personal information to you and wil |
| [glennneiger/Magento-2-affiliate-pro](https://github.com/glennneiger/Magento-2-affiliate-pro) | 26 | - | # MAGENTO 2 AFFILIATE PRO  This is a perfect extension for you to create your affiliate program |
| [denman2328/Help](https://github.com/denman2328/Help) | 26 | - | ------------------ System Information ------------------ Time of this report: 8/10/2013, 08:36: |
| [PaulVerhoeven1/grocy-dutch-supermarket](https://github.com/PaulVerhoeven1/grocy-dutch-supermarket) | 24 | Python | Python application that searches for product infromation with the Jumbo.com or AH.nl api to dow |
| [TanayGhanshyam/crispy-octo-guide](https://github.com/TanayGhanshyam/crispy-octo-guide) | 24 | - | We have come a long way since I was a child in the 1960s when all I wanted for Christmas was a  |
| [pimify/pimify](https://github.com/pimify/pimify) | 23 | Python | Pimify is an open-source product information management software built on the simple stack of D |
| [Mario-Kart-Felix/solar-wind-hacker-book](https://github.com/Mario-Kart-Felix/solar-wind-hacker-book) | 23 | - | 2020 was a roller coaster of major, world-shaking events. We all couldn't wait for the year to  |
| [3scale-labs/3scale_ws_api_for_nodejs](https://github.com/3scale-labs/3scale_ws_api_for_nodejs) | 22 | CoffeeScript | 3scale is an API Infrastructure service which handles API Keys, Rate Limiting, Analytics, Billi |
| [Poovizhi-Muthusamy/Stock-management-and-bill-handling](https://github.com/Poovizhi-Muthusamy/Stock-management-and-bill-handling) | 21 | - | File handling is used to record the stock’s  information like name, code, quantity and rate. Pr |

## 3. Canales de venta

### Integración WhatsApp · `whatsapp` · 92 repos · 232,760 resultados en GitHub

**Shortlist:** [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) · [wwebjs/whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js) · [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api) · [devlikeapro/waha](https://github.com/devlikeapro/waha) · [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | 38,074 | Ruby | Open-source live-chat, email support, omni-channel desk. An alternative to Intercom, Zendesk, S |
| [GorvGoyl/Clone-Wars](https://github.com/GorvGoyl/Clone-Wars) | 37,145 | - | 100+ open-source clones of popular sites like Airbnb, Amazon, Instagram, Netflix, Tiktok, Spoti |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 30,977 | TypeScript | A lightweight alternative to OpenClaw that runs in containers for security. Connects to WhatsAp |
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 26,045 | - | 280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord |
| [wechaty/wechaty](https://github.com/wechaty/wechaty) | 23,393 | TypeScript | Conversational RPA SDK for Chatbot Makers. Join our Discord: https://discord.gg/7q8NBZbQzt |
| [wwebjs/whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js) | 22,772 | JavaScript | A WhatsApp client library for NodeJS that connects through the WhatsApp Web browser app |
| [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | 16,079 | TypeScript | Free, Open Source, Self-Hosted WhatsApp API Gateway |
| [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | 15,106 | TypeScript | 本地优先的跨平台 Claude Code / AI Agent 桌面工作台：多 Agent 协作、Git Worktree、代码 Diff、技能市场、多模型、Computer Use、桌面宠 |
| [tinode/chat](https://github.com/tinode/chat) | 13,528 | Go | Instant messaging platform. Backend in Go. Clients: Swift iOS, Java Android, JS webapp, scripta |
| [wangrongding/wechat-bot](https://github.com/wangrongding/wechat-bot) | 11,451 | JavaScript | 🤖 Multi-platform IM AI Agent for Telegram, WhatsApp, Lark, and WeChat. Connects ChatGPT / Claud |
| [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | 11,415 | JavaScript | Socket-based TS/JavaScript API for WhatsApp Web |
| [evolution-foundation/evolution-api](https://github.com/evolution-foundation/evolution-api) | 9,916 | TypeScript | Evolution API is an open-source WhatsApp integration API |
| [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | 8,156 | JavaScript | A simple WhatsApp bot to manage groups |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 7,968 | Kotlin | The chat decision assistant: before you reply, Jev reads the chat, judges intent and risk, and  |
| [devlikeapro/waha](https://github.com/devlikeapro/waha) | 7,654 | TypeScript | WAHA - WhatsApp HTTP API (REST API) that you can configure in a click! Multiple engines: WEBJS  |
| [tulir/whatsmeow](https://github.com/tulir/whatsmeow) | 7,630 | Go | Go library for the WhatsApp web multidevice API |
| [42wim/matterbridge](https://github.com/42wim/matterbridge) | 7,591 | Go | bridge between mattermost, IRC, gitter, xmpp, slack, discord, telegram, rocketchat, twitch, ssh |
| [tgalal/yowsup](https://github.com/tgalal/yowsup) | 7,175 | Python | The WhatsApp lib |
| [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | 6,687 | Go | WhatsApp MCP server |
| [vynect/venom](https://github.com/vynect/venom) | 6,596 | TypeScript | Venom is a high-performance system developed with JavaScript to create a bot for WhatsApp, supp |
| [sigalor/whatsapp-web-reveng](https://github.com/sigalor/whatsapp-web-reveng) | 6,513 | JavaScript | Reverse engineering WhatsApp Web. |
| [Prince-Mendiratta/BotsApp](https://github.com/Prince-Mendiratta/BotsApp) | 5,526 | TypeScript | Your personal assistant, on WhatsApp! The most user friendly userbot for the platform! |
| [gommzystudio/device-activity-tracker](https://github.com/gommzystudio/device-activity-tracker) | 5,165 | TypeScript | A phone number can reveal whether a device is active, in standby or offline (and more). This Po |
| [aldinokemal/go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice) | 4,943 | Go | GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. B |
| [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | 4,786 | TypeScript | Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alterna |
| [meetfranz/franz](https://github.com/meetfranz/franz) | 4,728 | JavaScript | Franz is a free messaging app for services like WhatsApp, Slack, Messenger and many more. |
| [nikoksr/notify](https://github.com/nikoksr/notify) | 3,919 | Go | A dead simple Go library for sending notifications to various messaging services. |
| [askrella/whatsapp-chatgpt](https://github.com/askrella/whatsapp-chatgpt) | 3,794 | TypeScript | ChatGPT + DALL-E + WhatsApp = AI Assistant :rocket: :robot: |
| [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | 3,790 | JavaScript | 🦞 OpenClaw (Clawdbot/Moltbot) 汉化版 - 开源个人 AI 助手中文版 / Claude/ChatGPT LLM 接入 / WhatsApp/Telegram/D |
| [ramonszo/zuck.js](https://github.com/ramonszo/zuck.js) | 3,730 | TypeScript | A javascript library that lets you add stories EVERYWHERE. |

### CRM · `crm` · 95 repos · 272,887 resultados en GitHub

**Shortlist:** [twentyhq/twenty](https://github.com/twentyhq/twenty) · [frappe/erpnext](https://github.com/frappe/erpnext) · [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) · [hcengineering/platform](https://github.com/hcengineering/platform)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | 59,219 | TypeScript | The open alternative to Salesforce, designed for AI. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | 40,434 | Python | Free and Open Source Enterprise Resource Planning (ERP) |
| [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | 39,967 | Java | 🔥 官方推荐 🔥 RuoYi-Vue 全新 Pro 版本，优化重构所有功能。基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + |
| [hcengineering/platform](https://github.com/hcengineering/platform) | 27,958 | TypeScript | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Moti |
| [monicahq/monica](https://github.com/monicahq/monica) | 25,513 | PHP | Personal CRM. Remember everything about your friends, family and business relationships. |
| [nocobase/nocobase](https://github.com/nocobase/nocobase) | 24,660 | TypeScript | NocoBase is an open-source AI + no-code platform for building business systems fast. Instead of |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 24,043 | PHP | Krayin CRM is Free & Open Source CRM Built with Laravel for Customer, Lead, and Sales Managemen |
| [YunaiV/yudao-cloud](https://github.com/YunaiV/yudao-cloud) | 19,658 | Java | ruoyi-vue-pro 全新 Cloud 版本，优化重构所有功能。基于 Spring Cloud Alibaba + MyBatis Plus + Vue & Element 实现的后台 |
| [illacloud/illa-builder](https://github.com/illacloud/illa-builder) | 12,334 | TypeScript | Low-code platform allows you to build business apps, enables you to quickly create internal too |
| [trycompai/crm](https://github.com/trycompai/crm) | 11,588 | TypeScript | Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM. |
| [akaunting/akaunting](https://github.com/akaunting/akaunting) | 10,200 | PHP | Online Accounting Software |
| [crmeb/CRMEB](https://github.com/crmeb/CRMEB) | 9,430 | Vue | 🔥CRMEB开源商城免费开源多语言商城系统，Tp6框架商城，系统可商用；包含小程序商城、H5商城、公众号商城、PC商城、App，支持分销、拼团、砍价、秒杀、优惠券、积分、会员等级、小程序直播 |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 8,905 | JavaScript | Free Open Source ERP CRM Software Accounting Invoicing / Node.Js React |
| [ever-co/ever-gauzy](https://github.com/ever-co/ever-gauzy) | 8,412 | TypeScript | Ever® Gauzy™ - Open Business Management Platform (ERP/CRM/HRM/ATS/PM) - https://gauzy.co |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 7,761 | PHP | Dolibarr ERP CRM is a modern software package to manage your company or foundation's activity ( |
| [openblocks-dev/openblocks](https://github.com/openblocks-dev/openblocks) | 6,238 | TypeScript | 🔥 🔥 🔥 The Open Source Retool Alternative |
| [SuiteCRM/SuiteCRM](https://github.com/SuiteCRM/SuiteCRM) | 5,806 | PHP | SuiteCRM - Open source CRM for the world |
| [macro-inc/macro](https://github.com/macro-inc/macro) | 4,810 | Rust | Macro is a unified workspace for teams: email, chat, docs, tasks, agents, calls, and CRM — @-li |
| [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | 4,786 | TypeScript | Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alterna |
| [Volmarg/personal-management-system](https://github.com/Volmarg/personal-management-system) | 4,182 | PHP | Your web application for managing personal data. |
| [yudaocode/yudao-ui-admin-vue3](https://github.com/yudaocode/yudao-ui-admin-vue3) | 3,915 | Vue | 芋道管理后台，基于 Vue3 + Element Plus 实现，支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP、 |
| [frappe/crm](https://github.com/frappe/crm) | 3,841 | Vue | Fully featured, open source CRM |
| [fatfreecrm/fat_free_crm](https://github.com/fatfreecrm/fat_free_crm) | 3,635 | Ruby | Ruby on Rails CRM platform |
| [espocrm/espocrm](https://github.com/espocrm/espocrm) | 3,508 | PHP | EspoCRM – Open Source CRM Application |
| [cirosantilli/china-dictatorship](https://github.com/cirosantilli/china-dictatorship) | 3,285 | HTML | 反中共政治宣传库。Anti Chinese government propaganda. 住在中国真名用户的网友请别给星星，不然你要被警察请喝茶。常见问答集，新闻集和饭店和音乐建议。卐习万岁 |
| [InvoicePlane/InvoicePlane](https://github.com/InvoicePlane/InvoicePlane) | 3,221 | PHP | A self-hosted open source application for managing your invoices, clients and payments. |
| [ONLYOFFICE/CommunityServer](https://github.com/ONLYOFFICE/CommunityServer) | 3,170 | C# | Free open source office suite with business productivity tools: document and project management |
| [crmeb/crmeb_java](https://github.com/crmeb/crmeb_java) | 3,078 | Vue | Java商城 免费 开源 CRMEB商城JAVA版，SpringBoot + Maven + Swagger + Mybatis Plus + Redis + Uniapp +Vue+ele |
| [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | 2,804 | Java | 🔥 Cordys 是由飞致云匠心打造的新一代的开源 AI CRM 系统，深度融合信息化、数字化与智能化能力，支持私有化部署，全面保障企业数据安全与主权。 |
| [frappe/frappe_docker](https://github.com/frappe/frappe_docker) | 2,603 | Python | Docker environment for developing, deploying, and running Frappe applications (ERPNext and cust |

### Email marketing · `email-marketing` · 16 repos · 791 resultados en GitHub

**Shortlist:** [vitorfs/colossus](https://github.com/vitorfs/colossus) · [ElliotKillick/rss2newsletter](https://github.com/ElliotKillick/rss2newsletter) · [agnitas-org/openemm](https://github.com/agnitas-org/openemm)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [vitorfs/colossus](https://github.com/vitorfs/colossus) | 574 | Python | Self-hosted email marketing solution |
| [ElliotKillick/rss2newsletter](https://github.com/ElliotKillick/rss2newsletter) | 282 | Python | Convert RSS/Atom feed to email newsletters |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | - | Skip to content github / docs Code Issues 80 Pull requests 35 Discussions Actions Projects 2 Se |
| [agnitas-org/openemm](https://github.com/agnitas-org/openemm) | 169 | JavaScript | Web-based software for email automation and marketing (newsletters, multi-stage mail campaigns, |
| [mailchimp/mc-magento2](https://github.com/mailchimp/mc-magento2) | 159 | PHP | MailChimp for Magento 2. Syncs all data (subscriber, customers, orders, products) and enables m |
| [AgriciDaniel/claude-email](https://github.com/AgriciDaniel/claude-email) | 132 | Python | AI-powered email management and marketing skill for Claude Code. Inbox triage, composition, qua |
| [mailchimp/mc-magento](https://github.com/mailchimp/mc-magento) | 120 | PHP | Mailchimp for Magento 1 Integration. Syncs all data (subscriber, customers, orders, products) a |
| [mailchimp/mc-woocommerce](https://github.com/mailchimp/mc-woocommerce) | 84 | PHP | MailChimp for Woocommerce Integration. Syncs all data (subscriber, customers, orders, products) |
| [marketinguys/awesome-email-marketing](https://github.com/marketinguys/awesome-email-marketing) | 61 | - | A curated list of tools, templates, platforms, and resources for email marketing, covering news |
| [sequence-so/sequence](https://github.com/sequence-so/sequence) | 55 | TypeScript | Sequence is an open source email marketing automation tool. |
| [krishna-build/claude-coach-kit](https://github.com/krishna-build/claude-coach-kit) | 46 | TypeScript | 🚀 Open-source marketing automation toolkit for coaches & solopreneurs — built entirely with Cla |
| [mailxem/mail](https://github.com/mailxem/mail) | 43 | Go | A thoughtful home for your email marketing. Open-source campaigns, automations, and APIs. Self- |
| [inboundnow/inbound-pro](https://github.com/inboundnow/inbound-pro) | 30 | PHP | Inbound Pro Plugin for WordPress - Landing Page Framework, Calls to Action Framework, Visitor A |
| [Mr-Asante/AI-Automations](https://github.com/Mr-Asante/AI-Automations) | 27 | - | A collection of Make.com AI automation blueprints for marketing, sales, and productivity — feat |
| [gh-ost00/SQL_Injection](https://github.com/gh-ost00/SQL_Injection) | 22 | - | Icegram Express - Email Subscribers, Newsletters and Marketing Automation Plugin <= 5.7.14 - Un |
| [achref-soua/helio](https://github.com/achref-soua/helio) | 20 | TypeScript | The open-source growth platform — AI-native marketing automation: CDP, segmentation, cross-chan |

### Meta/Facebook Ads · `facebook-ads` · 74 repos · 3,630 resultados en GitHub

**Shortlist:** [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) · [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) · [anudeepND/blacklist](https://github.com/anudeepND/blacklist) · [nonbili/Nora](https://github.com/nonbili/Nora)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) | 5,478 | - | Google Ads MCP server + Meta Ads MCP (Facebook Ads MCP) + Google Analytics MCP (GA4) + Search C |
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 1,323 | Python | Meta Ads (Facebook/Instagram) MCP server for Claude, ChatGPT, Perplexity & Cursor — the Meta no |
| [anudeepND/blacklist](https://github.com/anudeepND/blacklist) | 1,317 | Hosts File | Curated and well-maintained hostfile to block ads, tracking, cryptomining, and more! Updated re |
| [nonbili/Nora](https://github.com/nonbili/Nora) | 1,146 | TypeScript | SNS browser. Facebook, Instagram, Reddit, Threads, X and more in a single app. No ads. |
| [huanz/surge-hosts](https://github.com/huanz/surge-hosts) | 602 | - | hosts for surge,翻墙,强力去APP广告,google,facebook,twitter,youtube,etc |
| [ppgee/cocos-pnp](https://github.com/ppgee/cocos-pnp) | 390 | TypeScript | Cocos Playable Ads in Multi-Network(facebook, google, unity, tiktok etc.) |
| [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | 366 | Python | - |
| [SysAdminDoc/HushFacebook](https://github.com/SysAdminDoc/HushFacebook) | 345 | Java | Hushfacebook Morphe patches for Facebook. Hide ads, suggested posts, save videos and photos, tu |
| [proxy-intell/facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp) | 317 | Python | MCP Server for Facebook ADs Library - Get instant answers from FB's ad library |
| [RamsesAguirre777/facebook-ads-library-mcp](https://github.com/RamsesAguirre777/facebook-ads-library-mcp) | 278 | Python | Free, self-hosted MCP server that scrapes the public Facebook Ad Library (no API token) for com |
| [papa-torb/adtruth](https://github.com/papa-torb/adtruth) | 251 | HTML | Open-source ad fraud detection for small businesses using machine learning. Detect click fraud  |
| [megadose/facebook_totem](https://github.com/megadose/facebook_totem) | 181 | Python | Totem allows you to retrieve information about ads of a facebook page , we can retrieve the num |
| [fredericharnois/facebook-ads-reporting-google-apps-script](https://github.com/fredericharnois/facebook-ads-reporting-google-apps-script) | 178 | JavaScript | This script pushes Facebook Ads data to Google Sheets. |
| [dreamsoftin/facebook_audience_network](https://github.com/dreamsoftin/facebook_audience_network) | 153 | Swift | Flutter Facebook Audience Network |
| [vishalgojha/social-flow](https://github.com/vishalgojha/social-flow) | 151 | TypeScript | Run Meta operations without chaos.  Social Flow is a guided control plane for agencies, growth  |
| [lucasrcosta/facebook-js-ads-sdk](https://github.com/lucasrcosta/facebook-js-ads-sdk) | 141 | JavaScript | [DEPRECATED] OFFICIAL FACEBOOK SDK: https://github.com/facebook/facebook-nodejs-ads-sdk |
| [mgziminsky/FacebookTrackingRemoval](https://github.com/mgziminsky/FacebookTrackingRemoval) | 136 | JavaScript | Browser extension that removes ads and the user interaction tracking from content on Facebook |
| [edbizarro/laravel-facebook-ads](https://github.com/edbizarro/laravel-facebook-ads) | 135 | PHP | Facebook & Instagram Ads API for Laravel |
| [nonbili/Nora-Desktop](https://github.com/nonbili/Nora-Desktop) | 115 | - | Facebook, Instagram, Reddit, Threads and X in a single app. No ads. |
| [Lejo1/facebook_ad_library](https://github.com/Lejo1/facebook_ad_library) | 103 | HTML | Copy of the Ads from Facebook Ad Library API |
| [SHAJON-404/Facebook-Plus](https://github.com/SHAJON-404/Facebook-Plus) | 96 | Logos | A cleaner, ad‑free Facebook — no ads, no clutter, a few handy tweaks. |
| [songhuixiang/playable-demo](https://github.com/songhuixiang/playable-demo) | 93 | HTML | Bingo is a desktop application designed specifically for ad developers. It helps you quickly bu |
| [mikusnuz/meta-ads-mcp](https://github.com/mikusnuz/meta-ads-mcp) | 91 | TypeScript | MCP server for Meta Marketing API v25.0 — 135 tools for Facebook & Instagram ad campaign manage |
| [qcl/QCLean](https://github.com/qcl/QCLean) | 78 | JavaScript | QCLean - Remove Facebook Ads, Suggested Pages & Posts |
| [EfrainTorres/armavita-meta-ads-mcp](https://github.com/EfrainTorres/armavita-meta-ads-mcp) | 78 | Rust | Instagram & Facebook MCP server for Meta Marketing API v26 with secure token redaction, cursor  |
| [Xposed-Modules-Repo/tn.loukious.facebookappadsremover](https://github.com/Xposed-Modules-Repo/tn.loukious.facebookappadsremover) | 75 | Kotlin | Facebook App Ads Remover |
| [snegireff/facebook_ads_bigquery_etl](https://github.com/snegireff/facebook_ads_bigquery_etl) | 74 | Python | ETL based on google cloud function to save facebook ads statistics in google bigquery |
| [Vette1123/social-media-downloader](https://github.com/Vette1123/social-media-downloader) | 72 | TypeScript | Free, no-login downloader for public posts on TikTok, X, Instagram, Facebook, YouTube, Pinteres |
| [Loukious/FacebookAppAdsRemover](https://github.com/Loukious/FacebookAppAdsRemover) | 71 | Kotlin | Facebook App Ads Remover Xposed Module |
| [RitwikGA/FacebookReportingTool](https://github.com/RitwikGA/FacebookReportingTool) | 70 | JavaScript | Export Facebook Ads Data in Spreadsheet with the help of DIY sheet add-on |

## 4. Inventario y fulfillment

### Gestión de inventario · `inventory-management` · 94 repos · 139,640 resultados en GitHub

**Shortlist:** [inventree/InvenTree](https://github.com/inventree/InvenTree) · [cloudquery/cloudquery](https://github.com/cloudquery/cloudquery) · [glpi-project/glpi](https://github.com/glpi-project/glpi) · [GreaterWMS/GreaterWMS](https://github.com/GreaterWMS/GreaterWMS)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [inventree/InvenTree](https://github.com/inventree/InvenTree) | 7,743 | Python | Open Source Inventory Management System |
| [cloudquery/cloudquery](https://github.com/cloudquery/cloudquery) | 6,543 | Go | Data pipelines for cloud config and security data. Build cloud asset inventory, CSPM, FinOps, a |
| [glpi-project/glpi](https://github.com/glpi-project/glpi) | 6,488 | PHP | GLPI is a Free Asset and IT Management Software package, Data center management, ITIL Service D |
| [GreaterWMS/GreaterWMS](https://github.com/GreaterWMS/GreaterWMS) | 4,413 | Python | This Inventory management system is the currently Ford Asia Pacific after-sales logistics wareh |
| [allegro/ralph](https://github.com/allegro/ralph) | 2,529 | Python | Ralph is the CMDB / Asset Management system for data center and back office hardware. |
| [Part-DB/Part-DB-server](https://github.com/Part-DB/Part-DB-server) | 1,807 | PHP | Part-DB is an Open source inventory management system for your electronic components |
| [fjykTec/ModernWMS](https://github.com/fjykTec/ModernWMS) | 1,788 | Vue | The open source simple and complete warehouse management system is derived from our many years  |
| [nornir-automation/nornir](https://github.com/nornir-automation/nornir) | 1,632 | Python | Pluggable multi-threaded framework with inventory management to help operate collections of dev |
| [fabriziosalmi/certmate](https://github.com/fabriziosalmi/certmate) | 1,474 | Python | Self-hosted certificate lifecycle management: issue, renew, discover, inventory and deploy TLS  |
| [go2ismail/Asp.Net-Core-Inventory-Order-Management-System](https://github.com/go2ismail/Asp.Net-Core-Inventory-Order-Management-System) | 1,298 | C# | Now upgraded to .NET 9, this project is a super-fast, completely headless API powered by Clean  |
| [Blair2004/NexoPOS](https://github.com/Blair2004/NexoPOS) | 1,289 | PHP | Laravel-based web POS system with Vue.js, Tailwind CSS, inventory management, sales processing, |
| [bitbrain/pandora](https://github.com/bitbrain/pandora) | 1,128 | GDScript | Godot 4 addon for RPG data management such items, inventories, spells, mobs, quests and NPCs. |
| [openboxes/openboxes](https://github.com/openboxes/openboxes) | 917 | Groovy | OpenBoxes is a warehouse management system designed to manage inventory and track stock movemen |
| [FahimAnzamDip/triangle-pos](https://github.com/FahimAnzamDip/triangle-pos) | 874 | Blade | Triangle POS is an open source Inventory Management with POS System. Developed with Laravel 10, |
| [rubyforgood/human-essentials](https://github.com/rubyforgood/human-essentials) | 594 | Ruby | Human Essentials is an inventory management system for diaper, incontinence, and period-supply  |
| [amirsanni/Mini-Inventory-and-Sales-Management-System](https://github.com/amirsanni/Mini-Inventory-and-Sales-Management-System) | 561 | PHP | An Inventory and Sales Management System written in PHP (codeIgniter) with support for MySQL an |
| [fajarghifar/inventory-management-system](https://github.com/fajarghifar/inventory-management-system) | 525 | PHP | ✍Building an Inventory Management System with Laravel 10. |
| [ronknight/InventorySystem](https://github.com/ronknight/InventorySystem) | 469 | PHP | 🖥️Create an open-source Inventory Management System using CodeIgniter web framework, Php and My |
| [siamon123/warehouse-inventory-system](https://github.com/siamon123/warehouse-inventory-system) | 466 | PHP | Open source inventory management system with php and mysql |
| [ed-roh/inventory-management](https://github.com/ed-roh/inventory-management) | 440 | TypeScript | - |
| [Zakarialabib/myStockMaster](https://github.com/Zakarialabib/myStockMaster) | 440 | PHP | Your All-in-One Inventory and ERP Management with Laravel TALLSTACK |
| [mauricecalhoun/inventory](https://github.com/mauricecalhoun/inventory) | 432 | PHP | Inventory Management for Laravel 4 / 5 |
| [opendcim/openDCIM](https://github.com/opendcim/openDCIM) | 367 | PHP | An open source (GPL v3) Data Center Inventory Management (DCIM) application. |
| [zetavg/Inventory](https://github.com/zetavg/Inventory) | 361 | TypeScript | An RFID asset management app for home or businesses. |
| [harismuneer/Restaurant-Management-System](https://github.com/harismuneer/Restaurant-Management-System) | 348 | Java | 👨‍🍳  An Android based RMS that aims to digitalize the day to day processes of various restauran |
| [sajxraj/InventoryManagementSystem](https://github.com/sajxraj/InventoryManagementSystem) | 344 | Java | A software developed using Java SE which provides as easy way to track the products, suppliers, |
| [sadatrafsanjani/Point-of-Sales](https://github.com/sadatrafsanjani/Point-of-Sales) | 313 | Java | Point of Sales with inventory management system |
| [IndomaximTechID/storaji](https://github.com/IndomaximTechID/storaji) | 307 | PHP | :ledger: The light/responsive inventory management system available on Windows, macOS and Linux |
| [stemword/php-inventory-management-system](https://github.com/stemword/php-inventory-management-system) | 292 | PHP | Open source inventory management system with php and mysql Invoice generation and easy to downl |
| [mamun724682/Inventory-Management-System-Laravel-SPA](https://github.com/mamun724682/Inventory-Management-System-Laravel-SPA) | 271 | PHP | An Inventory and Sales Management System using Laravel 10, Inertia, Vue js (SPA) |

### Punto de venta (POS) · `pos` · 91 repos · 20,432 resultados en GitHub

**Shortlist:** [opensourcepos/opensourcepos](https://github.com/opensourcepos/opensourcepos) · [tngoman/Store-POS](https://github.com/tngoman/Store-POS) · [ucraft-com/POS-Awesome](https://github.com/ucraft-com/POS-Awesome) · [angkosal/laravel-pos](https://github.com/angkosal/laravel-pos)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [opensourcepos/opensourcepos](https://github.com/opensourcepos/opensourcepos) | 4,455 | PHP | Open Source Point of Sale is a web based point of sale application written in PHP using CodeIgn |
| [tngoman/Store-POS](https://github.com/tngoman/Store-POS) | 1,046 | TypeScript | Modern Electron Point of Sale — React till, Express + SQLite API, LAN multi-terminal, catalog/p |
| [ucraft-com/POS-Awesome](https://github.com/ucraft-com/POS-Awesome) | 518 | Vue | POS Awesome is an open-source Point of Sale for Erpnext using Vue.js and Vuetify |
| [angkosal/laravel-pos](https://github.com/angkosal/laravel-pos) | 509 | PHP | Web Based Point Of Sale(POS) Application using Laravel |
| [shanmugharajk/react-point-of-sale](https://github.com/shanmugharajk/react-point-of-sale) | 423 | JavaScript | A simple point of sale app built in nodejs and reactjs |
| [deenseth/PHP-Point-Of-Sale](https://github.com/deenseth/PHP-Point-Of-Sale) | 399 | PHP | PHP Point Of Sale (POS) is designed to help small businesses with keeping track of customers, i |
| [aryadwiputra/point-of-sales](https://github.com/aryadwiputra/point-of-sales) | 384 | JavaScript | Aplikasi kasir (point of sales) yang dibuat menggunakan Laravel 13, Inertia 3, React 19 dan Tai |
| [bagashiz/go-pos](https://github.com/bagashiz/go-pos) | 353 | Go | Simple RESTful Point of Sale (POS) Service API written in Go using Gin web framework, PostgreSQ |
| [sadatrafsanjani/Point-of-Sales](https://github.com/sadatrafsanjani/Point-of-Sales) | 313 | Java | Point of Sales with inventory management system |
| [livealvi/.NET-Point-of-Sale-POS--Csharp](https://github.com/livealvi/.NET-Point-of-Sale-POS--Csharp) | 290 | C# | This POS Project was developed with N-Tier Architecture in C# and follows Object Relational Map |
| [nursandiid/tutorial-membuat-aplikasi-point-of-sales](https://github.com/nursandiid/tutorial-membuat-aplikasi-point-of-sales) | 286 | HTML | Aplikasi Point Of Sales yang dibangun dengan Laravel v8 dan AdminLTE v2.4 |
| [papyrussolution/OpenPapyrus](https://github.com/papyrussolution/OpenPapyrus) | 286 | C++ | Sophisticated ERP, CRM, Point-Of-Sale, etc. Open source now. This system is developed since 199 |
| [fajarghifar/laravel-point-of-sale](https://github.com/fajarghifar/laravel-point-of-sale) | 255 | CSS | ✍️Building a Point of Sale system with Laravel 10. |
| [julvikramsupandi/flutter-pos-app-ui](https://github.com/julvikramsupandi/flutter-pos-app-ui) | 248 | Dart | Flutter Point Of Sale App UI |
| [AsjadIqbal/InventoryManagementSystem](https://github.com/AsjadIqbal/InventoryManagementSystem) | 234 | Java | This is an inventory management software built in Java using MySQL database that can be used at |
| [chrisidakwo/EFLInventory-V2](https://github.com/chrisidakwo/EFLInventory-V2) | 232 | PHP | :department_store: Point-of-sale and inventory tracking for small-scale retail stores. Easily m |
| [ViewTouch/viewtouch](https://github.com/ViewTouch/viewtouch) | 220 | C++ | ViewTouch Point of Sale (PoS) - official |
| [elrizwiraswara/flutter_pos](https://github.com/elrizwiraswara/flutter_pos) | 218 | Dart | A Point of Sale (POS) application built with Flutter, demonstrating Clean Architecture principl |
| [danderfer/Comp_Sci_Sem_2](https://github.com/danderfer/Comp_Sci_Sem_2) | 216 | Python | According to all known laws of aviation, there is no way that a bee should be able to fly. Its  |
| [hanlinag/point-of-sale-system](https://github.com/hanlinag/point-of-sale-system) | 215 | Java | Point of Sale System written in JAVAFX |
| [mailmug/laravel-easy-pos](https://github.com/mailmug/laravel-easy-pos) | 209 | PHP | Web Based Point Of Sale(POS) Application using Laravel |
| [st-tu-dresden/salespoint](https://github.com/st-tu-dresden/salespoint) | 202 | Java | A framework to develop point of sales applications, powered by Java and Spring Boot |
| [rudi-krsoftware/open-retail](https://github.com/rudi-krsoftware/open-retail) | 197 | C# | Perangkat lunak open source yang dikembangkan khusus untuk bidang usaha ritel, grosir, toko ban |
| [tariqbuilds/hunts-point-pos](https://github.com/tariqbuilds/hunts-point-pos) | 185 | JavaScript | A real-time, simple web Point of Sale system written in Node.js & Angular.js |
| [be-BOP-io-SA/be-BOP](https://github.com/be-BOP-io-SA/be-BOP) | 180 | TypeScript | The ethical sales toolbox. One libre platform for e-commerce, point of sale, subscriptions, tic |
| [amiuhle/kasisto](https://github.com/amiuhle/kasisto) | 173 | JavaScript | A Monero Point of Sale payment system |
| [mesinkasir/larapos](https://github.com/mesinkasir/larapos) | 168 | JavaScript | Laravel Point of sale with invoice full source code free download pos apps. |
| [BrainWise-DEV/POSNext](https://github.com/BrainWise-DEV/POSNext) | 168 | Vue | A modern, high-performance Point of Sale system for ERPNext with offline capabilities, real-tim |
| [hiramvillarreal/iotpos](https://github.com/hiramvillarreal/iotpos) | 165 | C++ | IotPOS, an open source Point of Sale software. |
| [go2ismail/POS---Point-Of-Sales](https://github.com/go2ismail/POS---Point-Of-Sales) | 160 | C# | Point of sales proof of concept developed using Asp.Net Core 2.2. Features: Customer, Vendor, P |

### Ruteo de entregas · `delivery-routing` · 27 repos · 5,948 resultados en GitHub

**Shortlist:** [VROOM-Project/vroom](https://github.com/VROOM-Project/vroom) · [grubhub/mdrplib](https://github.com/grubhub/mdrplib)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [VROOM-Project/vroom](https://github.com/VROOM-Project/vroom) | 1,898 | C++ | Vehicle Routing Open-source Optimization Machine |
| [zhnt/loushang](https://github.com/zhnt/loushang) | 1,831 | Python | AI-native agent harness for coding workflows by python: multi-model LLM orchestration, stateful |
| [zszszszsz/.config](https://github.com/zszszszsz/.config) | 363 | Shell | # # Automatically generated file; DO NOT EDIT. # OpenWrt Configuration # CONFIG_MODULES=y CONFI |
| [analytix-energy-solutions/ticker](https://github.com/analytix-energy-solutions/ticker) | 178 | Python | Smart notification management for Home Assistant. Centralized routing, user subscriptions, smar |
| [jettbrains/-L-](https://github.com/jettbrains/-L-) | 166 | - | W3C Strategic Highlights  September 2019  This report was prepared for the September 2019 W3C A |
| [dungtran209/Modelling-and-Analysis-of-a-Vehicle-Routing-Problem-with-Time-Windows-in-Freight-Delivery](https://github.com/dungtran209/Modelling-and-Analysis-of-a-Vehicle-Routing-Problem-with-Time-Windows-in-Freight-Delivery) | 156 | Python | A MSc's Dissertation Project which focuses on Vehicle Routing Problem with Time Windows (VRPTW) |
| [endmr11/routing_app](https://github.com/endmr11/routing_app) | 117 | Java | This project provides comprehensive solutions for vehicle routing, delivery scheduling, and opt |
| [grubhub/mdrplib](https://github.com/grubhub/mdrplib) | 78 | Python | Meal Delivery Routing Problem Test Instance Library |
| [txxa/hass-ans](https://github.com/txxa/hass-ans) | 70 | Python | Home Assistant integration for intelligent, centralized notification routing with advanced filt |
| [javonn13/AWS-Basic-for-Beginners](https://github.com/javonn13/AWS-Basic-for-Beginners) | 55 | - | This course will teach you AWS basics right through to advanced cloud computing concepts.  Idea |
| [NeiH4207/evrp-python](https://github.com/NeiH4207/evrp-python) | 41 | Python | The Electric Vehicle Routing Problem (EVRP) is a twist on the classic Vehicle Routing Problem ( |
| [ecterceocgan/pickup-delivery-vrp](https://github.com/ecterceocgan/pickup-delivery-vrp) | 39 | Python | Naive branching implementation of a specific pick-up and delivery vehicle routing optimization  |
| [aws-samples/delivery-routes-optimization-for-logistics](https://github.com/aws-samples/delivery-routes-optimization-for-logistics) | 33 | TypeScript | Optimize Delivery Route and Order Dispatching |
| [goyal-aman/email-router](https://github.com/goyal-aman/email-router) | 33 | Go | Email Router is a programmable SMTP proxy that multiplexes outbound email at runtime via plugin |
| [taxideftis/bathos](https://github.com/taxideftis/bathos) | 30 | Rust | AI Workflow Agent method of overwhelming depth — 18 specialist roles, a 7-wave delivery pipelin |
| [ShadowOS/Vechicle-Routing-Problem-VRP-with-Pickup-and-Delivery](https://github.com/ShadowOS/Vechicle-Routing-Problem-VRP-with-Pickup-and-Delivery) | 29 | Python | Pickup-and-Delivery Problems (PDPs) constitute an important family of routing problems in which |
| [kristogodari/drone-delivery-routing-algorithm](https://github.com/kristogodari/drone-delivery-routing-algorithm) | 25 | Java | Given a fleet of drones, a list of customer orders, and availability of the individual products |
| [VsevolodUstinov/openclaw-worker-relay](https://github.com/VsevolodUstinov/openclaw-worker-relay) | 24 | Python | Supervise Codex CLI and Claude Code workers from OpenClaw with async progress, routed delivery, |
| [Viewovershock24/american-truck-simulator-hack-2026-trucking-toolkit](https://github.com/Viewovershock24/american-truck-simulator-hack-2026-trucking-toolkit) | 24 | - | American Truck Simulator Hack 2026 themed PC companion for truck profiles, garage planning, upg |
| [Genius-Society/rogsoft_goofish](https://github.com/Genius-Society/rogsoft_goofish) | 24 | Classic ASP | Goofish for Asuswrt is a Koolcenter plugin that brings Xianyu shop automation to ASUS routers.  |
| [vnvo/deltaforge](https://github.com/vnvo/deltaforge) | 23 | Rust | A versatile, high-performance Change Data Capture (CDC) engine built in Rust. Streams database  |
| [Aiomx/Gisyit-Shop](https://github.com/Aiomx/Gisyit-Shop) | 23 | TypeScript | A high-performance, enterprise-ready full-stack e-commerce storefront built on React Router v7, |
| [RenatoMaynard/Routing-Problems-using-Google-Maps](https://github.com/RenatoMaynard/Routing-Problems-using-Google-Maps) | 22 | Jupyter Notebook | Optimal routing and delivery solutions using Google Maps and Python. |
| [ideas4u/Trading-Platform](https://github.com/ideas4u/Trading-Platform) | 22 | - | This project is the most awaited project in open source community where every user who belongs  |
| [Trinkle23897/URBER](https://github.com/Trinkle23897/URBER) | 21 | Python | Code for URBER: Ultrafast Rule-Based Escape Routing Method for Large-Scale Sample Delivery Bioc |
| [ZainJavaid/AlertNotify](https://github.com/ZainJavaid/AlertNotify) | 21 | JavaScript | Self-Healing Adaptive Notification Framework leveraging multi-threaded delivery and load-balanc |
| [meydanipamungkas/MATLAB_Code](https://github.com/meydanipamungkas/MATLAB_Code) | 20 | MATLAB | Code ini adalah Code Tugas Akhir berjudul "Multi-Objective Vehicle Routing Problem with Time Wi |

## 5. Dinero y facturación

### Facturación · `invoicing` · 97 repos · 72,818 resultados en GitHub

**Shortlist:** [midday-ai/midday](https://github.com/midday-ai/midday) · [invoiceninja/invoiceninja](https://github.com/invoiceninja/invoiceninja) · [akaunting/akaunting](https://github.com/akaunting/akaunting) · [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [midday-ai/midday](https://github.com/midday-ai/midday) | 15,087 | TypeScript | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant |
| [invoiceninja/invoiceninja](https://github.com/invoiceninja/invoiceninja) | 10,312 | PHP | A source-available invoice, quote, project and time-tracking app built with Laravel |
| [akaunting/akaunting](https://github.com/akaunting/akaunting) | 10,200 | PHP | Online Accounting Software |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 8,905 | JavaScript | Free Open Source ERP CRM Software Accounting Invoicing / Node.Js React |
| [ever-co/ever-gauzy](https://github.com/ever-co/ever-gauzy) | 8,412 | TypeScript | Ever® Gauzy™ - Open Business Management Platform (ERP/CRM/HRM/ATS/PM) - https://gauzy.co |
| [crater-invoice-inc/crater](https://github.com/crater-invoice-inc/crater) | 8,354 | PHP | Open Source Invoicing Solution for Individuals & Businesses |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 7,761 | PHP | Dolibarr ERP CRM is a modern software package to manage your company or foundation's activity ( |
| [alvarcarto/url-to-pdf-api](https://github.com/alvarcarto/url-to-pdf-api) | 7,106 | HTML | Web page PDF/PNG rendering done right. Self-hosted service for rendering receipts, invoices, or |
| [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | 6,755 | TypeScript | Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom pr |
| [al1abb/invoify](https://github.com/al1abb/invoify) | 6,379 | TypeScript | An invoice generator app built using Next.js, Typescript, and Shadcn |
| [hql287/Manta](https://github.com/hql287/Manta) | 5,486 | JavaScript | 🎉 Flexible invoicing desktop app with beautiful & customizable templates. |
| [kimai/kimai](https://github.com/kimai/kimai) | 5,087 | PHP | Kimai is the #1 open-source time-tracking application. From freelancers to companies and organi |
| [bigcapitalhq/bigcapital](https://github.com/bigcapitalhq/bigcapital) | 3,950 | TypeScript | 💵 Independent financial accounting with intelligent reporting, alternative to Quickbooks, Xero, |
| [InvoicePlane/InvoicePlane](https://github.com/InvoicePlane/InvoicePlane) | 3,221 | PHP | A self-hosted open source application for managing your invoices, clients and payments. |
| [naiveHobo/InvoiceNet](https://github.com/naiveHobo/InvoiceNet) | 2,699 | Python | Deep neural network to extract intelligent information from invoice documents. |
| [OnedocLabs/react-print-pdf](https://github.com/OnedocLabs/react-print-pdf) | 2,559 | TypeScript | Build and generate PDF using React 📄 UI kit for PDFs and print documents. Simple, reusable comp |
| [Django-CRM/Django-CRM](https://github.com/Django-CRM/Django-CRM) | 2,456 | Python | BottleCRM: free, open-source (MIT) CRM with sales, support tickets and invoicing in one app. Un |
| [invoice-x/invoice2data](https://github.com/invoice-x/invoice2data) | 2,236 | Python | Extract structured data from PDF invoices |
| [Hasnayeen/invobook](https://github.com/Hasnayeen/invobook) | 2,234 | PHP | Self-hosted app for Time Tracking, Invoice Generation, Project & Client Management, built with  |
| [maaslalani/invoice](https://github.com/maaslalani/invoice) | 2,197 | Go | Command line invoice generator |
| [InvoiceShelf/InvoiceShelf](https://github.com/InvoiceShelf/InvoiceShelf) | 1,865 | PHP | Open Source Invoicing Solution for Individuals & Businesses |
| [invoiceninja/admin-portal](https://github.com/invoiceninja/admin-portal) | 1,755 | Dart | Invoice Ninja: Desktop/mobile admin portal built with Flutter |
| [sparksuite/simple-html-invoice-template](https://github.com/sparksuite/simple-html-invoice-template) | 1,726 | HTML | A modern, clean, and very simple responsive HTML invoice template |
| [panshak/accountill](https://github.com/panshak/accountill) | 1,698 | JavaScript | Fullstack open source Invoicing application made with MongoDB, Express, React & Nodejs (MERN) |
| [LaravelDaily/laravel-invoices](https://github.com/LaravelDaily/laravel-invoices) | 1,549 | PHP | Laravel package to generate PDF invoices from various customizable parameters |
| [andrewdwallo/erpsaas](https://github.com/andrewdwallo/erpsaas) | 1,478 | PHP | A Laravel and Filament-powered accounting platform featuring full double-entry accrual accounti |
| [kdeldycke/awesome-billing](https://github.com/kdeldycke/awesome-billing) | 1,359 | - | 💰 Billing & Payments knowledge for cloud platforms |
| [meteroid-oss/meteroid](https://github.com/meteroid-oss/meteroid) | 1,338 | Rust | Open-source Pricing and Billing Infrastructure 🚀 Subscription management, Invoicing, Pricing, U |
| [piratuks/invoice-builder](https://github.com/piratuks/invoice-builder) | 1,319 | TypeScript | Invoice and quotation builder desktop app with PDF export, designed for small businesses and fr |
| [cmichi/latex-template-collection](https://github.com/cmichi/latex-template-collection) | 1,265 | TeX | Collection of different LaTeX/XeTeX templates (cv, invoices, timesheets, letters, etc.). |

### OCR de documentos · `document-ocr` · 6 repos · 234 resultados en GitHub

**Shortlist:** [ReceiptManager/receipt-parser-legacy](https://github.com/ReceiptManager/receipt-parser-legacy) · [agrawalamod/Receipt-Scanner-in-OpenCV](https://github.com/agrawalamod/Receipt-Scanner-in-OpenCV)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [ReceiptManager/receipt-parser-legacy](https://github.com/ReceiptManager/receipt-parser-legacy) | 853 | Python | A supermarket receipt parser written in Python using tesseract OCR |
| [knotsberryofficial-hash/n8n-node-billflux-invoice-receipt-ocr](https://github.com/knotsberryofficial-hash/n8n-node-billflux-invoice-receipt-ocr) | 81 | TypeScript | - |
| [veryfi/veryfi-nodejs](https://github.com/veryfi/veryfi-nodejs) | 32 | JavaScript | Node.js module for communicating with the Veryfi OCR API. // read: https://veryfi.com/nodejs |
| [veryfi/veryfi-python](https://github.com/veryfi/veryfi-python) | 31 | Python | Python module for communicating with the Veryfi OCR API. |
| [veryfi/veryfi-go](https://github.com/veryfi/veryfi-go) | 24 | Go | Go module for communicating with the Veryfi OCR API. |
| [agrawalamod/Receipt-Scanner-in-OpenCV](https://github.com/agrawalamod/Receipt-Scanner-in-OpenCV) | 21 | C++ | Image Analysis Project: Built a system to take images of receipts or invoices as input and segm |

## 6. Plataforma de IA y orquestación

### Frameworks de agentes IA · `ai-agent-framework` · 97 repos · 19,785 resultados en GitHub

**Shortlist:** [obra/superpowers](https://github.com/obra/superpowers) · [langchain-ai/langchain](https://github.com/langchain-ai/langchain) · [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) · [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 303,191 | Shell | An agentic skills framework & software development methodology that works. |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 148,231 | Python | The agent engineering platform. |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70,955 | Python | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 69,267 | TypeScript | Write HTML. Render video. Built for agents. |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 61,518 | Python | A programming framework for agentic AI |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 59,966 | Python | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative inte |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 49,259 | Python | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, t |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 43,678 | Python | Build resilient agents. |
| [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | 42,635 | Python | AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins  |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 34,822 | Python | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST  |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 30,205 | Python | A lightweight, powerful framework for multi-agent workflows |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 29,763 | TypeScript | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs,  |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | 28,986 | TypeScript | Mastra is the modern TypeScript framework for AI-powered applications and agents. |
| [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 26,819 | TypeScript | What are the principles we can use to build LLM-powered software that is actually good enough t |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 26,804 | Python | Open-source AI orchestration framework for building context-engineered, production-ready LLM ap |
| [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | 26,446 | Python | An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone |
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 19,633 | TypeScript | Open source agentic operating system |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | 19,536 | Python | Agent Zero AI framework |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,947 | Python | 🐫 CAMEL: The first and the best multi-agent framework. Finding the Scaling Law of Agents. https |
| [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,711 | Python | <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to b |
| [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | 16,826 | HTML | AI 时代的伯克希尔：基于 Claude Code / Codex 的价值投资研究框架。巴菲特·芒格·段永平·李录四大师方法论 + 多Agent并行研究。/ AI-era Berkshire |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | 16,699 | Python | Open Source framework for voice agents, multimodal apps, and realtime AI. Maintained by Daily a |
| [raga-ai-hub/RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16,179 | Python | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features l |
| [livekit/agents](https://github.com/livekit/agents) | 14,885 | Python | A framework for building realtime voice AI agents 🤖🎙️📹 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 14,258 | Python | A framework for building, orchestrating and deploying AI agents and multi-agent workflows with  |
| [pestphp/pest](https://github.com/pestphp/pest) | 11,743 | PHP | The elegant testing framework for PHP developers and AI agents. |
| [TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework) | 11,188 | Python | Open-source framework for conversational voice AI agents |
| [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | 11,045 | Java | Agentic AI Framework for Java Developers |
| [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | 10,968 | Python | Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 10,854 | TypeScript | AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework |

### Gateways/ruteo LLM · `llm-gateway` · 99 repos · 11,376 resultados en GitHub

**Shortlist:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow) · [BerriAI/litellm](https://github.com/BerriAI/litellm) · [QuantumNous/new-api](https://github.com/QuantumNous/new-api) · [casdoor/casdoor](https://github.com/casdoor/casdoor)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,258 | Python | An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the he |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 61,758 | Python | The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or nat |
| [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 50,421 | Go | A unified AI model hub for aggregation & distribution. It supports cross-converting various LLM |
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | 14,629 | Go | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and au |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 13,245 | TypeScript | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails w |
| [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk) | 10,868 | Go | Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Proto |
| [coaidev/coai](https://github.com/coaidev/coai) | 9,333 | TypeScript | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade  |
| [maximhq/bifrost](https://github.com/maximhq/bifrost) | 9,004 | Go | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent  |
| [mnfst/llm-gateway](https://github.com/mnfst/llm-gateway) | 7,595 | TypeScript | Open Source LLM Gateway 🦚 |
| [tbphp/gpt-load](https://github.com/tbphp/gpt-load) | 7,163 | Go | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription a |
| [katanemo/plano](https://github.com/katanemo/plano) | 7,097 | Rust | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observab |
| [looplj/axonhub](https://github.com/looplj/axonhub) | 5,378 | Go | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, c |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | 3,898 | Rust | LeanCTX is the Context Gateway for AI Systems. Select task-relevant context, apply supported co |
| [jwadow/kiro-gateway](https://github.com/jwadow/kiro-gateway) | 2,327 | Python | 👻 Proxy API gateway for Kiro IDE & CLI (Amazon Q Developer / AWS CodeWhisperer). Use free Claud |
| [theagentrouter/agent-router](https://github.com/theagentrouter/agent-router) | 2,261 | Go | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [future-agi/future-agi](https://github.com/future-agi/future-agi) | 2,187 | Python | Open-source, end-to-end platform for evaluating, observing, and improving LLM and AI agent appl |
| [APIParkLab/APIPark](https://github.com/APIParkLab/APIPark) | 1,822 | TypeScript | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, o |
| [ENTERPILOT/GoModel](https://github.com/ENTERPILOT/GoModel) | 1,266 | Go | AI gateway / AI control plane / AI proxy written in Go. Unified OpenAI-compatible and Anthropic |
| [bricks-cloud/BricksLLM](https://github.com/bricks-cloud/BricksLLM) | 1,230 | Go | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API ke |
| [ASCIT31/Dark-Moon](https://github.com/ASCIT31/Dark-Moon) | 1,126 | Python | Open-source autonomous AI penetration testing. 50 specialist agents across web, API, cloud, Act |
| [kittors/CliRelay](https://github.com/kittors/CliRelay) | 1,039 | Go | Self-hosted AI gateway for coding CLIs — one OpenAI/Claude/Gemini/Codex-compatible endpoint, wi |
| [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway) | 890 | C# | MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session |
| [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) | 775 | TypeScript | MCP gateway for AI agents: turn any REST/OpenAPI, GraphQL, SOAP or SQL API into MCP tools. 517  |
| [myccarl/ai-shortVideo-pipeline](https://github.com/myccarl/ai-shortVideo-pipeline) | 763 | Python | End-to-end AI short-video production pipeline. FastAPI orchestration + Spring Boot gateway with |
| [mozilla-ai/otari](https://github.com/mozilla-ai/otari) | 719 | Python | Open-source, OpenAI-compatible LLM gateway you run yourself. One endpoint for 40+ providers, wi |
| [smg-project/smg](https://github.com/smg-project/smg) | 659 | Rust | Engine-agnostic LLM gateway in Rust. Full OpenAI & Anthropic API compatibility across vLLM, TRT |
| [apache/casbin-gateway](https://github.com/apache/casbin-gateway) | 643 | Go | See what every AI coding agent on your machine is doing, and whether the API behind it is the o |
| [Helicone/ai-gateway](https://github.com/Helicone/ai-gateway) | 638 | Rust | The fastest, lightest, and easiest-to-integrate AI gateway on the market. Fully open-sourced. |
| [sdcb/chats](https://github.com/sdcb/chats) | 613 | C# | A powerful and flexible frontend & AI gateway for large language models, supporting 21+ mainstr |
| [adaline/gateway](https://github.com/adaline/gateway) | 607 | TypeScript | The only fully local production-grade Super SDK that provides a simple, unified, and powerful i |

### Servidores MCP · `mcp-servers` · 94 repos · 15,140 resultados en GitHub

**Shortlist:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) · [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) · [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 91,459 | TypeScript | Model Context Protocol Servers |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24,636 | Python | The official Python SDK for Model Context Protocol servers and clients |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 13,636 | TypeScript | The official TypeScript SDK for Model Context Protocol servers and clients |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | 12,501 | TypeScript | Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes  |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | 9,863 | TypeScript | Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simu |
| [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | 7,393 | Go | A community driven registry service for Model Context Protocol (MCP) servers. |
| [getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) | 6,497 | TypeScript | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on |
| [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | 6,374 | Python | Programmatic access to Gemini Notebook - via command-line interface (CLI), Model Context Protoc |
| [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) | 5,669 | TypeScript | Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop |
| [nanbingxyz/5ire](https://github.com/nanbingxyz/5ire) | 5,373 | TypeScript | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service pro |
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | 5,256 | Go | The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration |
| [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | 4,595 | C# | The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | 4,378 | - | A curated list of Model Context Protocol (MCP) servers |
| [Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | 4,303 | TypeScript | A Model Context Protocol (MCP) server that provides structured spec-driven development workflow |
| [microsoft/mcp](https://github.com/microsoft/mcp) | 3,790 | C# | Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powere |
| [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk) | 3,733 | Java | The official Java SDK for Model Context Protocol servers and clients. Maintained in collaborati |
| [opensumi/core](https://github.com/opensumi/core) | 3,660 | TypeScript | A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context  |
| [coddingtonbear/obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) | 3,053 | TypeScript | A secure REST API and Model Context Protocol (MCP) server for your vault. |
| [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | 2,996 | Python | FreeCAD MCP(Model Context Protocol) server |
| [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | 2,996 | TypeScript | A Model Context Protocol server for converting almost anything to Markdown |
| [mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server) | 2,894 | Python | KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models ( |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | 2,685 | JavaScript | A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public  |
| [duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server) | 2,584 | Zig | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the d |
| [Joooook/12306-mcp](https://github.com/Joooook/12306-mcp) | 2,397 | JavaScript | This is a 12306 ticket search server based on the Model Context Protocol (MCP). |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | 2,304 | Go | ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP)  |
| [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 2,175 | Go | Model Context Protocol (MCP) server for Kubernetes and OpenShift |
| [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) | 2,169 | JavaScript | A Model Context Protocol server that provides read-only access to MySQL databases. This server  |
| [bitbonsai/mcpvault](https://github.com/bitbonsai/mcpvault) | 1,697 | TypeScript | A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access |
| [modelcontextprotocol/php-sdk](https://github.com/modelcontextprotocol/php-sdk) | 1,635 | PHP | The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboratio |
| [f/mcptools](https://github.com/f/mcptools) | 1,630 | Go | A command-line interface for interacting with MCP (Model Context Protocol) servers using both s |

### MCP de comercio · `commerce-mcp` · 36 repos · 1,220 resultados en GitHub

**Shortlist:** [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) · [xixihhhh/clipforge](https://github.com/xixihhhh/clipforge) · [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) · [innocommerce/innoshop](https://github.com/innocommerce/innoshop)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | 12,474 | TypeScript | The Apify MCP server enables your AI agents to extract data from social media, search engines,  |
| [xixihhhh/clipforge](https://github.com/xixihhhh/clipforge) | 1,052 | TypeScript | ClipForge（原『带货剪手』/ daihuo-jianshou）：开源 AI 带货短视频神器——上传一张商品图，AI 自动提炼卖点 + 写种草脚本 + 锁定商品原图不变形 + 配画面/ |
| [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) | 775 | TypeScript | MCP gateway for AI agents: turn any REST/OpenAPI, GraphQL, SOAP or SQL API into MCP tools. 517  |
| [innocommerce/innoshop](https://github.com/innocommerce/innoshop) | 664 | PHP | InnoShop is an AI-powered open source e-commerce system built on Laravel 13. It supports multip |
| [daydreamsai/daydreams](https://github.com/daydreamsai/daydreams) | 621 | TypeScript | Daydreams is a set of tools for building agents for commerce |
| [Lifecycle-Innovations-Limited/claude-ops](https://github.com/Lifecycle-Innovations-Limited/claude-ops) | 547 | Shell | Business operating system for Claude Code — 57 skills, 21 agents, smart daemon. Unified inbox ( |
| [bighadj22/codflow](https://github.com/bighadj22/codflow) | 377 | TypeScript | The open-source, COD-first e-commerce + delivery platform for Algeria  built agentic-ready. |
| [codespar/mcp-dev-latam](https://github.com/codespar/mcp-dev-latam) | 274 | TypeScript | Open-source MCP servers for Latin American commerce — Pix, NF-e, banking, fiscal, logistics, an |
| [darjeeling/awesome-mcp-korea](https://github.com/darjeeling/awesome-mcp-korea) | 252 | - | A curated list of MCP servers for the Korean market, including legal, commerce, public data, an |
| [0xNyk/awesome-agent-cortex](https://github.com/0xNyk/awesome-agent-cortex) | 226 | JavaScript | Curated map of AI agent frameworks, protocols, runtimes, skills, memory, identity, security, ev |
| [daydreamsai/lucid-agents](https://github.com/daydreamsai/lucid-agents) | 199 | TypeScript | Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participat |
| [cporter202/coreclaw-api-directory](https://github.com/cporter202/coreclaw-api-directory) | 179 | Python | An unofficial, categorized directory of 118 CoreClaw Worker APIs for web scraping, automation,  |
| [Eleven617/mall-ai-after-sales-platform](https://github.com/Eleven617/mall-ai-after-sales-platform) | 111 | Java | Trusted e-commerce AI after-sales platform — RAG, controlled tools, human confirmation, Java-au |
| [kangise/ecommerce-ai-skills](https://github.com/kangise/ecommerce-ai-skills) | 103 | Python | Cross-border e-commerce AI knowledge base, read by people and installed by agents: 69 trilingua |
| [TonyWang-hub/mcp-cn-commerce](https://github.com/TonyWang-hub/mcp-cn-commerce) | 87 | Python | 中国电商 MCP 连接器：8 个平台、155 个已注册工具。开源标准版，含能力矩阵与实际工程验收记录；真实商家联调状态逐项公开。Chinese commerce MCP connectors |
| [gnuboard/g7](https://github.com/gnuboard/g7) | 87 | PHP | Gnuboard7(그누보드7) - Open-source CMS & e-commerce platform built with Laravel 12 + React |
| [NVIDIA-AI-Blueprints/Retail-Agentic-Commerce](https://github.com/NVIDIA-AI-Blueprints/Retail-Agentic-Commerce) | 81 | Python | Reference implementation of the Agentic Commerce Protocol (ACP) and Universal Commerce Protocol |
| [SerendipityOneInc/ZooData-Skills](https://github.com/SerendipityOneInc/ZooData-Skills) | 77 | Python | ZooData Skills - AI Agent skills for e-commerce data intelligence across Amazon, TikTok & beyon |
| [MentionNetwork/awesome-agentic-commerce](https://github.com/MentionNetwork/awesome-agentic-commerce) | 65 | - | A curated list of awesome agentic commerce resources — protocols, MCP servers, tools, apps, API |
| [devlab-group/agent-commerce](https://github.com/devlab-group/agent-commerce) | 63 | TypeScript | Self-hosted, non-custodial gateway between the API you already run and the protocols AI agents  |
| [oliverames/meta-mcp-server](https://github.com/oliverames/meta-mcp-server) | 59 | TypeScript | The most comprehensive MCP server for Meta's business platform. 200+ tools covering Facebook Pa |
| [SalesforceCommerceCloud/b2c-developer-tooling](https://github.com/SalesforceCommerceCloud/b2c-developer-tooling) | 56 | TypeScript | B2C CLI, VSCode Extension, Skills+MCP, and Tooling SDK for Salesforce Agentforce Commerce B2C |
| [zeptonow/mcp](https://github.com/zeptonow/mcp) | 50 | - | Your favourite quick commerce app, now available as a MCP 🚀 |
| [visa/ai](https://github.com/visa/ai) | 45 | TypeScript | Integration toolkit for connecting AI agents to the Visa Intelligent Commerce platform. |
| [rhein1/agoragentic-integrations](https://github.com/rhein1/agoragentic-integrations) | 41 | JavaScript | Public adapters and discovery catalog for Triptych OS (Agent OS): agent frameworks, MCP/A2A/x40 |
| [OrcaQubits/agentic-commerce-skills-plugins](https://github.com/OrcaQubits/agentic-commerce-skills-plugins) | 39 | Python | Skills & plugins for agentic commerce : UCP, ACP, AP2, A2A, WebMCP, Magento 2, BigCommerce, Woo |
| [mguozhen/voc-amazon-reviews](https://github.com/mguozhen/voc-amazon-reviews) | 37 | Python | Review Analyzer — agent-native VOC for e-commerce. 6 MCP tools, ASIN or CSV input, black-gold d |
| [elsahafy/ux-mcp-server](https://github.com/elsahafy/ux-mcp-server) | 35 | JavaScript | MCP server providing 28 UX knowledge resources, 23 analysis tools & 4 workflow prompts. Works w |
| [orylite/lindyson-ai](https://github.com/orylite/lindyson-ai) | 33 | TypeScript | AI video & image generation workspace for e-commerce teams, built on Volcengine Seedance / Seed |
| [nguyennguyenit/pancake-pos-mcp](https://github.com/nguyennguyenit/pancake-pos-mcp) | 32 | TypeScript | MCP server for Pancake POS — 23 tools across orders, inventory, CRM, multi-channel commerce. Bu |

### RAG / conocimiento · `rag-knowledge` · 97 repos · 11,588 resultados en GitHub

**Shortlist:** [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) · [labring/FastGPT](https://github.com/labring/FastGPT) · [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) · [OpenSPG/KAG](https://github.com/OpenSPG/KAG)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 38,702 | Python | Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应 |
| [labring/FastGPT](https://github.com/labring/FastGPT) | 29,892 | TypeScript | FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,866 | TypeScript | LLM Wiki is a cross-platform desktop application that turns your documents into an organized, i |
| [OpenSPG/KAG](https://github.com/OpenSPG/KAG) | 9,117 | Python | KAG is a logical form-guided reasoning and retrieval framework based on OpenSPG engine and LLMs |
| [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | 4,801 | Python | OpenKB: Open LLM Knowledge Base |
| [53AI/53AIHub](https://github.com/53AI/53AIHub) | 4,334 | Go | 53AI Hub is an open-source AI portal and knowledge base for managing enterprise knowledge, AI a |
| [SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 3,645 | Python | A personal knowledge base that builds and maintains itself. Drop in sources — Claude (or Codex/ |
| [pingcap/autoflow](https://github.com/pingcap/autoflow) | 2,979 | TypeScript | pingcap/autoflow is a Graph RAG based and conversational knowledge base tool built with TiDB Se |
| [Zleap-AI/SAG](https://github.com/Zleap-AI/SAG) | 2,619 | Python | A new SOTA for RAG — an original retrieval architecture and an open-source knowledge base for h |
| [finic-ai/rag-stack](https://github.com/finic-ai/rag-stack) | 1,581 | TypeScript | 🤖 Deploy a private ChatGPT alternative hosted within your VPC. 🔮 Connect it to your organizatio |
| [nduckmink/arkon](https://github.com/nduckmink/arkon) | 1,495 | Python | Arkon: Enterprise AI Knowledge Hub & MCP Server. Self-hosted knowledge base for teams to manage |
| [shuyu-labs/AntSK](https://github.com/shuyu-labs/AntSK) | 1,327 | CSS | An AI knowledge base/agent built with .Net 9, AntBlazor, Semantic Kernel, and Kernel Memory, su |
| [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) | 1,283 | Python | Awesome AI Memory / LLM Memory / A curated knowledge base on AI memory for LLMs and agents, cov |
| [proinsight-io/crewmeld](https://github.com/proinsight-io/crewmeld) | 995 | TypeScript | CrewMeld — Enterprise AI Digital Workforce Platform. Manage AI employees like real team members |
| [BaranziniLab/KG_RAG](https://github.com/BaranziniLab/KG_RAG) | 947 | Jupyter Notebook | Empower Large Language Models (LLM) using Knowledge Graph based Retrieval-Augmented Generation  |
| [nuwax-ai/nuwax](https://github.com/nuwax-ai/nuwax) | 895 | TypeScript | Nuwax Agent OS - An enterprise-grade AI Agent Development and Operation Platform - Providing a  |
| [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault) | 728 | TypeScript | The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent me |
| [ConardLi/rag-skill](https://github.com/ConardLi/rag-skill) | 723 | Python | A Skill dedicated to local knowledge base retrieval |
| [lycohana/BiliSum](https://github.com/lycohana/BiliSum) | 641 | Python | 为 Bilibili、YouTube 及本地视频提供 AI 视频摘要和知识库.AI video summarizer and knowledge base for Bilibili, You |
| [tgoai/tgo](https://github.com/tgoai/tgo) | 636 | TypeScript | Open-source AI Agent Customer Service Platform. Build AI agent teams with LLM orchestration, RA |
| [docsagent/docsagent](https://github.com/docsagent/docsagent) | 576 | TypeScript | ⚡ DocsAgent — give your AI agents instant, private access to your personal knowledge base (Zote |
| [aws-samples/bedrock-engineer](https://github.com/aws-samples/bedrock-engineer) | 484 | TypeScript | Universal AI Agent using Amazon Bedrock, capable of customize to create/edit files, execute com |
| [Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas) | 450 | Python | Your First LLM-Wiki Conversation Knowledge Base |
| [ageerle/ruoyi-web](https://github.com/ageerle/ruoyi-web) | 425 | Vue | RuoYi-AI user frontend for AI conversations, agent interactions, and knowledge-base Q&A. |
| [2dogsandanerd/Knowledge-Base-Self-Hosting-Kit](https://github.com/2dogsandanerd/Knowledge-Base-Self-Hosting-Kit) | 356 | Python | A Docker-powered RAG system that understands the difference between code and prose. Ingest your |
| [software-mansion-labs/react-native-rag](https://github.com/software-mansion-labs/react-native-rag) | 348 | TypeScript | Private, local RAGs. Supercharge LLMs with your own knowledge base. |
| [zhimaAi/ChatClaw](https://github.com/zhimaAi/ChatClaw) | 309 | Go | ChatClaw: Get OpenClaw-like knowledge base personal AI agent in 5 mins. Sandbox-secured, ultra- |
| [xuwei95/ezdata](https://github.com/xuwei95/ezdata) | 294 | Python | AI-native data platform: 60+ connectors, dlt-based ETL, DAG scheduling, per-source RAG knowledg |
| [lhh737/KnowledgeBase-RAG-LLM-System](https://github.com/lhh737/KnowledgeBase-RAG-LLM-System) | 291 | Python | 轻量级本地知识库 RAG 问答系统 · Streamlit + LangChain + Chroma，支持知识库上传与检索增强问答 |
| [KnowledgeXLab/LeanRAG](https://github.com/KnowledgeXLab/LeanRAG) | 260 | Python | (AAAI 2026) Knowledge-Graph-Based Generation with Semantic Aggregation and Hierarchical Retriev |

### Automatización de flujos · `workflow-automation` · 96 repos · 54,221 resultados en GitHub

**Shortlist:** [n8n-io/n8n](https://github.com/n8n-io/n8n) · [langgenius/dify](https://github.com/langgenius/dify) · [HKUDS/nanobot](https://github.com/HKUDS/nanobot) · [apache/airflow](https://github.com/apache/airflow)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 208,261 | TypeScript | Fair-code workflow automation platform with native AI capabilities. Combine visual building wit |
| [langgenius/dify](https://github.com/langgenius/dify) | 159,168 | Python | Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborativ |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 77,626 | Python | A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflo |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 49,259 | Python | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, t |
| [apache/airflow](https://github.com/apache/airflow) | 47,251 | Python | Apache Airflow - A platform to programmatically author, schedule, and monitor workflows |
| [kestra-io/kestra](https://github.com/kestra-io/kestra) | 29,941 | Java | Event Driven Orchestration & Scheduling Platform for Mission Critical Applications |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29,864 | TypeScript | Sim is the collaborative workspace to build, deploy, and monitor AI agents and workflows. Used  |
| [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 26,045 | - | 280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 25,165 | TypeScript | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation /  |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | 24,058 | Python | Prefect is a workflow orchestration framework for building resilient data pipelines in Python. |
| [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) | 23,244 | Python | Automate browser based workflows with AI |
| [AutomaApp/automa](https://github.com/AutomaApp/automa) | 21,674 | Vue | A browser extension for automating your browser by connecting blocks |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 19,445 | Python | Turns Data and AI algorithms into production-ready web applications in no time. |
| [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | 16,593 | TypeScript | Trigger.dev – build and deploy durable AI agents and workflows |
| [waooAI/waoowaoo](https://github.com/waooAI/waoowaoo) | 14,645 | TypeScript | 首家工业级全流程 AI 影视生产平台。Industry-first professional AI Agent platform for controllable film & video  |
| [automatisch/automatisch](https://github.com/automatisch/automatisch) | 14,002 | JavaScript | The open source Zapier alternative. Build workflow automation without spending time and money. |
| [google/artemis](https://github.com/google/artemis) | 13,603 | Python | ARTEMIS turns natural-language instructions into reliable Android automation. It automates end- |
| [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream) | 11,758 | JavaScript | Connect APIs, remarkably fast.  Free for developers. |
| [bytedance/flowgram.ai](https://github.com/bytedance/flowgram.ai) | 8,512 | TypeScript | FlowGram is an extensible workflow development framework with built-in canvas, form, variable,  |
| [refly-ai/refly](https://github.com/refly-ai/refly) | 7,536 | TypeScript | The first open-source agent skills builder. Define skills by vibe workflow, run on Claude Code, |
| [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | 6,902 | JavaScript | AI-assisted TradingView chart analysis — connect Claude Code to your TradingView Desktop for pe |
| [StackStorm/st2](https://github.com/StackStorm/st2) | 6,550 | Python | StackStorm (aka "IFTTT for Ops") is event-driven automation for auto-remediation, incident resp |
| [muesli/beehive](https://github.com/muesli/beehive) | 6,489 | Go | A flexible event/agent & automation system with lots of bees 🐝 |
| [wassupjay/n8n-free-templates](https://github.com/wassupjay/n8n-free-templates) | 6,231 | - | A curated set of 200+ plug-and-play n8n workflows that fuse classic automation with today’s AI  |
| [MontFerret/ferret](https://github.com/MontFerret/ferret) | 6,013 | Go | Declarative data automation language and Go runtime for structured extraction workflows. |
| [ATH-MaaS/ComfyUI-Copilot](https://github.com/ATH-MaaS/ComfyUI-Copilot) | 5,554 | TypeScript | An AI-powered custom node for ComfyUI designed to enhance workflow automation and provide intel |
| [iflow-ai/iflow-cli](https://github.com/iflow-ai/iflow-cli) | 5,082 | Shell | iFlow cli is a comprehensive command-line intelligence that embeds in your terminal, analyzes y |
| [totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids) | 5,057 | TypeScript | Cross-platform local MCP capabilities for ChatGPT with Chrome integration, Goal, Compact & Resu |
| [darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) | 4,925 | TypeScript | AI agent framework for plan-first development workflows with approval-based execution. Multi-la |
| [golutra/golutra](https://github.com/golutra/golutra) | 3,860 | Rust | Multi-agent AI orchestration platform for automation, workflows, and developer tools. Golutra t |

## 7. Back-office y BI

### ERP · `erp` · 98 repos · 159,659 resultados en GitHub

**Shortlist:** [odoo/odoo](https://github.com/odoo/odoo) · [frappe/erpnext](https://github.com/frappe/erpnext) · [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) · [Dujltqzv/Some-Many-Books](https://github.com/Dujltqzv/Some-Many-Books)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [odoo/odoo](https://github.com/odoo/odoo) | 55,237 | Python | Odoo. Open Source Apps To Grow Your Business. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | 40,434 | Python | Free and Open Source Enterprise Resource Planning (ERP) |
| [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | 39,968 | Java | 🔥 官方推荐 🔥 RuoYi-Vue 全新 Pro 版本，优化重构所有功能。基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + |
| [Dujltqzv/Some-Many-Books](https://github.com/Dujltqzv/Some-Many-Books) | 25,055 | - | 个人收藏书籍列表 |
| [nocobase/nocobase](https://github.com/nocobase/nocobase) | 24,660 | TypeScript | NocoBase is an open-source AI + no-code platform for building business systems fast. Instead of |
| [YunaiV/yudao-cloud](https://github.com/YunaiV/yudao-cloud) | 19,658 | Java | ruoyi-vue-pro 全新 Cloud 版本，优化重构所有功能。基于 Spring Cloud Alibaba + MyBatis Plus + Vue & Element 实现的后台 |
| [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 12,095 | PHP | Free and Open Source ERP software |
| [akaunting/akaunting](https://github.com/akaunting/akaunting) | 10,200 | PHP | Online Accounting Software |
| [grocy/grocy](https://github.com/grocy/grocy) | 9,604 | Blade | ERP beyond your fridge - Grocy is a web-based self-hosted groceries & household management solu |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 8,905 | JavaScript | Free Open Source ERP CRM Software Accounting Invoicing / Node.Js React |
| [ever-co/ever-gauzy](https://github.com/ever-co/ever-gauzy) | 8,412 | TypeScript | Ever® Gauzy™ - Open Business Management Platform (ERP/CRM/HRM/ATS/PM) - https://gauzy.co |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 7,761 | PHP | Dolibarr ERP CRM is a modern software package to manage your company or foundation's activity ( |
| [xaboy/form-create](https://github.com/xaboy/form-create) | 7,106 | JavaScript | :fire::fire::fire: 强大的低代码动态表单组件，通过 JSON 数据驱动表单渲染，适配移动端，支持可视化设计。提高开发者对表单的开发效率。目前在政务系统、OA系统、ERP系统 |
| [jishenghua/jshERP](https://github.com/jishenghua/jshERP) | 4,672 | Java | 管伊佳ERP（原名华夏ERP）基于SpringBoot框架和SaaS模式，立志为中小企业提供开源好用的ERP软件，目前专注进销存+财务功能。主要模块有零售管理、采购管理、销售管理、仓库管理、 |
| [yudaocode/yudao-ui-admin-vue3](https://github.com/yudaocode/yudao-ui-admin-vue3) | 3,915 | Vue | 芋道管理后台，基于 Vue3 + Element Plus 实现，支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP、 |
| [crbnos/carbon](https://github.com/crbnos/carbon) | 2,751 | TypeScript | Open-source manufacturing ERP, MES and QMS. Quoting, MRP, inventory, shop floor, quality and lo |
| [frappe/frappe_docker](https://github.com/frappe/frappe_docker) | 2,603 | Python | Docker environment for developing, deploying, and running Frappe applications (ERPNext and cust |
| [andeya/erpc](https://github.com/andeya/erpc) | 2,526 | Go | An efficient, extensible and easy-to-use RPC framework. |
| [metasfresh/metasfresh](https://github.com/metasfresh/metasfresh) | 2,457 | Java | We do Open Source ERP - Fast, Flexible & Free Software to scale your Business. |
| [xaboy/form-create-designer](https://github.com/xaboy/form-create-designer) | 2,372 | Vue | 好用的Vue低代码可视化 AI 表单设计器，可以通过拖拽的方式快速创建表单，提高开发者对表单的开发效率。支持PC端和移动端，目前在政务系统、OA系统、ERP系统、电商系统、流程管理等系统中已 |
| [FJ-OMS/oms-erp](https://github.com/FJ-OMS/oms-erp) | 1,928 | Java | 一站式全渠道业务中台系统包括订单管理系统OMS/电商ERP、库存WMS统一管理系统和SAP财务管理系统等，实现快速部署，并帮助企业后续自主进行开发迭代，实现数字化转型，并有多个经典案例。中台 |
| [open-mercato/open-mercato](https://github.com/open-mercato/open-mercato) | 1,878 | TypeScript | The AI-Engineering Foundation Framework for business apps: open-source TypeScript, with multi-t |
| [fjykTec/ModernWMS](https://github.com/fjykTec/ModernWMS) | 1,788 | Vue | The open source simple and complete warehouse management system is derived from our many years  |
| [steedos/steedos-platform](https://github.com/steedos/steedos-platform) | 1,589 | TypeScript | The AI-Native Infrastructure for Enterprise Apps. Powered by ObjectStack (ObjectQL, ObjectOS, O |
| [likeadmin-likeshop/likeshop](https://github.com/likeadmin-likeshop/likeshop) | 1,587 | PHP | 🔥🔥🔥 likeshop开源免费商用电商系统，PC商城、H5商城、小程序商城、安卓APP商城、苹果APP商城，免费商用。场景：B2C商城，新零售商城，社交电商商城，分销系统商城，分销电商商城 |
| [WebVella/WebVella-ERP](https://github.com/WebVella/WebVella-ERP) | 1,496 | C# | Free and open-source pluggable ERP and CRM software based on ASP.NET Core 9, RazorPages and Pos |
| [andrewdwallo/erpsaas](https://github.com/andrewdwallo/erpsaas) | 1,478 | PHP | A Laravel and Filament-powered accounting platform featuring full double-entry accrual accounti |
| [zhuinfo/Django-ERP](https://github.com/zhuinfo/Django-ERP) | 1,474 | Python | Django-ERP是一款基于Django开发的ERP管理软件，包含常用的销售管理、采购管理、库存管理、组织管理等，支持按项目归集费用，支持工作流审批，支持采购单、报价单的批量导入。 |
| [osbzr/gooderp_addons](https://github.com/osbzr/gooderp_addons) | 1,340 | - | 可能是中国用户数最多的开源ERP |
| [OCA/web](https://github.com/OCA/web) | 1,239 | JavaScript | Odoo web client UI related addons |

### Analytics / BI · `analytics-bi` · 36 repos · 50,622 resultados en GitHub

**Shortlist:** [metabase/metabase](https://github.com/metabase/metabase) · [getredash/redash](https://github.com/getredash/redash) · [perspective-dev/perspective](https://github.com/perspective-dev/perspective) · [briefercloud/briefer](https://github.com/briefercloud/briefer)

| Repo | ★ | Lang | Descripción |
|---|---|---|---|
| [metabase/metabase](https://github.com/metabase/metabase) | 49,789 | Clojure | The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyon |
| [getredash/redash](https://github.com/getredash/redash) | 28,843 | Python | Make Your Company Data Driven. Connect to any data source, easily visualize, dashboard and shar |
| [perspective-dev/perspective](https://github.com/perspective-dev/perspective) | 11,333 | Rust | A data visualization and analytics component, especially well-suited for large and/or streaming |
| [briefercloud/briefer](https://github.com/briefercloud/briefer) | 4,326 | TypeScript | Dashboards and notebooks in a single place. Create powerful and flexible dashboards using code, |
| [running-elephant/datart](https://github.com/running-elephant/datart) | 2,308 | TypeScript | Datart is a next generation Data Visualization Open Platform |
| [helicalinsight/helicalinsight](https://github.com/helicalinsight/helicalinsight) | 1,097 | JavaScript | Free, open source BI platform with AI conversational analytics (BYO-LLM), pixel-perfect paginat |
| [frappe/insights](https://github.com/frappe/insights) | 1,028 | Python | Open Source Business Intelligence Tool |
| [sy-vendor/Gobi](https://github.com/sy-vendor/Gobi) | 276 | Go | 🚀 Modern Go-Native Business Intelligence (BI) Engine – API-first, lightweight BI for analytics, |
| [nbrown02/FlowViz](https://github.com/nbrown02/FlowViz) | 246 | TypeScript | A Power BI template that provides easy to understand, actionable flow metrics and predictive an |
| [virajbhutada/InsightForge](https://github.com/virajbhutada/InsightForge) | 175 | - | Discover a curated collection of dynamic Power BI dashboards covering financial analytics, HR m |
| [xxiaouw/SteamSmartBuy](https://github.com/xxiaouw/SteamSmartBuy) | 156 | Jupyter Notebook | An intelligent Steam deal analytics dashboard leveraging Python, MySQL, and Power BI to surface |
| [tushar2704/PowerBI-Portfolio](https://github.com/tushar2704/PowerBI-Portfolio) | 128 | - | Welcome to my Old Power BI portfolio repository! Here you will find a collection of Power BI pr |
| [apiko-dev/Databazel](https://github.com/apiko-dev/Databazel) | 125 | JavaScript | The analytical and reporting solution for MongoDB |
| [datainsider-co/rocket-bi](https://github.com/datainsider-co/rocket-bi) | 124 | TypeScript | A free, open-source,  web-based self-service BI tailor-made for clickhouse, google bigquery, my |
| [MahbubNibir/power-bi-retail-analytics-viz](https://github.com/MahbubNibir/power-bi-retail-analytics-viz) | 119 | HTML | Top Power BI Sales Dashboard 2026 for Profit & Regional Analysis |
| [MUDAS100/Swiggy-Instamart-Metrics-Dashboard-Power-BI](https://github.com/MUDAS100/Swiggy-Instamart-Metrics-Dashboard-Power-BI) | 118 | HTML | Interactive Logistics & Delivery Analytics Dashboard for Quick Commerce 2026 |
| [dchainapp2021/cosmetics-retail-finance-optimizer](https://github.com/dchainapp2021/cosmetics-retail-finance-optimizer) | 117 | HTML | Power BI Cosmetics Revenue Analytics Dashboard 2026: Sales Quality & Asset Performance |
| [goodmorningbeautyful-lab/PhonePe-Pulse-Analyzer](https://github.com/goodmorningbeautyful-lab/PhonePe-Pulse-Analyzer) | 115 | HTML | PhonePe Transaction Trends & User Analytics Dashboard 2026 – Power BI Guide |
| [visivo-io/visivo](https://github.com/visivo-io/visivo) | 104 | JavaScript | ✨ Build dashboards with end-to-end version control. 🔋 CLI w/ batteries included, no infra requi |
| [microsoft/AI-in-One-Dashboard](https://github.com/microsoft/AI-in-One-Dashboard) | 93 | PowerShell | Free Power BI dashboard for Microsoft 365 Copilot, Copilot Chat and agent adoption. Nearly 20 r |
| [Humphrey4data/tableau-to-hex-skill](https://github.com/Humphrey4data/tableau-to-hex-skill) | 91 | - | Agent skill for migrating Tableau, Looker, and Power BI dashboards to Hex apps: extract specs,  |
| [flowkraft/datapallas](https://github.com/flowkraft/datapallas) | 80 | TypeScript | 🔥One modern BI and data platform. AI data exploration, dashboards, and pixel-perfect report gen |
| [bonfirer/LingxiBI](https://github.com/bonfirer/LingxiBI) | 48 | TypeScript | AI-powered data analytics & reporting platform. Connect databases, ask questions in natural lan |
| [Pandey-Adarsh/HR-Analytics-PowerBI](https://github.com/Pandey-Adarsh/HR-Analytics-PowerBI) | 47 | - | HR Data Analytics portfolio project on a dataset of 80K records that deals with HR KPIs like Pe |
| [Suraj-G-Rao/Complete_Data_Analysis](https://github.com/Suraj-G-Rao/Complete_Data_Analysis) | 46 | Jupyter Notebook | A comprehensive Data Analysis repository covering the complete learning path from Python fundam |
| [nbrown02/FlowViz-Jira](https://github.com/nbrown02/FlowViz-Jira) | 44 | TypeScript | A Power BI template that provides easy to understand, actionable flow metrics and predictive an |
| [parlhad/Uber_Power-BI_Project](https://github.com/parlhad/Uber_Power-BI_Project) | 39 | - | This repository contains a Power BI analytics dashboard built to explore Uber ride booking data |
| [pvn-ptl/AdventureWorks-Analytics](https://github.com/pvn-ptl/AdventureWorks-Analytics) | 34 | - | Analyzing Manufacturing and Inventory Operations of the AdventureWorks Database using Power BI |
| [Nivetha0310/HR_Analytics_PowerBi-dashboard](https://github.com/Nivetha0310/HR_Analytics_PowerBi-dashboard) | 34 | - | Visualisation of employee details in Excel file in a interactive way using  Microsoft Power Bi  |
| [Dashboard-Design/Power-BI-UDF-Library](https://github.com/Dashboard-Design/Power-BI-UDF-Library) | 33 | - | A curated library of reusable User Defined Functions UDFs  for Power BI analytics, reporting, a |

## Notables cross-topic (≥3 temas)

| Repo | ★ | Temas |
|---|---|---|
| [spree/spree](https://github.com/spree/spree) | 15,769 | ecommerce-platform, headless-storefront, marketplace-software |
| [reactioncommerce/reaction](https://github.com/reactioncommerce/reaction) | 12,399 | ecommerce-platform, headless-storefront, marketplace-software |
| [akaunting/akaunting](https://github.com/akaunting/akaunting) | 10,200 | crm, erp, invoicing |
| [idurar/idurar-erp-crm](https://github.com/idurar/idurar-erp-crm) | 8,905 | crm, erp, invoicing |
| [ever-co/ever-gauzy](https://github.com/ever-co/ever-gauzy) | 8,412 | crm, erp, invoicing |
| [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | 7,761 | crm, erp, invoicing |
| [andrewdwallo/erpsaas](https://github.com/andrewdwallo/erpsaas) | 1,478 | crm, erp, invoicing |
| [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) | 775 | commerce-mcp, erp, llm-gateway |
| [Sfedfcv/redesigned-pancake](https://github.com/Sfedfcv/redesigned-pancake) | 268 | email-marketing, marketplace-software, pim, price-tracking, product-search |
| [ManojKumarPatnaik/Major-project-list](https://github.com/ManojKumarPatnaik/Major-project-list) | 259 | inventory-management, pim, price-tracking, product-search |
| [Rastaman4e/-1](https://github.com/Rastaman4e/-1) | 78 | marketplace-software, pim, pos |

*Total: **1710 repos únicos** · 25 consultas · 1,816 filas · top-30/tema aquí, resto en `data/oss/`.*