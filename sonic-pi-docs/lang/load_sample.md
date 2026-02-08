# Pre-load first matching sample

## Uso

```ruby
load_sample  path (string)
```

Given a path to a `.wav`, `.wave`, `.aif`, `.aiff`, `.ogg`, `.oga` or `.flac` file, pre-loads the sample into memory.

You may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will then load all matching samples. See `sample` ’s docs for more information.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>load_sample :elec_blip
sample :elec_blip</code></pre></td>
<td># :elec_blip is now loaded and ready to play as a sample<br>
# No delay takes place when attempting to trigger it</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>dir = "/path/to/sample/dir"
load_sample dir
load_sample dir, 1
load_sample dir, :foo
load_sample dir, "quux"
load_sample dir, /[Bb]ar/</code></pre></td>
<td># Using source and filter pre-args<br>
 <br>
# loads first matching sample in "/path/to/sample/dir"<br>
# loads sample with index 1 in "/path/to/sample/dir"<br>
# loads sample with name "foo" in "/path/to/sample/dir"<br>
# loads first sample with file name containing "quux" in "/path/to/sample/dir"<br>
# loads first sample which matches regex /[Bb]ar/ in "/path/to/sample/dir"</td>
</tr>
</table>
