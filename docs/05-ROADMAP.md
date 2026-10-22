# Roadmap — PY Dropship AI

## Fase 0 — Validación (semanas 1-3) · Presupuesto: Gs. 2-4M

- [ ] Elegir nicho con los criterios (02-MODELO-NEGOCIO) y validarlo en Facebook Marketplace/grupos (¿se vende? ¿a qué precio?)
- [ ] Contactar 5-8 mayoristas CDE (lista 03-PROVEEDORES) — pedir lista mayorista, condiciones de despacho, política de fallas, muestras
- [ ] Cerrar con **2 proveedores** mínimo (redundancia)
- [ ] RUC (gratis) + alta de factura electrónica SIFEN
- [ ] Tienda freemium (Tiendli/Shoperly) con 10-20 productos del nicho — descripciones propias, fotos propias
- [ ] Número WhatsApp Business dedicado
- **Hito de salida:** primera venta manual de punta a punta (pedido → CDE → delivery → factura)

## Fase 1 — Automatización del núcleo (semanas 4-8)

- [ ] VPS + Hermes: agentes 2 (WhatsApp), 3 (tienda), 4 (pagos/pedidos/SIFEN) online
- [ ] Tabla canónica producto (proveedor CDE + precio + stock + margen) — semiautomática al inicio
- [ ] Meta Ads con presupuesto Gs. 300k-1M: 2-3 productos test, creativos generados, kill/scale manual-diario
- **Métricas de salida:** 3-5 ventas/día sostenidas; tiempo del dueño por pedido < 10 min; tasa de respuesta WhatsApp < 1 min en horario completo

## Fase 2 — Motores de margen (semanas 9-16)

- [ ] Agente CDE online: mapa de precios semanal, alertas de oportunidad/quiebre
- [ ] Agente publicidad en modo automático (kill/scale por costo-por-venta)
- [ ] Primeros 3 SKUs validados → agente sourcing China cotiza landed; decisión de stock propio
- [ ] Preventa controlada para 1-2 productos en contenedor
- **Métricas de salida:** margen neto ≥ 15%; publicidad ≤ 18% del ticket; 150+ ventas/mes (Gs. 3M+ neto/mes)

## Fase 3 — Escala (trimestre 2)

- [ ] Nicho #2 y #3 (el stack lo hace configuración)
- [ ] Negociar ingreso a Umarket/Tupi marketplace si el volumen lo justifica
- [ ] Importación propia en volumen (agente aduanero; LAC para marítimo)
- [ ] Marca propia sobre los ganadores (white-label del fabricante chino — la lección WiseQ aplicada a PY)
- **Métricas:** Gs. 10M+ neto/mes; 2+ proveedores por categoría; NPS/reseñas creciendo

## Costos fijos estimados (mes típico, fase 1-2)

| Concepto | Gs./mes |
|---|---|
| VPS + IA (plan proveedor) | ~1.500.000 (US$~90 clase europea + margen tipo de cambio) |
| WhatsApp Business API | ~300.000-800.000 (según volumen) |
| Tienda freemium → plan pago | 0 → ~300.000 |
| Dominio + misc | ~100.000 |
| **Total fijo** | **~2-3M** |

Con 150 ventas/mes × Gs. 20.000 neto = Gs. 3M → el stack se paga solo desde fase 1 tardía. (Publicidad es variable, presupuestada por producto.)

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Proveedor CDE se queda sin stock / despacha tarde | 2 proveedores por categoría; SLA escrito; agente detecta y re-encamina |
| Contra entrega con rechazo | Comprobante de intención (seña QR 10-20% para desconocidos); zona de cobertura acotada al inicio |
| Aduana cambia régimen courier | Preventa documentada; agente aduanero formal para volumen |
| Competencia de precio en el mismo mayorista | Diferenciar en servicio (respuesta, contenido, entrega) y en sourcing directo de ganadores |
| Dependencia de Meta Ads | Canal propio WhatsApp creciente; contenido orgánico; marketplace cuando abra |
