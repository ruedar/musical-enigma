# Get current volume

## Uso

```ruby
current_volume
```

Returns the current volume.

This can be set via the fn `set_volume!`.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts current_volume</code></pre></td>
<td># Print out the current volume</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>set_volume! 2
puts current_volume</code></pre></td>
<td>#=&gt; 2</td>
</tr>
</table>
