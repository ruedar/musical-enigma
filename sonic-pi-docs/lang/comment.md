# Block level commenting

## Uso

```ruby
comment
```

Does not evaluate any of the code within the block. However, any optional args passed before the block *will* be evaluated although they will be ignored. See `uncomment` for switching commenting off without having to remove the comment form.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>comment do
    play 50
    sleep 1
    play 62
  end</code></pre></td>
<td># starting a block level comment:<br>
# not played<br>
# no sleep happens<br>
# not played</td>
</tr>
</table>
