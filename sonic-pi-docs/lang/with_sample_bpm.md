# Block-scoped sample-duration-based bpm modification

## Uso

```ruby
with_sample_bpm  string_or_number (sample_name_or_duration)
```

Block-scoped modification of bpm so that sleeping for 1 will sleep for the duration of the sample.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>live_loop :dnb do
  with_sample_bpm :loop_amen do
    sample :bass_dnb_f
    sample :loop_amen
    sleep 1                    
  end
end</code></pre></td>
<td>#Set bpm based on :loop_amen duration<br>
 <br>
 <br>
#`sleep`ing for 1 sleeps for duration of :loop_amen</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>live_loop :dnb do
  with_sample_bpm :loop_amen, num_beats: 4 do
                                             
                                             
    sample :bass_dnb_f
    sample :loop_amen
    sleep 4                    
                               
                               
  end
end</code></pre></td>
<td># Set bpm based on :loop_amen duration<br>
# but also specify that the sample duration<br>
# is actually 4 beats long.<br>
 <br>
 <br>
#`sleep`ing for 4 sleeps for duration of :loop_amen<br>
# as we specified that the sample consisted of<br>
# 4 beats</td>
</tr>
</table>
