# Inhibit synth triggers if too late

## Uso

```ruby
use_timing_guarantees  bool (true_or_false)
```

If set to true, synths will not trigger if it is too late. If false, some synth triggers may be late.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_timing_guarantees true
sample :loop_amen</code></pre></td>
<td>#=&gt; if time is behind by any margin, this will not trigger</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_timing_guarantees false
sample :loop_amen</code></pre></td>
<td>#=&gt; unless time is too far behind, this will trigger even when late.</td>
</tr>
</table>
