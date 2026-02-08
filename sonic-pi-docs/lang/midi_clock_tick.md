# Send an individual MIDI clock tick

## Uso

```ruby
midi_clock_tick
```

Sends a MIDI clock tick message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

Typical MIDI devices expect the clock to send 24 ticks per quarter note (typically a beat). See `midi_clock_beat` for a simple way of sending all the ticks for a given beat.

MIDI 1.0 Specification - System Real-Time Messages - Timing Clock

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_clock_tick</code></pre></td>
<td>#=&gt; Send an individual clock tick to all connected MIDI devices on all ports.</td>
</tr>
</table>
