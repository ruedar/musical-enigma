# Return information about the internal SuperCollider sound server

## Uso

```ruby
scsynth_info
```

Create a map of information about the running audio synthesiser SuperCollider.

## Introduced in v2.11

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts scsynth_info</code></pre></td>
<td>#=&gt;  (map sample_rate: 44100.0,<br>
#         sample_dur: 2.2675736545352265e-05,<br>
#         radians_per_sample: 0.00014247585204429924,<br>
#         control_rate: 689.0625,<br>
#         control_dur: 0.001451247138902545,<br>
#         subsample_offset: 0.0,<br>
#         num_output_busses: 16.0,<br>
#         num_input_busses: 16.0,<br>
#         num_audio_busses: 1024.0,<br>
#         num_control_busses: 4096.0,<br>
#         num_buffers: 4096.0)</td>
</tr>
</table>
