# POC 27: Capas que entran una tras otra (crescendo de entradas)
# Estrategia: primero solo bajo; luego entra melodía; luego percusión.
# Sensación de "llenado" progresivo.

use_bpm 85
use_synth :beep
use_synth_defaults release: 0.4, amp: 0.6

# Solo bajo (4 tiempos)
in_thread do
  2.times do
    play 43, sustain: 1.5
    sleep 2
    play 48, sustain: 1.5
    sleep 2
  end
end
sleep 4

# Bajo sigue; entra melodía
in_thread do
  2.times do
    play 43, sustain: 1.5
    sleep 2
    play 48, sustain: 1.5
    sleep 2
  end
end
in_thread do
  play_pattern_timed [60, 64, 67, 64], [0.5, 0.5, 0.5, 0.5]
  play_pattern_timed [62, 60], [0.5, 1]
  sleep 1
  play_pattern_timed [60, 64, 67], [0.5, 0.5, 1.5]
end
sleep 4

# Entra percusión; las otras siguen (resumen final)
in_thread do
  play 43, sustain: 2
  sleep 2
  play 48, sustain: 2
  sleep 2
end
in_thread do
  4.times do
    sample :bd_haus, amp: 0.4
    sleep 1
  end
end
play 60, sustain: 1.5
sleep 4.5
