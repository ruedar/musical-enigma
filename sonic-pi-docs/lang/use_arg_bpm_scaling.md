# Enable and disable BPM scaling

## Uso

```ruby
use_arg_bpm_scaling  bool (boolean)
```

Turn synth argument bpm scaling on or off for the current thread. This is on by default. Note, using `rt` for args will result in incorrect times when used after turning arg bpm scaling off.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
play 50, release: 2
sleep 2            
use_arg_bpm_scaling false
play 50, release: 2
sleep 2</code></pre></td>
<td># release is actually 1 due to bpm scaling<br>
# actually sleeps for 1 second<br>
 <br>
# release is now 2<br>
# still sleeps for 1 second</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
play 50, release: rt(2)
sleep rt(2)            
use_arg_bpm_scaling false
play 50, release: rt(2)
sleep rt(2)</code></pre></td>
<td># Interaction with rt<br>
 <br>
# release is 2 seconds<br>
# sleeps for 2 seconds<br>
 <br>
# ** Warning: release is NOT 2 seconds! **<br>
# still sleeps for 2 seconds</td>
</tr>
</table>
