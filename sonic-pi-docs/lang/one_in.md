# Random true value with specified probability

## Uso

```ruby
one_in  num (number)
```

Returns `true` or `false` with a specified probability - it will return true every one in num times where num is the param you specify

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>one_in 2</code></pre></td>
<td># will return true with a probability of 1/2, false with probability 1/2</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>one_in 3</code></pre></td>
<td># will return true with a probability of 1/3, false with a probability of 2/3</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>one_in 100</code></pre></td>
<td># will return true with a probability of 1/100, false with a probability of 99/100</td>
</tr>
</table>
