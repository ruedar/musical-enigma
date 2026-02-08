# Free all loaded samples on the synth server

## Uso

```ruby
sample_free_all
```

Unloads all samples therefore freeing the memory and resources consumed. Subsequent calls to `sample` and friends will re-load the sample on the server.

## Introduced in v2.9

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen       
sample :ambi_lunar_land 
sleep 2
sample_free_all
sample :loop_amen</code></pre></td>
<td># load and play :loop_amen<br>
# load and play :ambi_lunar_land<br>
 <br>
 <br>
# re-loads and plays amen</td>
</tr>
</table>
