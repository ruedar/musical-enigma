# Relative MIDI pitch to frequency ratio

## Uso

```ruby
pitch_to_ratio  pitch (midi_number)
```

Convert a midi note to a ratio which when applied to a frequency will scale the frequency by the number of semitones. Useful for changing the pitch of a sample by using it as a way of generating the rate.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>pitch_to_ratio 12</code></pre></td>
<td>#=&gt; 2.0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>pitch_to_ratio 1</code></pre></td>
<td>#=&gt; 1.05946</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>pitch_to_ratio -12</code></pre></td>
<td>#=&gt; 0.5</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>sample :ambi_choir, rate: pitch_to_ratio(3)</code></pre></td>
<td># Plays :ambi_choir 3 semitones above default.</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>(range 0, 16).each do |n|                 
  sample :ambi_choir, rate: pitch_to_ratio(n)
  sleep 0.5                               
end</code></pre></td>
<td># Play a chromatic scale of semitones<br>
# For each note in the range 0-&gt;16<br>
# play :ambi_choir at the relative pitch<br>
# and wait between notes</td>
</tr>
</table>
