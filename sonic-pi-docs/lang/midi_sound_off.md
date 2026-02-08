# Silence all MIDI devices

## Uso

```ruby
midi_sound_off
```

Sends a MIDI sound off message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

All oscillators will turn off, and their volume envelopes are set to zero as soon as possible.

MIDI 1.0 Specification - Channel Mode Messages - All Sound Off

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_sound_off</code></pre></td>
<td>#=&gt; Silence MIDI devices on all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_sound_off channel: 2</code></pre></td>
<td>#=&gt; Silence MIDI devices on channel 2</td>
</tr>
</table>
