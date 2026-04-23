# POC 19: Arco formal: intro – desarrollo – climax – final
# Estrategia: cuatro bloques con carácter distinto (menos → más → menos).
# Técnica: amplitud y densidad que suben y bajan; final con reverb.

use_bpm 78
use_synth :beep
use_synth_defaults release: 0.5, amp: 0.5

# Intro: pocas notas, suave
play 60, amp: 0.35, release: 1
sleep 1.5
play 64, amp: 0.4, release: 0.8
sleep 1

# Desarrollo: más notas
play_pattern_timed [64, 67, 69], [0.5, 0.5, 0.5]
sleep 0.5
play_pattern_timed [67, 64, 60], [0.5, 0.5, 1]
sleep 0.5

# Climax: más volumen y nota aguda
play 72, amp: 0.8, release: 0.4
sleep 0.5
play 74, amp: 0.75, release: 0.5
sleep 0.5
play 72, amp: 0.7, release: 0.6
sleep 1

# Final: vuelta a la calma, con reverb
with_fx :reverb, mix: 0.5, room: 0.7 do
  play 60, amp: 0.4, release: 2
  sleep 2.5
end
