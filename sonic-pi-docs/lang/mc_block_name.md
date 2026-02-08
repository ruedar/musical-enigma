# Minecraft Pi - normalise block name

## Uso

```ruby
mc_block_name  id (number_or_symbol)
```

Given a block id or a block name will return a symbol representing the block name or throw an exception if the id or name isn’t valid.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts mc_block_name :air</code></pre></td>
<td>#=&gt; :air</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts mc_block_name 0</code></pre></td>
<td>#=&gt; :air</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts mc_block_name 19</code></pre></td>
<td>#=&gt; Throws an invalid block id exception</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts mc_block_name :foo</code></pre></td>
<td>#=&gt; Throws an invalid block name exception</td>
</tr>
</table>
