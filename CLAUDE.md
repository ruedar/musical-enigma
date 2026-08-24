# musical-enigma

Repo de **algocoding** con Sonic Pi. El enfoque es generar **beats y piezas finitas** — obras con inicio, desarrollo y cierre que **Run** ejecuta de principio a fin sin depender de **Stop** manual — usando agentes generativos.

Canon de referencia para pieza cerrada: [`sonic-pi-docs/examples/sorcerer/bach.rb`](sonic-pi-docs/examples/sorcerer/bach.rb).

---

## Regla 1 — Composición con duración finita

Para obras con inicio, desarrollo y cierre:

- **Preferir** secuencias finitas: bucles con número fijo de repeticiones, `play_pattern_timed` + `sleep`, etc., y **`in_thread`** para cada capa (bajo, melodía, percusión).
- **Evitar `live_loop`** salvo que se use como **bloque repetible con salida controlada** (condiciones o duración explícita). Un `live_loop` bien acotado puede servir como "sección A de 16 compases"; no descartarlo por principio.

**Objetivo:** que **Run** ejecute la pieza de principio a fin sin depender de **Stop** para el "final" musical.

Ver patrón en `bach.rb`: `use_bpm`, bloques por sección (`2.times do`), `in_thread` por parte con `play` / `play_pattern_timed` y `sleep`.

---

## Regla 2 — Índice de documentación (no cargar todo)

Los README del repo funcionan como **mapas conceptuales**. Antes de profundizar en un tema:

1. **Consultar el README correspondiente** de la lista.
2. **Identificar el archivo concreto** donde está la información.
3. Leer/grepear dirigido — **no** cargar documentos largos por defecto.

**Índices disponibles:**

| Tema | Mapa |
|------|------|
| Tutorial oficial de Sonic Pi | [`sonic-pi-docs/tutorial/README.md`](sonic-pi-docs/tutorial/README.md) |
| Sintetizadores por categoría | [`sonic-pi-docs/synths/README.md`](sonic-pi-docs/synths/README.md) |
| Samples por categoría | [`sonic-pi-docs/samples/samples.md`](sonic-pi-docs/samples/samples.md) |
| Referencia del lenguaje (`use_*`, `with_*`, `play*`, etc.) | [`sonic-pi-docs/lang/README.md`](sonic-pi-docs/lang/README.md) |
| Efectos (`with_fx :reverb`, etc.) | [`sonic-pi-docs/fx/README.md`](sonic-pi-docs/fx/README.md) |
| Ejemplos por nivel (apprentice → wizard) | [`sonic-pi-docs/examples/README.md`](sonic-pi-docs/examples/README.md) |
| Workshop Mehackit | [`recursos/mehackit/en/README.md`](recursos/mehackit/en/README.md) |
| 30 POCs progresivos de técnicas finitas | [`poc/README.md`](poc/README.md) |
| Curso para escribir beats a mano (M0→M8, sonidos/modificadores/tiempos/groove) | [`guia-beats/README.md`](guia-beats/README.md) |
| Obras finitas del workspace | [`composiciones/README.md`](composiciones/README.md) |
| Herramientas de análisis (ej: analizar beats existentes) | [`tools/README.md`](tools/README.md) |

El índice **no implica** memorizar toda la documentación. Implica **saber dónde buscar**.

---

## Regla 3 — Observación y evolución del workspace

Observar de forma **pasiva** el trabajo realizado y detectar:

- **Patrones** que se repiten en composiciones.
- **Estrategias** que parecen estabilizarse.
- **Roles conceptuales** emergentes (estructura, sonido, ritmo).
- **Fricción recurrente** o complejidad creciente.

Cuando detectes algo así, **no** crear ni modificar automáticamente reglas, skills ni agents. En su lugar:

1. **Mencionar brevemente** el patrón o rol emergente.
2. **Proponer de forma opcional** una nueva regla, skill o agent, explicando **por qué** y **qué problema resolvería**.

Mantener propuestas **pocas y claras**, **no interrumpir** tareas creativas, tratar la evolución del sistema como algo **gradual y consensuado**.

---

## Memoria y skills: cuándo usar qué

- **CLAUDE.md** (este archivo): reglas fundamentales, siempre en contexto, versionadas en git.
- **Auto-memory** (`~/.claude/.../memory/`): preferencias del usuario, observaciones entre sesiones, feedback estable. Usar para cosas que deben persistir pero no son reglas universales del repo.
- **Skills** (`.claude/skills/*`): crear **solo** cuando un flujo se haya repetido 3+ veces con pasos estables (ej: "componer pieza finita con estructura A-B-A con estas capas"). Antes de eso, CLAUDE.md + memory bastan. Cuando veas el patrón, **propón** la skill al usuario según la Regla 3 — no la crees sin consentimiento.
