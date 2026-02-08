# Block-level cent tuning

## Uso

```ruby
with_cent_tuning  cent_shift (number)
```

Similar to `use_cent_tuning` except only applies cent shift to code within supplied `do` / `end` block. Previous cent tuning value is restored after block. One semitone consists of 100 cents. To transpose entire semitones see `with_transpose`.

## Introduced in v2.9

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_cent_tuning 1
play 50
with_cent_tuning 2 do
  play 50
end

play 50</code></pre></td>
<td># Plays note 50.01<br>
 <br>
# Plays note 50.02<br>
 <br>
# Original cent tuning value is restored<br>
# Plays note 50.01</td>
</tr>
</table>
