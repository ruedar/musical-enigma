# Free a sample on the synth server

## Uso

```ruby
sample_free  path (string)
```

Frees the memory and resources consumed by loading the sample on the server. Subsequent calls to `sample` and friends will re-load the sample on the server.

You may also specify the same set of source and filter pre-args available to `sample` itself. `sample_free` will then free all matching samples. See `sample` ’s docs for more information.

## Introduced in v2.9

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen
sleep 2
sample :loop_amen
sleep 2
sample_free :loop_amen
sample :loop_amen</code></pre></td>
<td># The Amen break is now loaded into memory and played<br>
 <br>
# The Amen break is not loaded but played from memory<br>
 <br>
# The Amen break is freed from memory<br>
# the Amen break is re-loaded and played</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts sample_info(:loop_amen).to_i
puts sample_info(:loop_amen).to_i
                                 
sample_free :loop_amen
puts sample_info(:loop_amen).to_i</code></pre></td>
<td># This returns the buffer id of the sample i.e. 1<br>
# The buffer id remains constant whilst the sample<br>
# is loaded in memory<br>
 <br>
# The Amen break is re-loaded and gets a *new* id.</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen
sample :ambi_lunar_land
sleep 2
sample_free :loop_amen, :ambi_lunar_land
sample :loop_amen                       
sample :ambi_lunar_land</code></pre></td>
<td># re-loads and plays amen<br>
# re-loads and plays lunar land</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>dir = "/path/to/sample/dir"
sample_free dir
sample_free dir, 1
sample_free dir, :foo
sample_free dir, /[Bb]ar/</code></pre></td>
<td># Using source and filter pre-args<br>
 <br>
# frees any loaded samples in "/path/to/sample/dir"<br>
# frees sample with index 1 in "/path/to/sample/dir"<br>
# frees sample with name "foo" in "/path/to/sample/dir"<br>
# frees sample which matches regex /[Bb]ar/ in "/path/to/sample/dir"</td>
</tr>
</table>
