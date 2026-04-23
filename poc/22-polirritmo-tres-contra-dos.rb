# POC 22: Polirritmo (3 contra 2)
# Estrategia: una capa toca 3 notas en el mismo tiempo que otra toca 2.
# Sensación de cruce de ritmos sin salir de la cuadrícula.

use_bpm 72
use_synth :beep
use_synth_defaults release: 0.2, amp: 0.6

# Capa "en 3": 3 notas por ciclo
in_thread do
  6.times do
    play 72, release: 0.25
    sleep 0.333
    play 74, release: 0.25
    sleep 0.333
    play 76, release: 0.25
    sleep 0.334
  end
end

# Capa "en 2": 2 notas por ciclo (mismo ciclo de 1 tiempo)
in_thread do
  6.times do
    play 55, release: 0.4
    sleep 0.5
    play 59, release: 0.4
    sleep 0.5
  end
end

sleep 6.5
