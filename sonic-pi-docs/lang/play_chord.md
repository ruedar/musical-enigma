# Play notes simultaneously

## Uso

```ruby
play_chord  notes (list)
```

Play a list of notes at the same time.

Accepts optional args for modification of the synth being played. See each synth’s documentation for synth-specific opts. See `use_synth` and `with_synth` for changing the current synth.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play_chord [40, 45, 47]

play 40
play 45
play 47</code></pre></td>
<td># same as:</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play_chord [40, 45, 47], amp: 0.5

play 40, amp: 0.5
play 45, amp: 0.5
play 47, amp: 0.5</code></pre></td>
<td># same as:</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>play_chord chord(:e3, :minor)</code></pre></td>
<td></td>
</tr>
</table>
