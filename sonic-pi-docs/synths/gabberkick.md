# Gabberkick

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 34 | amp | 0.5 | pan | 0 | attack | 0.001 |
| decay | 0.01 | sustain | 0.3 | release | 0.02 | attack_level | 1 |
| decay_level | 0.7 | sustain_level | 0.7 | cutoff | 119 | res | 0.2 |
| slope_start | 84 | slope_length1 | 0.015 | slope_intermediate | 69 | slope_length2 | 0.1 |
| boost | 8 |  |  |  |  |  |  |

```ruby
use_synth :gabberkick
```

An aggressive Gabber synth sound, adapted for Sonic Pi from SuperCollider Code. Play a :g1 with default values at about 200 bpm in order to get those punchy Gabber baseline kicks. Intended for short kick sounds, the synth is quite configurable and can produce lots of other interesting sounds, also with longer :sustain values. This synth alters the frequency while it is played along an exponential curve starting at :slope_start, passing through :slope_intermediate, and finally going to :note. This is why the :note parameter as such is not slideable.

## Introduced in v4.5

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30`, `52`, `:C`, `:C2`, `:Eb4`, or `:Ds3`

- **Default: 34**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### amp:

The amplitude of the sound. Typically a value between 0 and 1. Higher amplitudes may be used, but won't make the sound louder, they will just reduce the quality of all the sounds currently being played (due to compression.)

- **Default: 0.5**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### pan:

Position of sound in stereo. With headphones on, this means how much of the sound is in the left ear, and how much is in the right ear. With a value of -1, the sound is completely in the left ear, a value of 0 puts the sound equally in both ears and a value of 1 puts the sound in the right ear. Values in between -1 and 1 move the sound accordingly.

- **Default: 0**
- Must be a value between -1 and 1 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### attack:

Amount of time (in beats) for sound to reach full amplitude (attack_level). A short attack (i.e. 0.01) makes the initial part of the sound very percussive like a sharp tap. A longer attack (i.e 1) fades the sound in gently. Full length of sound is attack + decay + sustain + release.

- **Default: 0.001**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### decay:

Amount of time (in beats) for the sound to move from full amplitude (attack_level) to the sustain amplitude (sustain_level).

- **Default: 0.01**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### sustain:

Amount of time (in beats) for sound to remain at sustain level amplitude. Longer sustain values result in longer sounds. Full length of sound is attack + decay + sustain + release.

- **Default: 0.3**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### release:

Amount of time (in beats) for sound to move from sustain level amplitude to silent. A short release (i.e. 0.01) makes the final part of the sound very percussive (potentially resulting in a click). A longer release (i.e 1) fades the sound out gently. Full length of sound is attack + decay + sustain + release.

- **Default: 0.02**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### attack_level:

Amplitude level reached after attack phase and immediately before decay phase

- **Default: 1**
- Must be zero or greater
- Can not be changed once set

### decay_level:

Amplitude level reached after decay phase and immediately before sustain phase. Defaults to sustain_level unless explicitly set

- **Default: 0.7**
- Must be zero or greater
- Can not be changed once set

### sustain_level:

Amplitude level reached after decay phase and immediately before release phase.

- **Default: 0.7**
- Must be zero or greater
- Can not be changed once set

### cutoff:

MIDI note representing the highest frequencies allowed to be present in the sound. A low value like 30 makes the sound round and dull, a high value like 100 makes the sound buzzy and crispy.

- **Default: 119**
- Must be zero or greater, must be a value less than 131
- May be changed whilst playing
- Has slide options to shape changes

### res:

Filter resonance as a value between 0 and 1. Large amounts of resonance (a res: near 1) can create a whistling sound around the cutoff frequency. Smaller values produce less resonance.

- **Default: 0.2**
- Must be zero or greater, must be a value less than 1
- May be changed whilst playing
- Has slide options to shape changes

### slope_start:

The note where the frequency slope starts, typically much higher than the final note.

- **Default: 84**
- Must be zero or greater
- Can not be changed once set

### slope_length1:

The time in seconds between :slope_start and :slope_intermediate.

- **Default: 0.015**
- Must be zero or greater
- Can not be changed once set

### slope_intermediate:

The note where the frequency passes through after :slope_length1, typically much nearer to the final note.

- **Default: 69**
- Must be zero or greater
- Can not be changed once set

### slope_length2:

The time in seconds between :slope_intermediate and the final :note.

- **Default: 0.1**
- Must be zero or greater
- Can not be changed once set

### boost:

Changes the timbre of the synth by boosting the center frequency.

- **Default: 8**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

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
