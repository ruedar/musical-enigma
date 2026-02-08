# Reset MIDI devices

## Uso

```ruby
midi_reset  value (number)
```

Sends a MIDI reset all controllers message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

All controller values are reset to their defaults.

MIDI 1.0 Specification - Channel Mode Messages - Reset All Controllers

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_reset</code></pre></td>
<td>#=&gt; Reset MIDI devices on all channels (and ports)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_reset channel: 2</code></pre></td>
<td>#=&gt; Reset MIDI devices on channel 2</td>
</tr>
</table>
