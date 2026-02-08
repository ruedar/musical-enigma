# Quantise a value to resolution

## Uso

```ruby
quantise  n (number), step (positive_number)
```

Round value to the nearest multiple of step resolution.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>quantise(10, 1)</code></pre></td>
<td># 10 is already a multiple of 1, so returns 10</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>quantise(10, 1.1)</code></pre></td>
<td># Returns 9.9 which is 1.1 * 9</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>quantise(13.3212, 0.1)</code></pre></td>
<td># 13.3</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>quantise(13.3212, 0.2)</code></pre></td>
<td># 13.4</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>quantise(13.3212, 0.3)</code></pre></td>
<td># 13.2</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>quantise(13.3212, 0.5)</code></pre></td>
<td># 13.5</td>
</tr>
</table>
