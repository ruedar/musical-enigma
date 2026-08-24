"""
Analiza un beat/track de audio y extrae información útil para reproducirlo en Sonic Pi.

Pipeline:
  1. demucs       -> separa stems (drums, bass, other, vocals)
  2. librosa      -> BPM, tonalidad estimada, duración, onsets por stem
  3. basic-pitch  -> transcribe bass/other a MIDI (notas con pitch/start/duration)

Output: tools/out/<nombre_track>/
  - report.md          resumen legible (BPM, key, duración, rutas, onsets resumidos)
  - stems/*.wav        stems separados
  - midi/*.mid         transcripciones MIDI de bass y other
  - onsets.json        timestamps de onsets por stem

Uso:
    python tools/analyze_beat.py path/al/track.mp3
    python tools/analyze_beat.py path/al/track.mp3 --out tools/out --skip-midi
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def separate_stems(audio_path: Path, out_dir: Path) -> dict[str, Path]:
    """Separa stems con demucs. Devuelve dict {nombre_stem: path_wav}.

    Nombres largos + rutas anidadas pueden superar MAX_PATH en Windows (260 chars).
    Por eso copiamos el audio a un nombre corto fijo ("input.wav") dentro de out_dir.
    """
    demucs_out = out_dir / "_demucs"
    demucs_out.mkdir(parents=True, exist_ok=True)

    short_input = demucs_out / "input.wav"
    shutil.copy2(str(audio_path), str(short_input))

    cmd = [
        sys.executable, "-m", "demucs.separate",
        "-n", "htdemucs",
        "-o", str(demucs_out),
        str(short_input),
    ]
    print(f"[demucs] separando stems -> {demucs_out}")
    subprocess.run(cmd, check=True)

    model_dir = demucs_out / "htdemucs" / short_input.stem
    stems_dir = out_dir / "stems"
    stems_dir.mkdir(exist_ok=True)

    stems: dict[str, Path] = {}
    for wav in model_dir.glob("*.wav"):
        target = stems_dir / wav.name
        shutil.move(str(wav), target)
        stems[wav.stem] = target

    shutil.rmtree(demucs_out, ignore_errors=True)
    return stems


def analyze_global(audio_path: Path) -> dict:
    """BPM, tonalidad estimada y duración con librosa."""
    import librosa
    import numpy as np

    y, sr = librosa.load(str(audio_path), sr=None, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(np.atleast_1d(tempo)[0])

    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_mean = chroma.mean(axis=1)
    pitches = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    key_idx = int(chroma_mean.argmax())
    key = pitches[key_idx]

    return {
        "bpm": round(bpm, 2),
        "key_estimate": key,
        "duration_sec": round(duration, 2),
        "sample_rate": sr,
    }


def onsets_for_stem(stem_path: Path) -> list[float]:
    """Timestamps de onsets (en segundos) para un stem."""
    import librosa

    y, sr = librosa.load(str(stem_path), sr=None, mono=True)
    onset_times = librosa.onset.onset_detect(y=y, sr=sr, units="time")
    return [round(float(t), 4) for t in onset_times]


def drum_band_onsets(stem_path: Path) -> dict[str, list[float]]:
    """Onsets separados por banda de frecuencia para el stem de batería.

    El onset_detect genérico es ciego al timbre: no distingue kick de snare de
    hat. Filtrando en 3 bandas antes de detectar, se aproxima cada rol:
      - kick : graves  (< 120 Hz)
      - snare: el "crack" agudo de la caja (2.5–6 kHz), evita el cuerpo del kick
      - hat  : brillo   (> 9 kHz)

    Devuelve {"kick": [...], "snare": [...], "hat": [...]} en segundos.
    Nota: aproximación — un stem lossy (demucs) deja sangrado entre bandas;
    confirmar/corregir de oído.
    """
    import librosa
    import numpy as np
    from scipy.signal import butter, sosfilt

    y, sr = librosa.load(str(stem_path), sr=None, mono=True)

    def _band(low, high, kind):
        if kind == "low":
            sos = butter(4, low, btype="low", fs=sr, output="sos")
        elif kind == "high":
            sos = butter(4, low, btype="high", fs=sr, output="sos")
        else:
            sos = butter(4, [low, high], btype="band", fs=sr, output="sos")
        return sosfilt(sos, y)

    def _onsets(yb, delta, wait):
        env = librosa.onset.onset_strength(y=yb, sr=sr)
        t = librosa.onset.onset_detect(onset_envelope=env, sr=sr, units="time",
                                       delta=delta, wait=wait)
        return [round(float(x), 4) for x in t]

    return {
        "kick":  _onsets(_band(120, None, "low"), 0.25, 4),
        "snare": _onsets(_band(2500, 6000, "band"), 0.30, 6),
        "hat":   _onsets(_band(9000, None, "high"), 0.20, 2),
    }


def transcribe_midi(stem_path: Path, out_midi: Path) -> bool:
    """Convierte un stem a MIDI con basic-pitch. Devuelve True si tuvo éxito."""
    try:
        from basic_pitch.inference import predict_and_save
        from basic_pitch import ICASSP_2022_MODEL_PATH
    except Exception as e:
        print(f"[basic-pitch] no disponible: {e}")
        return False

    out_midi.parent.mkdir(parents=True, exist_ok=True)
    predict_and_save(
        audio_path_list=[str(stem_path)],
        output_directory=str(out_midi.parent),
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
        model_or_model_path=ICASSP_2022_MODEL_PATH,
    )
    # basic-pitch nombra <stem>_basic_pitch.mid
    generated = out_midi.parent / f"{stem_path.stem}_basic_pitch.mid"
    if generated.exists():
        generated.rename(out_midi)
        return True
    return False


def essentia_features(audio_path: Path) -> dict | None:
    """Extracción enriquecida con Essentia: key+modo, BPM, danceability, downbeats.

    Solo Linux/macOS. Devuelve None si essentia no está disponible.
    """
    try:
        import essentia.standard as es
    except Exception as e:
        print(f"[essentia] no disponible: {e}")
        return None

    print("[essentia] extrayendo features (key, BPM, danceability, downbeats)")
    audio = es.MonoLoader(filename=str(audio_path), sampleRate=44100)()

    key, scale, key_strength = es.KeyExtractor()(audio)

    # method="degara" es ~10x más rápido que "multifeature" con precisión similar.
    rhythm = es.RhythmExtractor2013(method="degara")
    bpm, beats, beats_confidence, _, beats_intervals = rhythm(audio)

    danceability, _ = es.Danceability()(audio)

    # Downbeats: primer beat de cada compás
    try:
        beats_loudness = es.BeatsLoudness(beats=beats.tolist())(audio)
        downbeats_idx = []  # placeholder; BeatsLoudness no marca downbeats
    except Exception:
        downbeats_idx = []

    return {
        "key": key,
        "scale": scale,
        "key_strength": round(float(key_strength), 3),
        "bpm": round(float(bpm), 2),
        "bpm_confidence": round(float(beats_confidence), 3),
        "danceability": round(float(danceability), 3),
        "n_beats": int(len(beats)),
        "first_beats_sec": [round(float(b), 3) for b in beats[:8].tolist()],
    }


def write_report(out_dir: Path, meta: dict):
    """Escribe report.md legible por humanos y por el agente."""
    lines = [
        f"# Análisis: {meta['source']}",
        "",
        "## Global",
        f"- **BPM estimado:** {meta['global']['bpm']}",
        f"- **Tonalidad estimada (cromagrama):** {meta['global']['key_estimate']}",
        f"- **Duración:** {meta['global']['duration_sec']} s",
        f"- **Sample rate:** {meta['global']['sample_rate']} Hz",
        "",
    ]

    if meta.get("essentia"):
        e = meta["essentia"]
        lines += [
            "",
            "## Essentia (análisis enriquecido)",
            f"- **Key + modo:** `{e['key']} {e['scale']}` (fuerza {e['key_strength']})",
            f"- **BPM (Essentia):** {e['bpm']} (confianza {e['bpm_confidence']})",
            f"- **Danceability:** {e['danceability']} (0=no bailable, ~3=muy bailable)",
            f"- **Beats detectados:** {e['n_beats']}",
            f"- **Primeros beats (s):** {', '.join(str(b) for b in e['first_beats_sec'])}",
            "",
            "_Comparar BPM Essentia vs librosa: si difieren ~2x, hay ambigüedad half-time/full-time._",
        ]

    lines += [
        "",
        "## Stems",
    ]
    for name, info in meta["stems"].items():
        lines.append(f"### {name}")
        lines.append(f"- Audio: `{info['path']}`")
        lines.append(f"- Onsets detectados: {len(info['onsets'])}")
        if info["onsets"]:
            head = ", ".join(f"{t:.2f}" for t in info["onsets"][:12])
            lines.append(f"- Primeros onsets (s): {head}{' ...' if len(info['onsets']) > 12 else ''}")
        if info.get("midi"):
            lines.append(f"- MIDI: `{info['midi']}`")
        if info.get("bands"):
            lines.append("- Onsets por banda (aproximación kick/snare/hat):")
            for role, times in info["bands"].items():
                head = ", ".join(f"{t:.2f}" for t in times[:8])
                lines.append(f"    - **{role}**: {len(times)} golpes — {head}{' ...' if len(times) > 8 else ''}")
        lines.append("")

    lines += [
        "## Notas para reproducir en Sonic Pi",
        "",
        f"- Empezar con `use_bpm {int(round(meta['global']['bpm']))}`.",
        f"- Tonalidad base sugerida: `{meta['global']['key_estimate']}` (estimación por cromagrama — confirmar a oído).",
        "- Los onsets de `drums` sirven como plantilla rítmica; cuantizar a la grilla del BPM para derivar el patrón.",
        "- Los MIDI de `bass` y `other` se pueden importar visualmente o convertir a listas de `play` con duraciones.",
        "- Recordar: esto es estructura, no timbre. El carácter sonoro se reconstruye eligiendo synths/samples/FX según la Regla 1 del repo.",
    ]
    (out_dir / "report.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("audio", type=Path, help="Archivo de audio (.mp3, .wav, .flac, etc.)")
    parser.add_argument("--out", type=Path, default=Path("tools/out"), help="Directorio de salida")
    parser.add_argument("--skip-stems", action="store_true", help="No correr demucs (usar si ya se hizo)")
    parser.add_argument("--skip-midi", action="store_true", help="No correr basic-pitch")
    parser.add_argument("--features", action="store_true", help="Análisis enriquecido con Essentia (Linux/macOS)")
    args = parser.parse_args()

    if not args.audio.exists():
        sys.exit(f"No existe: {args.audio}")

    track_out = args.out / args.audio.stem
    track_out.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] análisis global: {args.audio.name}")
    global_meta = analyze_global(args.audio)

    stems: dict[str, Path] = {}
    stems_dir = track_out / "stems"
    if args.skip_stems and stems_dir.exists():
        stems = {p.stem: p for p in stems_dir.glob("*.wav")}
        print(f"[2/3] stems existentes: {list(stems)}")
    else:
        print("[2/3] separando stems (puede tardar unos minutos)")
        stems = separate_stems(args.audio, track_out)

    print("[3/3] onsets + MIDI por stem")
    stems_meta: dict[str, dict] = {}
    onsets_raw: dict[str, list[float]] = {}
    for name, path in stems.items():
        info: dict = {
            "path": str(path.relative_to(track_out)),
            "onsets": onsets_for_stem(path),
        }
        onsets_raw[name] = info["onsets"]

        if not args.skip_midi and name in {"bass", "other"}:
            midi_path = track_out / "midi" / f"{name}.mid"
            if transcribe_midi(path, midi_path):
                info["midi"] = str(midi_path.relative_to(track_out))

        # Para batería: onsets por banda (kick/snare/hat), más útil que el genérico.
        if name == "drums":
            try:
                info["bands"] = drum_band_onsets(path)
                onsets_raw["drums_bands"] = info["bands"]
            except Exception as e:
                print(f"[bandas] no se pudo separar batería por banda: {e}")

        stems_meta[name] = info

    meta = {
        "source": str(args.audio),
        "global": global_meta,
        "stems": stems_meta,
    }

    if args.features:
        ess = essentia_features(args.audio)
        if ess:
            meta["essentia"] = ess

    (track_out / "onsets.json").write_text(json.dumps(onsets_raw, indent=2), encoding="utf-8")
    write_report(track_out, meta)

    print(f"\n[OK] Listo. Reporte: {track_out / 'report.md'}")


if __name__ == "__main__":
    main()
