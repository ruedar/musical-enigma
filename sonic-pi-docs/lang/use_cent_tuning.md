# Cent tuning

## Uso

```ruby
use_cent_tuning  cent_shift (number)
```

Uniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.

See `with_cent_tuning` for setting the cent tuning value only for a specific `do` / `end` block. To transpose entire semitones see `use_transpose`.

## Introduced in v2.9

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_cent_tuning 1
play 50</code></pre></td>
<td># Plays note 50<br>
 <br>
# Plays note 50.01</td>
</tr>
</table>
