# Reset all ticks

## Uso

```ruby
tick_reset_all
```

Reset all ticks - default and keyed

## Introduced in v2.6

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>tick     
  tick
  tick :foo
  tick :foo
  tick :foo
  puts look
  puts look(:foo)
  tick_reset_all
  puts look
  puts look(:foo)</code></pre></td>
<td># increment default tick and tick :foo<br>
 <br>
 <br>
 <br>
 <br>
#=&gt; 1<br>
#=&gt; 2<br>
 <br>
#=&gt; 0<br>
#=&gt; 0</td>
</tr>
</table>
