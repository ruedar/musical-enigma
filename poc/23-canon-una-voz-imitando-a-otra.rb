# POC 23: Canon simple (una voz imita a la otra con retraso)
# Estrategia: misma melodía en dos capas; la segunda empieza 1 compás después.
# Efecto: eco melódico, sensación de persecución.

use_bpm 80
use_synth :tri
use_synth_defaults release: 0.5, amp: 0.55

melodia = [60, 62, 64, 67, 64, 62]
duraciones = [0.5, 0.5, 0.5, 0.5, 0.5, 1]

# Voz 1 (aguda)
in_thread do
  play_pattern_timed melodia.map { |n| n + 12 }, duraciones
  sleep 0.5
  play 72, sustain: 1
end

# Voz 2 (grave): misma melodía, empieza 2 tiempos después
in_thread do
  sleep 2
  play_pattern_timed melodia, duraciones
  sleep 0.5
  play 60, sustain: 1
end

sleep 10
