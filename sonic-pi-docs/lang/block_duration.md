# Return block duration

## Uso

```ruby
block_duration
```

Given a block, runs it and returns the amount of time that has passed. This time is in seconds and is not scaled to the current BPM. Any threads spawned in the block are not accounted for.

## Introduced in v2.9

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>dur = block_duration do
  play 50
  sleep 1
  play 62
  sleep 2
end
puts dur</code></pre></td>
<td>#=&gt; Returns 3 as 3 seconds have passed within the block</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_bpm 120
dur = block_duration do
  play 50
  sleep 1
  play 62
  sleep 2
end
puts dur</code></pre></td>
<td>#=&gt; Returns 1.5 as 1.5 seconds have passed within the block<br>
#   (due to the BPM being 120)</td>
</tr>
</table>
