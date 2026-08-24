"""
Parsea archivos MIDI (típicamente exportados de NeuralNote a partir de stems)
y genera snippets listos para pegar en una plantilla Sonic Pi.

Uso:
    python tools/parse_midi.py sounds/midi-fufu/bass_NNTranscription.mid
    python tools/parse_midi.py sounds/midi-fufu/*.mid --bpm 88

Output:
    Por cada MIDI, imprime:
      - Tempo detectado (o el que pases con --bpm)
      - Cantidad de notas, rango de pitch, duración total en beats
      - Snippet de Sonic Pi con las notas y tiempos cargados
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mido


# Mapeo MIDI pitch -> símbolo de Sonic Pi
NOTE_NAMES = ["c", "cs", "d", "ds", "e", "f", "fs", "g", "gs", "a", "as", "b"]

# Mapeo General MIDI drums -> samples de Sonic Pi (con amp sugerido)
GM_DRUM_MAP = {
    35: (":bd_haus", 1.2),         # Acoustic Bass Drum
    36: (":bd_tek", 1.3),          # Bass Drum 1 (kick principal)
    37: (":drum_cymbal_pedal", 0.6),  # Side Stick (rim)
    38: (":sn_dolf", 0.9),         # Acoustic Snare
    39: (":perc_snap", 0.8),       # Hand Clap
    40: (":sn_zome", 0.9),         # Electric Snare
    41: (":drum_tom_lo_hard", 0.8),# Low Floor Tom
    42: (":drum_cymbal_closed", 0.5),  # Closed Hi-Hat
    43: (":drum_tom_mid_hard", 0.8),   # High Floor Tom
    44: (":drum_cymbal_pedal", 0.4),   # Pedal Hi-Hat
    45: (":drum_tom_mid_hard", 0.8),   # Low Tom
    46: (":drum_cymbal_open", 0.5),    # Open Hi-Hat
    47: (":drum_tom_hi_hard", 0.8),    # Mid Tom
    48: (":drum_tom_hi_hard", 0.8),    # Hi-Mid Tom
    49: (":drum_splash_hard", 0.7),    # Crash 1
    50: (":drum_tom_hi_hard", 0.8),    # High Tom
    51: (":drum_cymbal_hard", 0.6),    # Ride 1
}


def midi_to_sonicpi(pitch: int) -> str:
    """MIDI 60 (C4) -> 'c4'. Sonic Pi usa cs/ds/fs/gs/as para sostenidos."""
    octave = (pitch // 12) - 1
    return f":{NOTE_NAMES[pitch % 12]}{octave}"


def is_drum_track(notes: list[tuple]) -> bool:
    """Heurística: si >80% de las notas están en el rango GM drum (35-51), es batería."""
    if not notes:
        return False
    drum_notes = sum(1 for n in notes if 35 <= n[1] <= 51)
    return drum_notes / len(notes) > 0.8


def parse_midi(path: Path, target_bpm: float | None = None) -> dict:
    """Extrae notas con tiempos en BEATS DEL TARGET BPM.

    Pipeline: tick → segundos absolutos (usando tempo del MIDI) → beats en target_bpm.
    Esto permite que múltiples MIDIs con tempos distintos queden alineados en
    segundos reales, y se pisen sobre la grilla de Sonic Pi al target_bpm.
    """
    mid = mido.MidiFile(str(path))
    ticks_per_beat = mid.ticks_per_beat

    # Detectar tempo (default 500000 us/beat = 120 BPM si no hay set_tempo)
    tempo_us = 500000
    for track in mid.tracks:
        for msg in track:
            if msg.type == "set_tempo":
                tempo_us = msg.tempo
                break

    bpm_detected = round(60_000_000 / tempo_us, 2)
    target = target_bpm or bpm_detected

    # tick -> segundos: tick * (tempo_us / ticks_per_beat) / 1_000_000
    sec_per_tick = (tempo_us / ticks_per_beat) / 1_000_000
    # segundos -> beats target: sec * target / 60
    sec_to_target_beat = target / 60

    notes: list[tuple[float, int, float, int]] = []
    for track in mid.tracks:
        abs_tick = 0
        active: dict[int, tuple[int, int]] = {}
        for msg in track:
            abs_tick += msg.time
            if msg.type == "note_on" and msg.velocity > 0:
                active[msg.note] = (abs_tick, msg.velocity)
            elif msg.type in ("note_off", "note_on"):
                if msg.note in active:
                    start_tick, vel = active.pop(msg.note)
                    start_sec = start_tick * sec_per_tick
                    dur_sec = (abs_tick - start_tick) * sec_per_tick
                    start_beat = start_sec * sec_to_target_beat
                    dur_beat = dur_sec * sec_to_target_beat
                    notes.append((start_beat, msg.note, dur_beat, vel))

    notes.sort()

    return {
        "path": str(path),
        "bpm_detected": bpm_detected,
        "bpm_used": target,
        "ticks_per_beat": ticks_per_beat,
        "n_notes": len(notes),
        "pitch_min": min((n[1] for n in notes), default=0),
        "pitch_max": max((n[1] for n in notes), default=0),
        "duration_beats": round(max((n[0] + n[2] for n in notes), default=0), 3),
        "duration_sec": round(max((n[0] / sec_to_target_beat + n[2] / sec_to_target_beat for n in notes), default=0), 3),
        "notes": notes,
    }


def quantize(value: float, grid: float) -> float:
    """Cuantiza a la grilla más cercana (en beats). grid=0.25 = semicorcheas."""
    return round(value / grid) * grid


def render_sonicpi_snippet(meta: dict, name: str, grid: float = 0.25) -> str:
    """Genera un snippet Sonic Pi: data array + iteración con sleep relativo.

    Soporta polifonía porque sleep es entre note_starts (no entre note_ends).
    Si detecta que es track de drums, genera con `sample` en vez de `play`.
    """
    bpm = meta["bpm_used"]
    notes = meta["notes"]

    if not notes:
        return f"# {name}: sin notas detectadas\n"

    drums_mode = is_drum_track(notes)

    # Cuantizar
    quantized = []
    for start, pitch, dur, vel in notes:
        q_start = quantize(start, grid)
        q_dur = max(quantize(dur, grid), grid)
        amp = round(vel / 127, 2)
        quantized.append((round(q_start, 3), pitch, round(q_dur, 3), amp))

    quantized.sort()

    if drums_mode:
        return _render_drums(meta, name, quantized, grid)

    lines = [
        f"# === {name} ===",
        f"# Notas: {meta['n_notes']} | Duración: {meta['duration_beats']:.2f} beats | "
        f"Rango: {midi_to_sonicpi(meta['pitch_min'])} a {midi_to_sonicpi(meta['pitch_max'])}",
        f"# Cuantizado a grilla de {grid} beats — pensado para use_bpm {bpm}",
        "",
        f"# Formato: [start_beat, nota, duración_beat, amp]",
        f"{name}_notes = [",
    ]
    for start, pitch, dur, amp in quantized:
        lines.append(f"  [{start}, {midi_to_sonicpi(pitch)}, {dur}, {amp}],")
    lines += [
        "]",
        "",
        f"in_thread do",
        f"  use_synth :fm  # CAMBIAR según el carácter deseado",
        f"  last_t = 0",
        f"  {name}_notes.each do |t, n, d, a|",
        f"    sleep [t - last_t, 0].max",
        f"    play n, release: d, amp: a",
        f"    last_t = t",
        f"  end",
        f"end",
        "",
    ]
    return "\n".join(lines)


def _render_drums(meta: dict, name: str, quantized: list, grid: float) -> str:
    """Genera snippet para track de drums: usa sample con mapeo GM."""
    bpm = meta["bpm_used"]
    pitches_used = sorted(set(p for _, p, _, _ in quantized))

    lines = [
        f"# === {name} (DRUMS) ===",
        f"# Notas: {meta['n_notes']} | Duración: {meta['duration_beats']:.2f} beats | "
        f"Cuantizado a {grid} beats — pensado para use_bpm {bpm}",
        f"# Mapeo MIDI -> sample Sonic Pi:",
    ]
    for p in pitches_used:
        sample, _ = GM_DRUM_MAP.get(p, (f"# pitch {p} sin mapeo", 0))
        lines.append(f"#   {p} -> {sample}")
    lines += [
        "",
        f"# Formato: [start_beat, sample, amp]",
        f"{name}_hits = [",
    ]
    for start, pitch, _dur, amp in quantized:
        sample, default_amp = GM_DRUM_MAP.get(pitch, (f":bd_haus  # pitch {pitch} sin mapeo", 1.0))
        final_amp = round(default_amp * amp / 0.6, 2)  # normalizar contra vel media
        lines.append(f"  [{start}, {sample}, {final_amp}],")
    lines += [
        "]",
        "",
        f"in_thread do",
        f"  last_t = 0",
        f"  {name}_hits.each do |t, s, a|",
        f"    sleep [t - last_t, 0].max",
        f"    sample s, amp: a",
        f"    last_t = t",
        f"  end",
        f"end",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("midis", nargs="+", type=Path, help="Uno o más archivos .mid")
    parser.add_argument("--bpm", type=float, default=None, help="Forzar BPM (sobreescribe el del MIDI)")
    parser.add_argument("--grid", type=float, default=0.25, help="Grilla de cuantización en beats (0.25 = 16vos)")
    parser.add_argument("--out", type=Path, default=None, help="Guardar snippets a archivo .pi (default: stdout)")
    parser.add_argument("--template", action="store_true", help="Envolver salida como plantilla Sonic Pi ejecutable (use_bpm + headers)")
    args = parser.parse_args()

    snippets = []
    for midi_path in args.midis:
        if not midi_path.exists():
            print(f"# Skip: {midi_path} no existe")
            continue
        meta = parse_midi(midi_path, target_bpm=args.bpm)
        name = midi_path.stem.replace("_NNTranscription", "")
        print(f"\n[{midi_path.name}] BPM_midi={meta['bpm_detected']} -> usando={meta['bpm_used']} | "
              f"notas={meta['n_notes']} | dur={meta['duration_sec']:.2f}s = {meta['duration_beats']:.2f} beats")
        snippet = render_sonicpi_snippet(meta, name, grid=args.grid)
        # Reemplazar el synth placeholder por la variable apropiada según el nombre
        if args.template:
            synth_var = "SYNTH_BASS" if "bass" in name.lower() else "SYNTH_OTHER"
            snippet = snippet.replace("use_synth :fm  # CAMBIAR según el carácter deseado", f"use_synth {synth_var}")
        snippets.append(snippet)

    body = "\n".join(snippets)

    if args.template:
        bpm = args.bpm or 120
        header = f"""# === Plantilla generada desde MIDI ===
# Editá los parámetros de abajo y corré con Alt+R en Sonic Pi.
# Cada track abre un in_thread; corren en paralelo desde el segundo 0.

use_bpm {bpm}

# --- Parámetros tweakeables ---
# Cambiá los synths y los amps generales según el carácter que busques.
SYNTH_BASS  = :fm        # opciones: :fm, :tb303, :prophet, :sine
SYNTH_OTHER = :hollow    # opciones: :hollow, :blade, :pretty_bell, :saw
AMP_BASS    = 1.0
AMP_OTHER   = 0.7
AMP_DRUMS   = 1.0

# --- FX globales (envolver el run_track con with_fx si querés) ---
# Ejemplo: with_fx :reverb, room: 0.6, mix: 0.3 do ... end
"""
        output = header + "\n" + body
    else:
        output = body

    if args.out:
        args.out.write_text(output, encoding="utf-8")
        print(f"\n[OK] Snippets guardados en {args.out}")
    else:
        print("\n" + "=" * 60)
        print(output)


if __name__ == "__main__":
    main()
