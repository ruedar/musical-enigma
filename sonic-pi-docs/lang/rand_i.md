# Generate a random whole number below a value (exclusive)

## Uso

```ruby
rand_i  max (number_or_range)
```

Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rand_i(5)</code></pre></td>
<td>#=&gt; will print either 0, 1, 2, 3, or 4 to the output pane</td>
</tr>
</table>
