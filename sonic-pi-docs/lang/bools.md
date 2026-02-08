# Create a ring of boolean values

## Uso

```ruby
bools  list (array)
```

Create a new ring of booleans values from 1s and 0s, which can be easier to write and manipulate in a live setting.

## Introduced in v2.2

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(bools 1, 0)</code></pre></td>
<td>#=&gt; (ring true, false)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(bools 1, 0, true, false, nil)</code></pre></td>
<td>#=&gt; (ring true, false, true, false, false)</td>
</tr>
</table>
