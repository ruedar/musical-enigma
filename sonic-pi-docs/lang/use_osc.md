# Set the default hostname and port number for outgoing OSC messages.

## Uso

```ruby
use_osc  hostname (string), port (number)
```

Sets the destination host and port that `osc` will send messages to. If no port number is specified - will default to port 4560 (Sonic Pi’s default OSC listening port).

OSC (Open Sound Control) is a simple way of passing messages between two separate programs on the same computer or even on different computers via a local network or even the internet. `use_osc` allows you to specify which computer ( `hostname` ) and program ( `port` ) to send messages to.

It is possible to send messages to the same computer by using the host name `"localhost"`

This is a thread-local setting - therefore each thread (or live loop) can have their own separate `use_osc` values.

Note that calls to `osc_send` will ignore these values.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7000 
osc "/foo/bar"</code></pre></td>
<td># Send a simple OSC message to another program on the same machine<br>
# Specify port 7000 on this machine<br>
# Send an OSC message with path "/foo/bar"<br>
# and no arguments</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7000       
osc "/foo/bar" 1, 3.89, "baz"</code></pre></td>
<td># Send an OSC messages with arguments to another program on the same machine<br>
# Specify port 7000 on this machine<br>
# Send an OSC message with path "/foo/bar"<br>
# and three arguments:<br>
# 1) The whole number (integer) 1<br>
# 2) The fractional number (float) 3,89<br>
# 3) The string "baz"</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>use_osc "10.0.1.5", 7000        
osc "/foo/bar" 1, 3.89, "baz"</code></pre></td>
<td># Send an OSC messages with arguments to another program on a different machine<br>
# Specify port 7000 on the machine with address 10.0.1.5<br>
# Send an OSC message with path "/foo/bar"<br>
# and three arguments:<br>
# 1) The whole number (integer) 1<br>
# 2) The fractional number (float) 3,89<br>
# 3) The string "baz"</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7000 
osc "/foo/bar"            
osc "/foo/baz"            
use_osc "localhost", 7005 
osc "/foo/bar"            
osc "/foo/baz"</code></pre></td>
<td># use_osc only affects calls to osc until the next call to use_osc<br>
# Specify port 7000 on this machine<br>
# Send an OSC message to port 7000<br>
# Send another OSC message to port 7000<br>
# Specify port 7000 on this machine<br>
# Send an OSC message to port 7005<br>
# Send another OSC message to port 7005</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>use_osc "localhost", 7000 
live_loop :foo do
  osc "/foo/bar"            
  sleep 1                     
end
live_loop :bar do
  use_osc "localhost", 7005 
                              
                              
  osc "/foo/bar"            
  sleep 1
end
use_osc "localhost", 7010 
osc "/foo/baz"</code></pre></td>
<td># threads may have their own use_osc value<br>
# Specify port 7000 on this machine<br>
 <br>
# Thread inherits outside use_osc values<br>
# and therefore sends OSC messages to port 7000<br>
 <br>
 <br>
# Override OSC hostname and port for just this<br>
# thread (live loop :bar). Live loop :foo is<br>
# unaffected.<br>
# Send OSC messages to port 7005<br>
 <br>
 <br>
# Specify port 7010<br>
# Send another OSC message to port 7010<br>
# Note that neither live loops :foo or :bar<br>
# are affected (their use_osc values are<br>
# independent and isolated.</td>
</tr>
</table>
