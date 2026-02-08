# Bitcrusher

## Key
`:bitcrusher`

## Descripción

Creates lo-fi output by decimating and deconstructing the incoming audio by lowering both the sample rate and bit depth. The default sample rate for CD audio is 44100, so use values less than that for that crunchy chip-tune sound full of artefacts and bitty distortion. Similarly, the default bit depth for CD audio is 16, so use values less than that for lo-fi sound.

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

### sample_rate:
- **Descripción**: The sample rate the audio will be resampled at. This represents the number of times per second the audio is sampled. The higher the sample rate, the closer to the original the sound will be, the lower the more low-fi it will sound. The highest sample rate is 44100 (full quality) and the lowest is ~100 (extremely low quality). Try values in between such as 1000, 3000, 8000...
- **Default**: 10000
- **Restricciones**: must be greater than zero
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### bits:
- **Descripción**: The bit depth of the resampled audio. Lower bit depths make the audio sound grainy and less defined. The highest bit depth is 16 (full quality) and the lowest is 1 (lowest quality).
- **Default**: 8
- **Restricciones**: must be greater than zero
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### cutoff:
- **Descripción**: MIDI note representing the highest frequencies allowed to be present in the sound. A low value like 30 makes the sound round and dull, a high value like 100 makes the sound buzzy and crispy.
- **Default**: 0
- **Restricciones**: must be zero or greater, must be a value less than 131
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
