# Block-level synth switching

## Uso

```ruby
with_synth  synth_name (symbol)
```

Switch the current synth to `synth_name` but only for the duration of the `do` / `end` block. After the `do` / `end` block has completed, the previous synth is restored.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
sleep 2
use_synth :supersaw
play 50
sleep 2
with_synth :saw_beep do
  play 50
end
sleep 2

play 50</code></pre></td>
<td># Plays with default synth<br>
 <br>
 <br>
# Plays with supersaw synth<br>
 <br>
 <br>
# Plays with saw_beep synth<br>
 <br>
 <br>
# Previous synth is restored<br>
# Plays with supersaw synth</td>
</tr>
</table>
