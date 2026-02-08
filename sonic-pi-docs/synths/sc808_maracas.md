# SC-808 Maracas

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| amp | 1 | pan | 0 | hpf | 113 | click | 1 |
| decay | 0.1 | decay_curve | -20 |  |  |  |  |

```ruby
use_synth :sc808_maracas
```

Maracas of the SC808 drum machine based on Yoshinosuke Horiuchi's implementation of the legendary rhythm composer from the early 80s. This is a percussive synth, so it does not use the standard envelope parameters, neither does it feature slideable parameters.

## Introduced in v4.5

## Parámetros

### amp:

The amplitude of the sound. Typically a value between 0 and 1. Higher amplitudes may be used, but won't make the sound louder, they will just reduce the quality of all the sounds currently being played (due to compression.)

- **Default: 1**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### pan:

Position of sound in stereo. With headphones on, this means how much of the sound is in the left ear, and how much is in the right ear. With a value of -1, the sound is completely in the left ear, a value of 0 puts the sound equally in both ears and a value of 1 puts the sound in the right ear. Values in between -1 and 1 move the sound accordingly.

- **Default: 0**
- Must be a value between -1 and 1 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### hpf:

High pass filter cutoff value for the maracas. A MIDI note representing the lowest frequencies allowed to be present in the sound. A high value like 100 makes the sound thin and whispy, a low value like 40 removes just the lower bass components of the sound.

- **Default: 113**
- Must be zero or greater, must be a value less than 119
- May be changed whilst playing
- Has slide options to shape changes

### click:

Amount of initial click to the maraca sound. 0 is no click and 1 is a hard click.

- **Default: 1**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### decay:

Amount of decay for the maracas. Higher numbers increase the decay duration.

- **Default: 0.1**
- Must be greater than zero
- Can not be changed once set

### decay_curve:

Curve value for the decay of the maracas

- **Default: -20**
- Can not be changed once set

Any parameter that is slidable has three additional options named _slide, _slide_curve, and _slide_shape. For example, 'amp' is slidable, so you can also set amp_slide, amp_slide_curve, and amp_slide_shape with the following effects:

### _slide:

Amount of time (in beats) for the parameter value to change. A long parameter_slide value means that the parameter takes a long time to slide from the previous value to the new value. A parameter_slide of 0 means that the parameter instantly changes to the new value.

- **Default: 0**

### _slide_shape:

Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed.

- **Default: 5**

### _slide_curve:

Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively.

- **Default: 0**
