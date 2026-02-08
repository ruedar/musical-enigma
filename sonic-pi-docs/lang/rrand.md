# Generate a random float between two numbers

## Uso

```ruby
rrand  min (number), max (number)
```

Given two numbers, this produces a float between the supplied min and max values exclusively. Both min and max need to be supplied. For random integers, see `rrand_i`. If optional arg `step:` is used, the result is quantised by step.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rrand(0, 10)</code></pre></td>
<td>#=&gt; will print a number like 8.917730007820797 to the output pane</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>loop do
    play rrand(60, 72)
    sleep 0.125
  end</code></pre></td>
<td>#=&gt; Will play a random non-integer midi note between C4 (60) and C5 (72) such as 67.3453 or 71.2393</td>
</tr>
</table>
