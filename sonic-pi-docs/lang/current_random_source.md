# Get current random source

## Uso

```ruby
current_random_source
```

Returns the source of the current random number generator (what kind of noise is generating the random numbers).

This can be set via the fns use_random_source and with_random_source. Each source will provide a different pattern of random numbers.

## Introduced in v4.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts current_random_source</code></pre></td>
<td># Print out the current random source</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_random_source :white
puts rand
puts rand
a = current_random_source
use_random_source :perlin
puts rand
puts rand
use_random_source a
puts rand
puts rand</code></pre></td>
<td># Use white noise as the distribution (default)<br>
#=&gt; 0.75006103515625<br>
#=&gt; 0.733917236328125<br>
# Grab the current random number source (:white)<br>
# Use perlin noise as the distribution<br>
#=&gt; 0.58526611328125<br>
#=&gt; 0.597015380859375<br>
# Restore the previous random number source (:white)<br>
# The numbers will again be generated from a white noise distribution<br>
#=&gt; 0.10821533203125<br>
#=&gt; 0.54010009765625</td>
</tr>
</table>
