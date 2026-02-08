# Squash and repeat time

## Uso

```ruby
density  d (density)
```

Runs the block `d` times with the bpm for the block also multiplied by `d`. Great for repeating sections a number of times faster yet keeping within a fixed time. If `d` is less than 1, then time will be stretched accordingly and the block will take longer to complete.

## Introduced in v2.3

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 60  
  density 2 do      
                    
    sample :bd_haus
    sleep 0.5       
  end</code></pre></td>
<td># Set the BPM to 60<br>
# BPM for block is now 120<br>
# block is called 2.times<br>
# sample is played twice<br>
# sleep is 0.25s</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>density 2 do |idx|
    puts idx        
    sleep 0.5       
  end</code></pre></td>
<td># You may also pass a param to the block similar to n.times<br>
# prints out 0, 1<br>
# sleep is 0.25s</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>density 0.5 do         
                         
                         
    play 80, release: 1  
    sleep 0.5            
  end</code></pre></td>
<td># Specifying a density val of &lt; 1 will stretch out time<br>
# A density of 0.5 will double the length of the block's<br>
# execution time.<br>
# plays note 80 with 2s release<br>
# sleep is 1s</td>
</tr>
</table>
