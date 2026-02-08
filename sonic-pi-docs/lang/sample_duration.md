# Get duration of sample in beats

## Uso

```ruby
sample_duration  path (string)
```

Given the name of a loaded sample, or a path to a `.wav`, `.wave`, `.aif`, `.aiff`, `.ogg`, `.oga` or `.flac` file returns the length of time in beats that the sample would play for. `sample_duration` understands and accounts for all the opts you can pass to `sample` which have an effect on the playback duration such as `rate:`. The time returned is scaled to the current BPM.

*Note:* avoid using `sample_duration` to set the sleep time in `live_loop` s, prefer stretching the sample with the `beat_stretch:` opt or changing the BPM instead. See the examples below for details.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts sample_duration(:loop_garzul)</code></pre></td>
<td># Simple use<br>
# returns 8.0 because this sample is 8 seconds long</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
puts sample_duration(:loop_garzul)
use_bpm 90
puts sample_duration(:loop_garzul)
use_bpm 21
puts sample_duration(:loop_garzul)</code></pre></td>
<td># The result is scaled to the current BPM<br>
 <br>
# =&gt; 16.0<br>
 <br>
# =&gt; 12.0<br>
 <br>
# =&gt; 2.8</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :avoid_this do              
  with_fx :slicer do                  
    sample :loop_amen                 
    sleep sample_duration(:loop_amen) 
  end                                 
end
live_loop :prefer_this do             
  use_sample_bpm :loop_amen           
  with_fx :slicer do                  
    sample :loop_amen
    sleep 1
  end
end
live_loop :or_this do                 
  with_fx :slicer do                  
    sample :loop_amen, beat_stretch: 1
    sleep 1
  end
end</code></pre></td>
<td># Avoid using sample_duration to set the sleep time in live_loops<br>
# It is possible to use sample_duration to drive the frequency of a live loop.<br>
# However, if you're using a rhythmical sample such as a drum beat and it isn't<br>
# in the same BPM as the current BPM, then the FX such as this slicer will be<br>
# badly out of sync. This is because the slicer slices at the current BPM and<br>
# this live_loop is looping at a different BPM (that of the sample)<br>
 <br>
# Instead prefer to set the BPM of the live_loop to match the sample. It has<br>
# two benefits. Now our sleep is a nice and simple 1 (as it's one beat).<br>
# Also, our slicer now works with the beat and sounds much better.<br>
 <br>
 <br>
 <br>
 <br>
# Alternatively we can beat_stretch the sample to match the current BPM. This has the<br>
# side effect of changing the rate of the sample (and hence the pitch). However, the<br>
# FX works nicely in time and the sleep time is also a simple 1.</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>sample_duration :loop_garzul, rate: 1                            
                                                                 
sample_duration :loop_garzul, rate: 0.5                          
                                                                 
sample_duration :loop_garzul, rate: 2                            
                                                                 
sample_duration :loop_garzul, rate: -2                           
                                                                 
sample_duration :loop_garzul, attack: 1                          
sample_duration :loop_garzul, attack: 100                        
sample_duration :loop_garzul, attack: 0                          
                                                                 
sample_duration :loop_garzul, release: 1                         
sample_duration :loop_garzul, release: 100                       
sample_duration :loop_garzul, release: 0                         
                                                                 
sample_duration :loop_garzul, decay: 1                           
sample_duration :loop_garzul, decay: 100                         
sample_duration :loop_garzul, decay: 0                           
                                                                 
                                                                 
                                                                 
sample_duration :loop_garzul, sustain: 0, attack: 0.5            
sample_duration :loop_garzul, sustain: 0, decay: 0.1             
sample_duration :loop_garzul, sustain: 0, release: 1             
sample_duration :loop_garzul, sustain: 2, attack: 0.5, release: 1
                                                                 
                                                                 
sample_duration :loop_garzul, sustain: 0, attack: 8, release: 3  
                                                                 
sample_duration :loop_garzul, rate: 10                           
sample_duration :loop_garzul, sustain: 0, attack: 0.9, rate: 10  
                                                                 
                                                                 
sample_duration :loop_garzul, rpitch: 12                         
sample_duration :loop_garzul, rpitch: -12                        
                                                                 
sample_duration :loop_garzul, rpitch: 12, rate: 2                
                                                                 
                                                                 
sample_duration :loop_garzul, beat_stretch: 3                    
sample_duration :loop_garzul, beat_stretch: 3, rate: 0.5         
                                                                 
                                                                 
sample_duration :loop_garzul, pitch_stretch: 3                   
sample_duration :loop_garzul, pitch_stretch: 3, rate: 0.5        
                                                                 
                                                                 
sample_duration :loop_garzul, start: 0.5                         
sample_duration :loop_garzul, start: 0.5, finish: 0.75           
sample_duration :loop_garzul, finish: 0.5, start: 0.75           
sample_duration :loop_garzul, rate: 2, finish: 0.5, start: 0.75</code></pre></td>
<td># The standard sample opts are also honoured<br>
# Playing a sample at standard speed will return standard length<br>
# =&gt; 8.0<br>
# Playing a sample at half speed will double duration<br>
# =&gt; 16.0<br>
# Playing a sample at double speed will halve duration<br>
# =&gt; 4.0<br>
# Playing a sample backwards at double speed will halve duration<br>
# =&gt; 4.0<br>
# Without an explicit sustain: opt attack: just affects amplitude not duration<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# Without an explicit sustain: opt release: just affects amplitude not duration<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# Without an explicit sustain: opt decay: just affects amplitude not duration<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# =&gt; 8.0<br>
# With an explicit sustain: opt, if the attack + decay + sustain + release envelope<br>
# duration is less than the sample duration time, the envelope will shorten the<br>
# sample time.<br>
# =&gt; 0.5<br>
# =&gt; 0.1<br>
# =&gt; 1.0<br>
# =&gt; 3.5<br>
# If the envelope duration is longer than the sample it will not affect the<br>
# sample duration<br>
# =&gt; 8<br>
# All other opts are taken into account before the comparison with the envelope opts.<br>
# =&gt; 0.8<br>
# =&gt; 0.8 (The duration of the sample is less than the envelope length so wins)<br>
# The rpitch: opt will modify the rate to shift the pitch of the sample up and down<br>
# and therefore affects duration.<br>
# =&gt; 4.0<br>
# =&gt; 16<br>
# The rpitch: and rate: opts combine together.<br>
# =&gt; 2.0<br>
# The beat_stretch: opt stretches the sample so that its duration matches the value.<br>
# It also combines with rate:<br>
# =&gt; 3.0<br>
# =&gt; 6.0<br>
# The pitch_stretch: opt acts identically to beat_stretch when just considering sample<br>
# duration.<br>
# =&gt; 3.0<br>
# =&gt; 6.0<br>
# The start: and finish: opts can also shorten the sample duration and also combine<br>
# with other opts such as rate:<br>
# =&gt; 4.0<br>
# =&gt; 2.0<br>
# =&gt; 2.0<br>
# =&gt; 1.0</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen                   
sleep sample_duration(:loop_amen)   
sample :loop_amen</code></pre></td>
<td># Triggering samples one after another<br>
# start the :loop_amen sample<br>
# wait for the duration of :loop_amen before<br>
# starting it again</td>
</tr>
</table>
