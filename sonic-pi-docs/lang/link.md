# Use Ableton Link network metronome with automatic phase syncing

## Uso

```ruby
link  quantum (number), phase (number)
```

By default link waits for the start of the next bar of the shared network metronome link. You can choose how many beats there are in a bar by setting the quantum option and/or which beat to wait for by setting the phase option.

By default, the phase to sync on is 0 and the quantum (max number of beats) is 4.

Also switches BPM to :link mode so there is no explicit need to call use_bpm :link. The time and beat set to match the network Link metronome.

This function will block the current thread until the next matching phase as if sleep had been called with the exact sleep time.

If the quantum is 4 (the default) this suggests there are 4 beats in each bar. If the phase is set to 0 (also the default) this means that calling link will sleep until the very start of the next bar before continuing.

This can be used to sync multiple instances of Sonic Pi running on different computers connected to the same network (via wifi or ethernet). It can also be used to share and coordinate time with other apps and devices. For a full list of link-compatible apps and devices see: https://www.ableton.com/en/link/products/

For other related link functions see link_sync, use_bpm :link, set_link_bpm!

## Introduced in v4.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
link
puts current_bpm</code></pre></td>
<td># bpm is at 120<br>
# wait for the start of the next bar before continuing<br>
# (where each bar has 4 beats)<br>
#=&gt; :link (not 120)</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>link 8</code></pre></td>
<td># wait for the start of the next bar<br>
# (where each bar has 8 beats)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>link 7, 2</code></pre></td>
<td># wait for the 2nd beat of the next bar<br>
# (where each bar has 7 beats)</td>
</tr>
</table>
