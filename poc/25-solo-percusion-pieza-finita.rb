# POC 25: Pieza finita solo con percusión
# Estrategia: sin melodía; estructura inicio–desarrollo–final solo con samples.
# Técnica: patrones de bd, sn, hi-hat (o similar) que cambian por sección.

use_bpm 95

# Intro: solo bombo, poco a poco
2.times do
  sample :bd_haus, amp: 0.5
  sleep 1
end

# Desarrollo: bombo + caja
4.times do
  sample :bd_haus, amp: 0.45
  sleep 0.5
  sample :sn_dolf, amp: 0.3
  sleep 0.5
end

# Más densidad: bombo en 1 y 3, caja en 2 y 4
4.times do
  sample :bd_haus, amp: 0.45
  sleep 0.25
  sample :sn_dolf, amp: 0.25
  sleep 0.25
  sample :bd_haus, amp: 0.4
  sleep 0.25
  sample :sn_dolf, amp: 0.25
  sleep 0.25
end

# Final: solo bombo, más espaciado
2.times do
  sample :bd_haus, amp: 0.4
  sleep 1.5
end
sleep 1
