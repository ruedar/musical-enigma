# Whammy

## Key
`:whammy`

## Descripción

A cheap sounding transposition effect, with a slightly robotic edge. Good for adding alien sounds and harmonies to everything from beeps to guitar samples. It's similar to pitch shift although not as smooth sounding.

## Introducido en
v2.10

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

### transpose:
- **Descripción**: This is how much to transpose the input, expressed as a midi pitch.
- **Default**: 12
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### max_delay_time:
- **Descripción**: The max delay time to be used for the effect. This shouldn't need to be adjusted.
- **Default**: 1
- **Restricciones**: must be zero or greater
- No puede cambiarse una vez establecido

### deltime:
- **Descripción**: The delay time to be used for the effect. This shouldn't need to be adjusted.
- **Default**: 0.05
- **Restricciones**: must be zero or greater
- No puede cambiarse una vez establecido

### grainsize:
- **Descripción**: The size of the initial grain used for transposition. This shouldn't need to be adjusted.
- **Default**: 0.075
- **Restricciones**: must be zero or greater
- No puede cambiarse una vez establecido
