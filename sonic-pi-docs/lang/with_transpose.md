# Block-level note transposition

## Uso

```ruby
with_transpose  note_shift (number)
```

Similar to use_transpose except only applies to code within supplied `do` / `end` block. Previous transpose value is restored after block. To transpose entire octaves see `with_octave`.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_transpose 3
play 62
with_transpose 12 do
  play 50
  sleep 1
  play 72
end

play 80</code></pre></td>
<td># Plays note 65<br>
 <br>
# Plays note 62<br>
 <br>
# Plays note 84<br>
 <br>
# Original transpose value is restored<br>
# Plays note 83</td>
</tr>
</table>
