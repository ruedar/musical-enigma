# POC 26: Pan (sonido que se mueve izquierda–derecha)
# Estrategia: pan: -1 (izq) a 1 (der) para colocar cada nota en el espacio.
# Puede ser alternado o progresivo.

use_bpm 82
use_synth :tri
use_synth_defaults release: 0.4, amp: 0.65

# Notas que van de izquierda a derecha
[60, 62, 64, 67, 64, 62, 60].each_with_index do |n, i|
  pan = -1 + (i.to_f / 6) * 2  # -1 -> 1
  play n, pan: pan, release: 0.5
  sleep 0.5
end
sleep 0.5

# Vuelta: de derecha a izquierda
[60, 64, 67].each_with_index do |n, i|
  pan = 1 - (i.to_f / 2) * 2
  play n, pan: pan, release: 0.6
  sleep 0.6
end
sleep 1
