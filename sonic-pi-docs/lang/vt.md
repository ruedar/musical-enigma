# Get virtual time

## Uso

```ruby
vt
```

Get the virtual time of the current thread.

## Introduced in v2.1

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts vt
   sleep 1
   puts vt</code></pre></td>
<td># prints 0<br>
 <br>
# prints 1</td>
</tr>
</table>
