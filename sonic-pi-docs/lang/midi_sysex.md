# Send MIDI System Exclusive (SysEx) message

## Uso

```ruby
midi_sysex
```

Sends the MIDI SysEx message to *all* connected MIDI devices.

MIDI SysEx messages, unlike all other MIDI messages, are variable in length. They allow MIDI device manufacturers to define device-specific messages, for example loading/saving patches, or programming device features such as illuminated buttons.

Floats will be rounded up or down to the nearest whole number e.g. 176.1 -> 176, 120.5 -> 121, 0.49 -> 0.

Non-number values will be automatically turned into numbers prior to sending the event if possible (if this conversion does not work an Error will be thrown).

## Introduced in v3.2

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_sysex 0xf0, 0x00, 0x20, 0x6b, 0x7f, 0x42, 0x02, 0x00, 0x10, 0x77, 0x11, 0xf7</code></pre></td>
<td>#=&gt; Program an Arturia Beatstep controller to turn the eighth pad pink</td>
</tr>
</table>
