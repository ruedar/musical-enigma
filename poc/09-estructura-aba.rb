# POC 09: Estructura A – B – A (arco con vuelta)
# Estrategia: sección A, luego B (contraste), luego A otra vez = cierre.
# Técnica: definir patrones y repetir A con un bloque.

use_bpm 80
use_synth :beep

def seccion_a
  play_pattern_timed [60, 62, 64, 60], [0.5, 0.5, 0.5, 0.5]
  sleep 0.5
end

def seccion_b
  play_pattern_timed [67, 69, 67, 64], [0.5, 0.5, 0.5, 1]
  sleep 0.5
end

# A
seccion_a
# B (contraste)
seccion_b
# A (vuelta = final)
seccion_a
play 60, sustain: 1
sleep 1
