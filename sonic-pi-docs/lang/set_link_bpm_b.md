# Set the tempo for the link metronome

## Uso

```ruby
set_link_bpm!  bpm (number)
```

Set the tempo for the link metronome in BPM. This is 'global' in that the BPM of all threads/live_loops in Link BPM mode will be affected.

Note that this will also change the tempo of all link metronomes connected to the local network. This includes other instances of Sonic Pi, Music Production tools like Ableton Live, VJ tools like Resolume, DJ hardware like the MPC and many iPad music apps.

For a full list of link-compatible apps and devices see: https://www.ableton.com/en/link/products/

Also note that the current thread does not have to be in Link BPM mode for this function to affect the Link clock's BPM.

To change the current thread/live_loop to Link BPM mode see: use_bpm :link

## Introduced in v4.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm :link
set_link_bpm! 30

8.times do
  bpm += 10
  set_link_bpm! bpm
  sample :loop_amen, beat_stretch: 2
  sleep 2
end</code></pre></td>
<td># Switch to Link BPM mode<br>
# Change Link BPM to 30<br>
# Gradually increase the Link BPM</td>
</tr>
</table>
