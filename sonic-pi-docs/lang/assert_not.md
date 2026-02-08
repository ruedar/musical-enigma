# Ensure arg is not valid

## Uso

```ruby
assert_not  arg (anything)
```

Raises an exception if the argument is not either nil or false.

## Introduced in v3.3

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert_not false  
assert_not nil    
assert_not 1 == 5 
assert true</code></pre></td>
<td># Simple assertions<br>
# As false is either nil or false, this assertion passes<br>
# As nil is either nil or false, this assertion passes<br>
# These numbers are not equal<br>
# This will raise an exception</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert_not true, "oops"</code></pre></td>
<td># Communicating error messages<br>
# This will raise an exception containing the message "oops"</td>
</tr>
</table>
