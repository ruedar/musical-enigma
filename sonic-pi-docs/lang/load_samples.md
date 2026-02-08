# Pre-load all matching samples

## Uso

```ruby
load_samples  paths (list)
```

Given a directory containing multiple `.wav`, `.wave`, `.aif`, `.aiff`, `.ogg`, `.oga` or `.flac` files, pre-loads all the samples into memory.

You may also specify the same set of source and filter pre-args available to `sample` itself. `load_sample` will load all matching samples (not just the sample `sample` would play given the same opts) - see `sample` ’s docs for more information.

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
# loads all samples in "/path/to/sample/dir"<br>
# loads sample with index 1 in "/path/to/sample/dir"<br>
# loads sample with name "foo" in "/path/to/sample/dir"<br>
# loads all samples with file names containing "quux" in "/path/to/sample/dir"<br>
# loads all samples which match regex /[Bb]ar/ in "/path/to/sample/dir"</td>
</tr>
</table>
