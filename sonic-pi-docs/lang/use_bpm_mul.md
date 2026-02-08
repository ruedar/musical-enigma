# Set new tempo as a multiple of current tempo

## Uso

```ruby
use_bpm_mul  mul (number)
```

Sets the tempo in bpm (beats per minute) as a multiplication of the current tempo. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`

## Introduced in v2.3

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 60  
  play 50
  sleep 1     
  play 62
  sleep 2     
  use_bpm_mul 0.5
  play 50
  sleep 1          
  play 62</code></pre></td>
<td># Set the BPM to 60<br>
 <br>
# Sleeps for 1 seconds<br>
 <br>
# Sleeps for 2 seconds<br>
# BPM is now (60 * 0.5) == 30<br>
 <br>
# Sleeps for 2 seconds</td>
</tr>
</table>
