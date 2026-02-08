# Set sched ahead time to 0 for the current thread

## Uso

```ruby
use_real_time
```

Set sched ahead time to 0 for the current thread. Shorthand for `use_sched_ahead_time 0`.

See `use_sched_ahead_time` for a version of this function which allows you to set the schedule ahead time to any arbitrary value. Note, `use_real_time` will override any value set with `set_sched_ahead_time!` for the current thread.

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
