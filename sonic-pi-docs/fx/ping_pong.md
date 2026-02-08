# Ping Pong Echo

## Key
`:ping_pong`

## Descripción

Echo FX with each delayed echo swapping between left and right channels. Has variable phase duration (time between echoes) and feedback (proportion of sound fed into each echo). If you wish to have a phase duration longer than 1s, you need to specify the longest phase duration you'd like with the arg max_phase. Be warned, `:ping_pong` FX with very long phases can consume a lot of memory and take longer to initialise. Also, large values for feedback will cause the echo to last for a very long time.

Note: sliding the `phase:` opt with `phase_slide:` will also cause each echo during the slide to change in pitch, in much the same way that a sample's pitch changes when altering its rate.

## Introducido en
v3.2

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
- **Descripción**: The time between echoes in beats.
- **Default**: 0.25
- **Restricciones**: must be greater than zero
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
- Escalado con el valor BPM actual

### feedback:
- **Descripción**: Proportion of sound fed into each successive echo from the previous one.
- **Default**: 0.5
- **Restricciones**: must be greater than zero, must be a value less than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### max_phase:
- **Descripción**: The maximum phase duration in beats.
- **Default**: 1
- **Restricciones**: must be greater than zero
- No puede cambiarse una vez establecido
- Escalado con el valor BPM actual

### pan_start:
- **Descripción**: Starting position of sound in the stereo field. With headphones on, this means how much of the sound starts in the left ear, and how much starts in the right ear. With a value of -1, the sound starts completely in the left ear, a value of 0 starts the sound equally in both ears, and a value of 1 starts the sound completely in the right ear. Values in between -1 and 1 move the sound accordingly. Each echo will swap between left and right at the same distance away from 0 (the centre) that this `pan_start:` opt is set to.
- **Default**: 1
- **Restricciones**: must be a value between -1 and 1 inclusively
- No puede cambiarse una vez establecido
