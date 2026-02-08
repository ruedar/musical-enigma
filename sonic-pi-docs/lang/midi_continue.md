# Send MIDI system message - continue

## Uso

```ruby
midi_continue
```

Sends the MIDI continue system message to *all* connected MIDI devices on *all* ports.  Use the `port:` opt to restrict which MIDI ports are used.

Upon receiving the MIDI continue event, the MIDI device(s) will continue at the point the sequence was stopped.

MIDI 1.0 Specification - System Real-Time Messages - Continue

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_continue</code></pre></td>
<td>#=&gt; Send continue message to all connected MIDI devices</td>
</tr>
</table>
