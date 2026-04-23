# POC 10: Cambiar timbre por sección (inicio / desarrollo / final)
# Estrategia: use_synth distinto en cada parte = colores diferentes.
# Técnica: use_synth antes de cada bloque de notas.

use_bpm 72

# Inicio: sonido suave
use_synth :tri
play_pattern_timed [60, 64, 67], [0.75, 0.75, 1]
sleep 1

# Desarrollo: sonido más brillante
use_synth :beep
play_pattern_timed [67, 69, 71, 67, 64], [0.4, 0.4, 0.4, 0.4, 1]
sleep 1

# Final: sonido más redondo
use_synth :piano
play 60, release: 2
sleep 2.5
