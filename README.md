# PY Dropship AI — Dropshipping con stack de IA para Paraguay

**Operación de dropshipping con orquestación de IA** para el mercado de Asunción y Central (Gran Asunción), con sourcing dual: mayoristas de **Ciudad del Este** + importación directa desde **China** (1688/Alibaba).

Un proyecto de [AI Whisperers](https://github.com/Ai-Whisperers). Construido sobre la misma arquitectura de agentes que usamos para clientes de e-commerce en Europa (ver [wiseq-ai-onboarding](https://github.com/Ai-Whisperers/wiseq-ai-onboarding)) — adaptada a la realidad paraguaya: efectivo contra entrega, WhatsApp como canal de ventas, y Ciudad del Este como proveedor logístico natural.

> *An AI-orchestrated dropshipping operation for the Asunción metro area (Gran Asunción), sourcing from Ciudad del Este wholesalers and direct-from-China imports. English summary below.*

## La idea en un párrafo

El dropshipping internacional clásico (AliExpress → cliente paraguayo) **no funciona**: 3-8 semanas de envío, aduana, y el mismo producto ya está en Ciudad del Este a precio de importador. Lo que sí funciona en Paraguay es el **dropshipping local** (mayoristas de CDE/Asunción despachan en 24-72h) con márgenes brutos de 20-35%. Nuestra propuesta: montar esa operación con un **stack de IA que la vuelve rentable a escala** — agente de monitoreo de precios en CDE, agente de sourcing en 1688, tienda con cobros locales (QR/transferencia/contra entrega), bucle de atención y venta por WhatsApp automatizado, facturación SIFEN, y motor de publicidad en Meta — todo orquestado 24/7 por Hermes Agent.

## Documentos

| Doc | Contenido |
|---|---|
| [Análisis de mercado](docs/01-ANALISIS-MERCADO.md) | PY e-commerce en cifras verificadas, pagos, logística, competencia |
| [Modelo de negocio](docs/02-MODELO-NEGOCIO.md) | Sourcing dual CDE+China, unit economics en guaraníes, los 3 modelos |
| [Fuentes de suministro](docs/03-PROVEEDORES.md) | Mayoristas CDE verificados, couriers China→PY, criterios de selección |
| [Stack de IA](docs/04-STACK-IA.md) | **La propuesta central** — arquitectura Hermes para dropshipping PY |
| [Roadmap](docs/05-ROADMAP.md) | Fases 0-3 con costos y métricas |
| [Transferencia WiseQ](docs/06-TRANSFERENCIA-WISEQ.md) | Qué reutilizamos del playbook europeo |
| [Análisis de 40 sombreros](docs/07-ANALISIS-40-SOMBREROS.md) | **100+ ideas** por rol (40 hats): OSS verificado, scrapeabilidad CDE, top-10 ROI, descartes |
| [Catálogo OSS](docs/08-OSS-CATALOG.md) | **25 temas · 1,710 repos** investigados vía GitHub API, shortlists curadas, stack adoptado |
| [Profundización](docs/09-PROFUNDIZACION-2026-10.md) | Pagos post-BCP (tope 3%/2%), Ley 7593/2025 datos, régimen courier USD 1.000, competencia ampliada, 12 mejoras técnicas |

## Estado

- 2026-10-21: repositorio creado; investigación de mercado completada; arquitectura definida. Próximo: selección de nicho + contacto con proveedores CDE.
- 2026-10-22: análisis de 40 sombreros + investigación OSS (InvenTree, Medusa, Evolution API, meta-mcp-server, Scrapling) + sonda de scrapeabilidad CDE (Cellshop/Nissei 403, Fastrax/ShoppingChina/Tupi abiertos).
- 2026-10-22: catálogo OSS completo — 25 búsquedas × top-100 por estrellas, 1,710 repos únicos indexados en `data/oss/`, doc curado con stack adoptado y shortlists por capa.
- 2026-10-22: profundización — tope de comisiones BCP (3% crédito/2% débito desde jul-2026, uPay Gs.0/mes), Ley 7593/2025 de datos (ventana hasta nov-2027), courier USD 33/kg CN→PY impuestos incl., competencia (Tiendamia/Shein-Temu/MELI 13-20%), última milla Gs. 15-30k, y 12 mejoras técnicas (evals, observabilidad, precios dinámicos, privacidad).
