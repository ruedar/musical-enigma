# Ensure arg is valid

## Uso

```ruby
assert  arg (anything)
```

Raises an exception if the argument is either nil or false.

## Introduced in v2.8

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert true  
assert 1     
assert "foo"
assert false</code></pre></td>
<td># Simple assertions<br>
# As true is neither nil or false, this assertion passes<br>
# Similarly, 1 passes<br>
# As do string<br>
# This will raise an exception</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert false, "oops"</code></pre></td>
<td># Communicating error messages<br>
# This will raise an exception containing the message "oops"</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>assert (1 + 1) == 2
assert [:a, :b, :c].size == 3</code></pre></td>
<td># More interesting assertions<br>
# Ensure that arithmetic is sane!<br>
# ensure lists can be correctly counted</td>
</tr>
</table>
