# POC 28: Mismo ritmo, dos timbres
# Estrategia: la misma secuencia de notas/duraciones en dos synths.
# Suenan a la vez o alternados; sensación de "doble voz".

use_bpm 90
ritmo = [0.5, 0.25, 0.25, 0.5, 0.5, 1]
notas = [60, 62, 64, 62, 60, 60]

# Las dos voces juntas, mismo ritmo
in_thread do
  use_synth :tri
  use_synth_defaults release: 0.3, amp: 0.45
  notas.each_with_index do |n, i|
    play n, release: 0.35
    sleep ritmo[i]
  end
  play 60, sustain: 1
end

in_thread do
  use_synth :beep
  use_synth_defaults release: 0.25, amp: 0.4
  notas.each_with_index do |n, i|
    play n + 12, release: 0.3  # una octava arriba
    sleep ritmo[i]
  end
  play 72, sustain: 1
end

sleep 5
