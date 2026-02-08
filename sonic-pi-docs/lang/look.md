# Obtain value of a tick

## Uso

```ruby
look
```

Read and return value of default tick. If a `key` is specified, read the value of that specific tick. Ticks are `in_thread` and `live_loop` local, so the tick read will be the tick of the current thread calling `look`.

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts look
  puts look
  puts look</code></pre></td>
<td>#=&gt; 0<br>
#=&gt; 0<br>
#=&gt; 0 # look doesn't advance the tick, it just returns the current value</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts look
  tick
  puts look
  tick
  puts look
  puts look
  tick
  puts look</code></pre></td>
<td>#=&gt; 0 # A look is always 0 before the first tick<br>
# advance the tick<br>
#=&gt; 0 # Note: a look is still 0 after the first tick.<br>
 <br>
#=&gt; 1<br>
#=&gt; 1 # making multiple calls to look doesn't affect tick value<br>
 <br>
#=&gt; 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>tick(:foo)
  tick(:foo)
  puts look(:foo)
  puts look
  puts look(:bar)</code></pre></td>
<td>#=&gt; 1 (keyed look :foo has been advanced)<br>
#=&gt; 0 (default look hasn't been advanced)<br>
#=&gt; 0 (other keyed looks haven't been advanced either)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
    tick                                     
    use_synth :beep
    play (scale :e3, :minor_pentatonic).look 
    sleep 0.5
    use_synth :square
    play (ring :e1, :e2, :e3).look, release: 0.25
    sleep 0.25
  end</code></pre></td>
<td># You can call look on lists and rings<br>
 <br>
# advance the default tick<br>
 <br>
# look into the default tick to play all notes in sequence<br>
 <br>
 <br>
# use the same look on another ring</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>puts look(0)    
puts look(4)    
puts look(-4)   
puts look(20.3)</code></pre></td>
<td># Returns numbers unchanged if single argument<br>
#=&gt; 0<br>
#=&gt; 4<br>
#=&gt; -4<br>
#=&gt; 20.3</td>
</tr>
</table>
