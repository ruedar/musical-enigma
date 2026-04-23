# POC 02: Melodía lineal con duraciones
# Estrategia: varias notas en secuencia con ritmo definido.
# Técnica: play_pattern_timed [notas], [duraciones].

use_bpm 80
use_synth :beep

# Frase corta: notas y duraciones en paralelo
play_pattern_timed [60, 62, 64, 65], [0.5, 0.5, 0.5, 1]
sleep 0.5
play_pattern_timed [65, 64, 62, 60], [0.25, 0.25, 0.5, 1]

# Final: nota larga
play 60, sustain: 2
sleep 2
