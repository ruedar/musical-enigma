# Create a ramp vector

## Uso

```ruby
ramp  list (array)
```

Create a new immutable ramp vector from args. Indexes always return first or last value if out of bounds.

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[0]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[1]</code></pre></td>
<td>#=&gt; 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[2]</code></pre></td>
<td>#=&gt; 3</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[3]</code></pre></td>
<td>#=&gt; 3</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[1000]</code></pre></td>
<td>#=&gt; 3</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[-1]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>(ramp 1, 2, 3)[-1000]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
</table>
