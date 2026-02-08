# Rhodey

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 69 | amp | 1 | pan | 0 | attack | 0.001 |
| decay | 1 | sustain | 0 | release | 1 | attack_level | 1 |
| decay_level | sustain_level | sustain_level | 0 | lfo_width | 0.3 | lfo_rate | 0.4 |
| vel | 0.8 | mod_index | 0.2 | mix | 0.2 |  |  |

```ruby
use_synth :rhodey
```

The sound of an electric piano from the 60's and 70's, producing a characteristic metallic sound for notes below :g2. Adapted for Sonic Pi from SuperCollider Code. Note the remarks on :sustain_level, if you are looking for a sustained sound, rather than a plucked one.

## Introduced in v4.5

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: `30`, `52`, `:C`, `:C2`, `:Eb4`, or `:Ds3`

- **Default: 69**
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

- **Default: 0.001**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### decay:

Amount of time (in beats) for the sound to move from full amplitude (attack_level) to the sustain amplitude (sustain_level).

- **Default: 1**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### sustain:

Amount of time (in beats) for sound to remain at sustain level amplitude. Longer sustain values result in longer sounds. Full length of sound is attack + decay + sustain + release. Note that for this value to take effect, the :sustain_level must be greater than zero.

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

Amplitude level reached after decay phase and immediately before release phase. Note that the default is zero, so that the envelope rises to the :attack_level taking the :attack time and then goes directly to zero in the :decay time, emulating a plucked instrument. For a sustained sound, set the :sustain_level to a value greater than zero.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set

### lfo_width:

Width of the low-frequency oscillator (LFO) which determines how wide base tones oscillate around their base frequencies; a dimensionless scaled ratio between base and peak oscillator frequencies

- **Default: 0.3**
- Must be zero or greater, must be a value less than 1
- May be changed whilst playing
- Has slide options to shape changes

### lfo_rate:

Rate of the low-frequency oscillator (LFO) in Hz which determines how fast base tones oscillate around their base frequencies

- **Default: 0.4**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### vel:

The velocity of the attack, makes the sound louder and changes the timbre

- **Default: 0.8**
- Must be zero or greater, must be a value less than 10
- Can not be changed once set

### mod_index:

Controls the basic oscillator's amplitude in the sound generation. For typical electric piano sounds use values between 0 and 1. Values beyond 1 also produce interesting sounds, albeit untypical for an electric piano.

- **Default: 0.2**
- Must be zero or greater
- May be changed whilst playing
- Has slide options to shape changes

### mix:

Controls the composition of the oscilators. Use values near 1 for a softer, xylophone-like timbre.

- **Default: 0.2**
- Must be a value between 0 and 1 inclusively
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
