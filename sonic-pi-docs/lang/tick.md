# Increment a tick and return value

## Uso

```ruby
tick  key (symbol)
```

Increment the default tick by 1 and return value. Successive calls to `tick` will continue to increment the default tick. If a `key` is specified, increment that specific tick. If an increment `value` is specified, increment key by that value rather than 1. Ticks are `in_thread` and `live_loop` local, so incrementing a tick only affects the current thread’s version of that tick. See `tick_reset` and `tick_set` for directly manipulating the tick vals.

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts tick
  puts tick
  puts tick
  puts tick</code></pre></td>
<td>#=&gt; 0<br>
#=&gt; 1<br>
#=&gt; 2<br>
#=&gt; 3</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts tick(:foo)
  puts tick(:foo)
  puts tick(:foo)
  puts tick(:bar)</code></pre></td>
<td>#=&gt; 0 # named ticks have their own counts<br>
#=&gt; 1<br>
#=&gt; 2<br>
#=&gt; 0 # tick :bar is independent of tick :foo</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts tick            
  puts tick            
  puts tick            
  puts tick(step: 2)   
  puts tick(step: 2)   
  puts tick(step: 10)  
  puts tick</code></pre></td>
<td># You can tick by more than increments of 1<br>
# using the step: opt<br>
#=&gt; 0<br>
#=&gt; 1<br>
#=&gt; 2<br>
#=&gt; 4<br>
#=&gt; 6<br>
#=&gt; 16<br>
#=&gt; 17</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>live_loop :fast_tick do
    puts tick  
    sleep 2    
  end
  live_loop :slow_tick do
    puts tick  
    sleep 4    
               
               
  end</code></pre></td>
<td># Each_live loop has its own separate ticks<br>
 <br>
# the fast_tick live_loop's tick will<br>
# be updated every 2 seconds<br>
 <br>
 <br>
# the slow_tick live_loop's tick is<br>
# totally independent from the fast_tick<br>
# live loop and will be updated every 4<br>
# seconds</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>live_loop :regular_tick do
    puts tick  
    sleep 1    
  end
  live_loop :random_reset_tick do
    if one_in 3
      tick_reset
      puts "reset tick!"
    end
    puts tick  
    sleep 1    
               
  end</code></pre></td>
<td># the regular_tick live_loop's tick will<br>
# be updated every second<br>
 <br>
 <br>
# randomly reset tick<br>
 <br>
 <br>
 <br>
# this live_loop's tick is totally<br>
# independent and the reset only affects<br>
# this tick.</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>live_loop :scale do
    play [:c, :d, :e, :f, :g].tick  
    sleep 1
  end</code></pre></td>
<td># Ticks work directly on lists, and will tick through each element<br>
# However, once they get to the end, they'll return nil<br>
 <br>
# play all notes just once, then rests</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>live_loop :odd_scale do
    tick 
    play [:c, :d, :e, :f, :g, :a].tick  
                                        
    sleep 1
  end</code></pre></td>
<td># Normal ticks interact directly with list ticks<br>
 <br>
# Increment the default tick<br>
# this now play every *other* note just once,<br>
# then rests</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>live_loop :looped_scale do
    play (ring :c, :d, :e, :f, :g).tick  
    sleep 1
  end</code></pre></td>
<td># Ticks work wonderfully with rings<br>
# as the ring ensures the tick wraps<br>
# round internally always returning a<br>
# value<br>
 <br>
# play all notes just once, then repeats</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>live_loop :looped_scale do
    play (scale :e3, :minor_pentatonic).tick  
    sleep 0.25
  end</code></pre></td>
<td># Ticks work wonderfully with scales<br>
# which are also rings<br>
 <br>
# play all notes just once, then repeats</td>
</tr>
</table>
