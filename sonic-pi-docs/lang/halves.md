# Create a ring of successive halves

## Uso

```ruby
halves  start (number), num_halves (int)
```

Create a ring containing the results of successive halving of the `start` value. If `num_halves` is negative, will return a ring of `doubles`.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(halves 60, 2)</code></pre></td>
<td>#=&gt; (ring 60, 30)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(halves 120, 3)</code></pre></td>
<td>#=&gt; (ring 120, 60, 30)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(halves 120, 5)</code></pre></td>
<td>#=&gt; (ring 120, 60, 30, 15, 7.5)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(halves 30, -5)</code></pre></td>
<td>#=&gt; (ring 30, 60, 120, 240, 480)</td>
</tr>
</table>
