# Block-level enable and disable arg checks

## Uso

```ruby
with_arg_checks  true_or_false (boolean)
```

Similar to `use_arg_checks` except only applies to code within supplied `do` / `end` block. Previous arg check value is restored after block.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_arg_checks true
play 80, cutoff: 100
with_arg_checks false do
 
  play 50, release: 3
  sleep 1
  play 72            
end

play 90</code></pre></td>
<td># Turn on arg checking:<br>
 <br>
# Args are checked<br>
 <br>
#Arg checking is now disabled<br>
# Args are not checked<br>
 <br>
# Arg is not checked<br>
 <br>
# Arg checking is re-enabled<br>
# Args are checked</td>
</tr>
</table>
