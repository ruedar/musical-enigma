# Ensure block throws an error

## Uso

```ruby
assert_error  class (Exception)
```

Runs the block and ensures that it raises the correct Exception. Useful for asserting that an Exception will be raised. You may specify the particular Exception class, which defaults to `Exception`.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert_error do
  play 70
end</code></pre></td>
<td># Will throw an exception: "Assert error failed!" as the block<br>
# contains no errors.</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert_error do
  1 / 0
end</code></pre></td>
<td># Will not throw an exception as the block contains an error.</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>assert_error ZeroDivisionError do
  1 / 0
end</code></pre></td>
<td># Will not throw an exception as the block contains a ZeroDivisionError.</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>assert_error ThreadError do
  1 / 0
end</code></pre></td>
<td># Will throw an exception as the block contains a ZeroDivisionError rather than<br>
# a ThreadError.</td>
</tr>
</table>
