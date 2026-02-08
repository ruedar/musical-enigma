# Hz to MIDI conversion

## Uso

```ruby
hz_to_midi  freq (number)
```

Convert a frequency in hz to a midi note. Note that the result isn’t an integer and there is a potential for some very minor rounding errors.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>hz_to_midi(261.63)</code></pre></td>
<td>#=&gt; 60.0003</td>
</tr>
</table>
