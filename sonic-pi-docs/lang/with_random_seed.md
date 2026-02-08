# Specify random seed for code block

## Uso

```ruby
with_random_seed  seed (number)
```

Resets the random number generator to the specified seed for the specified code block. All generated random numbers and randomisation functions such as `shuffle` and `choose` within the code block will use this new generator. Once the code block has completed, the original generator is restored and the code block generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_random_seed 1
  puts rand
  puts rand 
  use_random_seed 1
  puts rand
  with_random_seed 1 do
    puts rand
    puts rand
  end
  puts rand</code></pre></td>
<td># reset random seed to 1<br>
# =&gt; 0.417022004702574<br>
#=&gt; 0.7203244934421581<br>
# reset it back to 1<br>
# =&gt; 0.417022004702574<br>
# reset seed back to 1 just for this block<br>
# =&gt; 0.417022004702574<br>
#=&gt; 0.7203244934421581<br>
 <br>
# =&gt; 0.7203244934421581<br>
# notice how the original generator is restored</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>notes = (scale :eb3, :minor_pentatonic, num_octaves: 2) 
                                          
  with_fx :reverb do
    live_loop :repeating_melody do        
      with_random_seed 300 do             
                                          
                                          
                                          
                                          
        8.times do                        
                                          
                                          
          play notes.choose, release: 0.1 
                                          
                                          
                                          
          sleep 0.125
        end
      end
      play notes.choose, amp: 1.5, release: 0.5
                                               
                                               
                                               
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
# are therefore repeated over and over...<br>
 <br>
 <br>
 <br>
# Note that this line is outside of<br>
# the with_random_seed block and therefore<br>
# the randomisation never gets reset and this<br>
# part of the melody never repeats.</td>
</tr>
</table>
