# Random list selection

## Uso

```ruby
choose  list (array)
```

Choose an element at random from a list (array).

If no arguments are given, will return a lambda function which when called takes an argument which will be a list to be chosen from. This is useful for choosing random `onset:` vals for samples

Always returns a single element (or nil)

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>loop do
    play choose([60, 64, 67])
    sleep 1
    play chord(:c, :major).choose
    sleep 1
  end</code></pre></td>
<td>#=&gt; plays one of 60, 64 or 67 at random<br>
 <br>
#=&gt; You can also call .choose on the list</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  sample :loop_amen, onset: choose  
  sleep 0.125
end</code></pre></td>
<td># Using choose for random sample onsets<br>
 <br>
# choose a random onset value each time</td>
</tr>
</table>
