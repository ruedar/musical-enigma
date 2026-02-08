# SC-808 Snare

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 65 | detune | -11 | amp | 1 | pan | 0 |
| lpf | 93 | hpf | 121 | mix | 0.7 | head_hpf | 30 |
| decay | 4.2 | decay_curve | -115 | click | 0.999 |  |  |

```ruby
use_synth :sc808_snare
```

Snare drum of the SC808 drum machine based on Yoshinosuke Horiuchi's implementation of the legendary rhythm composer from the early 80s.

## Introduced in v4.5

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30`, `52`, `:C`, `:C2`, `:Eb4`, or `:Ds3`

- **Default: 65**
- Must be zero or greater
- May be changed whilst playing

### detune:

Detune multiplier of original pitch for the snare's timbre. A value of 1 indicates no deviation from the fundamental pitch

- **Default: -11**
- Can not be changed once set

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

### lpf:

Low pass filter cutoff value for the snare vibration. A MIDI note representing the highest frequencies allowed to be present in the sound. A low value like 30 makes the sound round and dull, a high value like 100 makes the sound buzzy and crispy.

- **Default: 93**
- Must be zero or greater, must be a value less than 131
- May be changed whilst playing
- Has slide options to shape changes

### hpf:

High pass filter cutoff value for the snare vibration. A MIDI note representing the lowest frequencies allowed to be present in the sound. A high value like 100 makes the sound thin and whispy, a low value like 40 removes just the lower bass components of the sound.

- **Default: 121**
- Must be zero or greater, must be a value less than 119
- May be changed whilst playing
- Has slide options to shape changes

### mix:

Ratio of amplitude between the sound of the head of the drum (the boom) and the snare of the drum (the buzz). A value of 1 is 100% snare, a value of 0 is 100% head and 0.5 is 50% of each.

- **Default: 0.7**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### head_hpf:

High pass filter cutoff value for the head of the drum. A MIDI note representing the lowest frequencies allowed to be present in the sound. Use a lower volume to make the boom part of the snare sound lower.

- **Default: 30**
- Must be zero or greater, must be a value less than 119
- Can not be changed once set

### decay:

Amount of decay for the snare. Higher numbers increase the decay duration.

- **Default: 4.2**
- Must be greater than zero
- Can not be changed once set

### decay_curve:

Curve value for the decay of the snare

- **Default: -115**
- Can not be changed once set

### click:

Amount of initial click to the drum sound. 0 is no click and 1 is a hard click.

- **Default: 0.999**
- Must be a value between 0 and 1 inclusively
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
