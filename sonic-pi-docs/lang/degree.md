# Convert a degree into a note

## Uso

```ruby
degree  degree (symbol_or_number), tonic (symbol), scale (symbol)
```

For a given scale and tonic it takes a symbol/string/number and resolves it to a midi note. The degree can be either a decimal number or a roman numeral (if it’s a string or symbol), and may optionally be prefixed an augmentation ( `a` / `d` for an augmented/diminished interval, `aa` / `dd` for double augmented/diminished or `p` for a perfect (unchanged) interval).

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play degree(:iii, :D3, :major)
play degree(3, :C3, :minor)
play degree('d5', :B3, :major)</code></pre></td>
<td># major third up from :D3<br>
# minor third up from :C3<br>
# diminished fifth up from :B3</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>chrd = []
[:i, :iii, :v, :dvii, :dix, :Axi, :xiii].each do |d| 
  chrd.append (degree d, :Fs, :major) 
end
play chrd</code></pre></td>
<td># for each degree in the chord<br>
# add the corresponding note<br>
 <br>
# play an F# 13+11-9 chord, using roman numeral symbols</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>chrd = []
['1', '3', '5', 'd7', 'd9', 'A11', '13'].each do |d|
  chrd.append (degree d, :Fs, :major)
end
play chrd</code></pre></td>
<td># the same chord as above, but using decimal number strings</td>
</tr>
</table>
