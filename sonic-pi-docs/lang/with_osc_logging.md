# Block-level enable and disable OSC logging

## Uso

```ruby
with_osc_logging  true_or_false (boolean)
```

Similar to use_osc_logging except only applies to code within supplied `do` / `end` block. Previous OSC log value is restored after block.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_osc_logging true
  osc "/foo"
  with_osc_logging false do
   
    osc "/foo"
  end
  sleep 1
 
  osc "/foo"</code></pre></td>
<td># Turn on OSC logging:<br>
 <br>
#  message is printed to log<br>
 <br>
#OSC logging is now disabled<br>
# OSC message *is* sent but not displayed in log<br>
 <br>
 <br>
# Debug is re-enabled<br>
# message is displayed in log</td>
</tr>
</table>
