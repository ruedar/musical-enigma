# Evaluate the contents of the file inline in the current thread like a function.

## Uso

```ruby
eval_file  filename (path)
```

Reads the full contents of the file with `path` and executes within the current thread like a function call.

## Introduced in v3.2

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>eval_file "~/path/to/sonic-pi-code.rb"</code></pre></td>
<td>#=&gt; will run the contents of this file</td>
</tr>
</table>
