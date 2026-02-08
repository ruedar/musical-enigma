# Get current random seed

## Uso

```ruby
current_random_seed
```

Returns the current random seed.

This can be set via the fns `use_random_seed` and `with_random_seed`. It is incremented every time you use the random number generator via fns such as `choose` and `rand`.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts current_random_seed</code></pre></td>
<td># Print out the current random seed</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts rand              
puts rand              
a = current_random_seed
puts rand              
puts rand              
use_random_seed a      
                       
puts rand              
puts rand</code></pre></td>
<td># Resetting the seed back to a known place<br>
#=&gt;  0.75006103515625<br>
#=&gt;  0.733917236328125<br>
# Grab the current seed<br>
#=&gt; 0.464202880859375<br>
#=&gt; 0.24249267578125<br>
# Restore the seed<br>
# we'll now get the same random values:<br>
#=&gt; 0.464202880859375<br>
#=&gt; 0.24249267578125</td>
</tr>
</table>
