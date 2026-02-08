# Get current sched ahead time

## Uso

```ruby
current_sched_ahead_time
```

Returns the current schedule ahead time.

This can be set via the fn `set_sched_ahead_time!`.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_sched_ahead_time! 0.5
puts current_sched_ahead_time</code></pre></td>
<td># Prints 0.5</td>
</tr>
</table>
