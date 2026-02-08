# Minecraft Pi - get type of block at coords

## Uso

```ruby
mc_get_block  x (number), y (number), z (number)
```

Returns the type of the block at the coords `x`, `y`, `z` as a symbol.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts mc_get_block 40, 50, 60</code></pre></td>
<td>#=&gt; :air</td>
</tr>
</table>
