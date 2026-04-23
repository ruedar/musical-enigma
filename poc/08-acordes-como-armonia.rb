# POC 08: Acordes para dar cuerpo (armonía simple)
# Estrategia: play_chord en momentos clave = inicio, cambio, final.
# Técnica: chord(:nota, :calidad) o lista de notas.

use_bpm 70
use_synth :piano
use_synth_defaults release: 0.8, amp: 0.6

# Inicio: acorde de tónica
play_chord chord(:C3, :major), sustain: 1.5
sleep 2

# Desarrollo: progresión breve
play_chord chord(:C3, :major), sustain: 1
sleep 1
play_chord chord(:G3, :major), sustain: 1
sleep 1
play_chord chord(:A3, :minor), sustain: 1
sleep 1
play_chord chord(:F3, :major), sustain: 1
sleep 1.5

# Final: tónica de nuevo
play_chord chord(:C3, :major), sustain: 2
sleep 2.5
