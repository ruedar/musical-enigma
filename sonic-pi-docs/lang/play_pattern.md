# Play pattern of notes

## Uso

```ruby
play_pattern  notes (list)
```

Play list of notes with the current synth one after another with a sleep of 1

Accepts optional args for modification of the synth being played. See each synth’s documentation for synth-specific opts. See use_synth and with_synth for changing the current synth.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play_pattern [40, 41, 42]</code></pre></td>
<td># Same as:<br>
#   play 40<br>
#   sleep 1<br>
#   play 41<br>
#   sleep 1<br>
#   play 42</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play_pattern [:d3, :c1, :Eb5]</code></pre></td>
<td># You can use keyword notes</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>play_pattern [:d3, :c1, :Eb5], amp: 0.5, cutoff: 90</code></pre></td>
<td># Supports the same arguments as play:</td>
</tr>
</table>
