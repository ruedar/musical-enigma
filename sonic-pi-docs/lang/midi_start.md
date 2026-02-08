# Send MIDI system message - start

## Uso

```ruby
midi_start
```

Sends the MIDI start system message to *all* connected MIDI devices on *all* ports.  Use the `port:` opt to restrict which MIDI ports are used.

Start the current sequence playing. (This message should be followed with calls to `midi_clock_tick` or `midi_clock_beat` ).

MIDI 1.0 Specification - System Real-Time Messages - Start

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_start</code></pre></td>
<td>#=&gt; Send start message to all connected MIDI devices</td>
</tr>
</table>
