# Sample Pack Filter Resolution

## Uso

```ruby
sample_paths  pre_args (source_and_filter_types)
```

Accepts the same pre-args and opts as `sample` and returns a ring of matched sample paths.

## Introduced in v2.10

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample_paths "/path/to/samples/"</code></pre></td>
<td>#=&gt; ring of all top-level samples in /path/to/samples</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>sample_paths "/path/to/samples/**"</code></pre></td>
<td>#=&gt; ring of all nested samples in /path/to/samples</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>sample_paths "/path/to/samples/", "foo"
                                                containing the string "foo" in their filename.</code></pre></td>
<td>#=&gt; ring of all samples in /path/to/samples</td>
</tr>
</table>
