# Random number in centred distribution

## Uso

```ruby
rdist  width (number), centre (number)
```

Returns a random number within the range with width around centre. If optional arg `step:` is used, the result is quantised by step.

## Introduced in v2.3

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>print rdist(1, 0)</code></pre></td>
<td>#=&gt; will print a number between -1 and 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>print rdist(1)</code></pre></td>
<td>#=&gt; centre defaults to 0 so this is the same as rdist(1, 0)</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>loop do
    play :c3, pan: rdist(1)
    sleep 0.125
  end</code></pre></td>
<td>#=&gt; Will play :c3 with random L/R panning</td>
</tr>
</table>
