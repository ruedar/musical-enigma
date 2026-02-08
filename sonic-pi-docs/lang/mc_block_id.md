# Minecraft Pi - normalise block code

## Uso

```ruby
mc_block_id  name (symbol_or_number)
```

Given a block name or id will return a number representing the id of the block or throw an exception if the name or id isn’t valid

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts mc_block_id :air</code></pre></td>
<td>#=&gt; 0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts mc_block_id 0</code></pre></td>
<td>#=&gt; 0</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts mc_block_id 19</code></pre></td>
<td>#=&gt; Throws an invalid block id exception</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts mc_block_id :foo</code></pre></td>
<td>#=&gt; Throws an invalid block name exception</td>
</tr>
</table>
