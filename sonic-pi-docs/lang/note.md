# Describe note

## Uso

```ruby
note  note (symbol_or_number)
```

Takes a midi note, a symbol (e.g. `:C` ) or a string (e.g. `"C"` ) and resolves it to a midi note. You can also pass an optional `octave:` parameter to get the midi note for a given octave. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`. If the note is `nil`, `:r` or `:rest`, then `nil` is returned ( `nil` represents a rest)

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts note(60)
puts note(:C)
puts note(:C4)
puts note('C')</code></pre></td>
<td># These all return 60 which is the midi number for middle C (octave 4)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts note(60, octave: 2)

puts note(:C, octave: 2)
puts note(:C4, octave: 2)
puts note('C', octave: 2)</code></pre></td>
<td># returns 60 - octave param has no effect if we pass in a number<br>
 <br>
# These all return 36 which is the midi number for C2 (two octaves below middle C)<br>
 <br>
# note the octave param overrides any octaves specified in a symbol</td>
</tr>
</table>
