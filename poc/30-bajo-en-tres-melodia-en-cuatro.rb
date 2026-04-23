# POC 30: Bajo en 3, melodía en 4 (ciclos que se cruzan)
# Estrategia: bajo con ciclo de 3 tiempos; melodía con ciclo de 4.
# Cada 12 tiempos vuelven a coincidir; en medio, destiempo.

use_bpm 84
use_synth_defaults release: 0.4, amp: 0.6
use_synth :tri

# Bajo: 3 notas por ciclo (sustain ~1)
in_thread do
  8.times do
    play 43, sustain: 1
    sleep 1
    play 47, sustain: 1
    sleep 1
    play 50, sustain: 1
    sleep 1
  end
end

# Melodía: frase de 4 tiempos, repetida
in_thread do
  3.times do
    play_pattern_timed [60, 62, 64, 67], [0.5, 0.5, 0.5, 0.5]
    play_pattern_timed [67, 64, 62, 60], [0.5, 0.5, 1, 0.5]
    sleep 0.5
  end
  play 60, sustain: 1
end

sleep 26
