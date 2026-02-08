# Block-level enable and disable MIDI logging

## Uso

```ruby
with_midi_logging  true_or_false (boolean)
```

Similar to use_midi_logging except only applies to code within supplied `do` / `end` block. Previous MIDI log value is restored after block.

## Introduced in v3.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_midi_logging true
  midi :e1
  with_midi_logging false do
   
    midi :f2
  end
  sleep 1
 
  midi :G3</code></pre></td>
<td># Turn on MIDI logging:<br>
 <br>
#  message is printed to log<br>
 <br>
#MIDI logging is now disabled<br>
# MIDI message *is* sent but not displayed in log<br>
 <br>
 <br>
# Debug is re-enabled<br>
# message is displayed in log</td>
</tr>
</table>
