# Optionally evaluate block

## Uso

```ruby
on  condition (truthy)
```

Optionally evaluate the block depending on the truthiness of the supplied condition. The truthiness rules are as follows: all values are seen as true except for: false, nil and 0. Lambdas will be automatically called and the truthiness of their results used.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>on true do
  play 70    
end</code></pre></td>
<td>#=&gt; will play 70 as true is truthy</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>on 1 do
  play 70    
end</code></pre></td>
<td>#=&gt; will play 70 as 1 is truthy</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>on 0 do
  play 70    
end</code></pre></td>
<td>#=&gt; will *not* play 70 as 0 is not truthy</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>on false do
  play 70    
end</code></pre></td>
<td>#=&gt; will *not* play 70 as false is not truthy</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>on nil do
  play 70    
end</code></pre></td>
<td>#=&gt; will *not* play 70 as nil is not truthy</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>on lambda{true} do
  play 70    
end</code></pre></td>
<td>#=&gt; will play 70 as the lambda returns a truthy value</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>on lambda{false} do
  play 70    
end</code></pre></td>
<td>#=&gt; will *not* play 70 as the lambda does not return a truthy value</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>on lambda{[true, false].choose} do
  play 70    
end</code></pre></td>
<td>#=&gt; will maybe play 70 depending on the choice in the lambda</td>
</tr>
</table>
