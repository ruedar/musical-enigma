# POC 15: Variar amplitud (crescendo / diminuendo) por frase
# Estrategia: subir o bajar amp en cada iteración = tensión o relajo.
# Técnica: loop con índice; amp: 0.3 + i * 0.1 (o similar).

use_bpm 80
use_synth :tri
use_synth_defaults release: 0.4

# Crescendo: 4 notas que suben de volumen
4.times do |i|
  play 60 + i * 2, amp: 0.3 + (i * 0.15)
  sleep 0.5
end
sleep 0.5

# Diminuendo: 4 notas que bajan de volumen
4.times do |i|
  play 67 - i * 2, amp: 0.9 - (i * 0.15)
  sleep 0.5
end
sleep 0.5

# Final: nota suave
play 60, amp: 0.25, release: 1.5
sleep 1.5
