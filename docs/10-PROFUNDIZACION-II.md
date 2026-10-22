# Profundización II — Fiscal, Publicidad, Garantías, Nicho y Finanzas

*Segunda ronda de investigación con fuentes verificadas, 2026-10-22. Complementa 09. Cada sección cierra con decisiones para el stack.*

## 1. Fiscal: RESIMPLE es el régimen del fase 0-1 (y el número que cambia el plan)

| Régimen | Ingresos anuales | Tasa | Nota |
|---|---|---|---|
| **RESIMPLE** | hasta ₲80.000.000 | **₲20.000-80.000/mes fijo** | Emite **Boleta Resimple** (no factura); no da crédito fiscal al cliente |
| SIMPLE | hasta ₲2.000M | 10% renta neta | Factura electrónica SIFEN por calendario de grupos 2025-2026 |
| General | >₲2.000M | 10% + complejidad | Fuera de alcance fase 0-2 |

**Implicancias operativas concretas:**
- **RESIMPLE dura hasta ~₲6,7M de facturación mensual.** Nuestro roadmap fase 2 (150 ventas/mes × ticket ₲250k = ₲37,5M/mes) **excede RESIMPLE 5×** — el salto a SIMPLE es un hito planificado, no una sorpresa. El agente lleva el contador de facturación acumulada y **alerta al 80% del tope** (₲64M acumulados) con el modelado SIMPLE-vs-RESIMPLE ya calculado.
- RESIMPLE = boleta, no factura → **B2B queda bloqueado en fase 0-1** (empresas no pueden deducir). Coherente con la estrategia B2C-primero; el salto a SIMPLE desbloquea el B2B (colegios, oficinas) — dos razones para el mismo salto.
- **IVA real:** sin factura de compra en CDE, el IVA crédito se pierde → regla de negocio: **pedir factura SIEMPRE al mayorista, aunque descuenten el precio sin factura**. La cuenta: IVA débito 10,91% del precio final menos IVA crédito de la compra; sin crédito, el IVA efectivo se duplica. El agente adjunta la factura de compra al SKU (sombrero A.4.2) y calcula IVA real por período.
- DNIT cruza transferencias/Tigo Money/Pagopar para detectar informalidad — la informalidad tiene fecha de vencimiento; el costo de formalizarse es ₲20k/mes.
- **IRP** (personal): solo si ingresos personales > 36 salarios mínimos (~₲100M/año); modelar al escalar.
- Formalización fase 0: RUC + obligación RESIMPLE vía Marangatú + **patente comercial municipal** (Asunción: DDJJ comercio + balance + uso de suelo). Para home-office sin depósito: patente mínima. Contador: ₲0 en RESIMPLE; ₲500-800k/mes al pasar a SIMPLE.

## 2. Publicidad: los números reales que faltaban

- **LATAM es la región más barata del mundo para Meta Ads**: CPM $2-8 USD por país; **PY no está tabulado pero se ubica con los mercados pequeños de la región (franja baja $2-4)**. CPC ecommerce ~$0,67 promedio, rango emergente $0,20-1,50.
- **El número que manda: presupuesto mínimo funcional $300-500 USD/mes** (Gs. 2,4-4M) para que el algoritmo salga de la fase de aprendizaje (~50 conversiones/semana). Por debajo, se paga más por venta.
- TikTok Ads CPC $0,10-0,30 (adquisición fría más barata), Google Shopping $0,20-0,66 (demanda existente).
- **Checklist pre-pauta** (del propio Meta, vía agencia): Pixel + Conversions API verificados, 3+ creativos, ubicaciones automáticas, objetivo conversión, **CPA máximo definido según margen ANTES de encender**, plan 60-90 días.

**Decisiones para el stack:**
- Presupuesto fase 0 validación: **Gs. 3M/mes (USD ~390)** — dentro del mínimo funcional; una sola campaña de conversión, no cinco.
- El **CPA máximo por producto = margen neto × 0,5** se calcula solo (de la tabla canónica) y el agente no lo deja subir sin aprobación (guardarrail ya definido en B.8.3, ahora con número ancla).
- Fase 0 mide creativos orgánicos (FB Marketplace/grupos) ANTES de pagar pauta — el ganador orgánico es el primer creativo pago.
- Facebook/Instagram = remarketing + demanda nueva; TikTok = experimento fase 2 (CPC más barato, audiencia PY en TikTok por confirmar).
- KPI publicitario inicial: **ROAS ≥ 2 en 30 días** con margen ≥25% bruto; si no, cortar y pivotar de creativo/producto, no subir presupuesto.

## 3. Garantía legal: la Ley 1334/98 tal como aplica a dropshipping

- **Art. 26: derecho de retractación de 7 días** desde la recepción (ventas a distancia) — el agente lo honra al pie: devolución + reembolso dentro del plazo, sin fricción. Es ley, no cortesía.
- Art. 27: cláusulas se interpretan a favor del consumidor → términos claros y simples, nada de letra chica.
- **Cadena de garantía:** frente al cliente SOMOS el vendedor responsable; frente al proveedor CDE recuperamos después. El agente de RMA (C.13.2) ejecuta ambos lados: al cliente se le resuelve en días; al proveedor se le reclama con evidencia.
- **Garantía comercial mínima**: 30 días por falla de fábrica (regla propia sobre el piso legal) — simple de comunicar: "falla en 30 días, cambio directo".
- Proveedores: exigir política de garantía por ESCRITO al alta (sombrero C.13.1) — sin política clara, no se publica el SKU.

## 4. Nicho: las señales de demanda ya visibles

Lo que los datos públicos ya muestran que se mueve en PY online:

| Señal | Dato | Fuente |
|---|---|--- fase
| Perfumes importados | Margen típico reventa **30%+** desde CDE | Shoperly guía perfumes 2026 |
| Tecnología/accesorios | Top-1 búsquedas: smartphones y electrónicos; Shopping China "variedad", Cellshop "tech y perfumes" | hoteltarobafoz / Shoperly |
| Accesorios Apple, cámaras, audio premium, gaming, perfumes | "Mejores productos para reventa" con margen destacado | Shoperly guía Nissei 2026 |
| Gaming global | Accesorios gaming: USD 13,09B (2025) → 14,39B (2026) | Mordor Intelligence |
| Crecimiento e-commerce PY | Proyección de crecimiento fuerte hasta 2027 | PCMI |

**Criterios aplicados (de 02-MODELO y sombrero 28):** ticket ₲150-500k ✓ (perfumes, audio, gaming accesorios), alta dispersión de precios CDE ✓, valor/peso alto para importación eventual ✓, contenido demostrable en video ✓. Los tres candidatos finales que emergen del cruce: **(1) perfumes/fragancias, (2) audio + gaming accesorios, (3) accesorios Apple/MFi**. La validación fase 0 (FB Marketplace velocity, sombrero F.28.1) decide entre los tres con datos, no con opiniones.

**Nota anti-riesgo:** perfumes = guerra de autenticidad (la guía entera de Shoperly gira en torno a "¿es original?"). Si se elige, la prueba de autenticidad (factura importador + lote) es parte del producto; el agente responde la objeción con evidencia en el primer mensaje.

## 5. Riesgo financiero operacional: los números de fallo

- **Margen real fase 0: 0-8%** (aprendizaje) — separar runway personal del capital operativo; jamás financiar stock con el mismo dinero que la pauta.
- **Punto de corte honesto (ya en H.40.3):** 90 días sin margen neto ≥8% → pivotar nicho o parar. El semáforo de 4 números (E.22.2) es el tablero de decisión.
- **Contingencia WhatsApp** (H.40.1): el número backup cuesta Gs. 0 mantenerse; la pérdida del canal principal sin lista propia = pérdida del negocio entero. La lista de difusión propia (permisos opt-in registrados — ahora también obligación 7593/2025) se construye desde la primera venta.
- **Estacionalidad negativa:** diciembre-enero (aguinaldo se va en Navidad+vacaciones), marzo flojo post-back-to-school. El forecast (T4) programa compras CDE a la baja en esos meses.

## 6. Otras consideraciones que surgieron y dónde viven

- **Dominio .com.py** (confianza local + SEO local): registrar el día 1 — ya anotado en §8 de doc 09.
- **Cuenta bancaria separada** del negocio (error fiscal #2 más común): la cuenta ueno bank de uPay sirve de cuenta operativo desde el día 1.
- **Comprobantes 5 años** (DNIT): el agente archiva compra+venta+comprobante de cobro por pedido en almacenamiento versionado — auditoría de 5 años resuelta por diseño.
- **Términos y condiciones + política de devolución visibles** en la tienda (1334/98 + confianza): el agente los publica y CUMPLE — inconsistencia entre política escrita y práctica real es el multiplying risk de reclamos.
- **Meta Business verification** para WhatsApp Business API oficial (fase 2+): con RUC + web + dominio propio es trámite; el plan Evolution API primero (fase 0-1) sigue siendo el correcto por costo.
- **Nombre de marca**: verificar registro en DINAPI (marcas PY) antes de invertir en identidad — barato ahora, caro después.

---

*Fuentes: shoperly.app (fiscal RESIMPLE/SIMPLE, perfumes, Nissei, Shopping China — guías 2026), somositera.com (Meta Ads LATAM 2026, extraída completa), BACN Ley 1334/98 (art. 26/27), asuncion.gov.py/suace.gov.py (patente comercial), Mordor Intelligence (gaming), PCMI (proyección e-commerce PY). Cacheadas en workspace.*
