# Sets sched ahead time to 0 within the block for the current thread

## Uso

```ruby
with_real_time
```

Sets sched ahead time to 0 within the block for the current thread. Shorthand for `with_sched_ahead_time 0`.

See `with_sched_ahead_time` for a version of this function which allows you to set the schedule ahead time to any arbitrary value. Note, `with_real_time` will override any value set with `set_sched_ahead_time!` for the current thread.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_real_time 1</code></pre></td>
<td># Code will now run approximately 1 second ahead of audio.</td>
</tr>
</table>
