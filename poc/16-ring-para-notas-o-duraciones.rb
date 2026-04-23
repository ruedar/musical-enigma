# POC 16: Ring para elegir notas o duraciones de forma cíclica
# Estrategia: ring(...).tick da el siguiente elemento cada vez; vuelve al inicio.
# Técnica: melodía o ritmo gobernado por rings = variación controlada.

use_bpm 85
use_synth :tri
use_synth_defaults release: 0.35, amp: 0.65

notas = (ring 60, 64, 67, 72, 67, 64)
duraciones = (ring 0.5, 0.25, 0.5, 0.5, 0.25, 0.75)

# Frase de 12 eventos: recorre notas y duraciones con .tick
12.times do
  play notas.tick, release: 0.4
  sleep duraciones.tick
end
sleep 0.5

# Final: tónica
play 60, release: 1.2
sleep 1.2
