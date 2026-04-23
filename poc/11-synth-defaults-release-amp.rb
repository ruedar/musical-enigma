# POC 11: Dar carácter global con use_synth_defaults
# Estrategia: release y amp por defecto = sonido más coherente en toda la pieza.
# Técnica: use_synth_defaults al inicio; las notas heredan.

use_bpm 78
use_synth :beep
use_synth_defaults release: 0.6, amp: 0.65, cutoff: 85

# Todas las notas comparten el mismo "aire" y volumen
play_pattern_timed [60, 62, 64, 65, 67], [0.4, 0.4, 0.4, 0.4, 0.8]
sleep 0.5
play_pattern_timed [67, 65, 64, 62, 60], [0.4, 0.4, 0.5, 0.5, 1.2]
sleep 1
