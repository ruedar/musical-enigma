# Initialise or return named buffer

## Uso

```ruby
buffer  symbol (name), number (duration)
```

Initialise or return a named buffer with a specific duration (defaults to 8 beats). Useful for working with the `:record` FX. If the buffer is requested with a different duration, then a new buffer will be initialised and the old one recycled.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>buffer(:foo)
b = buffer(:foo)
puts b.duration</code></pre></td>
<td># load a 8s buffer and name it :foo<br>
# return cached buffer and bind it to b<br>
#=&gt; 8.0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>buffer(:foo, 16)</code></pre></td>
<td># load a 16s buffer and name it :foo</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
buffer(:foo, 16)</code></pre></td>
<td># load a 8s buffer and name it :foo<br>
# (this isn't 16s as the BPM has been<br>
# doubled from the default of 60)</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>buffer(:foo)    
buffer(:foo, 8) 
buffer(:foo, 10)
buffer(:foo, 10)
buffer(:foo)    
buffer(:foo)</code></pre></td>
<td># init a 8s buffer and name it :foo<br>
# return cached 8s buffer (has the same duration)<br>
# init a new 10s buffer and name it :foo<br>
# return cached 10s buffer<br>
# init a 8s buffer and name it :foo<br>
# return cached 8s buffer (has the same duration)</td>
</tr>
</table>
