# Get current (logically quantized) time

## Uso

```ruby
current_time
```

Returns the current logical time. This is a ‘wall-clock’ time which should typically be pretty similar to Time.now but quantised to a nearby sleep point in the thread. May be quite different to Time.now within a time_warp!

Unlike `Time.now`, Multiple calls to `current_time` with no interleaved calls to `sleep` or `sync` will return the same value.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts current_time</code></pre></td>
<td># 2017-03-19 23:37:57 +0000</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts "A", Time.now.to_f
puts "B", __system_thread_locals.get(:sonic_pi_spider_time).to_f
puts "C", Time.now.to_f
puts "D", __system_thread_locals.get(:sonic_pi_spider_time).to_f
puts "E", __system_thread_locals.get(:sonic_pi_spider_time).to_f</code></pre></td>
<td># The difference between current_time and Time.now<br>
# See that Time.now is continuous and current_time is discrete<br>
#<br>
# {run: 19, time: 0.0}<br>
# ├─ "A" 1489966042.761211<br>
# ├─ "B" 1489966042.760181<br>
# ├─ "C" 1489966042.761235<br>
# ├─ "D" 1489966042.760181<br>
# └─ "E" 1489966042.760181</td>
</tr>
</table>
