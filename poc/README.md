# POC: Composición con inicio, desarrollo y final

Ejemplos cortos de estrategias y técnicas en Sonic Pi para piezas **finitas** (Run ejecuta de principio a fin, sin depender de Stop).

Orden sugerido: del **01** (más básico) al **20** (mini-pieza completa).

| # | Archivo | Idea principal |
|---|---------|-----------------|
| 01 | `01-una-nota-inicio-final.rb` | Una nota + silencio = arco mínimo |
| 02 | `02-secuencia-lineal-melodia.rb` | Melodía con `play_pattern_timed` |
| 03 | `03-duraciones-y-silencios.rb` | Release, sustain y pausas |
| 04 | `04-dos-frases-separadas.rb` | Dos bloques como inicio y final |
| 05 | `05-estructura-binaria-a-b.rb` | Sección A y sección B |
| 06 | `06-dos-capas-bajo-y-melodia.rb` | `in_thread` para bajo + melodía |
| 07 | `07-melodia-con-escala.rb` | `scale()` para tonalidad |
| 08 | `08-acordes-como-armonia.rb` | `play_chord` en momentos clave |
| 09 | `09-estructura-aba.rb` | A – B – A (vuelta y cierre) |
| 10 | `10-cambio-de-synth-por-seccion.rb` | Timbre distinto por sección |
| 11 | `11-synth-defaults-release-amp.rb` | Carácter global con `use_synth_defaults` |
| 12 | `12-mezcla-synth-y-sample.rb` | Synth + sample en pieza finita |
| 13 | `13-fx-reverb-por-capa.rb` | `with_fx :reverb` en un bloque |
| 14 | `14-seccion-repetida-n-times.rb` | `N.times do` sin live_loop |
| 15 | `15-crescendo-diminuendo-amp.rb` | Variar `amp` por frase |
| 16 | `16-ring-para-notas-o-duraciones.rb` | `ring(...).tick` para melodía/ritmo |
| 17 | `17-variar-bpm-o-release-por-seccion.rb` | Cambio de tempo o release por parte |
| 18 | `18-tres-capas-bajo-melodia-percusion.rb` | Bajo, melodía y percusión con threads |
| 19 | `19-arco-intro-desarrollo-climax-final.rb` | Arco formal en 4 bloques |
| 20 | `20-mini-pieza-completa-inicio-desarrollo-final.rb` | Pieza corta con varias técnicas |
| 21 | `21-desfase-capas-que-entran-desplazadas.rb` | Capas en destiempo (desfase al entrar) |
| 22 | `22-polirritmo-tres-contra-dos.rb` | Polirritmo 3 contra 2 |
| 23 | `23-canon-una-voz-imitando-a-otra.rb` | Canon: una voz imita a la otra con retraso |
| 24 | `24-call-and-response-pregunta-respuesta.rb` | Pregunta–respuesta (frases alternadas) |
| 25 | `25-solo-percusion-pieza-finita.rb` | Pieza finita solo con percusión |
| 26 | `26-pan-izquierda-derecha.rb` | Pan: sonido que se mueve izquierda–derecha |
| 27 | `27-capas-que-entran-una-tras-otra.rb` | Capas que entran progresivamente |
| 28 | `28-mismo-ritmo-dos-timbres.rb` | Mismo ritmo en dos synths (doble voz) |
| 29 | `29-minimal-una-nota-y-silencios.rb` | Minimal: una nota y muchos silencios |
| 30 | `30-bajo-en-tres-melodia-en-cuatro.rb` | Bajo en 3 tiempos, melodía en 4 (ciclos que se cruzan) |

Referente de pieza cerrada en el repo: `sonic-pi-docs/examples/sorcerer/bach.rb`.
