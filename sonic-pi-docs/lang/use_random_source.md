# Change how random numbers are chosen

## Uso

```ruby
use_random_source  noise_type (symbol)
```

Sets the random number source to be one of `:white`, `:pink`, `:light_pink`, `:dark_pink` or `:perlin`.

`:white` is totally random - between 0 and 1, you can expect an even spread of values around 0.1, 0.2, 0.3 etc. This means that jumping around within the range (including large jumps) is expected.

`:pink` is more likely to produce values in the middle of the range and less likely to produce values at the extremes. Between 0 and 1 you expect to see a concentration of values around 0.5. This can make random melodies a little bit more smooth.

`:perlin` is a special kind of noise which produces gradients, a bit like a mountain landscape. Large jumps are much less likely and you will tend to see lots of smooth motion going either up or down

`:light_pink` is halfway between white noise and pink noise - more random and jumpy

`:dark_pink` is halfway between pink noise and brown noise - less jumpy with smoother slopes

You can see the ‘buckets’ that the numbers between 0 and 1 fall into with the following code:

```ruby
rand_type :white
    puts 10000.times.collect { rand.round(1) }.tally.sort
    rand_type :pink
    puts 10000.times.collect { rand.round(1) }.tally.sort
    rand_type :perlin
    puts 10000.times.collect { rand.round(1) }.tally.sort
```

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
