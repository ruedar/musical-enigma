# Send MIDI note on message

## Uso

```ruby
midi_note_on  note (midi), velocity (midi)
```

Sends a MIDI Note On Event to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to indepently restrict which MIDI ports and channels are used.

Note and velocity values can be passed as a note symbol such as `:e3` or a MIDI number such as 52. Decimal values will be rounded down or up to the nearest whole number - so values between 3.5 and 4 will be rounded up to 4 and values between 3.49999… and 3 will be rounded down to 3. These values will also be clipped within the range 0->127 so all values lower than 0 will be increased to 0 and all values greater than 127 will be reduced to 127.

The `velocity` param may be omitted - in which case it will default to 127 unless you supply it as an opt via the keys `velocity:` or `vel_f:`.

You may also optionally pass the velocity value as a floating point value between 0 and 1 such as 0.2 or 0.785 (which will be linearly mapped to MIDI values between 0 and 127) using the vel_f: opt.

MIDI 1.0 Specification - Channel Voice Messages - Note on event

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3</code></pre></td>
<td>#=&gt; Sends MIDI note on :e3 with the default velocity of 12 to all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, 12</code></pre></td>
<td>#=&gt; Sends MIDI note on :e3 with velocity 12 to all channels</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, 12, channel: 3</code></pre></td>
<td>#=&gt; Sends MIDI note on :e3 with velocity 12 on channel 3</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, velocity: 100</code></pre></td>
<td>#=&gt; Sends MIDI note on for :e3 with velocity 100</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, vel_f: 0.8</code></pre></td>
<td>#=&gt; Scales velocity 0.8 to MIDI value 102 and sends MIDI note on for :e3 with velocity 102</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>midi_note_on 60.3, 50.5</code></pre></td>
<td>#=&gt; Rounds params up or down to the nearest whole number and sends MIDI note on for note 60 with velocity 51</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, channel: [1, 3, 5]</code></pre></td>
<td>#=&gt; Send MIDI note :e3 on to channels 1, 3, 5 on all connected ports</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, port: ["foo", "bar"]</code></pre></td>
<td>#=&gt; Send MIDI note :e3 on to on all channels on ports named "foo" and "bar"</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>midi_note_on :e3, channel: 1, port: "foo"</code></pre></td>
<td>#=&gt; Send MIDI note :e3 on only on channel 1 on port "foo"</td>
</tr>
</table>
