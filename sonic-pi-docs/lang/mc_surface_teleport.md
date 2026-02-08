# Minecraft Pi - teleport to world surface at x and z coords

## Uso

```ruby
mc_surface_teleport  x (number), z (number)
```

Teleports you to the specified x and z coordinates with the y automatically set to place you on the surface of the world. For example, if the x and z coords target a mountain, you’ll be placed on top of the mountain, not in the air or under the ground. See mc_ground_height for discovering the height of the ground at a given x, z point.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>mc_surface_teleport 40, 50</code></pre></td>
<td>#=&gt; Teleport user to coords x = 40, y = height of surface, z = 50</td>
</tr>
</table>
