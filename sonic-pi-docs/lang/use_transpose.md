# Note transposition

## Uso

```ruby
use_transpose  note_shift (number)
```

Transposes your music by shifting all notes played by the specified amount. To shift up by a semitone use a transpose of 1. To shift down use negative numbers. See `with_transpose` for setting the transpose value only for a specific `do` / `end` block. To transpose entire octaves see `use_octave`.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_transpose 1
play 50</code></pre></td>
<td># Plays note 50<br>
 <br>
# Plays note 51</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play 62
use_transpose -12
play 62
use_transpose 3
play 62</code></pre></td>
<td># You may change the transposition multiple times:<br>
# Plays note 62<br>
 <br>
# Plays note 50<br>
 <br>
# Plays note 65</td>
</tr>
</table>
