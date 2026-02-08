# Clear all thread locals to defaults

## Uso

```ruby
clear
```

All settings such as the current synth, BPM, random stream and tick values will be reset to their defaults. Consider using `reset` to reset all these values to those inherited from the parent thread.

## Introduced in v2.11

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>Clear wipes out the threads locals
use_synth :blade
use_octave 3
puts "before"        
puts current_synth     
puts current_octave    
puts rand              
puts tick              
at do
  use_synth :tb303
  puts rand              
  clear
  puts "thread"        
                         
                         
                         
                         
  puts current_synth     
                         
  puts current_octave    
                         
                         
  puts rand              
  puts tick              
end</code></pre></td>
<td>#=&gt; "before"<br>
#=&gt; :blade<br>
#=&gt; 3<br>
#=&gt; 0.75006103515625<br>
#=&gt; 0<br>
 <br>
 <br>
#=&gt; 0.9287109375<br>
 <br>
#=&gt; "thread"<br>
# The clear reset the current synth to the default<br>
# of :beep. We are therefore ignoring any inherited<br>
# synth settings. It is as if the thread was a completely<br>
# new Run.<br>
#=&gt; :beep<br>
# The current octave defaults back to 0<br>
#=&gt; 0<br>
# The random stream defaults back to the standard<br>
# stream used by every new Run.<br>
#=&gt; 0.75006103515625<br>
#=&gt; 0</td>
</tr>
</table>
