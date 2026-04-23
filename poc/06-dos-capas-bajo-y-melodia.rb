# POC 06: Dos capas simultáneas (bajo + melodía)
# Estrategia: in_thread para una capa; la otra en el hilo principal.
# Técnica: bajo con notas largas; melodía con play_pattern_timed.

use_bpm 75
use_synth_defaults release: 0.4, amp: 0.7
use_synth :beep

# Bajo (en thread): notas graves, ritmo lento
in_thread do
  play 43, sustain: 2
  sleep 2
  play 45, sustain: 2
  sleep 2
  play 48, sustain: 2
  sleep 2
  play 45, sustain: 2
  sleep 2
end

# Melodía (hilo principal)
play_pattern_timed [60, 62, 64, 67], [0.5, 0.5, 0.5, 0.5]
play_pattern_timed [67, 64, 62, 60], [0.5, 0.5, 1, 0.5]
sleep 2
play_pattern_timed [60, 64, 67], [0.5, 0.5, 2]
