# Get server status

## Uso

```ruby
status
```

This returns a Hash of information about the synthesis environment. Mostly used for debugging purposes.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts status</code></pre></td>
<td># Returns something similar to:<br>
# {<br>
#   :ugens=&gt;10,<br>
#   :synths=&gt;1,<br>
#   :groups=&gt;7,<br>
#   :sdefs=&gt;61,<br>
#   :avg_cpu=&gt;0.20156468451023102,<br>
#   :peak_cpu=&gt;0.36655542254447937,<br>
#   :nom_samp_rate=&gt;44100.0,<br>
#   :act_samp_rate=&gt;44099.9998411752,<br>
#   :audio_busses=&gt;2,<br>
#   :control_busses=&gt;0<br>
# }</td>
</tr>
</table>
