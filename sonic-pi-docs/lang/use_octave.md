# Note octave transposition

## Uso

```ruby
use_octave  octave_shift (number)
```

Transposes your music by shifting all notes played by the specified number of octaves. To shift up by an octave use a transpose of 1. To shift down use negative numbers. See `with_octave` for setting the octave shift only for a specific `do` / `end` block. For transposing the notes within the octave range see `use_transpose`.

## Introduced in v2.9

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_octave 1
play 50</code></pre></td>
<td># Plays note 50<br>
 <br>
# Plays note 62</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play 62
use_octave -1
play 62
use_octave 2
play 62</code></pre></td>
<td># You may change the transposition multiple times:<br>
# Plays note 62<br>
 <br>
# Plays note 50<br>
 <br>
# Plays note 86</td>
</tr>
</table>
