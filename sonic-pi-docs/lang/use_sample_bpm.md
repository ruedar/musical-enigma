# Sample-duration-based bpm modification

## Uso

```ruby
use_sample_bpm  string_or_number (sample_name_or_duration)
```

Modify bpm so that sleeping for 1 will sleep for the duration of the sample.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_sample_bpm :loop_amen 
live_loop :dnb do
  sample :bass_dnb_f
  sample :loop_amen
  sleep 1                 
end</code></pre></td>
<td>#Set bpm based on :loop_amen duration<br>
 <br>
 <br>
 <br>
#`sleep`ing for 1 actually sleeps for duration of :loop_amen</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_sample_bpm :loop_amen, num_beats: 4 
                                        
                                        
live_loop :dnb do
  sample :bass_dnb_f
  sample :loop_amen
  sleep 4                 
                          
                          
end</code></pre></td>
<td># Set bpm based on :loop_amen duration<br>
# but also specify that the sample duration<br>
# is actually 4 beats long.<br>
 <br>
 <br>
 <br>
#`sleep`ing for 4 actually sleeps for duration of :loop_amen<br>
# as we specified that the sample consisted of<br>
# 4 beats</td>
</tr>
</table>
