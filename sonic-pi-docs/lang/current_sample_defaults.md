# Get current sample defaults

## Uso

```ruby
current_sample_defaults
```

Returns the current sample defaults. This is a map of synth arg names to either values or functions.

This can be set via the fns `use_sample_defaults`, `with_sample_defaults`, `use_merged_sample_defaults` and `with_merged_sample_defaults`.

## Introduced in v2.5

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_sample_defaults amp: 0.5, cutoff: 80
sample :loop_amen
puts current_sample_defaults</code></pre></td>
<td># Plays amen break with amp 0.5 and cutoff 80<br>
#=&gt; Prints {amp: 0.5, cutoff: 80}</td>
</tr>
</table>
