# Set Volume globally

## Uso

```ruby
set_volume!  vol (number)
```

Set the main system volume to `vol`. Accepts a value between `0` and `5` inclusive. Vols greater or smaller than the allowed values are trimmed to keep them within range. Default is `1`.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_volume! 2</code></pre></td>
<td># Set the main system volume to 2</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>set_volume! -1</code></pre></td>
<td># Out of range, so sets main system volume to 0</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>set_volume! 7</code></pre></td>
<td># Out of range, so sets main system volume to 5</td>
</tr>
</table>
