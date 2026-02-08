# Sync with other threads

## Uso

```ruby
sync  cue_id (symbol)
```

Pause/block the current thread until a `cue` heartbeat with a matching `cue_id` is received. When a matching `cue` message is received, unblock the current thread, and continue execution with the virtual time set to match the thread that sent the `cue` heartbeat. The current thread is therefore synced to the `cue` thread. If multiple cue ids are passed as arguments, it will `sync` on the first matching `cue_id`. The BPM of the cueing thread can optionally be inherited by using the bpm_sync: opt.

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
<td># this parks the current thread waiting for a foo sync message to be received.<br>
 <br>
 <br>
 <br>
# We send a sync message from the main thread.<br>
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
# waiting for :tick sync messages<br>
# after which play the drum kick sample</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>sync :foo, :bar</code></pre></td>
<td># Wait for either a :foo or :bar cue</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
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
# waiting for :foo sync messages<br>
# after which play the elec beep sample<br>
 <br>
 <br>
 <br>
# In the main thread, just loop<br>
# waiting for :bar sync messages<br>
# after which play the elec flip sample<br>
 <br>
 <br>
 <br>
# In the main thread, just loop<br>
# waiting for :baz sync messages<br>
# after which play the elec blup sample</td>
</tr>
</table>
