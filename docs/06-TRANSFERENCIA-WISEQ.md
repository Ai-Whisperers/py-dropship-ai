# Transferencia WiseQ → PY Dropship

*Qué se reutiliza del playbook europeo (wiseq-ai-onboarding) y qué cambia. La tesis: una arquitectura, dos operaciones.*

## Se reutiliza directo

| Activo WiseQ | Aplicación en PY |
|---|---|
| **Tabla canónica de producto** (EAN↔SKU↔proveedores↔componentes) | Idéntico concepto: SKU propio ↔ proveedor CDE ↔ origen 1688 ↔ precio/rotación. La lección de "0/230 EAN en Shopify" se aplica desde el día 1: la clave canónica existe ANTES del catálogo |
| **Agente de monitoreo de proveedores** (el "which Chinese supplier is cheapest now" que Rob describió) | Se convierte en el Agente CDE + Agente sourcing 1688 — mismo patrón, otros endpoints |
| **Pipeline de pedido automático** (email → oferta → factura → booking) | Pedido → despacho CDE → delivery → factura SIFEN → conciliación de caja |
| **Factura electrónica** (SIFEN/XML — ecosistema sazon-rms ya lo resuelve) | Emisión por venta, parseo de facturas de proveedor |
| **Motor de reseñas/reputación** | Post-venta por WhatsApp pidiendo reseña/testimonio (FB/Google) |
| **Agente de contenido** (cópys propios, cadencia, imaginería IA en estilo de casa) | Fichas de producto propias (jamás copiar el mayorista), contenido de nicho IG/FB |
| **Guardarrails** (aprobación humana en lo que toca dinero, auditoría, kill switch) | Idénticos |
| **Lead-gen con registros públicos** (pattern DUO/Francia) | Rejugable para B2B en PY (colegios, empresas —.dataset MEC/SIP para futuras líneas) |

## Se adapta

| WiseQ (NL) | PY Dropship |
|---|---|
| bol.com/Amazon/ChannelDock/5X | Tienda propia + WhatsApp + FB Marketplace; sin marketplace autoservicio dominante |
| Email B2B formal (oferta→factura) | Venta conversacional WhatsApp + contra entrega (28% del mercado) |
| iDEAL/Klarna | QR (64%) / SPI transferencia / Tigo Money / Bancard |
| Envío postal NL/BE | Motomensajería Gran Asunción + encomienda interior |
| Clientes: escuelas (B2B) | Consumidor final Gran Asunción (B2C) primero; B2B después |
| Idioma: neerlandés | Español + guaraní (tono de marca local) |

## Lo que PY tiene de ventaja sobre NL

- **Sin legacy**: no hay incumbent con automatización — el primer jugador con stack de IA en un nicho tiene ventaja injusta
- **Margen de información**: nadie monitorea precios de CDE sistemáticamente para revender en la capital
- **El efectivo-contra-entrega comofeature**: en NL no existe; en PY lo operamos con conciliación por agente
- **Cerca del sourcing**: CDE a 3-5h de Asunción; China directo con agentes ya operando (3A, Chilat)

## Sinergia estratégica

1. **La operación PY es el caso de estudio viviente para el servicio de AI Whisperers**: "mira lo que hicimos funcionar en Asunción" es la demo más fuerte para el próximo cliente WiseQ-style en la región
2. **El agente CDE/1688 es producto reutilizable** — cada retailer PY de electro tiene el mismo problema de precios de proveedores
3. Si WiseQ (o un cliente similar) quiere entrar a LATAM, la infraestructura de pagos/logística/factura ya estará probada
