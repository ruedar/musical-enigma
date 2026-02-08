# Create a ring of octaves

## Uso

```ruby
octs  start (note), num_octaves (pos_int)
```

Create a ring of successive octaves starting at `start` for `num_octaves`.

## Introduced in v2.8

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(octs 60, 2)</code></pre></td>
<td>#=&gt; (ring 60, 72)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(octs :e3, 3)</code></pre></td>
<td>#=&gt; (ring 52, 64, 76)</td>
</tr>
</table>
