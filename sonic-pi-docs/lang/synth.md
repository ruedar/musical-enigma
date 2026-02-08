# Trigger specific synth

## Uso

```ruby
synth  synth_name (symbol)
```

Trigger specified synth with given opts. Bypasses `current_synth` value, yet still honours `current_synth_defaults`. When using `synth`, the note is no longer an explicit argument but an opt with the key `note:`.

If note: opt is `nil`, `:r` or `:rest`, play is ignored and treated as a rest. Also, if the `on:` opt is specified and returns `false`, or `nil` then play is similarly ignored and treated as a rest.

If the synth name is `nil` behaviour is identical to that of `play` in that the `current_synth` will determine the actual synth triggered.

If a block is given, it is assumed to take one arg which will be the controllable synth node and the body of the block is run in an implicit `in_thread`. This allows for asynchronous control of the synth without interfering with time. For synchronous control capture the result of `synth` as a variable and use that.

Note that the default opts listed are only a guide to the most common opts across all the synths. Not all synths support all the default opts and each synth typically supports many more opts specific to that synth. For example, the `:tb303` synth supports 45 unique opts. For a full list of a synth’s opts see its documentation in the Help system. This can be accessed directly by clicking on the name of the synth and using the shortcut `C-i`

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_synth :beep           
play 60                   
synth :dsaw, note: 60</code></pre></td>
<td># Set current synth to :beep<br>
# Play note 60 with opt defaults<br>
# Bypass current synth and play :dsaw<br>
# with note 60 and opt defaults</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>synth :fm, note: 60, amp: 0.5</code></pre></td>
<td># Play note 60 of the :fm synth with an amplitude of 0.5</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>use_synth_defaults release: 5
synth :dsaw, note: 50</code></pre></td>
<td># Play note 50 of the :dsaw synth with a release of 5</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>synth :dsaw, notes: (chord :e3, :minor)</code></pre></td>
<td># You can play chords with the notes: opt:</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>notes = (scale :e3, :minor_pentatonic, num_octaves: 2)
live_loop :rhyth do
  8.times do
    trig = (spread 3, 7).tick(:rhyth)
    synth :tri, on: trig, note: notes.tick, release: 0.1 
                                                         
                                                         
    sleep 0.125
  end
end
live_loop :rhyth2 do
  8.times do
    trig = (spread 3, 7).tick(:rhyth)
    synth :saw, note: notes.tick, release: 0.1 if trig 
                                                       
                                                       
    sleep 0.125
  end
end</code></pre></td>
<td># on: vs if<br>
 <br>
 <br>
 <br>
 <br>
# Here, we're calling notes.tick<br>
# every time we attempt to play the synth<br>
# so the notes rise faster than rhyth2<br>
 <br>
 <br>
 <br>
 <br>
 <br>
 <br>
# Here, we're calling notes.tick<br>
# only when the spread says to play<br>
# so the notes rise slower than rhyth</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>s = synth :beep, note: :e3, release: 4
sleep 1
control s, note: :e5
sleep 0.5
synth :dsaw, note: :e3</code></pre></td>
<td># controlling a synth synchronously<br>
 <br>
 <br>
 <br>
 <br>
# This is triggered after 1.5s from start</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>synth :beep, note: :e3, release: 4 do |s|
  sleep 1                                              
  control s, note: :e5                                 
end
sleep 0.5
synth :dsaw, note: :e3</code></pre></td>
<td># Controlling a synth asynchronously<br>
 <br>
# This block is run in an implicit in_thread<br>
# and therefore is asynchronous<br>
 <br>
 <br>
# This is triggered after 0.5s from start</td>
</tr>
</table>
