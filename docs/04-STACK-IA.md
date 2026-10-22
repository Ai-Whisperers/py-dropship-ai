# Stack de IA — Dropshipping Paraguay

*La propuesta central: la misma arquitectura de agentes de AI Whisperers (Hermes), adaptada al flujo paraguayo. Cada agente es un trabajo cron/webhook con memoria, habilidades y bitácora — no un chatbot.*

## Arquitectura

```
                          ┌────────────────────────────────┐
                          │     HERMES AGENT (24/7)        │
                          │ orquestador + memoria + cron   │
                          └───────────────┬────────────────┘
      ┌──────────┬───────────┬────────────┼─────────────┬─────────────┐
      ▼          ▼           ▼            ▼             ▼             ▼
 WhatsApp   Tienda online  Pagos      Proveedores    Meta Ads      Back-office
 (venta+   (catálogo,     (QR/SPI/   CDE + 1688     (creativos,   (SIFEN,
 soporte)   pedidos)      contra     (precio/stock  kill/scale)   planillas,
                           entrega)  /despacho)                   RUC)
```

Infra: VPS €20/mes (o el equipo local). Credenciales en vault. Toda acción con log de auditoría; pasos que tocan dinero con aprobación humana hasta ganar confianza.

## Los 8 agentes

### 1. Agente CDE (monitoreo de proveedores) 🔥
Scraping/API de precios y stock de mayoristas con presencia online (Cellshop, Shopping China, Fastrax, Nissei como referencia). Salida: tabla de precios semanal, alertas de oportunidades (producto en oferta en CDE → promo en Asunción), detección de quiebre de margen. **Este es el equivalente exacto del "monitoreo chino" que el fundador de WiseQ describió** — acá lo construimos para nosotros.

### 2. Agente WhatsApp (venta y soporte 24/7) 🔥
El canal donde PY compra. Responde consultas en guaraní/español con el catálogo vivo, cotiza con delivery, cierra el pedido, coordina pago (QR/transferencia/contra entrega), hace seguimiento post-venta y pide reseña. Escalada a humano en casos raros. WhatsApp Business API o número dedicado + gateway.

### 3. Agente de tienda
Publica/actualiza el catálogo (fotos + descripciones generadas en estilo propio — la lección WiseQ: nunca copiar la ficha del mayorista), precios IVA-incluido, sincroniza disponibilidad con la tabla canónica, baja lo que se agotó en CDE.

### 4. Agente de pagos y pedidos
Confirma transferencias/QR (comprobante por WhatsApp → conciliación), dispara el despacho al proveedor con la dirección, coordina motomensajería para contra entrega, y rinde caja diario. SIFEN: emite factura electrónica por venta (stack ya conocido del ecosistema sazon-rms/kiki).

### 5. Agente de publicidad (Meta Ads)
Genera creativos (imágenes IA en estilo consistente + copies en español/guaraní), lanza tests con presupuesto chico, mide costo-por-venta contra la tabla canónica, mata lo que no cierra y escala lo que sí. Target: mantener publicidad en 12-18% del ticket.

### 6. Agente de sourcing China
Para SKUs validados: cotiza en 1688 vía agente (Chilat/3A), calcula costo landed (flete+despacho+IVA+courier), compara con precio CDE, arma la recomendación de importación con MOQ y break-even. Orquesta muestras.

### 7. Agente de contenido
Instagram/Facebook Marketplace: re-publicación del catálogo, contenido de nicho generado (la validación local empieza en los grupos de compra-venta), respuestas a comentarios/DM.

### 8. Agente back-office
Planillas, IVA, RUC, reporte semanal del negocio (ventas, margen por SKU, rendimiento de proveedor, desempeño de publicidad) — el "informe que el dueño lee los lunes".

## Por qué este stack gana en este mercado

1. **Velocidad de respuesta** — en un mercado que compra por WhatsApp, contestar en segundos las 24h es la ventaja injusta #1
2. **Información de precios** — nadie monitorea CDE sistemáticamente para revender en Asunción; el que tiene el mapa de precios compra mejor siempre
3. **Consistencia** — catálogo prolijo, descripciones propias, seguimiento de pedido — el nivel Tupi en un nicho
4. **Costo** — el stack completo cuesta un VPS + un plan de IA + WhatsApp API; compite con operaciones de 5 personas
5. **Escalable por diseño** — la tabla canónica + agentes = agregar nicho/categoría es configuración, no reconstrucción (misma tesis del playbook WiseQ: una operación, muchos nichos)

## Guardarrails

- Contra entrega: la motomensajería cobra y rinde; el agente concilia — si hay gap, alerta inmediata
- Devoluciones/fallas: política escrita por proveedor ANTES de publicar el producto
- Preventa: plazo por escrito antes de cobrar; sena documentada
- Toda campaña publicitaria con presupuesto tope diario; kill automático
- Factura electrónica en cada venta — sin excepciones
- Datos de clientes: mínimos necesarios, almacenados en PY, sin terceros innecesarios
