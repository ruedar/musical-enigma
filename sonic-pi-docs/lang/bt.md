# Beat time conversion

## Uso

```ruby
bt  seconds (number)
```

Beat time representation. Scales the time to the current BPM. Useful for adding bpm scaling

## Introduced in v2.8

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120 
  puts bt(1)
  use_bpm 60  
  puts bt(1)
  use_bpm 30  
  puts bt(1)</code></pre></td>
<td># Set the BPM to be double the default<br>
# 0.5<br>
# BPM is now default<br>
# 1<br>
# BPM is now half the default<br>
# 2</td>
</tr>
</table>
