# Composiciones

Carpeta para código de **obras con inicio, desarrollo y cierre** escritas en Sonic Pi.

- Separada de `sonic-pi-docs/examples/` para no mezclar referencias oficiales con el material del workspace.
- El código aquí debe ser ejecutable de principio a fin (duración finita) y pensado como base para exportación de audio o referencia compositiva.
- Ver las reglas del workspace (índice de documentación y composición con duración finita) y el referente `sonic-pi-docs/examples/sorcerer/bach.rb`.

## fufu (beat de referencia, 52 s)

Reconstrucción del beat de `sounds/fufu.wav` (historia de IG). Dos archivos, mismos 88 BPM:

- [`fufu-stems.pi`](fufu-stems.pi) — reproduce el **audio real** separado en stems (batería/bajo/melodía/voz). Suena idéntico al original; sirve para tenerlo, escucharlo, aislar capas y **corregir la reconstrucción de oído**.
- [`fufu-reconstruccion.pi`](fufu-reconstruccion.pi) — el beat **reconstruido como código** editable con la notación `x`/`X`/`=`/`-`: batería con acentos y 808 con notas largas sostenidas (`=`). Base para extender el fragmento más allá de los 52 s. (La línea de bajo exacta transcrita del MIDI sigue disponible vía `tools/parse_midi.py` / historial git.)
- [`fufu.pibook`](fufu.pibook) — **notebook clickeable** (extensión s00500): las tres cosas de arriba en celdas con botón ▷ (escuchar original / aislar batería / beat reconstruido).

> Nota: la extensión de VS Code corre archivos **`.pi`** y notebooks **`.pibook`**, no `.rb`. Formato `.pibook` = Markdown con bloques de código entre ` ``` ` (cada bloque es una celda ejecutable).

Análisis fuente: [`../tools/out/fufu/report.md`](../tools/out/fufu/report.md) · loop de batería: `../tools/out/fufu/drum_loop.json`. La extracción por bandas (kick/snare/hat) vive en [`../tools/analyze_beat.py`](../tools/analyze_beat.py) (`drum_band_onsets`).
