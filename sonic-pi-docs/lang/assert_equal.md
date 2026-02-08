# Ensure args are equal

## Uso

```ruby
assert_equal  arg1 (anything), arg2 (anything)
```

Raises an exception if both arguments aren’t equal.

## Introduced in v2.8

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert_equal 1, 1</code></pre></td>
<td># Simple assertions</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert_equal 1 + 1, 2
assert_equal [:a, :b, :c].size,  3</code></pre></td>
<td># More interesting assertions<br>
# Ensure that arithmetic is sane!<br>
# ensure lists can be correctly counted</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>assert_equal 3, 5, "something is seriously wrong!"</code></pre></td>
<td># Add messages to the exceptions</td>
</tr>
</table>
