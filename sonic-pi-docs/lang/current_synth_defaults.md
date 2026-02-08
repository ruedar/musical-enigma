# Get current synth defaults

## Uso

```ruby
current_synth_defaults
```

Returns the current synth defaults. This is a map of synth arg names to values.

This can be set via the fns `use_synth_defaults`, `with_synth_defaults`, `use_merged_synth_defaults` and `with_merged_synth_defaults`.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_synth_defaults amp: 0.5, cutoff: 80
play 50
puts current_synth_defaults</code></pre></td>
<td># Plays note 50 with amp 0.5 and cutoff 80<br>
#=&gt; Prints {amp: 0.5, cutoff: 80}</td>
</tr>
</table>
