# POC 21: Capas en destiempo (desfase)
# Estrategia: cada capa hace sleep distinto al inicio para que no coincidan en el pulso.
# Así suena más "vivo" y menos mecánico.

use_bpm 88
use_synth_defaults release: 0.4, amp: 0.6
use_synth :tri

# Bajo: empieza en 0
in_thread do
  4.times do
    play 43, sustain: 1.2
    sleep 1.5
    play 48, sustain: 1.2
    sleep 1.5
  end
end

# Melodía: empieza medio tiempo después (desfase)
in_thread do
  sleep 0.5
  2.times do
    play_pattern_timed [60, 64, 67, 64], [0.5, 0.5, 0.5, 0.5]
    sleep 0.5
  end
  play 60, sustain: 1
end

# Percusión: empieza un tiempo después (otro desfase)
in_thread do
  sleep 1
  6.times do
    sample :bd_haus, amp: 0.35
    sleep 1
  end
end

sleep 12
