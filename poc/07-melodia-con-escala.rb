# POC 07: Melodía construida desde una escala
# Estrategia: usar scale() para quedarte en una tonalidad.
# Técnica: scale(:nombre, octava) + índices o .choose para variar.

use_bpm 85
use_synth :tri
escala = scale(:c3, :minor)

# Inicio: primeros grados de la escala
play_pattern_timed [escala[0], escala[2], escala[4], escala[3]], [0.5, 0.5, 0.5, 1]
sleep 0.5

# Desarrollo: subida por la escala
4.times do |i|
  play escala[i + 2], release: 0.4
  sleep 0.5
end
sleep 0.5

# Final: vuelta a la tónica
play escala[0], release: 1.5
sleep 1.5
