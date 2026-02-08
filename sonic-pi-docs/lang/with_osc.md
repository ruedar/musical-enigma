# Block-level setting for the default hostname and port number of outgoing OSC messages.

## Uso

```ruby
with_osc  hostname (string), port (number)
```

Sets the destination host and port that `osc` will send messages to for the given do/end block.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7000 
osc "/foo/baz"            
with_osc "localhost", 7010 do
                               
   osc "/foo/baz"            
end
osc "/foo/baz"</code></pre></td>
<td># Specify port 7010<br>
# Send an OSC message to port 7000<br>
# set hostname and port for the duration<br>
# of this do/end block<br>
# Send an OSC message to port 7010<br>
 <br>
# Send an OSC message to port 7000<br>
# as old setting is restored outside<br>
# do/end block</td>
</tr>
</table>
