# Organ Tonewheel

## Parámetros por defecto

| Parámetro | Valor | Parámetro | Valor | Parámetro | Valor | Parámetro | Valor |
|-----------|-------|-----------|-------|-----------|-------|-----------|-------|
| note | 60 | amp | 1 | pan | 0 | attack | 0.01 |
| decay | 0 | sustain | 1 | release | 0.01 | attack_level | 1 |
| decay_level | sustain_level | sustain_level | 1 | bass | 8 | quint | 8 |
| fundamental | 8 | oct | 8 | nazard | 0 | blockflute | 0 |
| tierce | 0 | larigot | 0 | sifflute | 0 | rs_freq | 6.7 |
| rs_freq_var | 0.1 | rs_pitch_depth | 0.008 | rs_delay | 0 | rs_onset | 0 |
| rs_pan_depth | 0.05 | rs_amplitude_depth | 0.2 |  |  |  |  |

```ruby
use_synth :organ_tonewheel
```

An emulation of a tonewheel organ with an optional rotary speaker. These instruments were the first electro-mechanical synthesisers, developed in the mid 1930s by Laurens Hammond. They generate sine-like signals with the tonewheels and mix them together. Up to 9 sine waves can be combined in order to control the organ's timbre, setting their individual levels with drawbar controls. Their sound is often output over a rotary speaker cabinet, producing a characteristic oscillating sound.

Based on work of Chris Wigington and Zé Craum.

## Introduced in v4.0

## Parámetros

### note:

Note to play. Either a MIDI number or a symbol representing a note. For example: 30, 52, 56.5, `:C`, `:C2`, `:Eb4`, or `:Ds3`. This synth does allow changing or sliding the note while playing. In real tonewheel organs one would get this effect only when fiddling with the motor driving the tonewheel.

- **Default: 60**
- Must be zero or greater, must be a value less than 231
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

- **Default: 0.01**
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

- **Default: 1**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### release:

Amount of time (in beats) for sound to move from sustain level amplitude to silent. A short release (i.e. 0.01) makes the final part of the sound very percussive (potentially resulting in a click). A longer release (i.e 1) fades the sound out gently. Full length of sound is attack + decay + sustain + release.

- **Default: 0.01**
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

### bass:

The drawbar for the tonewheel creating a sound component one octave below the base tone, i.e. half its frequency

- **Default: 8**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### quint:

The drawbar for the tonewheel creating a sound component 3/2 of the frequency of the base tone

- **Default: 8**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### fundamental:

The drawbar for the tonewheel creating the base tone component. If you turn vibrato off and set just this drawbar to 8 and all the others to 0, you basically get a sine tone for the note to be played.

- **Default: 8**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### oct:

The drawbar for the tonewheel creating a sound component one octave above the base tone, i.e. twice its frequency

- **Default: 8**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### nazard:

The drawbar for the tonewheel creating a sound component 3 times the frequency of the base tone

- **Default: 0**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### blockflute:

The drawbar for the tonewheel creating a sound component 2 octaves above the base tone, i.e. 4 times its frequency.

- **Default: 0**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### tierce:

The drawbar for the tonewheel creating a sound component 5 times the frequency of the base tone.

- **Default: 0**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### larigot:

The drawbar for the tonewheel creating a sound component 6 times the frequency of the base tone.

- **Default: 0**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### sifflute:

The drawbar for the tonewheel creating a sound component 3 octaves above the base tone, i.e. 8 times its frequency.

- **Default: 0**
- Must be a value between 0 and 8 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### rs_freq:

Rotation frequency of the rotary speaker in Hertz. The tonewheel organ's rotary speaker affects sound in (at least) 3 ways: The frequency changes due to a Doppler effect, so that the pitch oscillates around the base frequency, the note the synth is playing. The amplitude and hence the perceived loudness change. When the horns rotate, they sound louder when they point towards the listener. The pan changes: When the horns point sideways, they sound louder on the side they point to.

The 'chorale' speed of the speaker is 0.83 Hz, the 'tremolo' speed is 6.7 Hz, each referring to the horn. The woofer rotates at a slower speed, which is calculated from the horn's frequency.

Disable the rotary speaker by setting :rs_freq to 0. Note that while :rs_freq can be slid, sliding up from plain 0 is not possible and sliding to and from frequencies close to 0 may have unexpected effects.

- **Default: 6.7**
- Must be a value between 0 and 10 inclusively
- May be changed whilst playing
- Has slide options to shape changes

### rs_freq_var:

Irregularity of the rotation frequency, expressed as a proportion of the rotation frequency. This affects loudness, pan, and pitch.

- **Default: 0.1**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### rs_pitch_depth:

Size of the pitch deviation around the fundamental, as a proportion of the fundamental. 0.02 = 2% of the fundamental.

- **Default: 0.008**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### rs_delay:

Delay before rotary effect is established, in beats.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### rs_onset:

Transition time in beats from no rotary effect to full rotary effect after the initial delay time.

- **Default: 0**
- Must be zero or greater
- Can not be changed once set
- Scaled with current BPM value

### rs_pan_depth:

Size of the pan deviation from the centre caused by the rotary speaker.

- **Default: 0.05**
- Must be a value between 0 and 1 inclusively
- Can not be changed once set

### rs_amplitude_depth:

Size of the amplitude variation around the base amplitude.

- **Default: 0.2**
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
