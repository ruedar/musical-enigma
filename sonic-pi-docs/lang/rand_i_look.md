# Generate a random whole number without consuming a rand

## Uso

```ruby
rand_i_look  max (number_or_range)
```

Given a max number, produces a whole number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns either `0` or `1`.

Does not consume a random value from the stream. Therefore, multiple sequential calls to `rand_i_look` will all return the same value.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rand_i_look(5)</code></pre></td>
<td>#=&gt; will print either 0, 1, 2, 3, or 4 to the output pane</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>print rand_i_look(5)
print rand_i_look(5)
print rand_i_look(5)
print rand_i(5)
print rand_i_look(5)</code></pre></td>
<td>#=&gt; will print either 0, 1, 2, 3, or 4 to the output pane<br>
#=&gt; will print the same number again<br>
#=&gt; will print the same number again<br>
#=&gt; will print either 0, 1, 2, 3, or 4 to the output pane<br>
#=&gt; will print the same number as the previous statement</td>
</tr>
</table>
