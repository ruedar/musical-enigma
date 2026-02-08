# Reset tick to 0

## Uso

```ruby
tick_reset
```

Reset default tick to 0. If a `key` is referenced, set that tick to 0 instead. Same as calling tick_set(0)

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>tick
  tick
  tick
  puts look
  tick_set 0
  puts look</code></pre></td>
<td># increment default tick a few times<br>
 <br>
 <br>
 <br>
#=&gt; 2 (default tick is now 2)<br>
# default tick is now 0<br>
#=&gt; 0 (default tick is now 0</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>tick :foo
  tick :foo
  tick :foo
  puts look(:foo)
  tick_set 0
  puts look(:foo)
  tick_set :foo, 0
  puts look(:foo)</code></pre></td>
<td># increment tick :foo a few times<br>
 <br>
 <br>
 <br>
#=&gt; 2 (tick :foo is now 2)<br>
# default tick is now 0<br>
#=&gt; 2 (tick :foo is still 2)<br>
#  reset tick :foo<br>
#=&gt; 0 (tick :foo is now 0)</td>
</tr>
</table>
