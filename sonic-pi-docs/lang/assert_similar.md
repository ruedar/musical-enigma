# Ensure args are similar

## Uso

```ruby
assert_similar  arg1 (anything), arg2 (anything)
```

Raises an exception if both arguments aren’t similar.

Currently similarity is only defined for numbers - all other types are compared for equality with assert_equal.

Useful for testing in cases where floating point imprecision stops you from being able to use `assert_equal`.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>assert_similar 1, 1</code></pre></td>
<td># Simple assertions<br>
#=&gt; True</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>assert_similar(4.9999999999, 5.0)</code></pre></td>
<td># Handles floating point imprecision<br>
#=&gt; True</td>
</tr>
</table>
