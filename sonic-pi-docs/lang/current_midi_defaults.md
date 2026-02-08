# Get current MIDI defaults

## Uso

```ruby
current_midi_defaults
```

Returns the current MIDI defaults. This is a map of opt names to values

This can be set via the fns `use_midi_defaults`, `with_midi_defaults`, `use_merged_midi_defaults` and `with_merged_midi_defaults`.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_midi_defaults channel: 1, port: "foo"
midi_note_on :e1
current_midi_defaults</code></pre></td>
<td># Sends MIDI :e1 note on to channel 1 on port "foo"<br>
#=&gt; Prints {channel: 1, port: "foo"}</td>
</tr>
</table>
