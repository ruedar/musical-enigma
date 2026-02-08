# Determine if block contains sleep time

## Uso

```ruby
block_slept?
```

Given a block, runs it and returns whether or not the block contained sleeps or syncs

## Introduced in v2.9

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>slept = block_slept? do
  play 50
  sleep 1
  play 62
  sleep 2
end
puts slept</code></pre></td>
<td>#=&gt; Returns true as there were sleeps in the block</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>in_thread do
  sleep 1
  cue :foo 
end
slept = block_slept? do
  sync :foo 
  play 62
end
puts slept</code></pre></td>
<td># trigger a cue on a different thread<br>
 <br>
 <br>
# wait for the cue before playing the note<br>
 <br>
 <br>
#=&gt; Returns true as the block contained a sync.</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>slept = block_slept? do
  play 50
  play 62
end
puts slept</code></pre></td>
<td>#=&gt; Returns false as there were no sleeps in the block</td>
</tr>
</table>
