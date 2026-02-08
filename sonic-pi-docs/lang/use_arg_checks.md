# Enable and disable arg checks

## Uso

```ruby
use_arg_checks  true_or_false (boolean)
```

When triggering synths, each argument is checked to see if it is sensible. When argument checking is enabled and an argument isn’t sensible, you’ll see an error in the debug pane. This setting allows you to explicitly enable and disable the checking mechanism. See with_arg_checks for enabling/disabling argument checking only for a specific `do` / `end` block.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50, release: 5
use_arg_checks false
play 50, release: 5</code></pre></td>
<td># Args are checked<br>
 <br>
# Args are not checked</td>
</tr>
</table>
