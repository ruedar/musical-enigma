# Merge MIDI defaults

## Uso

```ruby
use_merged_midi_defaults
```

Specify new default values to be used by all subsequent calls to `midi_*` fns. Merges the specified values with any previous defaults, rather than replacing them

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
use_merged_midi_defaults channel: 1
midi_note_on :e2</code></pre></td>
<td># Sends MIDI :e1 note_on with default opts<br>
 <br>
# Sends MIDI :e3 note_on to channel 3 on port "foo"<br>
 <br>
# Sends MIDI :e2 note_on to channel 1 on port "foo".<br>
# This is because the call to use_merged_midi_defaults overrode the<br>
# channel but not the port which got merged in.</td>
</tr>
</table>
