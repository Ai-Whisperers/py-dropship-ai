# Fuentes de Suministro — Ciudad del Este + China

## A. Ciudad del Este (el depósito natural)

CDE es uno de los mayores hubs de importación de la región — la importación ya está hecha; nuestro trabajo es el eslabón de venta en Asunción/Central.

### Mayoristas / retailers con e-commerce (verificados online, 2026-10-21)

| Proveedor | Qué es | Notas |
|---|---|---|
| **Cellshop** (cellshop.com.py) | El icono de CDE; electrónica/gadgets; e-commerce propio con retiro y envíos | Benchmark de precios Y potencial proveedor mayorista (vende para revender — guía Shoperly "qué comprar y cómo revender" lo confirma como fuente de revendedores) |
| **Nissei** (nissei.com) | Retailer multimarca con online (comprá online - retirá en tienda) | Benchmark de catálogo/precios |
| **Fastrax S.A.** (fastrax.com.py) | Se autodenomina "el mejor mayorista de tecnología en Paraguay" — página mayorista explícita | Candidato proveedor #1 para línea tech |
| **Shopping China** (shoppingchina.com.py) | Mall icónico de CDE con e-commerce propio (envíos; FAQ de compras desde Asunción) | Sourcing mixto gaming/tech/hogar |
| **Grupos FB "IMPORTADORES MAYORISTAS – Ciudad del Este"** | Directorio informal de importadores mayoristas | Discovery de proveedores por rubro |

### Criterios de selección (los que importan, no la marca)

1. Lista de precios mayorista real (mínimo 25-30% bruto después de envío)
2. **Aviso de stock** (feed, hoja compartida o API — no "te enterás cuando ya vendiste")
3. Tiempo de despacho comprometido por escrito (WhatsApp sirve)
4. Quién coordina/paga envío y qué pasa si se pierde
5. Política de fallas (reposición o pérdida)
6. Packaging neutro (no que el mayorista le venda directo a tu cliente)
7. **Factura legal** — innegociable (filtro de seriedad + respaldo fiscal)

**Meta del stack:** convertir criterios 2-3 en datos — nuestro agente consulta stock/precio de los mayoristas con presencia online (Cellshop, Shopping China, Fastrax publican precios) y arma el mapa de precios semanal de CDE sin llamadas.

## B. China directa (1688/Alibaba) — para ganadores y preventa

### Couriers / agentes China → Paraguay (verificados)

| Actor | Servicio | Nota |
|---|---|---|
| **3A Courier** | Compra en Alibaba/1688 y traen a PY; contenido activo educando el canal | Candidato agente de importación |
| **Chilat** (chilat.com) | Guía completa 1688-desde-Paraguay; intermediación de compras | Agente de compra + logística |
| **Latin American Cargo** | Sea freight & air cargo China→PY | Para volumen/fase importador |
| Couriers con casilla Miami | Complemento para muestras | Suma costo/tiempo — solo muestras |

### Reglas del sourcing directo

- **Solo para SKUs validados** (los 3-5 ganadores) — nunca para catálogo largo
- Cotizar **todo el costo landed**: producto + flete aéreo/marítimo + despacho + IVA aduanero + courier interno
- Muestras SIEMPRE antes de primer pedido (el agente de compras lo orquesta)
- Preventa solo con plazo comunicado por escrito antes de cobrar
- MOQ negociado vía agente (Chilat/3A) — ellos hablan el idioma del proveedor

## C. El motor de datos que une todo

El activo diferencial del proyecto: **una tabla canónica producto (igual que el registro EAN de WiseQ)** que une:
- SKU propio + EAN/código de barra si existe
- Proveedor CDE (precio, stock, despacho) — múltiples por SKU (comparar)
- Origen 1688 (link, precio FOB, MOQ, costo landed estimado)
- Precio de venta actual + histórico + rotación

De ahí salen: decisiones de compra semanal, alertas de quiebre de margen, candidaturas a importación directa, y el feed de la tienda. Los agentes la mantienen actualizada solos.
