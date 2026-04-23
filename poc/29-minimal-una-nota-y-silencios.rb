# POC 29: Minimal (una nota y muchos silencios)
# Estrategia: casi todo es aire; una sola nota se repite con largas pausas.
# El "final" es que deja de sonar.

use_bpm 50
use_synth :piano
use_synth_defaults release: 1.5, amp: 0.5

play 64, release: 2
sleep 4
play 64, release: 1.5
sleep 3
play 67, release: 1
sleep 2
play 64, release: 2
sleep 5
