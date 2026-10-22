# Extracción PY — Auditoría del Equipo Dev Completo

*Master en repo WiseQ: [docs/16-DEV-TEAM-HATS.md](https://github.com/Ai-Whisperers/wiseq-ai-onboarding/blob/main/docs/16-DEV-TEAM-HATS.md). 18 roles auditaron ambos proyectos. Acá las acciones que caen del lado PY.*

## Acciones PY (del top-10 del master)

| # | Acción | Rol | Esfuerzo |
|---|---|---|---|
| 1 | `schema_version` en snapshots + test golden-file (detecta drift silencioso del parser) | DataEng/QA | 30m |
| 2 | MILESTONES.md con criterios de salida (fase 0: ¿cómo se que está DONE?) | PM | 30m |
| 4 | AGENTS.md (política de idioma, SSOT, validate-antes-de-commit) + GLOSSARY.md (jopara, contrapedido, RESIMPLE) | TechWriter | 1h |
| 5 | Crawler v2: retry/backoff 3x, run-log JSONL (ts, categoria, n, status), 1 test con fixture HTML | Backend | 2h |
| 9 | Schema del eval-set + primeras 50 conversaciones etiquetadas (antes de que el agente exista) | ML | 3h |
| 10 | Sanitizar títulos del snapshot antes de contexto LLM (superficie de prompt-injection) | Security | 30m |

## Notas PY por rol (resumen)

- **UX**: los flujos de conversación WhatsApp (saludo→calificar→oferta→cierre→pago→confirmación) aún no están escritos — es el producto real.
- **QA**: validadores son smoke-tier; falta test del propio validador (inyectar archivo malo, esperar exit 1).
- **SRE**: keepalive ok; falta heartbeat Better Stack sobre "sin run en 48h" + runbooks.md por workflow.
- **Perf**: crawler serial está bien hoy (10 cats × 2s); medir wall-clock por crawl en el run-log; optimizar cuando pase 30min.
- **Support**: ESCALATION.md — cuándo el agente WhatsApp deriva a humano, SLA, plantillas ES.

## Lo que el equipo mantiene tal cual

Cultura evidencia-primero, CI que atrapó sus propios bugs el día 1, stack reuso-primero, disciplina bilingüe, infra €0 verificada en vivo.
