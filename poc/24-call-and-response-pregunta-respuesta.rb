# POC 24: Call and response (pregunta – respuesta)
# Estrategia: frase corta (pregunta), silencio, otra frase (respuesta).
# Pueden ser el mismo synth o distinto para marcar roles.

use_bpm 75
use_synth :beep
use_synth_defaults release: 0.35, amp: 0.65

# Pregunta (más aguda, corta)
play_pattern_timed [67, 69, 67], [0.4, 0.4, 0.5]
sleep 1.2

# Respuesta (más grave, conclusiva)
play_pattern_timed [60, 64, 62, 60], [0.5, 0.5, 0.5, 1]
sleep 1

# Segunda ronda
play_pattern_timed [69, 71, 69, 67], [0.35, 0.35, 0.35, 0.5]
sleep 1.2
play_pattern_timed [64, 67, 64, 60], [0.5, 0.5, 0.5, 1.5]

sleep 2
