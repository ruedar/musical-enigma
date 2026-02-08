# Load the contents of a file to the current buffer

## Uso

```ruby
load_buffer  path (string)
```

Given a path to a file, will read the contents and load it into the current buffer. This will replace any previous content.

## Introduced in v2.10

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>load_buffer "~/sonic-pi-tracks/phat-beats.rb"</code></pre></td>
<td># will replace content of current buffer with contents of the file</td>
</tr>
</table>
