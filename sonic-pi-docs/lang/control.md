# Control running synth

## Uso

```ruby
control  node (synth_node)
```

Control a running synth node by passing new parameters to it. A synth node represents a running synth and can be obtained by assigning the return value of a call to play or sample or by specifying a parameter to the do/end block of an FX. You may modify any of the parameters you can set when triggering the synth, sample or FX. See documentation for opt details. If the synth to control is a chord, then control will change all the notes of that chord group at once to a new target set of notes - see example. Also, you may use the on: opt to conditionally trigger the control - see the docs for the `synth` and `sample` fns for more information.

If no synth to control is specified, then the last synth triggered by the current (or parent) thread will be controlled - see example below.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>my_node = play 50, release: 5, cutoff: 60
sleep 1
control my_node, cutoff: 70
sleep 1
control my_node, cutoff: 90</code></pre></td>
<td># Basic control<br>
# play note 50 with release of 5 and cutoff of 60. Assign return value to variable my_node<br>
# Sleep for a second<br>
# Now modify cutoff from 60 to 70, sound is still playing<br>
# Sleep for another second<br>
# Now modify cutoff from 70 to 90, sound is still playing</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>s = synth :prophet, note: :e1, cutoff: 70, cutoff_slide: 8, release: 8
control s, cutoff: 130</code></pre></td>
<td># Combining control with slide opts allows you to create nice transitions.<br>
# start synth and specify slide time for cutoff opt<br>
# Change the cutoff value with a control.<br>
# Cutoff will now slide over 8 beats from 70 to 130</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>notes = (scale :e3, :minor_pentatonic, num_octaves: 2).shuffle
s = synth :beep, note: :e3, sustain: 8, note_slide: 0.05
64.times do
  control s, note: notes.tick                           
  sleep 0.125
end</code></pre></td>
<td># Use a short slide time and many controls to create a sliding melody<br>
# get a random ordering of a scale<br>
# Start our synth running with a long sustain and short note slide time<br>
 <br>
# Keep quickly changing the note by ticking through notes repeatedly</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>with_fx :bitcrusher, sample_rate: 1000, sample_rate_slide: 8 do |bc|
                                                                    
                                                                    
  sample :loop_garzul, rate: 1
  control bc, sample_rate: 5000                                     
                                                                    
end</code></pre></td>
<td># Controlling FX<br>
# Start FX but also use the handy || goalposts<br>
# to grab a handle on the running FX. We can call<br>
# our handle anything we want. Here we've called it bc<br>
 <br>
# We can use our handle bc now just like we used s in the<br>
# previous example to modify the FX as it runs.</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>cg = play (chord :e4, :minor), sustain: 2 
sleep 1
control cg, notes: (chord :c3, :major)</code></pre></td>
<td># Controlling chords<br>
# start a chord<br>
 <br>
# transition to new chord.<br>
# Each note in the original chord is mapped onto<br>
# the equivalent in the new chord.</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>cg = play (chord :e4, :minor), sustain: 4, note_slide: 3 
sleep 1
control cg, notes: (chord :c3, :major)</code></pre></td>
<td># Sliding between chords<br>
# start a chord<br>
 <br>
# slide to new chord.<br>
# Each note in the original chord is mapped onto<br>
# the equivalent in the new chord.</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>cg = play (chord :e3, :m13), sustain: 4, note_slide: 3 
sleep 1
control cg, notes: (chord :c3, :major)</code></pre></td>
<td># Sliding from a larger to smaller chord<br>
# start a chord with 7 notes<br>
 <br>
# slide to new chord with fewer notes (3)<br>
# Each note in the original chord is mapped onto<br>
# the equivalent in the new chord using ring-like indexing.<br>
# This means that the 4th note in the original chord will<br>
# be mapped onto the 1st note in the second chord and so-on.</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>cg = play (chord :c3, :major), sustain: 4, note_slide: 3 
sleep 1
control cg, notes: (chord :e3, :m13)</code></pre></td>
<td># Sliding from a smaller to larger chord<br>
# start a chord with 3 notes<br>
 <br>
# slide to new chord with more notes (7)<br>
# Each note in the original chord is mapped onto<br>
# the equivalent in the new chord.<br>
# This means that the 4th note in the new chord<br>
# will not sound as there is no 4th note in the<br>
# original chord.</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>s = synth :prophet, note: :e1, release: 8, cutoff: 70, cutoff_slide: 8
sleep 1                                                               
control s, cutoff: 130                                                
sleep 3                                                               
control s, cutoff_slide: 1</code></pre></td>
<td># Changing the slide rate<br>
# Start a synth playing with a long cutoff slide<br>
# wait a beat<br>
# change the cutoff so it starts sliding slowly<br>
# wait for 3 beats<br>
# Change the cutoff_slide - the cutoff now slides more quickly to 130<br>
# it will now take 1 beat to slide from its *current* value<br>
# (somewhere between 70 and 130) to 130</td>
</tr>
<tr>
<th colspan="2"># Example 10</th>
</tr>
<tr>
<td><pre><code>synth :prophet, note: :e1, release: 8                                 
sleep 1
16.times do
  control note: (octs :e1, 3).tick                                    
  sleep 0.125                                                         
end</code></pre></td>
<td># Controlling the last triggered synth<br>
# Every time a synth is triggered, Sonic Pi automatically remembers the node<br>
 <br>
 <br>
# This means we don't need to use an explicit variable to control the synth<br>
# we last triggered.</td>
</tr>
<tr>
<th colspan="2"># Example 11</th>
</tr>
<tr>
<td><pre><code>synth :beep, release: 4                 
sleep 0.1
control note: :e5                       
sleep 0.5
synth :dsaw, release: 4                 
sleep 0.1
control note: :e4</code></pre></td>
<td># Controlling multiple synths without variables<br>
# Trigger a beep synth<br>
 <br>
# Control last triggered synth (:beep)<br>
 <br>
# Next, trigger a dsaw synth<br>
 <br>
# Control last triggered synth (:dsaw)</td>
</tr>
</table>
