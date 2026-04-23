# POC 17: Cambiar BPM o parámetros por sección (inicio / desarrollo / final)
# Estrategia: use_bpm o use_synth_defaults distinto = cada parte con otro pulso o carácter.
# Técnica: redefinir contexto al inicio de cada bloque.

use_synth :beep

# Inicio: tempo tranquilo
use_bpm 60
use_synth_defaults release: 0.8, amp: 0.6
play_pattern_timed [60, 64, 67], [0.75, 0.75, 1]
sleep 1.5

# Desarrollo: más rápido y más corto
use_bpm 100
use_synth_defaults release: 0.3, amp: 0.7
play_pattern_timed [67, 69, 71, 67, 64], [0.35, 0.35, 0.35, 0.35, 0.5]
sleep 0.5

# Final: vuelta lenta y release largo
use_bpm 65
use_synth_defaults release: 1.2, amp: 0.5
play 60, release: 2
sleep 2.5
