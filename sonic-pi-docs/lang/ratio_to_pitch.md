# Relative frequency ratio to MIDI pitch

## Uso

```ruby
ratio_to_pitch  ratio (number)
```

Convert a frequency ratio to a midi note which when added to a note will transpose the note to match the frequency ratio.

## Introduced in v2.7

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>ratio_to_pitch 2</code></pre></td>
<td>#=&gt; 12.0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>ratio_to_pitch 0.5</code></pre></td>
<td>#=&gt; -12.0</td>
</tr>
</table>
