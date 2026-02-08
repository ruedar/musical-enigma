# Block-level enable and disable cue logging

## Uso

```ruby
with_cue_logging  true_or_false (boolean)
```

Similar to use_cue_logging except only applies to code within supplied `do` / `end` block. Previous cue log value is restored after block.

## Introduced in v2.6

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_cue_logging true
  cue :foo
  with_cue_logging false do
   
    cue :bar
  end
  sleep 1
 
  cue :quux</code></pre></td>
<td># Turn on debugging:<br>
 <br>
# cue message is printed to log<br>
 <br>
#Cue logging is now disabled<br>
# cue *is* sent but not displayed in log<br>
 <br>
 <br>
# Debug is re-enabled<br>
# cue is displayed in log</td>
</tr>
</table>
