# Guía para escribir tus propios beats en Sonic Pi

Curso progresivo, **beat-céntrico**, para escribir beats a mano: de la rejilla vacía a una pieza de trap finita, entendiendo cada **sonido**, cada **modificador** y cada **tiempo**.

No reemplaza la referencia oficial (`sonic-pi-docs/`): la **usa**. Aquí aprendés; allí profundizás. Cada lección enlaza a los docs concretos.

## Cómo usar esta guía

Cada lección es un notebook **`.pibook`** (extensión Sonic Pi de VS Code): celdas de texto con la explicación + una celda de código con el botón ▷.

1. Abrí el `.pibook` de la lección. Si se abre como texto plano: click derecho → *Open With…* → **Sonic Pi**.
2. Leé las celdas de texto: explican *qué* vas a oír y *por qué*.
3. Dale **▷** a la celda de código (o `Alt+R` con la celda enfocada). Para parar: `Alt+S` con esa celda enfocada.
4. Editá el código y volvé a correr. **Aprender = modificar y escuchar.**
5. Todo es finito (Regla 1): la pieza termina sola, no dependés de **Stop** para el "final" musical.

## Ruta (M0 → M8)

**M0 — El grid y el tiempo**
- [M0·01 — El grid y el `sleep`](M0-grid/01-el-grid-y-el-sleep.pibook)
- [M0·02 — Fracciones de tiempo y el primer compás](M0-grid/02-fracciones-y-el-compas.pibook)

**M1 — Los sonidos de la batería**
- [M1·01 — Samples de percusión](M1-sonidos/01-samples-de-percusion.pibook)
- [M1·02 — Percusión sintética (synths)](M1-sonidos/02-synths-de-percusion.pibook)

**M2 — Modificadores por sonido**
- [M2·01 — `amp`, `pan`, `rate`](M2-modificadores/01-amp-pan-rate.pibook)
- [M2·02 — La envolvente ADSR](M2-modificadores/02-envolvente-adsr.pibook)
- [M2·03 — Modificadores propios del sample](M2-modificadores/03-modificadores-de-sample.pibook)
- [M2·04 — Tono y filtro: `note`, `cutoff`, `res`](M2-modificadores/04-tono-y-filtro-en-synths.pibook)

**M3 — Construir el beat capa por capa**
- [M3·01 — Patrones con `ring` y `tick`](M3-construir/01-ring-y-tick.pibook)
- [M3·02 — Ritmos euclídeos con `spread`](M3-construir/02-spread-euclideo.pibook)
- [M3·03 — Patrones legibles y primer beat completo](M3-construir/03-patrones-string-y-beat-completo.pibook)

**M4 — Groove**
- [M4·01 — Acentos con `amp`](M4-groove/01-acentos-con-amp.pibook)
- [M4·02 — Swing](M4-groove/02-swing.pibook)
- [M4·03 — Ghost notes y humanizar](M4-groove/03-ghost-notes-y-humanizar.pibook)
- [M4·04 — Rolls de hi-hat (trap)](M4-groove/04-rolls-de-hihat.pibook)

**M5 — Bajo / 808**
- [M5·01 — El sub-bajo](M5-bajo/01-sub-bajo.pibook)
- [M5·02 — El 808 con glissando (`slide`)](M5-bajo/02-808-con-slide.pibook)

**M6 — Capas y estructura finita**
- [M6·01 — Capas en paralelo con `in_thread`](M6-estructura/01-in-thread-por-capa.pibook)
- [M6·02 — El arco finito: intro → beat → drop → cierre](M6-estructura/02-arco-finito.pibook)

**M7 — FX y mezcla**
- [M7·01 — Filtros `lpf` / `hpf`](M7-fx/01-filtros-lpf-hpf.pibook)
- [M7·02 — Reverb y espacio](M7-fx/02-reverb-y-espacio.pibook)
- [M7·03 — Saturación y textura lo-fi](M7-fx/03-saturacion-lofi.pibook)
- [M7·04 — Pseudo-sidechain y orden de cadena](M7-fx/04-sidechain-y-cadena.pibook)

**M8 — Receta: trap / 808**
- [M8·01 — Una pieza de trap completa](M8-trap/01-pieza-de-trap-completa.pibook)

## Referencia rápida

- [CHEATSHEET.md](CHEATSHEET.md) — los parámetros que usás el 90% del tiempo, con rango y efecto audible.
- [PLANTILLA.pi](PLANTILLA.pi) — esqueleto en blanco comentado para arrancar un beat desde cero.

## Estado

Curso completo (M0–M8) + cheatsheet + plantilla. Ancla de género: **trap / 808**.
Se puede extender con recetas de otros géneros (boom-bap, house, techno) como M9+.
