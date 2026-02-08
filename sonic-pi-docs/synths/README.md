# Sonic Pi - Synths

Este directorio contiene la documentación completa de todos los sintetizadores (synths) disponibles en Sonic Pi.

## Lista de Synths

### Básicos
- [Beep](beep.md) - Sine Wave
- [Saw](saw.md) - Saw Wave
- [Square](square.md) - Square Wave
- [Tri](tri.md) - Triangle Wave
- [Pulse](pulse.md) - Pulse Wave

### Detuned
- [Dsaw](dsaw.md) - Detuned Saw Wave
- [Dpulse](dpulse.md) - Detuned Pulse Wave
- [Dtri](dtri.md) - Detuned Triangle Wave

### Modulados
- [Mod Saw](mod_saw.md) - Modulated Saw Wave
- [Mod Pulse](mod_pulse.md) - Modulated Pulse Wave
- [Mod Tri](mod_tri.md) - Modulated Triangle Wave
- [Mod Sine](mod_sine.md) - Modulated Sine Wave
- [Mod Dsaw](mod_dsaw.md) - Modulated Detuned Saw Wave
- [Mod FM](mod_fm.md) - Modulated FM Synthesis

### Chip/Retro
- [Chipbass](chipbass.md) - Chip Bass
- [Chiplead](chiplead.md) - Chip Lead
- [Chipnoise](chipnoise.md) - Chip Noise

### Ruido (Noise)
- [Noise](noise.md) - White Noise
- [Pnoise](pnoise.md) - Pink Noise
- [Bnoise](bnoise.md) - Brown Noise
- [Cnoise](cnoise.md) - Clip Noise
- [Gnoise](gnoise.md) - Grey Noise

### Campanas (Bells)
- [Pretty Bell](pretty_bell.md) - Pretty Bell
- [Dull Bell](dull_bell.md) - Dull Bell

### FM Synthesis
- [FM](fm.md) - FM Synthesis

### Bass
- [Subpulse](subpulse.md) - Sub Pulse
- [TB303](tb303.md) - TB-303 Bass

### Leads & Pads
- [Prophet](prophet.md) - Prophet Synth
- [Supersaw](supersaw.md) - Supersaw
- [Hoover](hoover.md) - Hoover Sound
- [Tech Saws](tech_saws.md) - Tech Saws
- [Zawa](zawa.md) - Zawa

### Texturas
- [Blade](blade.md) - Blade
- [Dark Ambience](dark_ambience.md) - Dark Ambience
- [Hollow](hollow.md) - Hollow

### Percusión/Pluck
- [Pluck](pluck.md) - Plucked String
- [Kalimba](kalimba.md) - Kalimba

### Clásicos
- [Piano](piano.md) - Piano

### Growl
- [Growl](growl.md) - Growl
- [Rodeo](rodeo.md) - Rodeo

### Audio Input
- [Sound In](sound_in.md) - Sound Input (Mono)
- [Sound In Stereo](sound_in_stereo.md) - Sound Input (Stereo)

## Estructura de cada archivo

Cada archivo de synth contiene:

1. **Nombre del Synth** - Título principal
2. **Parámetros por defecto** - Tabla con los valores iniciales
3. **Código de uso** - Ejemplo de cómo usar el synth
4. **Descripción** - Explicación del sonido y características
5. **Introducido en** - Versión de Sonic Pi donde se agregó
6. **Parámetros** - Lista detallada de todos los parámetros disponibles con:
   - Descripción
   - Valor por defecto
   - Restricciones
   - Si puede cambiarse mientras se reproduce
   - Si tiene opciones de slide
   - Si escala con BPM

## Uso

Para usar un synth en tu código Sonic Pi:

```ruby
use_synth :nombre_del_synth
play 60
```

O para una nota específica:

```ruby
synth :nombre_del_synth, note: :c4, amp: 0.5
```
