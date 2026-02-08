# Create a ring buffer

## Uso

```ruby
ring  list (array)
```

Create a new immutable ring buffer from args. Indexes wrap around positively and negatively

## Introduced in v2.2

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(ring 1, 2, 3)[0]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(ring 1, 2, 3)[1]</code></pre></td>
<td>#=&gt; 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(ring 1, 2, 3)[3]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(ring 1, 2, 3)[-1]</code></pre></td>
<td>#=&gt; 3</td>
</tr>
</table>
