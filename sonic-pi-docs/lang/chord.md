# Create chord

## Uso

```ruby
chord  tonic (symbol), name (symbol)
```

Creates an immutable ring of Midi note numbers when given a tonic note and a chord type. If only passed a chord type, will default the tonic to 0. See examples.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts (chord :e, :minor)</code></pre></td>
<td># returns a ring of midi notes - (ring 64, 67, 71)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play (chord :e, :minor)</code></pre></td>
<td># Play all the notes together</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>play (chord :e3, :minor, invert: 0)
play (chord :e3, :minor, invert: 1)
play (chord :e3, :minor, invert: 2)</code></pre></td>
<td># Chord inversions (see the fn chord_invert)<br>
# Play the basic :e3, :minor chord - (ring 52, 55, 59)<br>
# Play the first inversion of :e3, :minor - (ring 55, 59, 64)<br>
# Play the first inversion of :e3, :minor - (ring 59, 64, 67)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts (chord :minor)</code></pre></td>
<td># You can create a chord without a tonic:<br>
#=&gt; (ring 0, 3, 7)</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>live_loop :arp do
  play chord(:e, :minor, num_octaves: 2).tick, release: 0.1
  sleep 0.125
end</code></pre></td>
<td># chords are great for arpeggiators</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>(chord :C, '1')
(chord :C, '5')
(chord :C, '+5')
(chord :C, 'm+5')
(chord :C, :sus2)
(chord :C, :sus4)
(chord :C, '6')
(chord :C, :m6)
(chord :C, '7sus2')
(chord :C, '7sus4')
(chord :C, '7-5')
(chord :C, 'm7-5')
(chord :C, '7+5')
(chord :C, 'm7+5')
(chord :C, '9')
(chord :C, :m9)
(chord :C, 'm7+9')
(chord :C, :maj9)
(chord :C, '9sus4')
(chord :C, '6*9')
(chord :C, 'm6*9')
(chord :C, '7-9')
(chord :C, 'm7-9')
(chord :C, '7-10')
(chord :C, '9+5')
(chord :C, 'm9+5')
(chord :C, '7+5-9')
(chord :C, 'm7+5-9')
(chord :C, '11')
(chord :C, :m11)
(chord :C, :maj11)
(chord :C, '11+')
(chord :C, 'm11+')
(chord :C, '13')
(chord :C, :m13)
(chord :C, :add2)
(chord :C, :add4)
(chord :C, :add9)
(chord :C, :add11)
(chord :C, :add13)
(chord :C, :madd2)
(chord :C, :madd4)
(chord :C, :madd9)
(chord :C, :madd11)
(chord :C, :madd13)
(chord :C, :major)
(chord :C, :M)
(chord :C, :minor)
(chord :C, :m)
(chord :C, :major7)
(chord :C, :dom7)
(chord :C, '7')
(chord :C, :M7)
(chord :C, :minor7)
(chord :C, :m7)
(chord :C, :augmented)
(chord :C, :a)
(chord :C, :diminished)
(chord :C, :dim)
(chord :C, :i)
(chord :C, :diminished7)
(chord :C, :dim7)
(chord :C, :i7)</code></pre></td>
<td># Sonic Pi supports a large range of chords<br>
# Notice that the more exotic ones have to be surrounded by ' quotes</td>
</tr>
</table>
