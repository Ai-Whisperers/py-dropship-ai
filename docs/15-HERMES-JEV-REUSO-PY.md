# Hermes/Jev + Reuso AIW — Extracción PY

*Documento maestro en repo WiseQ: [docs/14-HERMES-JEV-AIW-REUSE.md](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/14-HERMES-JEV-AIW-REUSE.md). Acá la parte PY.*

## Jev (veredicto)

Activo y sano (`jev-1.13` vía OpenRouter, ~40k decisiones auditadas). En el asiento del operador es inerte por diseño (zai directo = calidad full). **Apunta a los carriles OpenRouter**: perfiles pydrop, cron nocturno, hijos delegados — enrutado por turno según la grilla (deepseek-flash general, kimi código profundo, glm razonamiento, minimax tool-sequences). Regla sombrero-36 automatizada: -60/70% costo en carriles de parseo.

## Checklist Hermes (instancia)

1. `hermes fallback add` — FIX TOP (el lote de 4 hijos murió por 429 MiniMax sin cadena de fallback)
2. Perfiles por engagement (`pydrop`) — aislamiento credenciales/sesiones/memoria
3. Pools de credenciales en carriles crawler
4. Aliases por tarea: parse→deepseek-flash, decide→glm, tools→minimax
5. Skill-ificar: parser Shopping China, decodificador bundle-spine, harvester v2
6. Webhooks `--deliver-only` (uPay/Bancard)
7. Widget TUI de ops (pedidos/caja/alertas)
8. Langfuse OSS core (ee/ OFF, línea roja) o Laminar al compose; OpenObserve para costo-token

## Reuso PY (de inventario AIW)

| Activo | Uso |
|---|---|
| **saskia-app** (org) | Esqueleto backend: SIFEN facturación PY probada, conciliación de pagos, disciplina de tests, deploy |
| **ai-whisperers-ops-toolkit** | Provisionador del VPS PY — el compose doc 13 aterriza sobre esto |
| **ai-whisperers-hermes-agent** | Observabilidad de agentes YA ESCRITA: cron-health + alert-router — day-1, no retrofit |
| **gaby-client-engine** (org) | Maquinaria de outreach/adquisición (1.090 leads) para clientes PY |
| **status** (org) | Página de estado por op — señal de confianza 24/7 |
| **aiw-monitoring** | Base del dashboard de ops |
| **paragu-auditor** | Servicio vivo: cron mensual CONATEL/DINAVISA/SET/DNIT → actualiza doc 11 solo |
| **BWS + Better Stack + Sentry + Cloudflare + Neon** | Capa ops medio-instalada ya |
| **telescope-ai** | Patrón MCP-wrapper probado (para wrappers finos propios) |

**Lo genuinamente nuevo** (el moat): matcher bundle-spine, parser pedidos-escolares, agente mapa-CDE, WhatsApp closer, repricing, componentes Commerce-OS. Todo lo demás es reuso.
