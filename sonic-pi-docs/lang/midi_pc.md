# Send MIDI program change message

## Uso

```ruby
midi_pc  program_num (midi)
```

Sends a MIDI program change message to *all* connected devices on *all* channels. Use the `port:` and `channel:` opts to restrict which MIDI ports and channels are used.

Program number can be passed as a note such as `:e3` and decimal values will be rounded down or up to the nearest whole number - so values between 3.5 and 4 will be rounded up to 4 and values between 3.49999… and 3 will be rounded down to 3.

MIDI 1.0 Specification - Channel Voice Messages - Program change

## Introduced in v3.0.2

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_pc 100</code></pre></td>
<td>#=&gt; Sends MIDI pc message to all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_pc :e7</code></pre></td>
<td>#=&gt; Sends MIDI pc message to all ports and channels</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>midi_pc 100, channel: 5</code></pre></td>
<td>#=&gt; Sends MIDI pc message on channel 5 to all ports</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>midi_pc 100, channel: 5</code></pre></td>
<td>#=&gt; Sends MIDI pc message on channel 5 to all ports</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>midi_pc 100, channel: [1, 5]</code></pre></td>
<td>#=&gt; Sends MIDI pc message on channel 1 and 5 to all ports</td>
</tr>
</table>
