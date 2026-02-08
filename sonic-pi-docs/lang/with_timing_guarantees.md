# Block-scoped inhibition of synth triggers if too late

## Uso

```ruby
with_timing_guarantees  bool (true_or_false)
```

For the given block, if set to true, synths will not trigger if it is too late. If false, some synth triggers may be late. After the block has completed, the previous value is restored.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>with_timing_guarantees true do
  sample :loop_amen 
end</code></pre></td>
<td>#=&gt; if time is behind by any margin, this will not trigger</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>with_timing_guarantees false do
  sample :loop_amen 
end</code></pre></td>
<td>#=&gt; unless time is too far behind, this will trigger even when late.</td>
</tr>
</table>
