# Randomly pick from list (with duplicates)

## Uso

```ruby
pick  list (array), n (number_or_nil)
```

Pick n elements from list or ring. Unlike shuffle, after each element has been picked, it is ‘returned’ to the list so it may be picked again. This means there may be duplicates in the result. If n is greater than the size of the ring/list then duplicates are guaranteed to be in the result.

If `n` isn’t supplied it defaults to a size of 1.

If no arguments are given, will return a lambda function which when called takes an argument which will be a list to be picked from. This is useful for choosing random `onset:` vals for samples.

Always returns a list-like thing (either an array or ring)

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts [1, 2, 3, 4, 5].pick(3)</code></pre></td>
<td>#=&gt; [4, 4, 3]</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts (ring 1, 2, 3, 4, 5).pick(3)</code></pre></td>
<td>#=&gt; (ring 4, 4, 3)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts (ring 1, 2).pick(5)</code></pre></td>
<td>#=&gt; (ring 2, 2, 1, 1, 1)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts (ring 1, 2, 3).pick</code></pre></td>
<td>#=&gt; (ring 3)</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  sample :loop_amen, onset: pick  
  sleep 0.125
end</code></pre></td>
<td># Using pick for random sample onsets<br>
 <br>
# pick a random onset value each time</td>
</tr>
</table>
