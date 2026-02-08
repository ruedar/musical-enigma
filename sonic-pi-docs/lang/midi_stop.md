# Send MIDI system message - stop

## Uso

```ruby
midi_stop
```

Sends the MIDI stop system message to *all* connected MIDI devices on *all* ports.  Use the `port:` opt to restrict which MIDI ports are used.

Stops the current sequence.

MIDI 1.0 Specification - System Real-Time Messages - Start

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_stop</code></pre></td>
<td>#=&gt; Send stop message to all connected MIDI devices</td>
</tr>
</table>
