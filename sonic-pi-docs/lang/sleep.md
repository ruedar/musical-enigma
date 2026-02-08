# Wait for beat duration

## Uso

```ruby
sleep  beats (number)
```

Wait for a number of beats before triggering the next command. Beats are converted to seconds by scaling to the current bpm setting.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50 
  play 55
  play 62
  sleep 1 
  play 50 
  sleep 0.5
  play 55
  sleep 0.5
  play 62</code></pre></td>
<td># Without calls to sleep, all sounds would happen at once:<br>
# This is actually a chord with all notes played simultaneously<br>
 <br>
 <br>
# Create a gap, to allow a moment's pause for reflection...<br>
# Let's try the chord again, but this time with sleeps:<br>
# With the sleeps, we turn a chord into an arpeggio</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
  play 50
  sleep 1
  play 55
  sleep 1
  play 62
 
  use_bpm 30
  play 50
  sleep 1
  play 55
  sleep 1
  play 62</code></pre></td>
<td># The amount of time sleep pauses for is scaled to match the current bpm. The default bpm is 60. Let's double it:<br>
 <br>
 <br>
# This actually sleeps for 0.5 seconds as we're now at double speed<br>
 <br>
 <br>
 <br>
# Let's go down to half speed:<br>
 <br>
 <br>
# This now sleeps for 2 seconds as we're now at half speed.</td>
</tr>
</table>
