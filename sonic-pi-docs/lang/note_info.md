# Get note info

## Uso

```ruby
note_info  note (symbol_or_number)
```

Returns an instance of `SonicPi::Note`. Please note - `octave:` param overrides any octave specified in a symbol i.e. `:c3`

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts note_info(:C, octave: 2)</code></pre></td>
<td># returns #</td>
</tr>
</table>
