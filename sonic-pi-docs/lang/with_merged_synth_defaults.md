# Block-level merge synth defaults

## Uso

```ruby
with_merged_synth_defaults
```

Specify synth arg values to be used by any following call to play within the specified `do` / `end` block. Merges the specified values with any previous synth defaults, rather than replacing them. After the `do` / `end` block has completed, previous defaults (if any) are restored.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>with_merged_synth_defaults amp: 0.5, pan: 1 do
  play 50
end</code></pre></td>
<td># =&gt; plays note 50 with amp 0.5 and pan 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play 50
with_merged_synth_defaults amp: 0.5 do
  play 50
  with_merged_synth_defaults pan: -1 do
    with_merged_synth_defaults amp: 0.7 do
      play 50
    end
  end
  play 50
end</code></pre></td>
<td>#=&gt; plays note 50<br>
 <br>
#=&gt; plays note 50 with amp 0.5<br>
 <br>
 <br>
#=&gt; plays note 50 with amp 0.7 and pan -1<br>
 <br>
 <br>
#=&gt; plays note 50 with amp 0.5</td>
</tr>
</table>
