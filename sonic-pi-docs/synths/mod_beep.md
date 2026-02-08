# Modulated Sine Wave

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 52 | amp | 1 | pan | 0 | attack | 0 |
| decay | 0 | sustain | 0 | release | 1 | attack_level | 1 |
| decay_level | sustain_level | sustain_level | 1 | env_curve | 2 | cutoff | 100 |
| mod_phase | 0.25 | mod_range | 5 | mod_pulse_width | 0.5 | mod_phase_offset | 0 |
| mod_invert_wave | 0 | mod_wave | 1 |  |  |  |  |

```ruby
use_synth :mod_beep
```

A sine wave passed through a low pass filter which modulates between two separate notes via a variety of control waves.

## Introduced in v2.0

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30`, `52`, `:C`, `:C2`, `:Eb4`, or `:Ds3`

- **Default: 52**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

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

- **Default: 100**
- Must be zero or greater, must be a value less than 131
- May be changed whilst playing
- Has slide options to shape changes

### mod_phase:

Phase duration in beats of oscillations between the two notes. Time it takes to switch between the notes.

- **Default: 0.25**
- Must be greater than zero
- May be changed whilst playing
- Has slide options to shape changes
- Scaled with current BPM value

### mod_range:

The size of gap between modulation notes. A gap of 12 is one octave.

- **Default: 5**
- May be changed whilst playing
- Has slide options to shape changes

### mod_pulse_width:

The width of the modulated pulse wave as a value between 0 and 1. A width of 0.5 will produce a square wave. Only valid if mod wave is type pulse.

- **Default: 0.5**
- Must be a value between 0 and 1 exclusively
- May be changed whilst playing
- Has slide options to shape changes

### mod_phase_offset:

Initial modulation phase offset (a value between 0 and 1).

- **Default: 0**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### mod_invert_wave:

Invert mod waveform (i.e. flip it on the y axis). 0=normal wave, 1=inverted wave.

- **Default: 0**
- Must be one of the following values: [0, 1]
- May be changed whilst playing

### mod_wave:

Wave shape of mod wave. 0=saw wave, 1=pulse, 2=triangle wave and 3=sine wave.

- **Default: 1**
- Must be one of the following values: [0, 1, 2, 3]
- May be changed whilst playing

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
