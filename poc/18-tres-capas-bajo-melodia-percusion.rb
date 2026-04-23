# POC 18: Tres capas (bajo, melodía, percusión) con in_thread
# Estrategia: cada capa en su thread; todas con secuencias finitas = pieza que termina.
# Técnica: un in_thread para bajo, otro para percusión; melodía en el hilo principal.

use_bpm 92
use_synth_defaults release: 0.4, amp: 0.65
use_synth :tri

# Bajo: 8 tiempos
in_thread do
  4.times do
    play 43, sustain: 1
    sleep 1
    play 45, sustain: 1
    sleep 1
  end
end

# Percusión: golpes cada 2 tiempos
in_thread do
  8.times do
    sample :bd_haus, amp: 0.4
    sleep 1
  end
end

# Melodía (hilo principal)
2.times do
  play_pattern_timed [60, 62, 64, 67], [0.5, 0.5, 0.5, 0.5]
  play_pattern_timed [67, 64, 62, 60], [0.5, 0.5, 1, 0.5]
  sleep 0.5
end
play 60, sustain: 1
sleep 1
