# Asynchronous Time. Run a block at the given time(s)

## Uso

```ruby
at  times (list), params (list)
```

Given a list of times, run the block once after waiting each given time. If passed an optional params list, will pass each param individually to each block call. If size of params list is smaller than the times list, the param values will act as rings (rotate through). If the block is given 1 arg, the times are fed through. If the block is given 2 args, both the times and the params are fed through. A third block arg will receive the index of the time.

Note, all code within the block is executed in its own thread. Therefore despite inheriting all thread locals such as the random stream and ticks, modifications will be isolated to the block and will not affect external code.

`at` is just-in-time scheduling using multiple isolated threads. See `time_warp` for ahead-of-time scheduling within the current thread.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>at 4 do
    sample :ambi_choir   
  end</code></pre></td>
<td># play sample after waiting for 4 beats</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>at [1, 2, 4] do 
    play 75          
  end</code></pre></td>
<td># plays a note after waiting 1 beat,<br>
# then after 1 more beat,<br>
# then after 2 more beats (4 beats total)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>at [1, 2, 3], [75, 76, 77] do |n| 
    play n
  end</code></pre></td>
<td># plays 3 different notes</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>at [1, 2, 3],
      [{:amp=&gt;0.5}, {:amp=&gt; 0.8}] do |p|
    sample :drum_cymbal_open, p         
  end</code></pre></td>
<td># alternate soft and loud<br>
# cymbal hits three times</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>at [0, 1, 2] do |t|
    puts t
  end</code></pre></td>
<td># when no params are given to at, the times are fed through to the block<br>
#=&gt; prints 0, 1, then 2</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>at [0, 1, 2], [:a, :b] do |t, b| 
    puts [t, b]
  end</code></pre></td>
<td>#If you specify the block with 2 args, it will pass through both the time and the param<br>
#=&gt; prints out [0, :a], [1, :b], then [2, :a]</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>at [0, 0.5, 2] do |t, idx| 
    puts [t, idx]
  end</code></pre></td>
<td>#If you specify the block with 2 args, and no param list to at, it will pass through both the time and the index<br>
#=&gt; prints out [0, 0], [0.5, 1], then [2, 2]</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>at [0, 0.5, 2], [:a, :b] do |t, b, idx| 
    puts [t, b, idx]
  end</code></pre></td>
<td>#If you specify the block with 3 args, it will pass through the time, the param and the index<br>
#=&gt; prints out [0, :a, 0], [0.5, :b, 1], then [2, :a, 2]</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>puts "main: ", rand 
rand_back
at 1 do        
               
  puts "at:", rand
  puts "at:", rand
end
sleep 2
puts "main: ", rand</code></pre></td>
<td># at does not consume &amp; interfere with the outer random stream<br>
# 0.75006103515625<br>
 <br>
# the random stream inside the at block is separate and<br>
# isolated from the outer stream.<br>
# 0.9287109375<br>
# 0.1043701171875<br>
 <br>
 <br>
# value is still 0.75006103515625</td>
</tr>
<tr>
<th colspan="2"># Example 10</th>
</tr>
<tr>
<td><pre><code>at [1, 2] do
           
  puts rand
  puts rand
end</code></pre></td>
<td># Each block run within at has its own isolated random stream:<br>
 <br>
# first time round (after 1 beat) prints:<br>
# 0.9287109375<br>
# 0.1043701171875<br>
 <br>
# second time round (after 2 beats) prints:<br>
# 0.1043701171875<br>
# 0.764617919921875</td>
</tr>
</table>
