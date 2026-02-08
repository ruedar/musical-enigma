# Ensure args are not equal

## Uso

```ruby
assert_not_equal  arg1 (anything), arg2 (anything)
```

Raises an exception if both arguments are qual.

## Introduced in v3.3

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert_not_equal 1, 3
assert_not_equal 1, -1
assert_not_equal 1, :foo</code></pre></td>
<td># Simple assertions</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert_not_equal 3, 3, "something is seriously wrong!"</code></pre></td>
<td># Add messages to the exceptions</td>
</tr>
</table>
