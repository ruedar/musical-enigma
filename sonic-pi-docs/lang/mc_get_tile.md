# Minecraft Pi - get location of current tile/block

## Uso

```ruby
mc_get_tile
```

Returns the coordinates of the nearest block that the player is next to. This is more course grained than `mc_location` as it only returns whole number coordinates.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts mc_get_tile</code></pre></td>
<td>#=&gt; [10, 20, 101]</td>
</tr>
</table>
