# Factor test

## Uso

```ruby
factor?  val (number), factor (number)
```

Test to see if factor is indeed a factor of `val`. In other words, can `val` be divided exactly by factor.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>factor?(10, 2)</code></pre></td>
<td># true - 10 is a multiple of 2 (2 * 5 = 10)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>factor?(11, 2)</code></pre></td>
<td>#false - 11 is not a multiple of 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>factor?(2, 0.5)</code></pre></td>
<td>#true - 2 is a multiple of 0.5 (0.5 * 4 = 2)</td>
</tr>
</table>
