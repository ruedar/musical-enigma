# Block level comment ignoring

## Uso

```ruby
uncomment
```

Evaluates all of the code within the block. Use to reverse the effect of the comment without having to explicitly remove it.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>uncomment do
    play 50
    sleep 1
    play 62
  end</code></pre></td>
<td># starting a block level comment:<br>
# played<br>
# sleep happens<br>
# played</td>
</tr>
</table>
