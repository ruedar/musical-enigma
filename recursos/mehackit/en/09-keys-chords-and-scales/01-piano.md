**Keys, chords and scales**

# Keys, chords and scales

Sometimes composing a melody with Sonic Pi can be tricky, if you don’t immediately know what `62` or `:c3` sounds like. To help with that, here’s a browser keyboard for trying out your ideas. If you want, you can select a scale from the drop menu to see what keys might sound nice in a certain key.

## What chords and notes to play?

Obviously you can play whatever notes and chords you like to. There’s no right or wrong. Music doesn’t have to sound harmonic and some dissonance or noise belongs to a track as much as the artist wants it to belong. However there’s some rules you can try out if you wish.

If your composition is in a certain key, let’s say C major for an example, you have certain chords that probably sound nice on the track. Here’s a table with some jazzy chords that should play along with each other quite nicely. If you want you can look more in to chord progressions here: [lotusmusic.com/chord-progression-map.html](http://www.lotusmusic.com/chord-progression-map.html)

| Common chord progressions in major | I - IV - V | I - VI - IV - V | II - V - I |
|---|---|---|---|

| Major key | I | II | III | IV | V | VI |
|---|---|---|---|---|---|---|
| C | chord(:C, :major7) | chord(:D, :minor7) | chord(:E, :minor7) | chord(:F, :major7) | chord(:G, "7") | chord(:A, :minor7) |
| Db | chord(:Db, :major7) | chord(:Eb, :minor7) | chord(:F, :minor7) | chord(:Gb, :major7) | chord(:Ab, "7") | chord(:Bb, :minor7) |
| D | chord(:D, :major7) | chord(:E, :minor7) | chord(:Gb, :minor7) | chord(:G, :major7) | chord(:A, "7") | chord(:B, :minor7) |
| Eb | chord(:Eb, :major7) | chord(:F, :minor7) | chord(:G, :minor7) | chord(:Ab, :major7) | chord(:Bb, "7") | chord(:C, :minor7) |
| E | chord(:E, :major7) | chord(:Gb, :minor7) | chord(:Ab, :minor7) | chord(:A, :major7) | chord(:B, "7") | chord(:Db, :minor7) |
| F | chord(:F, :major7) | chord(:G, :minor7) | chord(:A, :minor7) | chord(:Bb, :major7) | chord(:C, "7") | chord(:D, :minor7) |
| Gb | chord(:Gb, :major7) | chord(:Ab, :minor7) | chord(:Bb, :minor7) | chord(:Cb, :major7) | chord(:Db, "7") | chord(:Eb, :minor7) |
| G | chord(:G, :major7) | chord(:A, :minor7) | chord(:B, :minor7) | chord(:C, :major7) | chord(:D, "7") | chord(:E, :minor7) |
| Ab | chord(:Ab, :major7) | chord(:Bb, :minor7) | chord(:C, :minor7) | chord(:Db, :major7) | chord(:Eb, "7") | chord(:F, :minor7) |
| A | chord(:A, :major7) | chord(:B, :minor7) | chord(:Db, :minor7) | chord(:D, :major7) | chord(:E, "7") | chord(:Gb, :minor7) |
| Bb | chord(:Bb, :major7) | chord(:C, :minor7) | chord(:D, :minor7) | chord(:Eb, :major7) | chord(:F, "7") | chord(:G, :minor7) |
| B | chord(:B, :major7) | chord(:Db, :minor7) | chord(:Eb, :minor7) | chord(:E, :major7) | chord(:Gb, "7") | chord(:Ab, :minor7) |

| Common chord progressions in natural minor | I - VI - VII | I - IV - VII | I - IV - V | I - VI - III - VII | II - V - I |
|---|---|---|---|---|---|

| Minor key | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| Cm | chord(:C, :minor7) | chord(:D, "m7-5") | chord(:Eb, :major7) | chord(:F, :minor7) | chord(:G, :minor7) | chord(:Ab, :major7) | chord(:Bb, "7") |
| Ddm | chord(:Dd, :minor7) | chord(:Eb, "m7-5") | chord(:E, :major7) | chord(:Gb, :minor7) | chord(:Ab, :minor7) | chord(:A, :major7) | chord(:B, "7") |
| Dm | chord(:D, :minor7) | chord(:E, "m7-5") | chord(:F, :major7) | chord(:G, :minor7) | chord(:A, :minor7) | chord(:Bb, :major7) | chord(:C, "7") |
| Ebm | chord(:Eb, :minor7) | chord(:F, "m7-5") | chord(:Gb, :major7) | chord(:Ab, :minor7) | chord(:Bb, :minor7) | chord(:B, :major7) | chord(:Db, "7") |
| Em | chord(:E, :minor7) | chord(:Gb, "m7-5") | chord(:G, :major7) | chord(:A, :minor7) | chord(:B, :minor7) | chord(:C, :major7) | chord(:D, "7") |
| Fm | chord(:F, :minor7) | chord(:G, "m7-5") | chord(:Ab, :major7) | chord(:Bb, :minor7) | chord(:C, :minor7) | chord(:Db, :major7) | chord(:Eb, "7") |
| Gbm | chord(:Gb, :minor7) | chord(:Ab, "m7-5") | chord(:A, :major7) | chord(:B, :minor7) | chord(:Db, :minor7) | chord(:D, :major7) | chord(:E, "7") |
| Gm | chord(:G, :minor7) | chord(:A, "m7-5") | chord(:Bb, :major7) | chord(:C, :minor7) | chord(:D, :minor7) | chord(:Eb, :major7) | chord(:F, "7") |
| Abm | chord(:Ab, :minor7) | chord(:Bb, "m7-5") | chord(:B, :major7) | chord(:Db, :minor7) | chord(:Eb, :minor7) | chord(:E, :major7) | chord(:Gb, "7") |
| Am | chord(:A, :minor7) | chord(:B, "m7-5") | chord(:C, :major7) | chord(:D, :minor7) | chord(:E, :minor7) | chord(:F, :major7) | chord(:G, "7") |
| Bbm | chord(:Bb, :minor7) | chord(:C, "m7-5") | chord(:Db, :major7) | chord(:Eb, :minor7) | chord(:F, :minor7) | chord(:Gb, :major7) | chord(:Ab, "7") |
| Bm | chord(:B, :minor7) | chord(:Db, "m7-5") | chord(:D, :major7) | chord(:E, :minor7) | chord(:Gb, :minor7) | chord(:G, :major7) | chord(:A, "7") |