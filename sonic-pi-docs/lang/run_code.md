# Evaluate the code passed as a String as a new Run

## Uso

```ruby
run_code  code (string)
```

Executes the code passed as a string in a new Run. This works as if the code was in a buffer and Run button was pressed.

## Introduced in v2.11

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>run_code "sample :ambi_lunar_land"</code></pre></td>
<td>#=&gt; will play the :ambi_lunar_land sample</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>run_code "8.times do
play 60
sleep 1
end"</code></pre></td>
<td># Works with any amount of code:<br>
 <br>
 <br>
 <br>
# will play 60 8 times</td>
</tr>
</table>
