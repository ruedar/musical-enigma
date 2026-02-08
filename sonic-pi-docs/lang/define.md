# Define a new function

## Uso

```ruby
define  name (symbol)
```

Allows you to group a bunch of code and give it your own name for future re-use. Functions are very useful for structuring your code. They are also the gateway into live coding as you may redefine a function whilst a thread is calling it, and the next time the thread calls your function, it will use the latest definition.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>define :foo do
    play 50
    sleep 1
  end
 
  foo
 
 
  3.times do
    foo
  end</code></pre></td>
<td># Define a new function called foo<br>
 <br>
 <br>
 <br>
 <br>
# Call foo on its own<br>
 <br>
# You can use foo anywhere you would use normal code.<br>
# For example, in a block:</td>
</tr>
</table>
