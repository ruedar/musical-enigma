# EQ

## Key
`:eq`

## Descripción

Basic parametric EQ

## Introducido en
v3.0

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

### low_shelf:
- **Descripción**: Gain - boost or cut the centre frequency. The low shelf defines the characteristics of the lowest part of the eq FX. A value of 0 will neither boost or cut the low_shelf frequencies. A value of 1 will boost by 15 dB and a value of -1 will cut/attenuate by -15 dB.
- **Default**: 0
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### low_shelf_note:
- **Descripción**: Centre frequency of low shelf in MIDI notes.
- **Default**: 43.349957
- **Restricciones**: must be a value greater than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### low_shelf_slope:
- **Descripción**: Low shelf boost/cut slope. When set to 1 (the default), the shelf slope is as steep as it can be and remain monotonically increasing or decreasing gain with frequency.
- **Default**: 1
- **Restricciones**: must be a value greater than or equal to 0, must be a value less than or equal to 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### low:
- **Descripción**: Gain - boost or cut the centre frequency of the bass part of the sound. The low shelf defines the characteristics of the bass of the eq FX. A value of 0 will neither boost or cut the bass frequencies. A value of 1 will boost by 15 dB and a value of -1 will cut/attenuate by -15 dB.
- **Default**: 0
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### low_note:
- **Descripción**: Centre frequency of the low eq parameter in MIDI notes.
- **Default**: 59.2130948
- **Restricciones**: must be a value greater than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### low_q:
- **Descripción**: The Q factor for the low eq parameter. The Q factor controls the width of frequencies that will be affected by the low parameter of this eq FX. A low Q factor gives a wide bandwidth affecting a larger range of frequencies. A high Q factor will give a narrow bandwidth affecting a much smaller range of frequencies.
- **Default**: 0.6
- **Restricciones**: must be a value greater than or equal to 0.001, must be a value less than or equal to 100
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### mid:
- **Descripción**: Gain - boost or cut the centre frequency of the middle part of the sound. The mid shelf defines the characteristics of the bass of the eq FX. A value of 0 will neither boost or cut the bass frequencies. A value of 1 will boost by 15 dB and a value of -1 will cut/attenuate by -15 dB.
- **Default**: 0
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### mid_note:
- **Descripción**: Centre frequency of the mid eq parameter in MIDI notes.
- **Default**: 83.2130948
- **Restricciones**: must be a value greater than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### mid_q:
- **Descripción**: The Q factor for the mid eq parameter. The Q factor controls the width of frequencies that will be affected by the mid parameter of this eq FX.
- **Default**: 0.6
- **Restricciones**: must be a value greater than or equal to 0.001, must be a value less than or equal to 100
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high:
- **Descripción**: Gain - boost or cut the centre frequency of the high part of the sound. The high shelf defines the characteristics of the treble of the eq FX. A value of 0 will neither boost or cut the treble frequencies. A value of 1 will boost by 15 dB and a value of -1 will cut/attenuate by -15 dB.
- **Default**: 0
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high_note:
- **Descripción**: Centre frequency of the high eq parameter in MIDI notes.
- **Default**: 104.9013539
- **Restricciones**: must be a value greater than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high_q:
- **Descripción**: The Q factor for the high eq parameter. The Q factor controls the width of frequencies that will be affected by the high parameter of this eq FX.
- **Default**: 0.6
- **Restricciones**: must be a value greater than or equal to 0.001, must be a value less than or equal to 100
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high_shelf:
- **Descripción**: Gain - boost or cut the centre frequency. The high shelf defines the characteristics of the highest part of the eq FX. A value of 0 will neither boost or cut the high_shelf frequencies. A value of 1 will boost by 15 dB and a value of -1 will cut/attenuate by -15 dB.
- **Default**: 0
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high_shelf_note:
- **Descripción**: Centre frequency of high shelf in MIDI notes.
- **Default**: 114.2326448
- **Restricciones**: must be a value greater than 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios

### high_shelf_slope:
- **Descripción**: High shelf boost/cut slope. When set to 1 (the default), the shelf slope is as steep as it can be and remain monotonically increasing or decreasing gain with frequency.
- **Default**: 1
- **Restricciones**: must be a value greater than or equal to 0, must be a value less than or equal to 1
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
