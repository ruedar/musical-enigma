# Create a ring of successive doubles

## Uso

```ruby
doubles  start (number), num_doubles (int)
```

Create a ring containing the results of successive doubling of the `start` value. If `num_doubles` is negative, will return a ring of `halves`.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(doubles 60, 2)</code></pre></td>
<td>#=&gt; (ring 60, 120)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(doubles 1.5, 3)</code></pre></td>
<td>#=&gt; (ring 1.5, 3, 6)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(doubles 1.5, 5)</code></pre></td>
<td>#=&gt; (ring 1.5, 3, 6, 12, 24)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(doubles 100, -4)</code></pre></td>
<td>#=&gt; (ring 100, 50, 25, 12.5)</td>
</tr>
</table>
