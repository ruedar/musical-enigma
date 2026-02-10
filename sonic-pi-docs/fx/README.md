# FX - Efectos de Sonic Pi

Documentación completa de todos los efectos disponibles en Sonic Pi.

## Índice de archivos (contenido de esta carpeta)

[autotuner](autotuner.md) · [band_eq](band_eq.md) · [bitcrusher](bitcrusher.md) · [bpf](bpf.md) · [compressor](compressor.md) · [distortion](distortion.md) · [echo](echo.md) · [eq](eq.md) · [flanger](flanger.md) · [gverb](gverb.md) · [hpf](hpf.md) · [ixi_techno](ixi_techno.md) · [krush](krush.md) · [level](level.md) · [lpf](lpf.md) · [mono](mono.md) · [nbpf](nbpf.md) · [nhpf](nhpf.md) · [nlpf](nlpf.md) · [normaliser](normaliser.md) · [nrbpf](nrbpf.md) · [nrhpf](nrhpf.md) · [nrlpf](nrlpf.md) · [octaver](octaver.md) · [pan](pan.md) · [panslicer](panslicer.md) · [ping_pong](ping_pong.md) · [pitch_shift](pitch_shift.md) · [rbpf](rbpf.md) · [record](record.md) · [reverb](reverb.md) · [rhpf](rhpf.md) · [ring_mod](ring_mod.md) · [rlpf](rlpf.md) · [slicer](slicer.md) · [sound_out](sound_out.md) · [sound_out_stereo](sound_out_stereo.md) · [tanh](tanh.md) · [tremolo](tremolo.md) · [vowel](vowel.md) · [whammy](whammy.md) · [wobble](wobble.md)

## Índice de Efectos (con descripción)

- [Autotuner](autotuner.md) - Autotune/phase vocoder effect
- [Band EQ Filter](band_eq.md) - Attenuate or Boost a frequency band
- [Bitcrusher](bitcrusher.md) - Creates lo-fi output
- [Band Pass Filter](bpf.md) - Only allow a 'band' of frequencies through
- [Compressor](compressor.md) - Compresses the dynamic range
- [Distortion](distortion.md) - Distorts the signal
- [Echo](echo.md) - Standard echo effect
- [EQ](eq.md) - Basic parametric EQ
- [Flanger](flanger.md) - Creates a swirling/whooshing effect
- [GVerb](gverb.md) - Spacious reverb effect
- [High Pass Filter](hpf.md) - Dampens lower frequencies
- [Techno from IXI Lang](ixi_techno.md) - Moving resonant low pass filter
- [krush](krush.md) - Krush that sound!
- [Level Amplifier](level.md) - Amplitude modifier
- [Low Pass Filter](lpf.md) - Dampens higher frequencies
- [Mono](mono.md) - Sum left and right channels
- [Normalised Band Pass Filter](nbpf.md) - Like the Band Pass Filter but normalised
- [Normalised High Pass Filter](nhpf.md) - High pass filter chained to a normaliser
- [Normalised Low Pass Filter](nlpf.md) - Low pass filter chained to a normaliser
- [Normaliser](normaliser.md) - Raise or lower amplitude of sound
- [Normalised Resonant Band Pass Filter](nrbpf.md) - Like Band Pass Filter but normalised with resonance
- [Normalised Resonant High Pass Filter](nrhpf.md) - Resonant high pass filter with normalisation
- [Normalised Resonant Low Pass Filter](nrlpf.md) - Resonant low pass filter with normalisation
- [Octaver](octaver.md) - Adds three pitches based on the input sound
- [Pan](pan.md) - Specify position in stereo field
- [Pan Slicer](panslicer.md) - Slice the pan automatically from left to right
- [Ping Pong Echo](ping_pong.md) - Echo FX swapping between left and right channels
- [Pitch shift](pitch_shift.md) - Changes pitch without affecting tempo
- [Resonant Band Pass Filter](rbpf.md) - Band Pass Filter with resonance
- [Record](record.md) - Recorder!
- [Reverb](reverb.md) - Make signal sound spacious or distant
- [Resonant High Pass Filter](rhpf.md) - High pass filter with resonance
- [Ring Modulator](ring_mod.md) - Attack of the Daleks!
- [Resonant Low Pass Filter](rlpf.md) - Low pass filter with resonance
- [Slicer](slicer.md) - Modulates amplitude with control wave
- [Sound Out](sound_out.md) - Outputs mono signal to soundcard output
- [Sound Out Stereo](sound_out_stereo.md) - Outputs stereo signal to two consecutive outputs
- [Hyperbolic Tangent](tanh.md) - Distorted limiter effect
- [Tremolo](tremolo.md) - Modulate the volume of the sound
- [Vowel](vowel.md) - Filters to match human voice vowel sounds
- [Whammy](whammy.md) - Cheap sounding transposition effect
- [Wobble](wobble.md) - Versatile wobble FX

## Sobre los Efectos

Los efectos (FX) en Sonic Pi te permiten modificar el sonido de tus sintetizadores y samples. Se pueden encadenar, controlar en tiempo real y automatizar para crear texturas sonoras complejas.

Todos los FX comparten algunos parámetros comunes:
- `amp:` - Amplitud del sonido
- `mix:` - Cantidad de FX presente en el resultado
- `pre_mix:` - Cantidad de señal original que se alimenta al FX
- `pre_amp:` - Amplificación antes de pasar al FX

Para más información sobre cómo usar FX, consulta el tutorial en `../tutorial/06-FX.md`.
