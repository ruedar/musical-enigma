# Switch current synth

## Uso

```ruby
use_synth  synth_name (symbol)
```

Switch the current synth to `synth_name`. Affects all further calls to `play`. See `with_synth` for changing the current synth only for a specific `do` / `end` block.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_synth :mod_sine
play 50</code></pre></td>
<td># Plays with default synth<br>
 <br>
# Plays with mod_sine synth</td>
</tr>
</table>
