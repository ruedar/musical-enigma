# Create a ring buffer representing a straight line

## Uso

```ruby
line  start (number), finish (number)
```

Create a ring buffer representing a straight line between start and finish of steps elements. Steps defaults to `4`. Indexes wrap around positively and negatively. Similar to `range`.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(line 0, 4, steps: 4)</code></pre></td>
<td>#=&gt; (ring 0.0, 1.0, 2.0, 3.0)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(line 5, 0, steps: 5)</code></pre></td>
<td>#=&gt; (ring 5.0, 4.0, 3.0, 2.0, 1.0)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(line 0, 3, inclusive: true)</code></pre></td>
<td>#=&gt; (ring 0.0, 1.0, 2.0, 3.0)</td>
</tr>
</table>
