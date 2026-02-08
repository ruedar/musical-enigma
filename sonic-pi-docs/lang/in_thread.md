# Run code block at the same time

## Uso

```ruby
in_thread
```

Execute a given block (between `do` … `end` ) in a new thread. Use for playing multiple ‘parts’ at once. Each new thread created inherits all the use/with defaults of the parent thread such as the time, current synth, bpm, default synth args, etc. Despite inheriting defaults from the parent thread, any modifications of the defaults in the new thread will *not* affect the parent thread. Threads may be named with the `name:` optional arg. Named threads will print their name in the logging pane when they print their activity. If you attempt to create a new named thread with a name that is already in use by another executing thread, no new thread will be created.

It is possible to delay the initial trigger of the thread on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial thread creation first the delay will be honoured and then the sync.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>loop do     
    play 50   
    sleep 1   
  end
  loop do     
    play 55
    sleep 0.5
  end</code></pre></td>
<td># If you write two loops one after another like this,<br>
# then only the first loop will execute as the loop acts<br>
# like a trap not letting the flow of control out<br>
 <br>
# This code is never executed.</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>in_thread do
   
    loop do
     
      play 50
      sleep 1
    end
  end
 
  loop do     
    play 55
    sleep 0.5
  end</code></pre></td>
<td># In order to play two loops at the same time, the first loops need to<br>
# be in a thread (note that it's probably more idiomatic to use live_loop<br>
# when performing):<br>
# By wrapping our loop in an in_thread block, we split the<br>
# control flow into two parts. One flows into the loop (a) and<br>
# the other part flows immediately after the in_thread block (b).<br>
# both parts of the control flow execute at exactly the same time.<br>
 <br>
# (a)<br>
 <br>
# (a)<br>
 <br>
 <br>
 <br>
 <br>
# (b)<br>
# This loop is executed thanks to the thread above</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>use_bpm 120 
  use_synth :dsaw 
  in_thread do    
    play 50       
    use_synth :fm 
    sleep 1       
    play 38       
  end
  play 62         
  sleep 2         
  play 67</code></pre></td>
<td># Set the bpm to be double rate<br>
# Set the current synth to be :dsaw<br>
# Create a new thread<br>
# Play note 50 at time 0<br>
# Switch to fm synth (only affects this thread)<br>
# sleep for 0.5 seconds (as we're double rate)<br>
# Play note 38 at time 0.5<br>
 <br>
# Play note 62 at time 0 (with dsaw synth)<br>
# sleep 1s<br>
# Play note 67 at time 1s (also with dsaw synth)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>in_thread(name: :foo) do
    loop do
      sample :drum_bass_hard
      sleep 1
    end
  end
  in_thread(name: :foo) do
    loop do               
      sample :elec_chime  
      sleep 0.5
    end
  end</code></pre></td>
<td># Here we've created a named thread<br>
 <br>
 <br>
 <br>
 <br>
 <br>
# This thread isn't created as the name is<br>
# the same as the previous thread which is<br>
# still executing.</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>define :foo do 
    play 50      
    sleep 1      
  end
  in_thread(name: :main) do 
    loop do                 
      foo                   
    end
  end</code></pre></td>
<td># Named threads work well with functions for live coding:<br>
# Create a function foo<br>
# which does something simple<br>
# and sleeps for some time<br>
 <br>
# Create a named thread<br>
# which loops forever<br>
# calling our function<br>
 <br>
 <br>
# We are now free to modify the contents of :foo and re-run the entire buffer.<br>
# We'll hear the effect immediately without having to stop and re-start the code.<br>
# This is because our fn has been redefined, (which our thread will pick up) and<br>
# due to the thread being named, the second re-run will not create a new similarly<br>
# named thread. This is a nice pattern for live coding and is the basis of live_loop.</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>in_thread delay: 1 do
    sample :ambi_lunar_land
  end
  play 80</code></pre></td>
<td>#Delaying the start of a thread<br>
 <br>
# this sample is not triggered at time 0 but after 1 beat<br>
 <br>
# Note 80 is played at time 0</td>
</tr>
</table>
