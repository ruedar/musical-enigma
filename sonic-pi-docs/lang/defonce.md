# Define a named value only once

## Uso

```ruby
defonce  name (symbol)
```

Allows you to assign the result of some code to a name, with the property that the code will only execute once - therefore stopping re-definitions. This is useful for defining values that you use in your compositions but you don’t want to reset every time you press run. You may force the block to execute again regardless of whether or not it has executed once already by using the override option (see examples).

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>defonce :foo do 
    sleep 1       
                  
                  
    puts "hello"
    10            
  end
 
  puts foo
 
  puts foo
  defonce :foo do
    puts "you can't redefine me"
    15
  end
  puts foo
 
 
  3.times do
    play foo 
  end</code></pre></td>
<td># Define a new function called foo<br>
# Sleep for a beat in the function definition. Note that this amount<br>
# of time in seconds will depend on the current BPM of the live_loop<br>
# or thread calling this function.<br>
# Print hello<br>
# Return a value of 10<br>
 <br>
# Call foo on its own<br>
# The run sleeps for a beat and prints "hello" before returning 10<br>
# Try it again:<br>
# This time the run doesn't sleep or print anything out. However, 10 is still returned.<br>
# Try redefining foo<br>
 <br>
 <br>
 <br>
# We still don't see any printing or sleeping, and the result is still 10<br>
# You can use foo anywhere you would use normal code.<br>
# For example, in a block:<br>
 <br>
# play 10</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>defonce :bar do
    50
  end
  play bar
  defonce :bar do
    70
  end
  play bar
  defonce :bar, override: true do 
    80
  end
  play bar</code></pre></td>
<td># plays 50<br>
# This redefinition doesn't work due to the behaviour of defonce<br>
 <br>
 <br>
# Still plays 50<br>
# Force definition to take place with override option<br>
 <br>
 <br>
# plays 80</td>
</tr>
</table>
