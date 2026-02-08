# Block-level use new MIDI defaults

## Uso

```ruby
with_midi_defaults
```

Specify new default values to be used by all calls to `midi_*` fns within the `do` / `end` block. After the `do` / `end` block has completed the previous MIDI defaults (if any) are restored.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e1
with_midi_defaults channel: 3, port: "foo" do
  midi_note_on :e3
end
use_midi_defaults channel: 1  
with_midi_defaults channel: 5 do
  midi_note_on :e2
                  
end
  midi_note_on :e4</code></pre></td>
<td># Sends MIDI :e1 note on with default opts<br>
 <br>
# Sends MIDI :e3 note on to channel 3 on port "foo"<br>
 <br>
# this will be overridden by the following<br>
 <br>
# Sends MIDI :e2 note on to channel 5.<br>
# Note that the port is back to the default<br>
 <br>
# Sends MIDI :e4 note on to channel 1<br>
# Note that the call to use_midi_defaults is now honoured.</td>
</tr>
</table>
