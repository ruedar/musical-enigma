# Test if sample was pre-loaded

## Uso

```ruby
sample_loaded?  path (string)
```

Given a path to a `.wav`, `.wave`, `.aif`, `.aiff`, `.ogg`, `.oga` or `.flac` file, returns `true` if the sample has already been loaded.

## Introduced in v2.2

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>load_sample :elec_blip
puts sample_loaded? :elec_blip
puts sample_loaded? :misc_burp</code></pre></td>
<td># :elec_blip is now loaded and ready to play as a sample<br>
# prints true because it has been pre-loaded<br>
# prints false because it has not been loaded</td>
</tr>
</table>
