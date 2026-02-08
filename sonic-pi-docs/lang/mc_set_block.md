# Minecraft Pi - set block at specific coord

## Uso

```ruby
mc_set_block  x (number), y (number), z (number), block_name (symbol_or_number)
```

Change the block type of the block at coords `x`, `y`, `z` to `block_type`. The block type may be specified either as a symbol such as `:air` or a number. See `mc_block_ids` and `mc_block_types` for lists of valid symbols and numbers.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>mc_set_block :glass, 40, 50, 60</code></pre></td>
<td>#=&gt; set block at coords 40, 50, 60 to type glass</td>
</tr>
</table>
