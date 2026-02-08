# Techno from IXI Lang

## Key
`:ixi_techno`

## Descripción

Moving resonant low pass filter between min and max cutoffs. Great for sweeping effects across long synths or samples.

## Introducido en
v2.0

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
- **Descripción**: The phase duration (in beats) for filter modulation cycles
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

### cutoff_min:
- **Descripción**: Minimum (MIDI) note that filter will move to whilst wobbling. Choose a lower note for a higher range of movement. Full range of movement is the distance between cutoff_max and cutoff_min
- **Default**: 60
- **Restricciones**: must be zero or greater, must be a value less than 130
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### cutoff_max:
- **Descripción**: Maximum (MIDI) note that filter will move to whilst wobbling. Choose a higher note for a higher range of movement. Full range of movement is the distance between cutoff_max and cutoff_min
- **Default**: 120
- **Restricciones**: must be zero or greater, must be a value less than 130
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### res:
- **Descripción**: Filter resonance as a value between 0 and 1. Large amounts of resonance (a res: near 1) can create a whistling sound around the cutoff frequency. Smaller values produce less resonance.
- **Default**: 0.8
- **Restricciones**: must be zero or greater, must be a value less than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
