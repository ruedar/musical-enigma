# Set random seed generator to known seed

## Uso

```ruby
use_random_seed  seed (number)
```

Resets the random number generator to the specified seed. All subsequently generated random numbers and randomisation functions such as `shuffle` and `choose` will use this new generator and the current generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_random_seed 1
  puts rand
  use_random_seed 1
  puts rand</code></pre></td>
<td># Basic usage<br>
# reset random seed to 1<br>
# =&gt; 0.417022004702574<br>
# reset random seed back to 1<br>
#=&gt; 0.417022004702574</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>notes = (scale :eb3, :minor_pentatonic) 
                                          
  with_fx :reverb do
    live_loop :repeating_melody do        
      use_random_seed 300                 
                                          
                                          
                                          
                                          
      8.times do                          
                                          
                                          
        play notes.choose, release: 0.1   
                                          
                                          
                                          
        sleep 0.125
      end
    end
  end</code></pre></td>
<td># Generating melodies<br>
# Create a set of notes to choose from.<br>
# Scales work well for this<br>
 <br>
# Create a live loop<br>
# Set the random seed to a known value every<br>
# time around the loop. This seed is the key<br>
# to our melody. Try changing the number to<br>
# something else. Different numbers produce<br>
# different melodies<br>
# Now iterate a number of times. The size of<br>
# the iteration will be the length of the<br>
# repeating melody.<br>
# 'Randomly' choose a note from our ring of<br>
# notes. See how this isn't actually random<br>
# but uses a reproducible method! These notes<br>
# are therefore repeated over and over...</td>
</tr>
</table>
