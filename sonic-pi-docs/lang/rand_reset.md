# Reset rand generator to last seed

## Uso

```ruby
rand_reset
```

Resets the random stream to the last specified seed. See `use_random_seed` for changing the seed.

## Introduced in v2.7

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts rand
  puts rand
  puts rand
  puts rand
  rand_reset 
  puts rand</code></pre></td>
<td># prints 0.75006103515625<br>
# prints 0.733917236328125<br>
# prints 0.464202880859375<br>
# prints 0.24249267578125<br>
# reset the random stream<br>
# prints 0.75006103515625</td>
</tr>
</table>
