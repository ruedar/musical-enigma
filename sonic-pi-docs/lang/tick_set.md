# Set tick to a specific value

## Uso

```ruby
tick_set  value (number)
```

Set the default tick to the specified `value`. If a `key` is referenced, set that tick to `value` instead. Next call to `look` will return `value`.

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>tick_set 40
  puts look</code></pre></td>
<td># set default tick to 40<br>
#=&gt; 40</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>tick_set :foo, 40
  puts look(:foo)  
  puts look</code></pre></td>
<td># set tick :foo to 40<br>
#=&gt; 40 (tick :foo is now 40)<br>
#=&gt; 0 (default tick is unaffected)</td>
</tr>
</table>
