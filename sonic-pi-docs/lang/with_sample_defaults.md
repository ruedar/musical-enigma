# Block-level use new sample defaults

## Uso

```ruby
with_sample_defaults
```

Specify new default values to be used by all subsequent calls to `sample` within the `do` / `end` block. After the `do` / `end` block has completed, the previous sampled defaults (if any) are restored. For the contents of the block, will remove and override any previous defaults.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen
use_sample_defaults amp: 0.5, cutoff: 70
sample :loop_amen
with_sample_defaults cutoff: 90 do
  sample :loop_amen 
end
sample :loop_amen</code></pre></td>
<td># plays amen break with default arguments<br>
 <br>
# plays amen break with an amp of 0.5, cutoff of 70 and defaults for rest of args<br>
 <br>
# plays amen break with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5<br>
 <br>
# plays amen break with a cutoff of 70 and amp is 0.5 again as the previous defaults are restored.</td>
</tr>
</table>
