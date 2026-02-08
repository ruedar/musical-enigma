# Block-level tuning modification

## Uso

```ruby
with_tuning  tuning (symbol), fundamental_note (symbol_or_number)
```

Similar to use_tuning except only applies to code within supplied `do` / `end` block. Previous tuning value is restored after block.

## Introduced in v2.6

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_tuning :equal, :c
play :e4
with_tuning :just, :c do
  play :e4
  sleep 1
  play :c4
end

play :e4</code></pre></td>
<td># Plays note 64<br>
 <br>
# Plays note 63.8631<br>
 <br>
# Plays note 60<br>
 <br>
# Original tuning value is restored<br>
# Plays note 64</td>
</tr>
</table>
