# Print a string representing a list of numeric values as a spark graph/bar chart

## Uso

```ruby
spark
```

Given a list of numeric values, this method turns them into a string of bar heights and prints them out. Useful for quickly graphing the shape of an array.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>spark (range 1, 5)</code></pre></td>
<td>#=&gt; ▁▃▅█</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>spark (range 1, 5).shuffle</code></pre></td>
<td>#=&gt; ▃█▅▁</td>
</tr>
</table>
