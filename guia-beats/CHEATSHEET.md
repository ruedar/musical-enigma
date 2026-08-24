# Cheatsheet — beats en Sonic Pi

Los parámetros y funciones que usás el 90% del tiempo. Para el resto, andá al `sonic-pi-docs/` correspondiente.

## Tiempo (M0)

| Escribís | Significa |
|----------|-----------|
| `use_bpm 140` | tempo; define cuánto dura `sleep 1` |
| `sleep 1` | 1 tiempo (negra) |
| `sleep 0.5` / `0.25` / `0.125` | corchea / semicorchea / fusa |
| `1.0/3` | tresillo (un tiempo en 3) |
| `4.times do … end` | repetir un número fijo (finito, no `live_loop`) |

## Disparar sonido (M1)

| Escribís | Qué es |
|----------|--------|
| `sample :bd_haus` | reproduce un audio pregrabado |
| `synth :sc808_bassdrum, note: 40` | genera un sonido sintético afinable |
| `use_synth :prophet` | fija el synth por defecto para los `play` siguientes |

**Roles → dónde buscar:** kick `:bd_*`, snare `:sn_*`/`:drum_snare_*`, hat `:drum_cymbal_closed/open`, 808/perc synth `:sc808_*`. Catálogos: [`samples.md`](../sonic-pi-docs/samples/samples.md), [`synths/README.md`](../sonic-pi-docs/synths/README.md).

## Modificadores universales (M2)

| Param | Rango | Efecto al subir |
|-------|-------|-----------------|
| `amp:`   | 0–2 | más fuerte |
| `pan:`   | -1…1 | hacia la derecha |
| `rate:`  | 0.5–2 (sample) | más rápido y agudo (`-1` = reverse) |
| `note:`  | MIDI o `:c3` | más agudo |
| `cutoff:`| ~50–130 | más brillante (abre el filtro) |
| `res:`   | 0–1 | más resonante/ácido |

## Envolvente ADSR (M2·02)

| Param | Efecto |
|-------|--------|
| `attack:`  | tiempo de entrada (0 = seco, alto = fade-in) |
| `decay:`   | caída al sustain (da el pluck) |
| `sustain:` | cuánto se mantiene |
| `release:` | cola final (chico = seco, grande = 808/pad largo) |

## Modificadores de sample (M2·03)

`start:`/`finish:` (0–1, recorte) · `beat_stretch: 4` (encajar al tempo) · `rpitch: 5` (afinar sin acelerar).

## Patrones (M3)

```ruby
(ring 1,0,0,1).tick          # lista circular, tick avanza
spread(3, 8)                 # 3 golpes repartidos en 8 pasos (euclídeo)
"x--x--x-"[i] == "x"         # patrón legible como string
```

### Notación de patrones en texto

Cada carácter = un paso (1/16). Dos ejes **independientes**: fuerza (mayúscula) y duración (`=`).

| Símbolo | Significa |
|---------|-----------|
| `x` | golpe normal |
| `X` | golpe fuerte (acento) |
| `=` | sostiene el golpe anterior (un paso más) |
| `-` | silencio |

Ej: `X===----x---X---` = acento sostenido 4 pasos, silencio, golpe normal, acento.
Se combinan: normal-corto `x`, normal-largo `x===`, fuerte-corto `X`, fuerte-largo `X===`.
Decoder reutilizable (sample o synth con `nota:`):

```ruby
def toca(patron, sonido, nota: nil, base: 0.8)
  patron.length.times do |i|
    c = patron[i]
    if c == "x" || c == "X"
      amp   = base * (c == "X" ? 1.6 : 1.0)      # mayuscula = acento
      largo = 1
      largo += 1 while patron[i + largo] == "="  # cada '=' alarga un paso
      if nota
        synth sonido, note: nota, sustain: largo * 0.25, release: 0.1, amp: amp
      else
        sample sonido, sustain: largo * 0.25, release: 0.1, amp: amp
      end
    end
    sleep 0.25   # avanza el paso ('=' y '-' no disparan)
  end
end
```

## Groove (M4)

Acentos: `amp: (ring 1.0,0.4,0.7,0.4).tick` · Swing: `with_swing 0.1, pulse: 4 do … end` · Humanizar: `amp: rrand(0.4,0.7)`, `sleep 0.25 + rrand(-0.01,0.01)`, `use_random_seed 42` · Roll: `3.times { sample :drum_cymbal_closed; sleep 1.0/3 }`.

## Bajo / 808 (M5)

```ruby
b = synth :sc808_bassdrum, note: :c1, sustain: 2, release: 1, note_slide: 0.2
control b, note: :g1         # glissando del 808
```

## Capas y estructura (M6)

`in_thread do … end` por capa · secciones consecutivas (intro→beat→drop→cierre) · cada hilo con `N.times` → la pieza termina sola.

## FX (M7)

```ruby
with_fx :lpf, cutoff: 80 do … end        # quita agudos (oscurece)
with_fx :hpf, cutoff: 90 do … end        # quita graves (aligera)
with_fx :reverb, room: 0.6, mix: 0.3 do … end
with_fx :bitcrusher, bits: 6 do … end    # lo-fi
with_fx :krush, krush: 12, mix: 0.6 do … end
```
El FX **más interno actúa primero**. Kick/808: sin reverb.

## Regla de oro

Los `sleep` que corren en paralelo deben **sumar lo mismo** por compás, o las capas se desfasan.
