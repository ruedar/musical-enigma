# Shift time forwards or backwards for the given block

## Uso

```ruby
time_warp  delta_time (number)
```

The code within the given block is executed with the specified delta time shift specified in beats. For example, if the delta value is 0.1 then all code within the block is executed with a 0.1 beat delay. Negative values are allowed which means you can move a block of code *backwards in time*. For example a delta value of -0.1 will execute the code in the block 0.1 beats ahead of time. The time before the block started is restored after the execution of the block.

Given a list of times, run the block once after waiting each given time. If passed an optional params list, will pass each param individually to each block call. If size of params list is smaller than the times list, the param values will act as rings (rotate through). If the block is given 1 arg, the times are fed through. If the block is given 2 args, both the times and the params are fed through. A third block arg will receive the index of the time.

Note that the code within the block is executed synchronously with the code before and after, so all thread locals will be modified inline - as is the case for `with_fx`. However, as time is always restored to the value before `time_warp` started, you can use it to schedule events for the future in a similar fashion to a thread (via `at` or `in_thread` ) without having to use an entirely fresh and distinct set of thread locals - see examples.

Also, note that you cannot travel backwards in time beyond the `current_sched_ahead_time`.

If the `time_warp` block is within a `density` block, the delta time is not affected (although all the other times such as sleep and phase durations will be affected) - see example.

`time_warp` is ahead-of-time scheduling within the current thread. See `at` for just-in-time scheduling using multiple isolated threads.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 70           
sleep 1
play 75           
time_warp 0.1 do
                  
  play 80         
  sleep 0.5
  play 80         
end               
                  
                  
                  
play 70</code></pre></td>
<td># shift forwards in time<br>
#=&gt; plays at time 0<br>
 <br>
#=&gt; plays at time 1<br>
 <br>
# time shifts forward by 0.1 beats<br>
#=&gt; plays at 1.1<br>
 <br>
#=&gt; plays at 1.6<br>
# time shifts back by 0.6 beats<br>
# we now honour the original sleep 1 and the<br>
# sleep 0.5 within the time_warp block is<br>
# ignored including the 0.1 shift offset<br>
#=&gt; plays at 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play 70           
sleep 1
play 75           
time_warp -0.1 do
                  
  play 80         
  sleep 0.5
  play 80         
                  
end
                  
                  
                  
play 70</code></pre></td>
<td># shift backwards in time<br>
#=&gt; plays at time 0<br>
 <br>
#=&gt; plays at time 1<br>
 <br>
# time shifts backwards by 0.1 beats<br>
#=&gt; plays at 0.9<br>
 <br>
#=&gt; plays at 1.4<br>
# time shifts forward by 0.1 beats<br>
 <br>
# we now honour the original sleep 1 and the<br>
# sleep 0.5 within the time_warp block is<br>
# ignored, including the -0.1 offset<br>
#=&gt; plays at 1</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts tick         
sleep 1
time_warp 2 do
  puts tick       
end
sleep 0.5
puts tick</code></pre></td>
<td># Ticks count linearly through time_warp<br>
#=&gt; prints 0 (at time 0)<br>
 <br>
 <br>
#=&gt; prints 1 (at time 3)<br>
 <br>
 <br>
#=&gt; prints 2 (at time 1.5)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts tick         
sleep 0.5
puts tick         
time_warp 2 do
  puts tick       
  sleep 0.5
  puts tick       
end
at 3 do           
  puts tick       
  sleep 0.5
  puts tick       
end
sleep 0.5
puts tick</code></pre></td>
<td># Comparing time_warp with at<br>
#=&gt; prints 0 (at time 0)<br>
 <br>
#=&gt; prints 1 (at time 0.5)<br>
 <br>
#=&gt; prints 2 (at time 2.5)<br>
 <br>
#=&gt; prints 3 (at time 3)<br>
 <br>
# the at will reset all thread locals<br>
#=&gt; prints 0 (At time 3.5)<br>
 <br>
#=&gt; prints 1 (At time 4)<br>
 <br>
 <br>
#=&gt; prints 4 (at time 1)</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>density 2 do                       
                                   
  time_warp 0.5 do                 
    with_fx :slicer, phase: 0.5 do 
      play 60
      sleep 1                      
    end
  end
end</code></pre></td>
<td># Time Warp within Density<br>
# Typically this will double the BPM and affect all times<br>
# in addition to looping the internal block twice<br>
# However, this time is *not* affected and will remain 0.5<br>
# This phase duration *is* affected and will be 0.25<br>
 <br>
# This time *will* be affected by the density and be 0.5</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 1, 2, 3] do
  puts "hello"               
end</code></pre></td>
<td># Time Warp with lists of times<br>
 <br>
# Will print "hello" at 0, 1, 2, and 3 seconds<br>
 <br>
# Notice that the run completes before all the<br>
# messages have been delivered. This is because it<br>
# schedules all the messages at once so the program<br>
# can complete immediately. This is unlike at which<br>
# would appear to behave similarly, but would wait<br>
# for all messages to be delivered (on time) before<br>
# allowing the program to complete.</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>time_warp [1, 2, 4] do 
    play 75               
  end</code></pre></td>
<td># plays a note after waiting 1 beat,<br>
# then after 1 more beat,<br>
# then after 2 more beats (4 beats total)</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>time_warp [1, 2, 3], [75, 76, 77] do |n| 
    play n
  end</code></pre></td>
<td># plays 3 different notes</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>time_warp [1, 2, 3],
      [{:amp=&gt;0.5}, {:amp=&gt; 0.8}] do |p|
    sample :drum_cymbal_open, p         
  end</code></pre></td>
<td># alternate soft and loud<br>
# cymbal hits three times</td>
</tr>
<tr>
<th colspan="2"># Example 10</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 1, 2] do |t|
    puts t
  end</code></pre></td>
<td># when no params are given to at, the times are fed through to the block<br>
#=&gt; prints 0, 1, then 2</td>
</tr>
<tr>
<th colspan="2"># Example 11</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 1, 2], [:a, :b] do |t, b| 
    puts [t, b]
  end</code></pre></td>
<td># If you specify the block with 2 args, it will pass through both the time and the param<br>
#=&gt; prints out [0, :a], [1, :b], then [2, :a]</td>
</tr>
<tr>
<th colspan="2"># Example 12</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 0.5, 2] do |t, idx| 
    puts [t, idx]
  end</code></pre></td>
<td># If you specify the block with 2 args, and no param list to at, it will pass through both the time and the index<br>
#=&gt; prints out [0, 0], [0.5, 1], then [2, 2]</td>
</tr>
<tr>
<th colspan="2"># Example 13</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 0.5, 2], [:a, :b] do |t, b, idx| 
    puts [t, b, idx]
  end</code></pre></td>
<td># If you specify the block with 3 args, it will pass through the time, the param and the index<br>
#=&gt; prints out [0, :a, 0], [0.5, :b, 1], then [2, :a, 2]</td>
</tr>
<tr>
<th colspan="2"># Example 14</th>
</tr>
<tr>
<td><pre><code>puts "main: ", rand 
rand_back
time_warp 1 do        
                      
  puts "time_warp:", rand
  puts "time_warp:", rand
  rand_back          
end
sleep 2
puts "main: ", rand</code></pre></td>
<td># time_warp consumes &amp; interferes with the outer random stream<br>
# 0.75006103515625<br>
 <br>
# the random stream inside the at block is the<br>
# same as the one in the outer block<br>
# 0.75006103515625<br>
# 0.733917236328125<br>
# undo last call to rand<br>
 <br>
 <br>
# value is now 0.733917236328125 again</td>
</tr>
<tr>
<th colspan="2"># Example 15</th>
</tr>
<tr>
<td><pre><code>time_warp [0, 2] do
           
  puts tick
  puts tick
end</code></pre></td>
<td># Each block run inherits the same thread locals from the previous one.<br>
# This means things like the thread local counters can flow through<br>
# time warp iterations:<br>
 <br>
# first time round (after 1 beat) prints:<br>
# 0<br>
# 1<br>
 <br>
# second time round (after 2 beats) prints:<br>
# 2<br>
# 3</td>
</tr>
</table>
