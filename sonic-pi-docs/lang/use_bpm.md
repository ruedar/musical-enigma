# Set the tempo

## Uso

```ruby
use_bpm  bpm (number)
```

Sets the tempo in bpm (beats per minute) for everything afterwards. Affects all subsequent calls to `sleep` and all temporal synth arguments which will be scaled to match the new bpm. If you wish to bypass scaling in calls to sleep, see the fn `rt`. Also, if you wish to bypass time scaling in synth args see `use_arg_bpm_scaling`. See also `with_bpm` for a block scoped version of `use_bpm`.

For dance music here’s a rough guide for which BPM to aim for depending on your genre:

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>4.times do
    play 50, attack: 0.5, release: 0.25
    sleep 1
  end
  sleep 2 
 
  use_bpm 120 
  4.times do
    play 62, attack: 0.5, release: 0.25
    sleep 1
  end
  sleep 2
 
  use_bpm 240 
  8.times do
    play 62, attack: 0.5, release: 0.25
    sleep 1
  end</code></pre></td>
<td># default tempo is 60 bpm<br>
 <br>
# attack is 0.5s and release is 0.25s<br>
# sleep for 1 second<br>
 <br>
# sleep for 2 seconds<br>
# Let's make it go faster...<br>
# double the bpm<br>
 <br>
# attack is scaled to 0.25s and release is now 0.125s<br>
# actually sleeps for 0.5 seconds<br>
 <br>
# sleep for 1 second<br>
# Let's make it go even faster...<br>
#  bpm is 4x original speed!<br>
 <br>
# attack is scaled to 0.125s and release is now 0.0625s<br>
# actually sleeps for 0.25 seconds</td>
</tr>
</table>
