# Autotuner

## Key
`:autotuner`

## Descripción

Autotune/phase vocoder effect. Used without any arguments, it tries to detect the pitch and shift it to the nearest exact note. This can help with out of tune singing, but it's also an interesting effect in its own right. When used with the note: arg, it tries to shift the input to match that note instead. This gives that classic "robot singing" sound that people associate with vocoders. This can then be changed using the control method to create new melodies.

## Introducido en
v3.2

## Ejemplo

```ruby
with_fx :autotuner do |c|
  sample "~/Downloads/acappella.wav" # any sample with a voice is good
  sleep 4
  # listen to standard auto-tune behaviour for 4 seconds
  64.times do
    # now start changing note: to get robot voice behaviour
    control c, note: (scale :a2, :minor_pentatonic, num_octaves: 2).choose
    sleep 0.5
  end
end
```

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

### note:
- **Descripción**: Midi note to shift pitch to. The quality of the sound depends on how stable the pitch of the input is.
- **Default**: 0
- **Restricciones**: must be a value between 0 and 127 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### formant_ratio:
- **Descripción**: This effect separates pitched content of an input from the formant sounds (percussive, non-pitched sounds like "ssss" and "ttttt"). Changing the formant ratio shifts the non-pitched sounds - lower pitched formants (0.5) sound like someone with a deep voice, higher values (e.g. 2.0 and above) sound like a high pitched voice.
- **Default**: 1.0
- **Restricciones**: must be a value between 0 and 10 inclusively
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
