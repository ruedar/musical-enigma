# Merge synth defaults

## Uso

```ruby
use_merged_synth_defaults
```

Specify synth arg values to be used by any following call to play. Merges the specified values with any previous defaults, rather than replacing them.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_merged_synth_defaults amp: 0.5
play 50
use_merged_synth_defaults cutoff: 80
play 50
use_merged_synth_defaults amp: 0.7
play 50</code></pre></td>
<td>#=&gt; Plays note 50<br>
 <br>
#=&gt; Plays note 50 with amp 0.5<br>
 <br>
#=&gt; Plays note 50 with amp 0.5 and cutoff 80<br>
 <br>
#=&gt; Plays note 50 with amp 0.7 and cutoff 80</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_synth_defaults amp: 0.5, cutoff: 80, pan: -1
use_merged_synth_defaults amp: 0.7
play 50</code></pre></td>
<td>#=&gt; Plays note 50 with amp 0.7, cutoff 80 and pan -1</td>
</tr>
</table>
