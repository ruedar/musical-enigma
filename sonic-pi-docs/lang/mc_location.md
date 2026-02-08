# Minecraft Pi - get current location

## Uso

```ruby
mc_location
```

Returns a list of floats `[x, y, z]` coords of the current location for Steve. The coordinates are finer grained than raw block coordinates but may be used anywhere you might use block coords.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts mc_location</code></pre></td>
<td>#=&gt; [10.1, 20.67, 101.34]</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>x, y, z = mc_location</code></pre></td>
<td>#=&gt; Find the current location and store in x, y and z variables.</td>
</tr>
</table>
