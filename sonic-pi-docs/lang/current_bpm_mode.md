# Get current tempo mode

## Uso

```ruby
current_bpm_mode
```

Returns the current tempo mode - either a bpm value or :link.

To know the current BPM value when this thread is in :link mode see current_bpm.

This can be set via the fns use_bpm, with_bpm, use_sample_bpm and with_sample_bpm.

## Introduced in v4.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 60
  puts current_bpm_mode
  use_bpm 70
  puts current_bpm_mode
  use_bpm :link
  puts current_bpm_mode</code></pre></td>
<td>#=&gt; 60<br>
#=&gt; 70<br>
#=&gt; :link</td>
</tr>
</table>
