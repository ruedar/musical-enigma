# POC 03: Control explícito de duración y "respiración"
# Estrategia: alternar notas y silencios para dar forma a la frase.
# Técnica: play con sustain/release; sleep como pausa.

use_bpm 72
use_synth :piano

# Inicio: nota con release largo
play 64, release: 1.5
sleep 2

# Desarrollo: notas cortas con pausas
play 67, release: 0.3
sleep 0.5
play 69, release: 0.3
sleep 0.5
play 67, release: 0.5
sleep 1

# Final: acorde suave y largo
play_chord [64, 67, 72], release: 2
sleep 2.5
