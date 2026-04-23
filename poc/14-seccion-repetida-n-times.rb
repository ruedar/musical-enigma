# POC 14: Repetir una sección N veces (sin live_loop)
# Estrategia: N.times do ... end = sección fija que se repite; la pieza sigue y termina.
# Técnica: bloque repetido + después más código = desarrollo controlado.

use_bpm 90
use_synth :beep
use_synth_defaults release: 0.35, amp: 0.7

# Sección que se repite 2 veces
2.times do
  play_pattern_timed [60, 62, 64, 60], [0.5, 0.5, 0.5, 0.5]
  play_pattern_timed [64, 62, 60], [0.5, 0.5, 1]
  sleep 0.5
end

# Una vez terminadas las repeticiones: final
play 60, sustain: 1.5
sleep 1.5
