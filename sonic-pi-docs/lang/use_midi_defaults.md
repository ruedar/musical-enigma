# Use new MIDI defaults

## Uso

```ruby
use_midi_defaults
```

Specify new default values to be used by all subsequent calls to `midi_*` fns. Will remove and override any previous defaults.

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
use_midi_defaults channel: 1
midi_note_on :e2</code></pre></td>
<td># Sends MIDI :e1 note_on with default opts<br>
 <br>
# Sends MIDI :e3 note_on to channel 3 on port "foo"<br>
 <br>
# Sends MIDI :e2 note_on to channel 1. Note that the port is back to the default and no longer "foo".</td>
</tr>
</table>
