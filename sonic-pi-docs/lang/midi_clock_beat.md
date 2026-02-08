# Send a quarter-note's worth of MIDI clock ticks

## Uso

```ruby
midi_clock_beat  duration (beats)
```

Sends enough MIDI clock ticks for one beat to *all* connected MIDI devices. Use the `port:` opt to restrict which MIDI ports are used.

The MIDI specification requires 24 clock tick events to be sent per beat. These can either be sent manually using `midi_clock_tick` or all 24 can be scheduled in one go using this fn. `midi_clock_beat` will therefore schedule for 24 clock ticks to be sent linearly spread over duration beats. This fn will automatically take into account the current BPM and any `time_warp` s.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>midi_clock_beat</code></pre></td>
<td>#=&gt; Send 24 clock ticks over a period of 1 beat</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>midi_clock_beat 0.5</code></pre></td>
<td>#=&gt; Send 24 clock ticks over a period of 0.5 beats</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :clock do 
  midi_clock_beat   
  sleep 1
end</code></pre></td>
<td># Create a live loop which continually sends out MIDI clock<br>
# events at the current BPM</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>live_loop :clock do
  midi_start if tick == 0
  midi_clock_beat        
  sleep 1                
end</code></pre></td>
<td># Ensuring Clock Phase is Correct<br>
 <br>
# Send a midi_start event the first time round the live loop only<br>
# this will not just send a steady clock beat, but also ensure<br>
# the clock phase of the MIDI device matches Sonic Pi.</td>
</tr>
</table>
