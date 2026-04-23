# POC 01: La forma más simple de "pieza" con inicio y final
# Estrategia: una sola nota como evento; el silencio define el arco.
# Técnica: play + sleep para marcar duración total.

use_bpm 60

# Inicio: una nota
play 60
sleep 2

# "Desarrollo": silencio (o puedes añadir más notas después)
sleep 2

# Final: última nota más grave = sensación de cierre
play 48
sleep 2

# La pieza termina aquí; Run ejecuta de principio a fin.
