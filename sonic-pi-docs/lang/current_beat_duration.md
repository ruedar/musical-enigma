# Duration of current beat

## Uso

```ruby
current_beat_duration
```

Get the duration of the current beat in seconds. This is the actual length of time which will elapse with `sleep 1`.

Affected by calls to `use_bpm`, `with_bpm`, `use_sample_bpm` and `with_sample_bpm`.

## Introduced in v2.6

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 60
  puts current_beat_duration
  use_bpm 120
  puts current_beat_duration</code></pre></td>
<td>#=&gt; 1<br>
 <br>
#=&gt; 0.5</td>
</tr>
</table>
