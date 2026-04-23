# POC 05: Estructura binaria: sección A y sección B
# Estrategia: dos bloques distintos (A y B) = inicio + desarrollo/cambio.
# Técnica: repetición con 2.times o bloques separados; pieza finita.

use_bpm 90
use_synth :tri

# === Sección A (8 tiempos) ===
play_pattern_timed [60, 62, 64, 60], [0.5, 0.5, 0.5, 0.5]
play_pattern_timed [64, 62, 60, 60], [0.5, 0.5, 1, 0.5]
sleep 0.5

# === Sección B (contraste: notas más agudas) ===
play_pattern_timed [67, 69, 71, 67], [0.5, 0.5, 0.5, 0.5]
play_pattern_timed [64, 62, 60], [0.5, 0.5, 2]

# Final: una nota de cierre
play 60, sustain: 1
sleep 1
