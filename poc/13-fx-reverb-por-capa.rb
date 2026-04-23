# POC 13: FX (reverb) en una capa para dar espacio
# Estrategia: with_fx envuelve un bloque; solo esa parte tiene efecto.
# Técnica: with_fx :reverb, mix: 0.3 do ... end

use_bpm 75
use_synth :piano

# Sin FX: frase seca
play_pattern_timed [60, 62, 64], [0.5, 0.5, 1]
sleep 1

# Con reverb: misma frase con "espacio"
with_fx :reverb, mix: 0.4, room: 0.6 do
  play_pattern_timed [64, 67, 69], [0.5, 0.5, 1]
  sleep 1
end

# Final: reverb más largo = sensación de cierre
with_fx :reverb, mix: 0.5, room: 0.8 do
  play 60, release: 2
  sleep 2.5
end
