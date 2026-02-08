# Enable and disable debug

## Uso

```ruby
use_debug  true_or_false (boolean)
```

Enable or disable messages created on synth triggers. If this is set to false, the synths will be silent until debug is turned back on. Silencing debug messages can reduce output noise and also increase performance on slower platforms. See `with_debug` for setting the debug value only for a specific `do` / `end` block.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_debug true</code></pre></td>
<td># Turn on debug messages</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_debug false</code></pre></td>
<td># Disable debug messages</td>
</tr>
</table>
