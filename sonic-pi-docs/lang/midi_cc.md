# Send MIDI control change message

## Uso

```ruby
midi_cc  control_num (midi), value (midi)
```

Sends a MIDI control change message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

Control number and control value can be passed as a note such as `:e3` and decimal values will be rounded down or up to the nearest whole number - so values between 3.5 and 4 will be rounded up to 4 and values between 3.49999… and 3 will be rounded down to 3.

You may also optionally pass the control value as a floating point value between 0 and 1 such as 0.2 or 0.785 (which will be mapped to MIDI values between 0 and 127) using the `val_f:` opt.

MIDI 1.0 Specification - Channel Voice Messages - Control change

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_cc 100, 32</code></pre></td>
<td>#=&gt; Sends MIDI cc message to control 100 with value 32 to all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_cc :e7, 32</code></pre></td>
<td>#=&gt; Sends MIDI cc message to control 100 with value 32 to all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>midi_cc 100, 32, channel: 5</code></pre></td>
<td>#=&gt; Sends MIDI cc message to control 100 with value 32 on channel 5 to all ports</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>midi_cc 100, val_f: 0.8, channel: 5</code></pre></td>
<td>#=&gt; Sends MIDI cc message to control 100 with value 102 on channel 5 to all ports</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>midi_cc 100, value: 102, channel: [1, 5]</code></pre></td>
<td>#=&gt; Sends MIDI cc message to control 100 with value 102 on channel 1 and 5 to all ports</td>
</tr>
</table>
