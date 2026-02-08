# Turn off all notes on MIDI devices

## Uso

```ruby
midi_all_notes_off
```

Sends a MIDI all notes off message to *all* connected MIDI devices. on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

When an All Notes Off event is received, all oscillators will turn off.

MIDI 1.0 Specification - Channel Mode Messages - All Notes Off

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_all_notes_off</code></pre></td>
<td>#=&gt; Turn off all notes on MIDI devices on all channels (and ports)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_all_notes_off channel: 2</code></pre></td>
<td>#=&gt; Turn off all notes on MIDI devices on channel 2</td>
</tr>
</table>
