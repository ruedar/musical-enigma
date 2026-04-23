# POC 04: Dos frases como "inicio" y "final"
# Estrategia: bloques claros separados por sleep = dos ideas.
# Técnica: agrupar play en frases; el silencio entre ellas da estructura.

use_bpm 70
use_synth :beep

# Frase 1 (inicio)
play_pattern_timed [60, 64, 67], [0.5, 0.5, 1]
sleep 1

# Frase 2 (respuesta / cierre)
play_pattern_timed [67, 64, 60], [0.5, 0.5, 1.5]
sleep 1
