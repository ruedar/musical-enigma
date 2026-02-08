# Block-level set sched ahead time for the current thread

## Uso

```ruby
with_sched_ahead_time  time (number)
```

Specify how many seconds ahead of time the synths should be triggered for the block. See `use_sched_ahead_time` for further information.

See `set_sched_ahead_time!` for a global version of this function. Note, `with_sched_ahead_time` will override any value set with `set_sched_ahead_time!` for the given block within the current thread.

See `with_real_time` for a simple way of setting the schedule ahead time to 0.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>with_sched_ahead_time 1 do
  play 70 
end
play 70</code></pre></td>
<td># Sound will happen with a latency of 1<br>
 <br>
# Sound will happen with the default latency (0.5s)</td>
</tr>
</table>
