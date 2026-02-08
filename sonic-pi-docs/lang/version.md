# Get current version information

## Uso

```ruby
version
```

Return information representing the current version of Sonic Pi. This information may be further inspected with `version.major`, `version.minor`, `version.patch` and `version.dev`

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts version</code></pre></td>
<td># =&gt; Prints out the current version such as v2.0.1</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts version.major</code></pre></td>
<td># =&gt; Prints out the major version number such as 2</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>puts version.minor</code></pre></td>
<td># =&gt; Prints out the minor version number such as 0</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>puts version.patch</code></pre></td>
<td># =&gt; Prints out the patch level for this version such as 0</td>
</tr>
</table>
