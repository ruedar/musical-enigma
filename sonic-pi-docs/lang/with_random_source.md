# Specify random distribution for code block

## Uso

```ruby
with_random_source  noise_type (symbol)
```

Resets the random number generator to the specified noise type for the specified code block. All generated random numbers and randomisation functions such as `shuffle` and `choose` within the code block will use this new generator. Once the code block has completed, the original generator is restored and the code block generator is discarded. Use this to change the sequence of random numbers in your piece in a way that can be reproduced. Especially useful if combined with iteration. See examples.

## Introduced in v3.3

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_random_source :white
  rand_reset
  puts rand
  puts rand
  puts rand
  rand_reset
  use_random_source :pink
  puts rand
  puts rand
  rand_reset
  use_random_source :perlin
  puts rand
  puts rand
  with_random_source :white do
    puts rand
  end
  puts rand</code></pre></td>
<td># use white noise as the distribution (default)<br>
# reset random seed<br>
# =&gt; 0.75006103515625<br>
# =&gt; 0.733917236328125<br>
# =&gt; 0.464202880859375<br>
# reset it again<br>
# use pink noise as the distribution<br>
# =&gt; 0.47808837890625<br>
# =&gt; 0.56011962890625<br>
# reset it<br>
# use perlin noise as the distribution<br>
# =&gt; 0.546478271484375<br>
# =&gt; 0.573150634765625<br>
# use white noise just for this block<br>
# =&gt; 0.464202880859375<br>
 <br>
# =&gt; 0.597015380859375<br>
# notice how the last generator (perlin) is restored</td>
</tr>
</table>
