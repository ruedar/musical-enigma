# Block-level merge midi defaults

## Uso

```ruby
with_merged_midi_defaults
```

Specify opt values to be used by any following call to the `midi_*` fns within the specified `do` / `end` block. Merges the specified values with any previous midi defaults, rather than replacing them. After the `do` / `end` block has completed, previous defaults (if any) are restored.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e1
use_midi_defaults channel: 3, port: "foo"
midi_note_on :e3
with_merged_midi_defaults channel: 1 do
  midi_note_on :e2
                  
                  
end
midi_note_on :e2</code></pre></td>
<td># Sends MIDI :e1 note_on with default opts<br>
 <br>
# Sends MIDI :e3 note_on to channel 3 on port "foo"<br>
 <br>
# Sends MIDI :e2 note_on to channel 1 on port "foo".<br>
# This is because the call to use_merged_midi_defaults overrode the<br>
# channel but not the port which got merged in.<br>
 <br>
# Sends MIDI :e2 note_on to channel 3 on port "foo".<br>
# This is because the previous defaults were restored after<br>
# the call to with_merged_midi_defaults.</td>
</tr>
</table>
