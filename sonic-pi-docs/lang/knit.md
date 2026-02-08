# Knit a sequence of repeated values

## Uso

```ruby
knit  value (anything), count (number)
```

Knits a series of value, count pairs to create a ring buffer where each value is repeated count times.

## Introduced in v2.2

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(knit 1, 5)</code></pre></td>
<td>#=&gt; (ring 1, 1, 1, 1, 1)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(knit :e2, 2, :c2, 3)</code></pre></td>
<td>#=&gt; (ring :e2, :e2, :c2, :c2, :c2)</td>
</tr>
</table>
