# Determine if note or args is a rest

## Uso

```ruby
rest?  note_or_args (number_symbol_or_map)
```

Given a note or an args map, returns true if it represents a rest and false if otherwise

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts rest? nil</code></pre></td>
<td># true</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts rest? :r</code></pre></td>
<td># true</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts rest? :rest</code></pre></td>
<td># true</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts rest? 60</code></pre></td>
<td># false</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>puts rest? {}</code></pre></td>
<td># false</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>puts rest? {note: :rest}</code></pre></td>
<td># true</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>puts rest? {note: nil}</code></pre></td>
<td># true</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>puts rest? {note: 50}</code></pre></td>
<td># false</td>
</tr>
</table>
