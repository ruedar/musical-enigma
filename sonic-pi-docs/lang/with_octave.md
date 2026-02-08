# Block level octave transposition

## Uso

```ruby
with_octave  octave_shift (number)
```

Transposes your music by shifting all notes played by the specified number of octaves within the specified block. To shift up by an octave use a transpose of 1. To shift down use negative numbers. For transposing the notes within the octave range see `with_transpose`.

## Introduced in v2.9

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
sleep 1
with_octave 1 do
 play 50
end
sleep 1
play 50</code></pre></td>
<td># Plays note 50<br>
 <br>
 <br>
# Plays note 62<br>
 <br>
 <br>
# Plays note 50</td>
</tr>
</table>
