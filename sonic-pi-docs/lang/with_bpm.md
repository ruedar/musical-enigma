# Set the tempo for the code block

## Uso

```ruby
with_bpm  bpm (number)
```

Sets the tempo in bpm (beats per minute) for everything in the given block. Affects all containing calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. See also `use_bpm`

For dance music here’s a rough guide for which BPM to aim for depending on your genre:

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>4.times do
    sample :drum_bass_hard
    sleep 1
  end
  sleep 5
 
 
  with_bpm 120 do 
    4.times do
      sample :drum_bass_hard
      sleep 1
    end
  end
  sleep 5
 
  4.times do
    sample :drum_bass_hard
    sleep 1
  end</code></pre></td>
<td># default tempo is 60 bpm<br>
 <br>
 <br>
# sleeps for 1 second<br>
 <br>
# sleeps for 5 seconds<br>
# with_bpm sets a tempo for everything between do ... end (a block)<br>
# Hear how it gets faster?<br>
# set bpm to be twice as fast<br>
 <br>
 <br>
# now sleeps for 0.5 seconds<br>
 <br>
 <br>
 <br>
# bpm goes back to normal<br>
 <br>
 <br>
# sleeps for 1 second</td>
</tr>
</table>
