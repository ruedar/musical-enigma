# POC 20: Mini-pieza completa (inicio, desarrollo, final)
# Combina: estructura A-B-A, dos capas (bajo + melodía), escala, acordes, FX y cierre definido.
# Referente: estilo bach.rb (secuencias finitas, in_thread, sin live_loop).

use_bpm 72
use_synth_defaults release: 0.5, amp: 0.65, cutoff: 88
use_synth :beep
escala = scale(:c3, :minor)

# === INICIO (4 compases) ===
in_thread do
  play 43, sustain: 2
  sleep 2
  play 48, sustain: 2
  sleep 2
end
play_pattern_timed [escala[0], escala[2], escala[4], escala[3]], [0.5, 0.5, 0.5, 1]
sleep 0.5
play_pattern_timed [escala[3], escala[2], escala[0]], [0.5, 0.5, 1.5]
sleep 0.5

# === DESARROLLO (4 compases): más movimiento ===
in_thread do
  play 45, sustain: 1
  sleep 1
  play 48, sustain: 1
  sleep 1
  play 50, sustain: 1
  sleep 1
  play 48, sustain: 1
  sleep 1
end
2.times do
  play_pattern_timed [escala[2], escala[4], escala[5], escala[4]], [0.4, 0.4, 0.4, 0.4]
  sleep 0.4
end
play_chord chord(:c3, :minor), sustain: 1
sleep 1.5

# === FINAL (2 compases): vuelta a la tónica y cierre ===
with_fx :reverb, mix: 0.35, room: 0.5 do
  play escala[0], release: 1.5
  sleep 1
  play_chord chord(:c3, :minor), sustain: 1.5
  sleep 2
end
# La pieza termina aquí al acabar el hilo principal y los threads.
