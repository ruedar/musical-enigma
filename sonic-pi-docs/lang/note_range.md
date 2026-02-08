# Get a range of notes

## Uso

```ruby
note_range  low_note (note), high_note (note)
```

Produces a ring of all the notes between a low note and a high note. By default this is chromatic (all the notes) but can be filtered with a pitches: argument. This opens the door to arpeggiator style sequences and other useful patterns. If you try to specify only pitches which aren’t in the range it will raise an error - you have been warned!

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(note_range :c4, :c5)</code></pre></td>
<td># =&gt; (ring 60,61,62,63,64,65,66,67,68,69,70,71,72)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(note_range :c4, :c5, pitches: (chord :c, :major))</code></pre></td>
<td># =&gt; (ring 60,64,67,72)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(note_range :c4, :c6, pitches: (chord :c, :major))</code></pre></td>
<td># =&gt; (ring 60,64,67,72,76,79,84)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(note_range :c4, :c5, pitches: (scale :c, :major))</code></pre></td>
<td># =&gt; (ring 60,62,64,65,67,69,71,72)</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>(note_range :c4, :c5, pitches: [:c4, :g2])</code></pre></td>
<td># =&gt; (ring 60,67,72)</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>live_loop :arpeggiator do
 
  play (note_range :c4, :c5, pitches: (chord :c, :major)).tick
  sleep 0.125
end</code></pre></td>
<td># try changing the chord</td>
</tr>
</table>
