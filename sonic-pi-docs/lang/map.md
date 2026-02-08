# Create an immutable map

## Uso

```ruby
map  list (array)
```

Create a new immutable key/value map from args.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(map foo: 1, bar: 2)[:foo]</code></pre></td>
<td>#=&gt; 1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(map foo: 1, bar: 2)[:bar]</code></pre></td>
<td>#=&gt; 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>(map foo: 1, bar: 2)[:quux]</code></pre></td>
<td>#=&gt; nil</td>
</tr>
</table>
