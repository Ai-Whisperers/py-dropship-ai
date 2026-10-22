# Profundización 2026-10-22 — Pagos, Legal, Aduana, Competencia y Mejoras Técnicas

*Nueva ronda de investigación con fuentes verificadas. Complementa 01 (mercado) y 07 (40 sombreros). Cada sección termina en decisiones concretas para el stack.*

## 1. Pagos: el mapa cambió en julio 2026

**Hecho central:** desde el 1 de julio de 2026 rige la 2ª fase de la resolución del BCP que **tope las comisiones en 3% crédito / 2% débito, aplicando a toda la cadena** (bancos, pasarelas, agregadores). Guías anteriores a esa fecha (5-7% de Pagopar) están desactualizadas.

| Opción | Costo | Notas operativas |
|---|---|---|
| **uPay Base** (ueno bank; absorbió Pagopar) | Gs. 0/mes; 2% débito y QR propio, 2,9% crédito local, 3% intl | Exige ser cliente de ueno bank; **Link de Pagos** por WhatsApp (vence 48h) — hecho a nuestra medida |
| **Bancard vPOS** | Gs. 74.900/mes; 3% crédito / 2% débito | **Cuotas** con tarjetas locales + débito acredita en línea — la opción si vendemos tickets altos |
| **AdamsPay** | Capa encima de Bancard; plan gratis 10 cobros/mes | Solo si queremos ahorrarnos la integración |
| **Transferencia / QR bancario** | 0% para nosotros | La forma más natural de pagar en PY; el agente concilia por comprobante |
| **PayPal / Stripe / Mercado Pago** | ❌ No operan recepción en PY | Cualquier tutorial que los use, no aplica |

**Decisiones para el stack:**
- Canal principal de cobro: transferencia/QR bancario (0% comisión) + link uPay para tarjeta — el agente manda el link dentro del chat de WhatsApp y concilia el comprobante.
- Cuotas (Bancard) solo cuando el ticket medio del nicho supere ~Gs. 500k: ahí las cuotas son el arma de los grandes (Compumundo: 18 cuotas sin interés) y nuestro contra es precio+rapidez, no financiamiento.
- La comisión efectiva de cobro en el unit economics baja de ~3,5% (supuesto anterior) a **~1,2% ponderado** (70% QR/transferencia, 30% tarjeta) — recalibrar la tabla de 02-MODELO-NEGOCIO con esto.

## 2. Ley 7593/2025 de Protección de Datos — la ventana es AHORA

Promulgada 27-nov-2025; **vacatio legis de 24 meses → plena vigencia noviembre 2027**. Modelo tipo GDPR: alcance extraterritorial, 7 bases de licitud, datos sensibles, oficial de datos, notificación de brechas en 72h, multas hasta **10.000 jornales mínimos**. Autoridad: agencia bajo MITIC.

**Qué significa para una operación que arranca en 2026:**
- **Ventaja del que empieza tarde al papel, temprano al dato:** nosotros construimos el stack DENTRO de la ventana de adecuación — privacy-by-design desde el día 1 cuesta ~0; retrofit en 2027 cuesta caro y duele.
- Obligaciones concretas que el stack debe resolver solo: (a) registro de consentimiento con fecha/medio (carga de prueba es NUESTRA), (b) minimización — no pedir cédula si no hace falta, (c) contratos de encargado con cada proveedor que toca datos (hosting, Evolution API, pasarela), (d) protocolo de brecha 72h, (e) derecho de acceso/eliminación del cliente ejecutable en minutos, no semanas.
- **Agente de privacidad:** un cron job que mensualmente (1) lista qué datos personales existen y dónde, (2) verifica que cada consentimiento registrado tiene su entrada, (3) responde solicitudes DSR (acceso/borrado) semi-automáticamente con aprobación humana. *(impacto: compliance continua, no proyecto de pánico en 2027)*
- Base de licitud principal para nosotros: **ejecución de contrato** (el pedido) + **interés legítimo** (post-venta, recompra) — consentimiento explícito solo para marketing. El agente etiqueta cada mensaje saliente con su base legal.

## 3. Importación: régimen courier y economía por kilo

- **Régimen Courier** (DNCA): envíos simplificados **hasta USD 1.000** con trámite digital rápido; couriers consolidados incluyen impuestos hasta ese tope (paraguaycourier: USD 33/kg CN→PY impuestos incluidos; tarifas promocionales vistas a USD 26,50/kg; operadores con consolidado marítimo+aéreo llegan a ~USD 2/kg en volumen — TikTok operadores, verificar caso por caso).
- **Pequeños envíos ≠ sin impuestos:** hasta USD 400 por courier paga IVA + internos igual — el "free import" es mito.
- **Implicancia para 1688:** el costo landed aéreo (flete 26-33 USD/kg) hace que solo productos con alta relación valor/peso (accesorios, componentes, no electro grande) cierren directo. Para volumen: consolidado marítimo (semanas, ~10× más barato por kg) para reponer ganadores.

**Decisiones:** (1) el Agente 1688 calcula landed con tarifa/kg real del courier elegido (tabla configurable), no con estimación plana; (2) umbral de importación directa re-validado: FOB máx = (precio CDE × 0,7 − landed) con landed = f(peso); (3) fase 2 incluye cotizador multi-courier automático (3A, Chilat, ParaguayCourier, Asunción Courier) por envío.

## 4. Competencia ampliada — jugadores que el doc 01 no cubría

| Jugador | Qué es | Nuestra lectura |
|---|---|---|
| **Tiendamia** | Cross-border marketplace +10 países, presente en PY | Compite en marcas importadas; nuestro contra: entrega 24-72h local vs 1-3 semanas |
| **Shein/Temu vía couriers** (QXpress, Ñanduti) | Acceso con fricción (intermediario, umbral envío gratis 800k Gs) | Compite en precio crudo; nuestro contra: sin fricción, garantía local, español/guaraní |
| **MELI-PY** | Comisión **13-20% por venta** según categoría | El costo de canal más alto del mercado — publicar ahí solo con margen ≥35% o como tráfico de validación |
| **Compumundo / grandes** | 18 cuotas sin interés, pick-up gratis | Arma = financiamiento; nuestro nicho debe ser ticket medio donde las cuotas no deciden |
| **Importados CDE en FB/IG** (MaxiCdE etc.) | Venden "envíos a todo el país", transferencia | Competencia real directa — se gana por velocidad de respuesta (agente 24/7) y profesionalidad de ficha |

**Decisión:** el mapa de precios CDE (sombrero 1) ahora también rastrea **precios retail online de 4-5 vendedores FB/IG de CDE** — el benchmark real no es Nissei, es el importador con página de Instagram.

## 5. Logística última milla — números verificados

- Moto mensajería Gran Asunción: **Gs. 15.000-30.000 por envío** según zona (Luque desde 15k; zonas 30k+).
- Interior por encomienda de bus: **desde Gs. 20.000**.
- Recargos: horario especial Gs. +57.000 (Skypostal como referencia), embalaje especial extra.
- Ecosistema de motos en alquiler para plataformas (Rappi/PedidosYa) existe en Asunción — si el volumen llega a ~40+ envíos/día, arrender moto propia + repartidor fijo pinta mejor que por-envío.

**Decisiones:** zonificar tarifas reales en la tabla (no un promedio plano); el agente cobra delivery al cliente según zona con regla visible; punto de equilibrio moto propia documentado en fase 2 del roadmap.

## 6. SIFEN — trayectoria de obligatoriedad

La SET avanza por fases desde el piloto; la obligatoriedad llega progresivamente a pymes (régimen TIMBRE ya incorporado; pequeños contribuyentes entrando por calendario). **Decisión:** factura electrónica desde la primera venta (no esperar nuestra fase en el calendario SET) — el ecosistema propio (sazon-rms) ya resuelve emisión; el agente emite y archiva el XML por pedido sin toque humano.

## 7. Mejoras técnicas adicionales (capa 2 del stack)

Más allá de los 8 agentes del doc 04 — lo que la investigación de hoy agrega:

| # | Mejora | Qué resuelve | Effort |
|---|---|---|---|
| T1 | **Evals del agente WhatsApp** — set de 100 conversaciones reales etiquetadas, re-test en cada cambio de prompt/modelo | Evita regresiones silenciosas en el vendedor principal | M |
| T2 | **Observabilidad de agentes** — cada decisión logueada con input/output/costo; dashboard semanal | Sabe dónde se va el dinero IA y qué agente falla | M |
| T3 | **Precios dinámicos** — regla: precio = f(costo mayorista, precio competidor más bajo, stock, edad del listado) con piso de margen | Margen defendido sin repriceo manual | M |
| T4 | **Forecast de demanda simple** — promedio móvil + estacionalidad PY (madre-may, niño-ago, navidad, back-to-school-feb) | Compras CDE mejor timed | S |
| T5 | **Búsqueda vectorial del catálogo** — el cliente describe ("auriculares resistentes para nene de 7") y el agente encuentra el SKU | Conversación natural → producto correcto | S |
| T6 | **RAG interno de políticas** — garantías, cambios, coberturas; el agente responde con la política oficial, nunca inventa | Consistencia total en post-venta | S |
| T7 | **Pipeline de imagen** — foto proveedor → fondo blanco + logo (OSS ya indexado en doc 08) | Fichas nivel retail sin estudio | S |
| T8 | **Computer-use para admins sin API** — el agente opera el panel del courier/dropshipper como humano | Cubre el 100% del flujo aunque el proveedor no tenga API | M |
| T9 | **Catálogo expuesto como MCP** (patrón WiseQ/UCP) | Los agentes de compra (de clientes u otros) nos descubren | M |
| T10 | **Motor de reseñas post-venta** —WhatsApp D+1, incentivo 5% | Prueba social compuesta (28% contrapedido = desconfianza) | S |
| T11 | **Agente de privacidad** (ver §2) | Compliance 7593/2025 continua | S |
| T12 | **Simulador de escenarios** — qué pasa con el margen si el dólar sube 10% / courier sube 20% / MELI entra al nicho | Decisiones con estrés-test previo | S |

## 8. Consideraciones adicionales que faltaban (checklist ejecutivo)

**Legales/estructura:** elección de forma jurídica (unipersonal vs SRL) modelada al pasar Gs. 100M/año; seguro de stock cuando exista depósito propio; política de devolución 100% visible (Ley 1334/98).

**Operativas:** horario de despacho publicado y cumplido; SLA de respuesta WhatsApp <2min en horario (medido); segundo motomensajero por zona desde el día 1 (backup); plan de contingencia WhatsApp (número 2 + lista de difusión propia).

**Financieras:** runway separado del capital operativo; los primeros 90 días son de APRENDIZAJE (margen real esperado: 0-8%) — el semáforo de 4 números (E.22.2) define si seguimos, pivotamos de nicho o paramos.

**Marca/estrategia:** el "precio de la semana CDE" como franquia de contenido; elegir nombre+dominio .com.py desde el día 1; nula dependencia de un solo canal (WhatsApp + tienda + FB Marketplace simultáneos desde fase 1).

---

*Fuentes clave: builttoclick.com (pasarelas, verificado ago-2026), avanzialegal.com + BACN (Ley 7593/2025), paymentmedia/perspectivas (tope BCP), paraguaycourier.com (tarifas), shoperly.app (delivery), spomsolutions/wivoanalytics (comisiones MELI), icontainers/aduananews (régimen courier DNCA). Cacheadas en el workspace.*
