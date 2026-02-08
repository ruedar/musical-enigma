# Slicer

## Key
`:slicer`

## Descripción

Modulates the amplitude of the input signal with a specific control wave and phase duration. With the default pulse wave, slices the signal in and out, with the triangle wave, fades the signal in and out and with the saw wave, phases the signal in and then dramatically out. Control wave may be inverted with the arg invert_wave for more variety.

## Introducido en
v2.0

## Parámetros

### amp:
- **Descripción**: The amplitude of the resulting effect.
- **Default**: 1
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### mix:
- **Descripción**: The amount (percentage) of FX present in the resulting sound represented as a value between 0 and 1. For example, a mix of 0 means that only the original sound is heard, a mix of 1 means that only the FX is heard (typically the default) and a mix of 0.5 means that half the original and half of the FX is heard.
- **Default**: 1
- **Restricciones**: must be a value between 0 and 1 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### pre_mix:
- **Descripción**: The amount (percentage) of the original signal that is fed into the internal FX system as a value between 0 and 1. With a pre_mix: of 0 the FX is completely bypassed unlike a mix: of 0 where the internal FX is still being fed the original signal but the output of the FX is ignored. The difference between the two is subtle but important and is evident when the FX has a residual component such as echo or reverb. When switching mix: from 0 to 1, the residual component of the FX's output from previous audio is present in the output signal. With pre_mix: there is no residual component of the previous audio in the output signal.
- **Default**: 1
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### pre_amp:
- **Descripción**: Amplification applied to the input signal immediately before it is passed to the FX.
- **Default**: 1
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### phase:
- **Descripción**: The phase duration (in beats) of the slices
- **Default**: 0.25
- **Restricciones**: must be greater than zero
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
- Escalado con el valor BPM actual

### amp_min:
- **Descripción**: Minimum amplitude of the slicer
- **Default**: 0
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### amp_max:
- **Descripción**: Maximum amplitude of the slicer
- **Default**: 1
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### pulse_width:
- **Descripción**: The width of the pulse wave as a value between 0 and 1. A width of 0.5 will produce a square wave. Different values will change the timbre of the sound. Only valid if wave is type pulse.
- **Default**: 0.5
- **Restricciones**: must be a value between 0 and 1 exclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### phase_offset:
- **Descripción**: Initial phase offset.
- **Default**: 0
- **Restricciones**: must be a value between 0 and 1 inclusively
- No puede cambiarse una vez establecido

### wave:
- **Descripción**: Control waveform used to modulate the amplitude. 0=saw, 1=pulse, 2=tri, 3=sine
- **Default**: 1
- **Restricciones**: must be one of the following values: [0, 1, 2, 3]
- Puede cambiarse mientras se reproduce

### invert_wave:
- **Descripción**: Invert control waveform (i.e. flip it on the y axis). 0=uninverted wave, 1=inverted wave.
- **Default**: 0
- **Restricciones**: must be one of the following values: [0, 1]
- Puede cambiarse mientras se reproduce

### probability:
- **Descripción**: Probability (as a value between 0 and 1) that a given slice will be replaced by the value of the prob_pos opt (which defaults to 0, i.e. silence)
- **Default**: 0
- **Restricciones**: must be a value between 0 and 1 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### prob_pos:
- **Descripción**: Position of the slicer that will be jumped to when the probability test passes as a value between 0 and 1
- **Default**: 0
- **Restricciones**: must be a value between 0 and 1 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### seed:
- **Descripción**: Seed value for rand num generator used for probability test
- **Default**: 0
- No puede cambiarse una vez establecido

### smooth:
- **Descripción**: Amount of time in seconds to transition from the current value to the next. Allows you to round off harsh edges in the slicer wave which may cause clicks.
- **Default**: 0
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### smooth_up:
- **Descripción**: Amount of time in seconds to transition from the current value to the next only when the value is going up. This smoothing happens before the main smooth mechanism.
- **Default**: 0
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### smooth_down:
- **Descripción**: Amount of time in seconds to transition from the current value to the next only when the value is going down. This smoothing happens before the main smooth mechanism.
- **Default**: 0
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
