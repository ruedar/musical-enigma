# Enable local control on MIDI devices

## Uso

```ruby
midi_local_control_on
```

Sends a MIDI local control on message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

All devices on a given channel will respond both to data received over MIDI and played data, etc. See `midi_local_control_off` to disable local control.

MIDI 1.0 Specification - Channel Mode Messages - Local Control On

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_local_control_on</code></pre></td>
<td>#=&gt; Enable local control on MIDI devices on all channels (and ports)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_local_control_on channel: 2</code></pre></td>
<td>#=&gt; Enable local control on MIDI devices on channel 2</td>
</tr>
</table>
