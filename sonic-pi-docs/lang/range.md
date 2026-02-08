# Create a ring buffer with the specified start, finish and step size

## Uso

```ruby
range  start (number), finish (number), step_size (number)
```

Create a new ring buffer from the range arguments (start, finish and step size). Step size defaults to `1`. Indexes wrap around positively and negatively

## Introduced in v2.2

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(range 1, 5)</code></pre></td>
<td>#=&gt; (ring 1, 2, 3, 4)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(range 1, 5, inclusive: true)</code></pre></td>
<td>#=&gt; (ring 1, 2, 3, 4, 5)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(range 1, 5, step: 2)</code></pre></td>
<td>#=&gt; (ring 1, 3)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(range 1, -5, step: 2)</code></pre></td>
<td>#=&gt; (ring 1, -1, -3)</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>(range 1, -5, step: 2)[-1]</code></pre></td>
<td>#=&gt; -3</td>
</tr>
</table>
