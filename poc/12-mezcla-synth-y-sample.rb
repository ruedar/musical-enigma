# POC 12: Mezclar synth y sample en una pieza finita
# Estrategia: synth para melodía; sample para golpe o ambiente en momentos clave.
# Técnica: sample con rate o amp para integrarlo.

use_bpm 88
use_synth :tri
use_synth_defaults release: 0.4, amp: 0.6

# Inicio: un golpe + melodía
sample :bd_haus, amp: 0.5
sleep 0.25
play_pattern_timed [60, 64, 67], [0.5, 0.5, 1]
sleep 0.5

# Desarrollo: ritmo suave con sample
2.times do
  sample :bd_haus, amp: 0.4
  sleep 1
  play 64, release: 0.5
  sleep 1
end

# Final: último golpe + nota larga
sample :bd_haus, amp: 0.3
play 60, release: 1.5
sleep 2
