# Real time conversion

## Uso

```ruby
rt  seconds (number)
```

Real time representation. Returns the amount of beats for the value in real-time seconds. Useful for bypassing any bpm scaling

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120 
  play 50
  sleep 1     
  play 62
  sleep rt(1) 
  play 72</code></pre></td>
<td># modifies all time to be half<br>
 <br>
# actually sleeps for half of a second<br>
 <br>
# bypasses bpm scaling and sleeps for a second</td>
</tr>
</table>
