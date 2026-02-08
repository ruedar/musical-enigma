# Create a vector

## Uso

```ruby
vector  list (array)
```

Create a new immutable vector from args. Out of range indexes return nil.

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[0]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[1]</code></pre></td>
<td>#=&gt; 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[2]</code></pre></td>
<td>#=&gt; 3</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[3]</code></pre></td>
<td>#=&gt; nil</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[1000]</code></pre></td>
<td>#=&gt; nil</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[-1]</code></pre></td>
<td>#=&gt; nil</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>(vector 1, 2, 3)[-1000]</code></pre></td>
<td>#=&gt; nil</td>
</tr>
</table>
