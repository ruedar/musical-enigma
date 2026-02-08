# Create a ring buffer of midi note numbers

## Uso

```ruby
midi_notes  list (array)
```

Create a new immutable ring buffer of notes from args. Indexes wrap around positively and negatively. Final ring consists only of MIDI numbers and nil.

## Introduced in v2.7

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(midi_notes :d3, :d4, :d5)</code></pre></td>
<td>#=&gt; (ring 50, 62, 74)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(midi_notes :d3, 62,  nil)</code></pre></td>
<td>#=&gt; (ring 50, 62, nil)</td>
</tr>
</table>
