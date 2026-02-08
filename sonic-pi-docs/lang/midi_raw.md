# Send raw MIDI message

## Uso

```ruby
midi_raw
```

Sends the raw MIDI message to *all* connected MIDI devices. Gives you direct access to sending the individual bytes of a MIDI message. Typically this should be rarely used - prefer the other `midi_` fns where possible.

A raw MIDI message consists of multiple bytes as numbers in decimal notation (i.e. 176), hex (0xb0) or binary (0b10110000).

See https://www.midi.org/specifications/item/table-1-summary-of-midi-message for a summary of MIDI messages and their corresponding byte structures.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_raw 176, 121, 0</code></pre></td>
<td>#=&gt; Sends the MIDI reset command</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_raw 176.1, 120.5, 0.49</code></pre></td>
<td>#=&gt; Sends the MIDI reset command (values are rounded down, up and down respectively)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>midi_raw 0xb0, 0x79, 0x0</code></pre></td>
<td>#=&gt; Sends the MIDI reset command</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>midi_raw 0b10110000, 0b01111001, 0b00000000</code></pre></td>
<td>#=&gt; Sends the MIDI reset command</td>
</tr>
</table>
