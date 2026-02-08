# Reset main mixer

## Uso

```ruby
reset_mixer!
```

The main mixer is the final mixer that all sound passes through. This fn resets it to its default set - undoing any changes made via set_mixer_control!

## Introduced in v2.9

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_mixer_control! lpf: 70
sample :loop_amen         
sleep 3
reset_mixer!              
sample :loop_amen</code></pre></td>
<td># LPF cutoff value of main mixer is now 70<br>
# :loop_amen sample is played with low cutoff<br>
 <br>
# mixer is now reset to default values<br>
# :loop_amen sample is played with normal cutoff</td>
</tr>
</table>
