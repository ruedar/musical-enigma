# Stretch a sequence of values

## Uso

```ruby
stretch  list (anything), count (number)
```

Stretches a list of values each value repeated count times. Always returns a ring regardless of the type of the list that is stretched. To preserve type, consider using `.stretch` i.e. `(ramp 1, 2, 3).stretch(2) #=> (ramp 1, 1, 2, 2, 3, 3)`

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(stretch [1,2], 3)</code></pre></td>
<td>#=&gt; (ring 1, 1, 1, 2, 2, 2)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(stretch [:e2, :c3], 1, [:c2, :d3], 2)</code></pre></td>
<td>#=&gt; (ring :e2, :c3, :c2, :c2, :d3, :d3)</td>
</tr>
</table>
