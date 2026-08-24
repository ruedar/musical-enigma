# tools/

Scripts de apoyo para el workspace. No son parte del flujo compositivo — son utilidades que producen material que el agente puede consumir.

## `analyze_beat.py` — análisis de beats existentes

Extrae información de un track de audio para reproducirlo (estructura, no timbre) en Sonic Pi.

### Pipeline

1. **demucs** separa stems (drums, bass, other, vocals).
2. **librosa** estima BPM, tonalidad y detecta onsets por stem.
3. **basic-pitch** transcribe `bass` y `other` a MIDI.

### Instalación (una vez)

Usamos [uv](https://docs.astral.sh/uv/). Las deps viven en `pyproject.toml` en la raíz del repo.

```bash
uv sync                              # crea .venv/ y sincroniza deps core
uv pip install basic-pitch           # opcional: habilita transcripción MIDI (ver nota)
```

> Core (demucs + librosa) pesa ~200MB (PyTorch). Primera corrida descarga el modelo de demucs (~80MB).
>
> **basic-pitch es opcional** porque arrastra TensorFlow y en Windows `tensorflow-io-gcs-filesystem` no tiene wheels. El script detecta su ausencia y omite la generación de MIDI sin fallar. En Linux/macOS podés incluirlo con `uv sync --extra midi`.

### Uso

```bash
uv run python tools/analyze_beat.py ruta/al/beat.mp3
```

Opciones:
- `--out tools/out` — directorio de salida (default).
- `--skip-stems` — reutiliza stems ya generados.
- `--skip-midi` — no correr basic-pitch.

### Output

```
tools/out/<nombre_track>/
  report.md          resumen legible (BPM, key, duración, onsets, rutas MIDI)
  stems/             drums.wav, bass.wav, other.wav, vocals.wav
  midi/              bass.mid, other.mid
  onsets.json        timestamps de onsets por stem
```

El `report.md` es lo que el agente debería leer primero para derivar un esqueleto en Sonic Pi.

### Limitaciones conocidas

- **BPM y tonalidad son estimaciones** — confirmar a oído.
- **Transcripción de drums es poco fiable** con basic-pitch (por eso solo se aplica a bass/other). Para drums se usan onsets + decisión humana/agente sobre qué samples mapear.
- **Timbres no se recuperan.** Esto extrae estructura: tempo, patrón rítmico, línea melódica, progresión. El carácter sonoro lo reconstruye el agente eligiendo synths/samples/FX según la Regla 1 del repo.

### Output consumido por el agente

Cuando el usuario pida "reproducir este beat", el agente debería:
1. Leer `tools/out/<track>/report.md`.
2. Opcionalmente leer `onsets.json` si necesita patrón rítmico cuantizado.
3. Traducir a Sonic Pi respetando la Regla 1 (pieza finita, `in_thread` por capa, evitar `live_loop`).

---

## `beat-builder.html` — constructor visual de beats

Secuenciador visual (una sola página, sin dependencias) para armar beats finitos y **exportar el código Sonic Pi** listo para pegar en un `.pibook`.

- **Tracks × pasos** con la notación `x`/`X`/`=`/`-`: click = golpe, click de nuevo = acento (`X`), arrastrar a la derecha = sostener (`=`), click derecho = borrar. Rueda del mouse sobre un golpe de synth = cambiar la nota.
- **Resolución por track** (1/8, 1/16, 1/32 y tresillos 1/8T, 1/16T), catálogo completo de samples y synths, BPM/compases/repeticiones, y **preview de audio** aproximado (WebAudio) para oír el ritmo mientras construís.
- Exporta **JSON** (fuente de verdad) y **código Sonic Pi** (usa el decoder `toca` de la guía). El JSON es el formato pensado para, más adelante, un `tools/json_to_pibook.py`.

**Abrirlo:** con el preview del editor (`.claude/launch.json` trae la config `beatbuilder` que sirve la carpeta `tools/`), o simplemente abrir el `.html` en un navegador. El código generado se pega en una celda de código de un `.pibook`.
