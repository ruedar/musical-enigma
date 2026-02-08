# Flanger

## Key
`:flanger`

## Descripción

Mix the incoming signal with a copy of itself which has a rate modulating faster and slower than the original. Creates a swirling/whooshing effect.

## Introducido en
v2.3

## Parámetros

### amp:
- **Descripción**: The amplitude of the sound. Typically a value between 0 and 1. Higher amplitudes may be used, but won't make the sound louder, they will just reduce the quality of all the sounds currently being played (due to compression.)
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
- **Descripción**: Phase duration in beats of flanger modulation.
- **Default**: 4
- **Restricciones**: must be greater than zero
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
- Escalado con el valor de BPM actual

### phase_offset:
- **Descripción**: Initial modulation phase offset (a value between 0 and 1).
- **Default**: 0
- **Restricciones**: must be a value between 0 and 1 inclusively
- No puede cambiarse una vez establecido

### wave:
- **Descripción**: Wave type - 0 saw, 1 pulse, 2 triangle, 3 sine, 4 cubic. Different waves will produce different flanging modulation effects.
- **Default**: 4
- **Restricciones**: must be one of the following values: [0, 1, 2, 3, 4]
- Puede cambiarse mientras se reproduce

### invert_wave:
- **Descripción**: Invert flanger control waveform (i.e. flip it on the y axis). 0=uninverted wave, 1=inverted wave.
- **Default**: 0
- **Restricciones**: must be one of the following values: [0, 1]
- Puede cambiarse mientras se reproduce

### stereo_invert_wave:
- **Descripción**: Make the flanger control waveform in the left ear an inversion of the control waveform in the right ear. 0=uninverted wave, 1=inverted wave. This happens after the standard wave inversion with param :invert_wave.
- **Default**: 0
- **Restricciones**: must be one of the following values: [0, 1]
- Puede cambiarse mientras se reproduce

### delay:
- **Descripción**: Amount of delay time between original and flanged version of audio.
- **Default**: 5
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### max_delay:
- **Descripción**: Max delay time. Used to set internal buffer size.
- **Default**: 20
- **Restricciones**: must be zero or greater
- No puede cambiarse una vez establecido

### depth:
- **Descripción**: Flange depth - greater depths produce a more prominent effect.
- **Default**: 5
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### decay:
- **Descripción**: Flange decay time in ms
- **Default**: 2
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### feedback:
- **Descripción**: Amount of feedback.
- **Default**: 0
- **Restricciones**: must be a value between 0 and 1 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### invert_flange:
- **Descripción**: Invert flanger signal. 0=no inversion, 1=inverted signal.
- **Default**: 0
- **Restricciones**: must be one of the following values: [0, 1]
- Puede cambiarse mientras se reproduce
