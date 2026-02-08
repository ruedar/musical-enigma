# Level Amplifier

## Key
`:level`

## Descripción

Amplitude modifier. All FX have their own amp built in, so it may be the case that you don't specifically need an isolated amp FX. However, it is useful to be able to control the overall amplitude of a number of running synths. All sounds created in the FX block will have their amplitudes multipled by the amp level of this FX. For example, use an amp of 0 to silence all internal synths.

## Introducido en
v2.0

## Parámetros

### amp:
- **Descripción**: The amplitude of the sound. Typically a value between 0 and 1. Higher amplitudes may be used, but won't make the sound louder, they will just reduce the quality of all the sounds currently being played (due to compression.)
- **Default**: 1
- **Restricciones**: must be zero or greater
- Puede cambiarse mientras se reproduce
- Tiene parámetros de slide para dar forma a los cambios
