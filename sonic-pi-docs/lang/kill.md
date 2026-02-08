# Kill synth

## Uso

```ruby
kill  node (synth_node)
```

Kill a running synth sound or sample. In order to kill a sound, you need to have stored a reference to it in a variable.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>foo = play 50, release: 4
sleep 1

kill foo</code></pre></td>
<td># store a reference to a running synth in a variable called foo:<br>
 <br>
 <br>
# foo is still playing, but we can kill it early:</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>bar = sample :loop_amen
sleep 0.5
kill bar</code></pre></td>
<td></td>
</tr>
</table>
