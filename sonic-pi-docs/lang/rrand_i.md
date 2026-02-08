# Generate a random whole number between two points inclusively

## Uso

```ruby
rrand_i  min (number), max (number)
```

Given two numbers, this produces a whole number between the min and max you supplied inclusively. Both min and max need to be supplied. For random floats, see `rrand`

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rrand_i(0, 10)</code></pre></td>
<td>#=&gt; will print a random number between 0 and 10 (e.g. 4, 0 or 10) to the output pane</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>loop do
    play rrand_i(60, 72)
    sleep 0.125
  end</code></pre></td>
<td>#=&gt; Will play a random midi note between C4 (60) and C5 (72)</td>
</tr>
</table>
