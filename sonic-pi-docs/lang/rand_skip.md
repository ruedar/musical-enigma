# Jump forward random generator

## Uso

```ruby
rand_skip  amount (number)
```

Jump the random generator forward essentially skipping the next call to `rand`. You may specify an amount to jump allowing you to skip n calls to `rand`.

## Introduced in v2.7

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>puts rand
  rand_skip
           
  puts rand</code></pre></td>
<td># Basic rand stream skip<br>
# prints 0.75006103515625<br>
# jump random stream forward one<br>
# typically the next rand is 0.733917236328125<br>
# prints 0.464202880859375</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>puts rand
  puts rand
  puts rand
  puts rand
  rand_reset 
  puts rand
  rand_skip(2)
              
              
              
  puts rand 0.24249267578125</code></pre></td>
<td># Jumping forward multiple places in the rand stream<br>
# prints 0.75006103515625<br>
# prints 0.733917236328125<br>
# prints 0.464202880859375<br>
# prints 0.24249267578125<br>
# reset the random stream<br>
# prints 0.75006103515625<br>
# jump random stream forward three places<br>
# the result of the next call to rand will be<br>
# exactly the same as if rand had been called<br>
# three times</td>
</tr>
</table>
