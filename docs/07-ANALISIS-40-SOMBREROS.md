# Análisis de 40 Sombreros — PY Dropship AI

*Método: 40 roles específicos × 2-3 aportes cada uno ≈ 100 ideas, cada una con impacto estimado. Alimenta el roadmap (05) y el stack (04). Ground truth de investigación incluida abajo — los sombreros trabajan sobre datos verificados, no intuiciones.*

---

## 0. Ground truth de investigación (nuevo, 2026-10-21)

### Software open-source reutilizable (GitHub, verificado por estrellas)

| Categoría | Proyecto | ★ | Veredicto para nuestro stack |
|---|---|---|---|
| Inventario | **InvenTree** (inventree/InvenTree) | 7.7k | Candidato a registro canónico de producto con UI — PIH/API listo |
| Inventario | GreaterWMS | 4.4k | Orientado a bodega; overkill fase 1, opción fase 3 |
| ERP | **Odoo** | 55k | Si la operación crece a multi-nicho/multi-depósito; Odoo tiene módulo PY community |
| ERP | ERPNext | 40k | Alternativa; más liviano de self-hostear |
| Commerce | **Medusa** (medusajs/medusa) | 36.8k | "Commerce platform for agents" — API-first, exactamente nuestro patrón; alternativa a Tiendli cuando queramos controlar el stack |
| Commerce | Saleor | 23.5k | Headless GraphQL; segunda opción |
| WhatsApp | **whatsapp-web.js** / Baileys | 22.8k/11.4k | Librerías cliente (riesgo de ban — ver sombrero 40) |
| WhatsApp | **Evolution API** | 9.9k | Gateway self-hosted con API REST — la capa correcta para el agente |
| WhatsApp | WAHA | 7.7k | Alternativa Docker-friendly |
| Automation | **n8n** | 208k | Ya lo usamos en AIW; complementa cron de Hermes para flujos visuales |
| Scraping | **Scrapling** | 89k | Anti-bot adversario — necesario: Cellshop y Nissei ya nos dieron 403 |
| Scraping | Scrapy | 64.9k | Base para crawls masivos programados |
| Ads | **meta-mcp-server** (oliverames) | 59 | **200+ herramientas Meta como MCP** — el agente maneja campañas nativamente |
| Ads | meta-ads-cli | 36 | CLI de campañas — integración directa con Hermes terminal |
| Precios | Discount-Bandit | 754 | Price-tracker self-hosted multi-tienda — patrón a copiar para el mapa CDE |
| Precios | PriceDive | 88 | Tracker chino (Taobao/JD/PDD) — lógica reusable para 1688 |
| Facturación | InvoicePlane / TaxHacker | 3.2k/6.8k | Patrones; SIFEN PY ya lo resuelve el ecosistema propio (sazon-rms) |
| Guaraní NLP | (casi inexistente) | <50 total | **Hueco real** — ver sombrero 26 |

### Scrapeabilidad de proveedores CDE (sonda directa, 2026-10-21)

| Sitio | robots/sitemap | Implicancia |
|---|---|---|
| **Cellshop** | **403 Forbidden** (bot-wall) | Requiere Scrapling/browser-headless |
| **Nissei** | **403 Forbidden** | Ídem |
| **Fastrax** | robots 200 abierto | Scrape directo, empezar acá |
| **Shopping China** | robots+sitemap 200 | Scrape directo |
| Tupi | sitemap estático (xml-sitemaps) | Scrape fácil, benchmark de precios |
| Umarket | Next.js + sitemap | JSON interno explotable |

---

## A. Datos & Sourcing (sombreros 1-5)

### 1. Economista del mapa de precios CDE
La idea de "scrapear todos los proveedores" es correcta pero el activo no es el scrape — es la **tabla de diferencias**. Insight: en CDE el mismo SKU varía 10-25% entre mayoristas la misma semana; nadie publica esa dispersión.
- **A.1.1** Índice semanal "dispersión CDE" por categoría (max−min/mediana) → los productos con mayor dispersión son los de mayor margen de arbitraje. *(impacto: +5-10 pts de margen en SKUs elegidos)*
- **A.1.2** Alerta de inversión: cuando precio mayorista X < 0.75×precio de mercado Y sostenido 3 días → oportunidad de stock propio puntual. *(impacto: 2-4 operaciones/mes con 40%+ margen)*
- **A.1.3** Historial de precios como feature de venta: "este producto bajó 18% en CDE este mes" genera contenido de oferta legítimo. *(impacto: +CTR en campañas)*

### 2. SRE de web-scraping
Cellshop y Nissei ya devolvieron 403 — el muro existe el día 0.
- **A.2.1** Stack: Scrapling (stealth) + rotación de User-Agent + cache local; crawl nocturno, no en tiempo real (los precios CDE cambian por semana, no por hora). *(impacto: evita bloqueo IP; -80% costo vs scraping continuo)*
- **A.2.2** Fallback jerárquico por sitio: API/sitemap → HTML → browser headless → WhatsApp manual del proveedor (mensaje semanal automatizado pidiendo lista de precios en Excel — muchos mayoristas ya la tienen). *(impacto: 100% cobertura con 20% del esfuerzo)*
- **A.2.3** Deduplicación por producto entre sitios (los mayoristas CDE venden el mismo importado): fuzzy-match por título+especificaciones → un solo registro canónico con N fuentes de precio. *(impacto: catálogo limpio; base del agente de compras)*

### 3. Operador de sourcing China (1688)
- **A.3.1** El costo landed (flete+aduana+IVA+courier) duplica el precio FOB en aéreo; el agente debe calcular break-even FOB máximo por SKU antes de cotizar. *(impacto: evita las 2 de cada 3 cotizaciones chinas que parecen baratas y no cierran)*
- **A.3.2** Regla: importar directo solo cuando (precio CDE − costo landed) > 25% Y rotación validada ≥ 10 uds/mes. El agente aplica la regla, no el entusiasmo. *(impacto: capital inmovilizado mínimo)*
- **A.3.3** Monitorear el "precio CDE" como proxy de costo importador local: si CDE baja sostenido, el costo 1688 bajó — señal de recompra. *(impacto: timing de compra mejorado)*

### 4. Steward de datos GS1/EAN
La lección WiseQ (0/230 EAN) aplica el día 1.
- **A.4.1** Exigir EAN/código a proveedor en el alta del SKU; para productos sin código, generar código interno (prefijo propio) — nunca dejar el campo vacío. *(impacto: la tabla canónica nunca se pudre)*
- **A.4.2** Adjuntos por SKU: factura del proveedor (PDF), foto real, ficha técnica — el agente los archiva y enlaza. *(impacto: reclamos y garantías resueltos en minutos)*

### 5. Ingeniero de catálogo LLM-ops
- **A.5.1** Pipeline: título crudo del mayorista → LLM normaliza (marca, modelo, atributos) → descripción propia en español + jopara donde el nicho lo pida → ficha única. Nunca publicar la ficha del proveedor (SEO duplicado + el mayorista queda como el autoridad). *(impacto: +SEO, +confianza, identidad propia)*
- **A.5.2** Detección de "productos zombis": listados sin venta en 60 días → auto-pausa. El catálogo se poda solo. *(impacto: -30% ruido publicitario)*
- **A.5.3** Fotos: proveedor manda foto con fondo sucio → pipeline de imagen (recorte, fondo blanco, logo propio) antes de publicar. *(impacto: nivel Tupi sin estudio fotográfico)*

## B. Comercio & Ventas (6-10)

### 6. Vendedor conversacional de WhatsApp
- **B.6.1** El agente no responde preguntas — **cierra**: propone 2 opciones con delivery incluido, pide la dirección, manda QR/seña, agenda el envío. Guión de venta real, no FAQ. *(impacto: +conversión 2-3× vs catálogo pasivo)*
- **B.6.2** Contexto de cliente recurrente: "la última vez llevaste X para tu hijo" — recompra en 2 mensajes. *(impacto: LTV up; 20-30% ventas de recompra a los 6 meses)*
- **B.6.3** Horario honesto: fuera de horario, el agente igual cierra pero promete despacho al día hábil siguiente. La venta no espera. *(impacto: captura el 30-40% de consultas nocturnas que hoy se pierden)*

### 7. Analista de riesgo de contrapedido
El contra-entrega es 28% del mercado — y el vector de pérdida #1.
- **B.7.1** Scoring de pedido: cliente nuevo + ticket alto + zona lejana = seña 20% por QR antes de despachar. Cliente recurrente con historial = contrapedido directo. *(impacto: -50% rechazos en entrega)*
- **B.7.2** El motomensajero cobra y rinde al final del día → conciliación automática del agente contra el pedido; gap = alerta inmediata. *(impacto: caja cuadrada sin trabajo manual)*
- **B.7.3** Zonificación: cobertura Gran Asunción primero (densidad); interior solo con pago adelantado. *(impacto: margen de delivery positivo siempre)*

### 8. Media buyer de Meta Ads
- **B.8.1** Con meta-mcp-server (200+ tools, verificado) el agente crea/pausa/escala campañas nativamente — el "kill/scale" diario es automático contra costo-por-venta de la tabla canónica. *(impacto: publicidad 25% → 12-18% del ticket)*
- **B.8.2** Creativos generados en serie: 3 ángulos × 3 ganchos por producto (precio, beneficio, prueba social) — el agente detecta el ángulo ganador y clona variantes. *(impacto: -CTA cost; fatiga creativa combatida)*
- **B.8.3** Presupuesto tope diario por producto configurado en la tabla; el agente NUNCA lo sube sin aprobación (guardarrail). *(impacto: riesgo acotado por diseño)*

### 9. Estratega de marketplaces PY
- **B.9.1** Umarket (ueno) y Tupi marketplace no son autoservicio — preparar dossier de vendedor DESDE fase 1 (volumen, fotos, facturación) para cuando el acuerdo abra; entrar tarde = dependencia del canal propio para siempre. *(impacto: opción de canal escala)*
- **B.9.2** MELI-PY débil = listing barato: publicar los ganadores también ahí como experimento de bajo costo. *(impacto: canal incremental con esfuerzo mínimo)*
- **B.9.3** Facebook Marketplace como canal de validación Y venta simultánea (el agente re-publica el catálogo automáticamente). *(impacto: 0 costo de adquisición en fase de validación)*

### 10. Psicólogo de precios retail PY
- **B.10.1** Precios ancla en guaraníes redondos (Gs. 199.000, no 189.900) — el consumidor PY compara en múltiplos de 50k; testear A/B automáticamente en la tienda. *(impacto: +margen percibido)*
- **B.10.2** Mostrar precio con IVA siempre (estándar local) y el "en 3 cuotas de X" para tickets >300k vía Bancard. *(impacto: +conversión ticket alto)*
- **B.10.3** Regla de terminación .000 para promos y .900/.990 para precio normal — señal visual de oferta sin bajar tanto. *(impacto: margen defendido en promos)*

## C. Operaciones & Fulfillment (11-15)

### 11. Dispatcher de última milla
- **C.11.1** Agrupación de entregas por zona/horario (el agente arma las rutas del motomensajero cada mañana). *(impacto: -30% costo de delivery por entrega)*
- **C.11.2** Tracking proactivo: mensaje automático al cliente "sale hoy 14-18h" + confirmación de entrega → -llamadas de "¿dónde está mi pedido?". *(impacto: -1h/día de soporte)*
- **C.11.3** Backup de motomensajería: 2 proveedores por zona con tarifa en tabla; el agente elige por costo/disponibilidad por entrega. *(impacto: SLA no se rompe por un ausente)*

### 12. Planificador de stock mínimo
- **C.12.1** Punto de recompra por SKU ganador: promedio 30d × lead-time CDE (48h) + buffer 20% → el agente sugiere la compra semanal. *(impacto: cero quiebres en ganadores sin sobre-stock)*
- **C.12.2** El stock propio vive listado en InvenTree (open source, 7.7k★) sincronizado con la tienda — inventario real, no spreadsheet. *(impacto: contabilidad de stock auditable)*
- **C.12.3** Regla 80/20 del catálogo: 20% SKUs = 80% ventas; el agente marca los A/B/C semanalmente y el dropshipping solo lleva B/C. *(impacto: capital concentrado donde rinde)*

### 13. QA de fallas y devoluciones
- **C.13.1** Política por proveedor en la tabla ANTES de publicar (reposición/pérdida/ventana); el agente bloquea publicación si falta. *(impacto: nunca vender lo que no podés respaldar)*
- **C.13.2** RMA semi-auto: cliente manda foto+video por WhatsApp → agente clasifica (falla/uso/transporte) → genera el reclamo al proveedor con toda la evidencia. *(impacto: -80% tiempo por caso)*
- **C.13.3** Tasa de falla por proveedor como KPI visible — alimenta la decisión de compra semanal. *(impacto: proveedores malos salen solos por datos)*

### 14. Cajero de conciliación
- **C.14.1** Rendición diaria automática: QR+transferencia+contrapedido+tarjeta → un solo número de caja del día contra los pedidos. Gap = alerta. *(impacto: caja cuadrada siempre; detección de fuga en <24h)*
- **C.14.2** Comprobante por screenshot: el agente lee el comprobante del cliente (OCR/vision) y concilia sin mirar el banking manualmente. *(impacto: -30 min/día)*

### 15. Gestor de SLA proveedores
- **C.15.1** SLA medido automáticamente: pedido→despacho→entrega por proveedor; el que promete 24h y cumple 72 baja del ranking solo. *(impacto: negotiating power con datos)*
- **C.15.2** Penalización contractual ligada al dato: descuento % por incumplimiento de SLA (negociable con mayoristas medianos). *(impacto: margen recuperado)*

## D. Tecnología & Integración (16-20)

### 16. Arquitecto de integración Hermes
- **D.16.1** Compra/build vs rent: Evolution API (self-hosted, 9.9k★) como gateway WhatsApp ↔ Hermes; n8n para flujos visuales no-agentes (notificaciones simples); Hermes para todo lo que requiere decisión. *(impacto: costo/plata controlado, sin lock-in SaaS)*
- **D.16.2** La tienda como headless: fase 1 Tiendli/Shoperly (rápido, local, freemium); fase 2 Medusa (36.8k★, "commerce for agents") si el volumen justifica controlar el stack — migración del catálogo es 1 script porque la tabla canónica manda. *(impacto: sin re-plataformitis)*
- **D.16.3** Todo con MCP cuando exista: proveedores con API, Meta (ya existe el server),evolution; lo que no tiene API → browser-automation agent (patrón probado). *(impacto: integración universal)*

### 17. Evaluador de OSS reuse
- **D.17.1** Stack inicial verificado: InvenTree (inventario) + Evolution API (WhatsApp) + Scrapling (scraping) + n8n (flujos simples) + Hermes (orquestación) + sazon-rms/SIFEN (facturación PY, código propio). Odoo/ERPNext SOLO fase 3 si multi-depósito. *(impacto: -80% tiempo de build vs desde cero)*
- **D.17.2** Regla de adopción OSS: componente entra si (a) >1k estrellas o patrón probado AIW, (b) deploy Docker simple, (c) API/CLI completo para el agente. Si no, mejor un script propio de 200 líneas. *(impacto: no coleccionar software, usarlo)*
- **D.17.3** Auditoría de licencias antes de uso comercial (AGPL en algunos ERP/commerce — medusa es MIT, InvenTree MIT, n8n fair-code OK para uso interno). *(impacto: riesgo legal cero)*

### 18. SRE self-hoster
- **D.18.1** Un VPS (€20) lleva todo fase 1: Hermes + Evolution + InvenTree + n8n — docker-compose con backups diarios off-site (regla AIW: backup SIEMPRE antes de migración). *(impacto: costo fijo mínimo con DR)*
- **D.18.2** Health-checks por agente (heartbeat 5 min); si el agente WhatsApp muere, alerta al dueño en Telegram en <5 min — el canal de venta no puede morir en silencio. *(impacto: uptime del vendedor 24/7 real)*
- **D.18.3** Watchdog de reintegro: colas de mensajes persistentes — si WhatsApp cae 2h, los mensajes pendientes salen al volver, no se pierden. *(impacto: cero ventas perdidas por caída)*

### 19. Ingeniero de datos
- **D.19.1** Una sola base canónica (Postgres/SQLite) que TODOS los agentes leen/escriben: productos, precios por proveedor, pedidos, clientes, rendiciones. Sin bases paralelas — la lección WiseQ de canales divergentes, aplicada a nosotros. *(impacto: una sola verdad, cero drift)*
- **D.19.2** Eventos inmutables (append-only) para auditoría: cada precio visto, cada mensaje, cada decisión del agente con timestamp — reproducible y auditable. *(impacto: debugging + confianza)*
- **D.19.3** Export BI semanal automático (duckdb → reporte markdown al dueño). *(impacto: decisión del lunes con datos frescos)*

### 20. Builder de MCP/API interna
- **D.20.1** Exponer NUESTROS datos como MCP propio (productos, stock, precios) → cualquier agente futuro (incl. de clientes o marketplaces) consulta en estándar. Es el patrón agents.md/UCP de WiseQ, aplicado a PY. *(impacto: infra de agentic-commerce propia — ventaja de años en el mercado local)*
- **D.20.2** Los mayoristas scrapeados → feed JSON estandarizado por proveedor; el día que un proveedor dé API real, se cambia el conector y nada más cambia. *(impacto: el stack sobrevive a cambios de proveedor)*

## E. Dinero & Compliance (21-25)

### 21. Contador SET paraguayo
- **E.21.1** Régimen simplificado vs régimen general: modelar el umbral de ventas donde conviene cambiar (el agente calcula ambos escenarios mensualmente con datos reales). *(impacto: decisión fiscal con números, no miedo)*
- **E.21.2** Factura electrónica por venta automática (SIFEN) + factura de compra registrada → IVA crédito/débito claro por período. *(impacto: declaración mensual en minutos)*
- **E.21.3** RUC desde el día 1 aunque la primera venta tarde — sin RUC no hay campaña publicitaria formal ni acuerdo con mayorista serio. *(impacto: habilita todo lo demás)*

### 22. CFO de unit economics
- **E.22.1** Cada SKU con tarjeta de costo completa: mayorista + delivery + comisión cobro + publicidad asignada + IVA + empaque → margen neto REAL por unidad; el que no supera 12% no se publica. *(impacto: disciplina de margen automatizada)*
- **E.22.2** Semáforo semanal de salud: margen neto promedio, CAC, ticket medio, recompra — 4 números, un mensaje de WhatsApp al dueño. *(impacto: foco gerencial en 1 pantalla)*
- **E.22.3** Costo del stack visible como línea más del unit economics (IA+VPS+WhatsApp API por venta) — la automatización se paga sola o se recorta. *(impacto: honestidad total del modelo)*

### 23. Operador de tipo de cambio
- **E.23.1** Precio de compra en USD (China) y venta en Gs → el agente monitorea USD/Gs y ajusta precios de la línea importada con regla de banda (±2%); no repricing diario emocional. *(impacto: margen protegido contra devaluación)*
- **E.23.2** Timing de compra 1688 ligado al tipo de cambio: dólar barato = ventana de importación. *(impacto: +5-8% margen en línea importada)*

### 24. Oficial de riesgo/fraude
- **E.24.1** Catálogo de estafas PY conocido (comprobante editado, "ya transferí" falso, retiro por tercero): el agente verifica comprobante contra estado de cuenta/QR id antes de despachar tickets altos. *(impacto: -perdas por fraude)*
- **E.24.2** Lista interna de clientes conflictivos (rechazos repetidos de contrapedido) — bloqueo automático a prepago solamente. *(impacto: pérdida recurrente eliminada)*
- **E.24.3** Riesgo WhatsApp ban: Evolution API con número dedicado + calentamiento + volumen razonable; plan B = segundo número listo (la suspensión del canal principal es EL riesgo operacional #1 del modelo). *(impacto: continuidad del canal de ventas)*

### 25. Asegurador de riesgo de inventario
- **E.25.1** Stock propio asegurado + fotos de ingreso documentadas (el agente registra cada ingreso a InvenTree con evidencia) — siniestro demostrable. *(impacto: recuperación real ante robo/incendio)*
- **E.25.2** Límite de capital en stock propio como % del flujo (ej. máx 30%) — el agente bloquea compras que lo excedan. *(impacto: liquidez protegida)*

## F. Cliente & Mercado (26-30)

### 26. Escritor UX en guaraní/jopara
La investigación muestra el vacío: casi no hay NLP/tooling en guaraní (repos de <50★). Nadie atiende en guaraní en e-commerce PY.
- **F.26.1** El agente WhatsApp detecta el idioma del cliente (español/guaraní/jopara) y responde en el mismo — en guaraní con tono simple y cálido. *(impacto: diferenciación emocional IMPOSIBLE de copiar para Tupi/MELI; nicho interior/mercado local fiel)*
- **F.26.2** Glossario propio de venta en guaraní (términos de producto, promos, garantía) curado con hablantes nativos — activo lingüístico propietario. *(impacto: moat de contenido)*
- **F.26.3** Test A/B de idioma por campaña; medir conversión por idioma — dato que ningún competidor PY tiene. *(impacto: aprendizaje de mercado exclusivo)*

### 27. Investigador de confianza del consumidor PY
- **F.27.1** Prueba social local: reseñas de clientes reales con nombre/apellido/foto (con permiso) en la ficha — en un mercado donde el 28% paga contra entrega porque desconfía, la cara local vende. *(impacto: +conversión cliente nuevo)*
- **F.27.2** Garantía explícita en 3 frases (7 días, cambio directo, WhatsApp directo) repetida en cada punto de contacto. *(impacto: objeción de confianza neutralizada)*
- **F.27.3** Contar la operación: "somos de Asunción, compramos en CDE y te lo llevamos" — la transparencia del modelo como story de marca (vs la caos de importar solo). *(impacto: posicionamiento honesto y memorable)*

### 28. Quant de selección de nicho
- **F.28.1** Validación con datos antes de opinar: volumen de publicaciones y velocidad de venta en FB Marketplace/grupos medidos por scraper (cuántas publicaciones del rubro se marcan vendidas por semana). *(impacto: elegir nicho con evidencia, 2 semanas)*
- **F.28.2** Cruce con dispersión de precios CDE (sombrero 1): nicho ideal = demanda visible + alta dispersión + ticket 150-500k. *(impacto: el nicho sale del dato, no del gusto)*
- **F.28.3** Matriz de estacionalidad PY (Día de la Madre mayo, Navidad, día del niño aug, back-to-school feb) — el agente planifica stock y campañas contra el calendario. *(impacto: +30-50% ventas en picos)*

### 29. Analista de inteligencia competitiva
- **F.29.1** Tupi/Nissei/Umarket scrapeados como benchmark semanal (Tupi sitemap ya abierto; Umarket Next.js explotable) → alerta cuando un competidor entra a un nicho nuestro o baja de precio debajo de nuestro piso. *(impacto: reacción en horas, no meses)*
- **F.29.2** Detectar huecos de catálogo: categorías con demanda en FB pero sin oferta formal online → entrada preferencial. *(impacto: first-mover en nichos)*
- **F.29.3** Precio relativo: nuestra regla = siempre entre "CDE retail" y "Tupi" — el cliente percibe ahorro vs retailer y conveniencia vs viajar. *(impacto: posicionamiento de precio defendible)*

### 30. Ingeniero post-venta/reseñas
- **F.30.1** Bucle automático: entrega confirmada → 24h → mensaje de cuidado del producto + pedido de reseña con link directo → incentivo (5% próxima compra). *(impacto: reseñas crecen solas; prueba social compuesta)*
- **F.30.2** Detección de insatisfacción temprana (mensaje negativo → agente escala a humano en <15min con contexto completo). *(impacto: reclamo resuelto = cliente retenido)*

## G. Crecimiento & Contenido (31-35)

### 31. Escritor de contenido/SEO PY
- **G.31.1** La jugada SEO local: guías de compra en español (keyword PY de bajo volumen pero intención alta: "mejor X para Y precio Paraguay") — 2-3/sem por agente, índice de 100+ guías en 6 meses. *(impacto: tráfico orgánico compuesto; CAC estructural a la baja)*
- **G.31.2** Fichas con comparativa propia ("esto vs la versión Pro: cuál te conviene según uso") — contenido que ni el mayorista ni Tupi hacen. *(impacto: conversión + tiempo en página)*

### 32. Productor de social commerce
- **G.32.1** Reels/TikTok del producto real (video generado + voiceover IA en español rioplatense-neutro): demostración de uso, no unboxing genérico. *(impacto: canal orgánico de descubrimiento; PY es heavy Instagram/TikTok)*
- **G.32.2** El "precio de la semana CDE" como formato recurrente (transparencia del sombrero 27) — serie de contenido con audiencia propia. *(impacto: marca = referencia de precios del mercado)*

### 33. Operador de comunidades FB
- **G.33.1** El agente monitorea los grupos de compra-venta de Asunción/Central (palabras clave del nicho) y responde/consulta con propuesta directa donde las reglas del grupo lo permitan. *(impacto: demanda existente capturada a costo 0)*
- **G.33.2** Reporte mensual de "qué se pregunta en los grupos" → ideas de producto y contenido. *(impacto: pulso del mercado real)*

### 34. Constructor de marca
- **G.34.1** Marca paraguaya de confianza ("traído de CDE, garantizado en Asunción") — nombre propio + tono consistente en todo el stack; la marca es el activo cuando el proveedor es común a todos. *(impacto: la única defensa duradera vs competencia de precio)*
- **G.34.2** Fase 3 white-label de ganadores (la lección WiseQ): fabricante chino pone TU marca cuando el volumen lo justifica → margen y defensabilidad. *(impacto: de revendedor a marca)*

### 35. Lifecycle CRM (WhatsApp-first)
- **G.35.1** Segmentación automática de clientes (comprador de gaming/hogar/regalo) → mensajes de reposición y accesorio cruzado relevantes, no spam. *(impacto: recompra +15-20%)*
- **G.35.2** Carrito/consulta abandonada: el que preguntó y no cerró recibe seguimiento a las 2h con la oferta cerrada (delivery incluido). *(impacto: recuperación 10-15% de consultas tibias)*

## H. Estrategia & Riesgo (36-40)

### 36. Optimizador de costo IA
- **H.36.1** Ruteo de modelo por tarea: scraping-parseo y clasificación → modelo barato; decisiones de compra y conversaciones cliente → modelo fuerte. *(impacto: -60-70% costo IA vs todo-strong)*
- **H.36.2** Cacheo de respuestas repetidas (preguntas frecuentes reales del catálogo) — 70% de mensajes WhatsApp se responden sin LLM. *(impacto: latencia ↓, costo ↓)*

### 37. Abogado consumidor PY (defensa)
- **H.37.1** Ley 1334/98 (defensa del consumidor) aplica a e-commerce: política de devolución visible y honrada no es opcional — el agente la publica y la cumple al pie. *(impacto: cero sanciones/reclamos virales)*
- **H.37.2** Preventa = contrato: plazo escrito + seña documentada + opción de reembolso si se retrasa — regla automática del agente. *(impacto: riesgo legal de preventa eliminado)*

### 38. Estratega de escala/franquicia
- **H.38.1** El stack es replicable por ciudad: Encarnación, Ciudad del Este, Coronel Oviedo — mismo código, otros proveedores/motomensajerías; el playbook se documenta desde el día 1. *(impacto: expansión = configuración)*
- **H.38.2** "Operador local" como figura: un humano + nuestro stack por ciudad (el modelo de agente convierte un emprendedor con Gs. 5M en un competidor de retail). *(impacto: escala sin capital propio pesado)*

### 39. Estratega de reusabilidad AIW
- **H.39.1** Cada componente del stack se construye como producto reutilizable (agente CDE, WhatsApp-seller, conciliador) con su skill de documentación — la operación PY financia el desarrollo de las herramientas que AIW vende a retailers PY/LATAM. *(impacto: doble retorno — operación + servicio)*
- **H.39.2** El caso de éxito documentado (números reales de la operación) es el activo comercial más fuerte para el próximo cliente WiseQ-style regional. *(impacto: credibilidad de venta)*

### 40. Red-team / escéptico
Lo que puede matar esto, sin filtro:
- **H.40.1** **Riesgo #1: ban de WhatsApp.** Toda la venta vive en un canal prestado. Mitigación: Evolution API + número secundario + captación a canal propio (lista de difusión/telegram fallback) desde fase 1. *(sin mitigación = modelo frágil)*
- **H.40.2** **Riesgo #2: dependencia de 1-2 mayoristas.** El "dropshipping local" es un acuerdo de caballeros por WhatsApp — si el mayorista sube o corta, el negocio se detiene. Mitigación: 2+ proveedores por SKU ganador y el path a importación directa a los 6 meses.
- **H.40.3** **Riesgo #3: margen fantasma.** El 10-20% neto del mercado se evapora con publicidad mal medida y fallas no repuestas — la contabilidad por SKU del sombrero 22 no es opcional, es el negocio. Y si después de 90 días el margen neto real <8%, la conclusión honesta es pivotar de nicho o de modelo — el stack lo sabe antes que el dueño.

---

## Síntesis: Top 10 por ROI × frecuencia × esfuerzo

| # | Idea | Sombrero | Por qué primera |
|---|---|---|---|
| 1 | Agente WhatsApp que CIERRA (no FAQ) + contrapedido con scoring | 6,7 | El canal donde PY compra; ventaja desde semana 1 |
| 2 | Scraping jerárquico CDE empezando por los abiertos (Fastrax, Shopping China, Tupi) + índice de dispersión | 1,2 | El activo de información que nadie tiene |
| 3 | Tabla canónica única + EAN desde el día 1 | 4,19 | La lección WiseQ aplicada antes de necesitarla |
| 4 | meta-mcp-server → agente de campañas con guardarrail de presupuesto | 8 | Publicidad 25%→15% cambia la matemática entera |
| 5 | Conciliación de caja automática + comprobantes por vision | 14,24 | La condición para escalar contrapedido sin fugas |
| 6 | Killer de zombis + fichas propias LLM (nunca la del mayorista) | 5 | Catálogo prolijo = marca, desde el día 1 |
| 7 | Validación de nicho por datos (FB Marketplace velocity + dispersión CDE) | 28 | Elegir bien una vez vale más que optimizar después |
| 8 | Atención en guaraní | 26 | Diferenciador imposible de copiar, costo marginal ~0 |
| 9 | Riesgo WhatsApp: número backup + plan fallback desde fase 1 | 40 | El riesgo existencial, mitigado por Gs. 0 |
| 10 | Todo componente documentado como producto AIW reutilizable | 39 | La operación financia el arsenal de servicios |

## Descartes explícitos [NUNCA/DESPUÉS]

- **Odoo/ERPNext en fase 1** — complejidad de ERP para una operación que aún no tiene 150 ventas/mes. Fase 3 si multi-depósito. (Odoo = 55k★ pero es un hipopótamo para arrancar)
- **GreaterWMS** — orientado a bodega física propia; no aplica a dropshipping puro.
- **Tienda propia Medusa/Saleor en fase 0-1** — Tiendli/Shoperly primero; la tabla canónica hace la migración trivial cuando toque.
- **Scraping en tiempo real** — precios CDE cambian semanalmente; nocturno basta.
- **ML de predicción de demanda sofisticado** — con <5k ventas no hay datos; la regla de promedio-30d×lead-time es suficiente y explicable.
- **App móvil propia** — WhatsApp ES la app del cliente paraguayo.
- **Cryptopagos** — fuera del scope; el mercado pide QR/efectivo.

## Cambios al roadmap (delta sobre 05-ROADMAP)

- Fase 0 agrega: número WhatsApp backup (H.40.1), validación de nicho por scraper FB (F.28.1), glossario guaraní v0 (F.26.2)
- Fase 1 agrega: Evolution API como gateway (D.16.1), scraping jerárquico nocturno (A.2.1), conciliación de caja (C.14.1), meta-mcp-server (B.8.1)
- Fase 2 agrega: índice de dispersión CDE público-interno (A.1.1), zonificación de cobertura (B.7.3), semáforo semanal 4-números (E.22.2)
- Nueva fase transversal: documentación de cada componente como skill AIW (H.39.1)
