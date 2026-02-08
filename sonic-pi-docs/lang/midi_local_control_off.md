# Disable local control on MIDI devices

## Uso

```ruby
midi_local_control_off
```

Sends a MIDI local control off message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

All devices on a given channel will respond only to data received over MIDI. Played data, etc. will be ignored. See `midi_local_control_on` to enable local control.

MIDI 1.0 Specification - Channel Mode Messages - Local Control Off

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_local_control_off</code></pre></td>
<td>#=&gt; Disable local control on MIDI devices on all channels (and ports)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_local_control_off channel: 2</code></pre></td>
<td>#=&gt; Disable local control on MIDI devices on channel 2</td>
</tr>
</table>
