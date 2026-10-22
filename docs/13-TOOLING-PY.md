# Tooling & Instalaciones — Extracción PY

*El plan completo (ambas operaciones) vive en el repo WiseQ: [docs/13-TOOLING-MCP-INSTALLS.md](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/13-TOOLING-MCP-INSTALLS.md). Acá solo la parte PY.*

## MCP para PY (resumen)

| Prio | MCP | Tipo | Uso |
|---|---|---|---|
| P0 | **Evolution API MCP** (mcp-evolution-whatsapp-api) | install | WhatsApp enviar/recibir vía gateway self-hosted |
| P0 | sqlite/filesystem (ya activos) | — | Tabla canónica producto/precio |
| P0 | Scrapling/Scrapy (lib Python, cron) | script | Crawl nocturno CDE |
| P1 | changedetection.io API (wrapper fino) | build | Gestión de watches de precio |
| P1 | InvenTree MCP (wrapper fino, ~10 endpoints) | build | Stock/parts/suppliers |
| P1 | uPay/Bancard webhook → Hermes | custom | Eventos de pago como webhooks `--deliver-only` |
| P2 | Meta Ads MCP (oliverames) | install | Campañas con guardarrail de presupuesto |
| P2 | Google Business Profile (wrapper) | build | Reseñas + post semanal |
| P3 | SIFEN invoice MCP | build | Factura electrónica al pasar a SIMPLE |

## docker-compose fase 0 (un VPS)

```yaml
services:
  hermes:            # orquestador (profile pydrop)
  evolution-api:     # gateway WhatsApp
  changedetection:   # watches de precio/stock
  inventree:         # fase 1
  n8n:               # flujos simples
  umami:             # analítica fase 1
  billionmail:       # ESP fase 2
  caddy:             # proxy + TLS
```

Backups restic nocturnos; uptime vía Better Stack (ya activo); Postgres vía Neon cuando SQLite se quede chico.

## Regla de oro

Un dueño por capa; el catálogo de MCP es menú, no lista de compras. Nada sin uso programado.
