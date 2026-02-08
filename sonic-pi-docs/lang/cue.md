# Cue other threads

## Uso

```ruby
cue  cue_id (symbol)
```

Send a heartbeat synchronisation message containing the (virtual) timestamp of the current thread. Useful for syncing up external threads via the `sync` fn. Any opts which are passed are given to the thread which syncs on the `cue_id`. The values of the opts must be immutable. Currently numbers, symbols, booleans, nil and frozen strings, or vectors/rings/frozen arrays/maps of immutable values are supported.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>in_thread do
    sync :foo
    sample :ambi_lunar_land
  end
  sleep 5
  cue :foo</code></pre></td>
<td># this parks the current thread waiting for a foo cue message to be received.<br>
 <br>
 <br>
 <br>
# We send a cue message from the main thread.<br>
# This then unblocks the thread above and we then hear the sample</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>in_thread do  
    loop do     
      cue :tick 
      sleep 0.5 
    end
  end
 
  loop do                   
    sync :tick              
    sample :drum_heavy_kick 
  end</code></pre></td>
<td># Start a metronome thread<br>
# Loop forever:<br>
# sending tick heartbeat messages<br>
# and sleeping for 0.5 beats between ticks<br>
 <br>
 <br>
# We can now play sounds using the metronome.<br>
# In the main thread, just loop<br>
# waiting for :tick cue messages<br>
# after which play the drum kick sample</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>in_thread do  
    loop do     
      cue [:foo, :bar, :baz].choose
      sleep 0.5 
    end
  end
 
  in_thread do
    loop do             
      sync :foo         
      sample :elec_beep 
    end
  end
  in_thread do
    loop do             
      sync :bar         
      sample :elec_flip 
    end
  end
  in_thread do
    loop do             
      sync :baz         
      sample :elec_blup 
    end
  end</code></pre></td>
<td># Start a metronome thread<br>
# Loop forever:<br>
# sending one of three tick heartbeat messages randomly<br>
# and sleeping for 0.5 beats between ticks<br>
 <br>
 <br>
# We can now play sounds using the metronome:<br>
 <br>
# In the main thread, just loop<br>
# waiting for :foo cue messages<br>
# after which play the elec beep sample<br>
 <br>
 <br>
 <br>
# In the main thread, just loop<br>
# waiting for :bar cue messages<br>
# after which play the elec flip sample<br>
 <br>
 <br>
 <br>
# In the main thread, just loop<br>
# waiting for :baz cue messages<br>
# after which play the elec blup sample</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>in_thread do
    loop do
      cue :tick, foo: 64 
      sleep 0.5
    end
  end
 
  loop do
    values = sync :tick
    play values[:foo]   
  end</code></pre></td>
<td># sending tick heartbeat messages with a value :foo<br>
 <br>
 <br>
 <br>
# The value for :foo can now be used in synced threads<br>
 <br>
 <br>
# play the note value from :foo</td>
</tr>
</table>
