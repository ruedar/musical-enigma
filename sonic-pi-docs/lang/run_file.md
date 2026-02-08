# Evaluate the contents of the file as a new Run

## Uso

```ruby
run_file  filename (path)
```

Reads the full contents of the file with `path` and executes it in a new Run. This works as if the code in the file was in a buffer and Run button was pressed.

## Introduced in v2.11

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>run_file "~/path/to/sonic-pi-code.rb"</code></pre></td>
<td>#=&gt; will run the contents of this file</td>
</tr>
</table>
