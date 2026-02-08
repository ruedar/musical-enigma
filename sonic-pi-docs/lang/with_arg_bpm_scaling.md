# Block-level enable and disable BPM scaling

## Uso

```ruby
with_arg_bpm_scaling
```

Turn synth argument bpm scaling on or off for the supplied block. Note, using `rt` for args will result in incorrect times when used within this block.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
play 50, release: 2
with_arg_bpm_scaling false do
  play 50, release: 2
end</code></pre></td>
<td># release is actually 1 due to bpm scaling<br>
 <br>
# release is now 2</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
play 50, release: rt(2)  
sleep rt(2)              
with_arg_bpm_scaling false do
  play 50, release: rt(2)
  sleep rt(2)            
end</code></pre></td>
<td># Interaction with rt<br>
 <br>
# release is 2 seconds<br>
# sleeps for 2 seconds<br>
 <br>
# ** Warning: release is NOT 2 seconds! **<br>
# still sleeps for 2 seconds</td>
</tr>
</table>
