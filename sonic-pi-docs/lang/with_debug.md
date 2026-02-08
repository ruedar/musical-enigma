# Block-level enable and disable debug

## Uso

```ruby
with_debug  true_or_false (boolean)
```

Similar to use_debug except only applies to code within supplied `do` / `end` block. Previous debug value is restored after block.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_debug true
play 80
with_debug false do
 
  play 50
  sleep 1
  play 72
end

play 90</code></pre></td>
<td># Turn on debugging:<br>
 <br>
# Debug message is sent<br>
 <br>
#Debug is now disabled<br>
# Debug message is not sent<br>
 <br>
# Debug message is not sent<br>
 <br>
# Debug is re-enabled<br>
# Debug message is sent</td>
</tr>
</table>
