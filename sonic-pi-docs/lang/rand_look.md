# Generate a random number without consuming a rand

## Uso

```ruby
rand_look  max (number_or_range)
```

Given a max number, produces a number between `0` and the supplied max value exclusively. If max is a range produces an int within the range. With no args returns a value between `0` and `1`.

Does not consume a random value from the stream. Therefore, multiple sequential calls to `rand_look` will all return the same value.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rand_look(0.5)</code></pre></td>
<td>#=&gt; will print a number like 0.375030517578125 to the output pane</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>print rand_look(0.5)
  print rand_look(0.5)
  print rand_look(0.5)
  print rand(0.5)
  print rand_look(0.5)</code></pre></td>
<td>#=&gt; will print a number like 0.375030517578125 to the output pane<br>
#=&gt; will print the same number again<br>
#=&gt; will print the same number again<br>
#=&gt; will print a different random number<br>
#=&gt; will print the same number as the previous line again.</td>
</tr>
</table>
