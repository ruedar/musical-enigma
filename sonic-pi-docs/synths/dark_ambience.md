# Dark Ambience

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 52 | amp | 1 | pan | 0 | attack | 0 |
| decay | 0 | sustain | 0 | release | 1 | attack_level | 1 |
| decay_level | sustain_level | sustain_level | 1 | env_curve | 2 | cutoff | 110 |
| res | 0.7 | detune1 | 12 | detune2 | 24 | noise | 0 |
| ring | 0.2 | room | 70 | reverb_time | 100 |  |  |

```ruby
use_synth :dark_ambience
```

A slow rolling bass with a sparkle of light trying to escape the darkness. Great for an ambient sound.

## Introduced in v2.4

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30` , `52` , `:C` , `:C2` , `:Eb4` , or `:Ds3`

- **Default: 52**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### amp:

The amplitude of the sound. Typically a value between 0 and 1. Higher amplitudes may be used, but won’t make the sound louder, they will just reduce the quality of all the sounds currently being played (due to compression.)

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

### attack:

Amount of time (in beats) for sound to reach full amplitude (attack_level). A short attack (i.e. 0.01) makes the initial part of the sound very percussive like a sharp tap. A longer attack (i.e 1) fades the sound in gently. Full length of sound is attack + decay + sustain + release.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### decay:

Amount of time (in beats) for the sound to move from full amplitude (attack_level) to the sustain amplitude (sustain_level).

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### sustain:

Amount of time (in beats) for sound to remain at sustain level amplitude. Longer sustain values result in longer sounds. Full length of sound is attack + decay + sustain + release.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### release:

Amount of time (in beats) for sound to move from sustain level amplitude to silent. A short release (i.e. 0.01) makes the final part of the sound very percussive (potentially resulting in a click). A longer release (i.e 1) fades the sound out gently. Full length of sound is attack + decay + sustain + release.

- **Default: 1**
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

- **Default: sustain_level**
- Must be zero or greater
- Can not be changed once set

### sustain_level:

Amplitude level reached after decay phase and immediately before release phase.

- **Default: 1**
- Must be zero or greater
- Can not be changed once set

### env_curve:

Select the shape of the curve between levels in the envelope. 1=linear, 2=exponential, 3=sine, 4=welch, 6=squared, 7=cubed

- **Default: 2**
- Must be one of the following values: [1, 2, 3, 4, 6, 7]
- Can not be changed once set

### cutoff:

MIDI note representing the highest frequencies allowed to be present in the sound. A low value like 30 makes the sound round and dull, a high value like 100 makes the sound buzzy and crispy.

- **Default: 110**
- Must be zero or greater,must be a value less than 131
- May be changed whilst playing
- Has slide options to shape changes

### res:

Filter resonance as a value between 0 and 1. Large amounts of resonance (a res: near 1) can create a whistling sound around the cutoff frequency. Smaller values produce less resonance.

- **Default: 0.7**
- Must be zero or greater,must be a value less than 1
- May be changed whilst playing
- Has slide options to shape changes

### detune1:

Distance (in MIDI notes) between the main note and the second component of sound. Affects thickness, sense of tuning and harmony.

- **Default: 12**
- Can not be changed once set
- Has slide options to shape changes

### detune2:

Distance (in MIDI notes) between the main note and the third component of sound. Affects thickness, sense of tuning and harmony. Tiny values such as 0.1 create a thick sound.

- **Default: 24**
- Can not be changed once set
- Has slide options to shape changes

### noise:

Noise source. Has a subtle effect on the timbre of the sound. 0=pink noise (the default), 1=brown noise, 2=white noise, 3=clip noise and 4=grey noise

- **Default: 0**
- Must be one of the following values: [0, 1, 2, 3, 4]
- May be changed whilst playing

### ring:

Amount of ring in the sound. Lower values create a more rough sound, higher values produce a sound with more focus.

- **Default: 0.2**
- Must be a value between 0.1 and 50 inclusively
- May be changed whilst playing

### room:

Room size in squared metres used to calculate the reverb.

- **Default: 70**
- Must be a value greater than or equal to 0.1,must be a value less than or equal to 300
- Can not be changed once set

### reverb_time:

How long in beats the reverb should go on for.

- **Default: 100**
- Must be zero or greater
- Can not be changed once set

Any parameter that is slidable has three additional options named _slide, _slide_curve, and _slide_shape.  For example, 'amp' is slidable, so you can also set amp_slide, amp_slide_curve, and amp_slide_shape with the following effects:

### _slide:

Amount of time (in beats) for the parameter value to change. A long parameter_slide value means that the parameter takes a long time to slide from the previous value to the new value. A parameter_slide of 0 means that the parameter instantly changes to the new value.

- **Default: 0**

### _slide_shape:

Shape of curve. 0: step, 1: linear, 3: sine, 4: welch, 5: custom (use *_slide_curve: opt e.g. amp_slide_curve:), 6: squared, 7: cubed.

- **Default: 5**

### _slide_curve:

Shape of the slide curve (only honoured if slide shape is 5). 0 means linear and positive and negative numbers curve the segment up and down respectively.

- **Default: 0**
