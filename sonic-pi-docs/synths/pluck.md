# Pluck

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 52 | amp | 1 | pan | 0 | attack | 0 |
| sustain | 0 | release | 1 | attack_level | 1 | decay | 0 |
| decay_level | sustain_level | sustain_level | 1 | noise_amp | 0.8 | max_delay_time | 0.125 |
| pluck_decay | 30 | coef | 0.3 |  |  |  |  |

```ruby
use_synth :pluck
```

A basic plucked string synthesiser that uses Karplus-Strong synthesis. Note that due to the plucked nature of this synth the envelope opts such as `attack:` , `sustain:` and `release:` do not work as expected. They can only shorten the natural length of the note, not prolong it. Also, the `note:` opt will only honour whole tones.

## Introduced in v2.10

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30` , `52` , `:C` , `:C2` , `:Eb4` , or `:Ds3` . Note that the piano synth can only play whole tones such as 60 and does not handle floats such as 60.3

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

### sustain:

Amount of time (in beats) for sound to remain at sustain level amplitude. Longer sustain values result in longer sounds. With the piano synth, this opt can only have the effect of controlling the amp within the natural duration of the note and can not prolong the sound.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### release:

Amount of time (in beats) for sound to move from sustain level amplitude to silent. A short release (i.e. 0.01) makes the final part of the sound very percussive (potentially resulting in a click). A longer release (i.e 1) fades the sound out gently. With the piano synth, this opt can only have the effect of controlling the amp within the natural duration of the note and can not prolong the sound.

- **Default: 1**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### attack_level:

Amplitude level reached after attack phase and immediately before decay phase

- **Default: 1**
- Must be zero or greater
- Can not be changed once set

### decay:

Amount of time (in beats) for the sound to move from full amplitude (attack_level) to the sustain amplitude (sustain_level). With the piano synth, this opt can only have the effect of controlling the amp within the natural duration of the note and can not prolong the sound.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

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

### noise_amp:

Amplitude of source (pink) noise.

- **Default: 0.8**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### max_delay_time:

Maximum length of the delay line buffer.

- **Default: 0.125**
- Must be a value between 0.125 and 1 inclusively
- Can not be changed once set

### pluck_decay:

How long the pluck takes to stabilise on a note. This doesn’t have a dramatic effect on the sound.

- **Default: 30**
- Must be a value between 1 and 100 inclusively
- Can not be changed once set

### coef:

Coefficient of the internal OnePole filter. Values around zero are resonant and bright, values towards 1 sound more dampened and cutoff. It’s a little bit like playing nearer the soundhole/fingerboard for values near zero and more toward the bridge for values approaching one, although this isn’t an exact comparison.

- **Default: 0.3**
- Must be a value between -1 and 1 inclusively
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
