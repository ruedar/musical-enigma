# Roll back random generator

## Uso

```ruby
rand_back  amount (number)
```

Roll the random generator back essentially ‘undoing’ the last call to `rand`. You may specify an amount to roll back allowing you to skip back n calls to `rand`.

## Introduced in v2.7

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts rand
  rand_back
           
           
  puts rand
  puts rand</code></pre></td>
<td># Basic rand stream rollback<br>
# prints 0.75006103515625<br>
# roll random stream back one<br>
# the result of the next call to rand will be<br>
# exactly the same as the previous call<br>
# prints 0.75006103515625 again!<br>
# prints 0.733917236328125</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts rand
  puts rand
  puts rand
  puts rand
  rand_back(3)
              
              
              
  puts rand
  puts rand</code></pre></td>
<td># Jumping back multiple places in the rand stream<br>
# prints 0.75006103515625<br>
# prints 0.733917236328125<br>
# prints 0.464202880859375<br>
# prints 0.24249267578125<br>
# roll random stream back three places<br>
# the result of the next call to rand will be<br>
# exactly the same as the result 3 calls to<br>
# rand ago.<br>
# prints  0.733917236328125 again!<br>
# prints  0.464202880859375</td>
</tr>
</table>
