# Send an OSC message to a specific host and port

## Uso

```ruby
osc_send  hostname (string), port (number), path (osc_path), args (list)
```

Similar to `osc` except ignores any `use_osc` settings and sends the OSC message directly to the specified `hostname` and `port`.

See `osc` for more information.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>osc_send "localhost", 7000, "/foo/baz"</code></pre></td>
<td># Send an OSC message to port 7000 on the same machine</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7010                
osc "/foo/baz"                           
osc_send "localhost", 7000, "/foo/baz"</code></pre></td>
<td># set hostname and port<br>
# Send an OSC message to port 7010<br>
# Send an OSC message to port 7000<br>
# (ignores use_osc settings)</td>
</tr>
</table>
