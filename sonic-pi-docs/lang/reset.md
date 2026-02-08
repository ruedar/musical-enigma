# Reset all thread locals

## Uso

```ruby
reset
```

All settings such as the current synth, BPM, random stream and tick values will be reset to the values inherited from the parent thread. Consider using `clear` to reset all these values to their defaults.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_synth :blade
use_octave 3
puts "before"        
puts current_synth     
puts current_octave    
puts rand              
puts tick              
reset
puts "after"         
puts current_synth     
puts current_octave    
puts rand              
puts tick</code></pre></td>
<td># Basic Reset<br>
 <br>
 <br>
#=&gt; "before"<br>
#=&gt; :blade<br>
#=&gt; 3<br>
#=&gt; 0.75006103515625<br>
#=&gt; 0<br>
 <br>
#=&gt; "after"<br>
#=&gt; :beep<br>
#=&gt; 0<br>
#=&gt; 0.75006103515625<br>
#=&gt; 0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>Reset remembers defaults from when the thread was created:
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
  reset
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
# The call to reset ensured that the current<br>
# synth was returned to the the state at the<br>
# time this thread was started. Thus any calls<br>
# to use_synth between this line and the start<br>
# of the thread are ignored<br>
#=&gt; :blade<br>
#=&gt; 3<br>
# The call to reset ensured<br>
# that the random stream was reset<br>
# to the same state as it was when<br>
# the current thread was started<br>
#=&gt; 0.9287109375<br>
#=&gt; 0</td>
</tr>
</table>
