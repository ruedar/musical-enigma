# Generate a random float below a value

## Uso

```ruby
rand  max (number_or_range)
```

Given a max number, produces a float between `0` and the supplied max value. If max is a range, produces a float within the range. With no args returns a random value between `0` and `1`.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rand(0.5)</code></pre></td>
<td>#=&gt; will print a number like 0.375030517578125 to the output pane</td>
</tr>
</table>
