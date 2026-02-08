# Use Studio FX

## Uso

```ruby
with_fx  fx_name (symbol)
```

This applies the named effect (FX) to everything within a given `do` / `end` block. Effects may take extra parameters to modify their behaviour. See FX help for parameter details.

For advanced control, it is also possible to modify the parameters of an effect within the body of the block. If you define the block with a single argument, the argument becomes a reference to the current effect and can be used to control its parameters (see examples).

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>with_fx :distortion do
  play 50
  sleep 1
  sample :loop_amen
end</code></pre></td>
<td># Basic usage<br>
# Use the distortion effect with default parameters<br>
# =&gt; plays note 50 with distortion<br>
 <br>
# =&gt; plays the loop_amen sample with distortion too</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>with_fx :level, amp: 0.3 do
  play 50
  sleep 1
  sample :loop_amen
end</code></pre></td>
<td># Specify effect parameters<br>
# Use the level effect with the amp parameter set to 0.3</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>with_fx :reverb, mix: 0.1 do |fx|
 
 
  play 60
  sleep 2
  control fx, mix: 0.5
  play 60
  sleep 2
  control fx, mix: 1
  play 60
  sleep 2
end</code></pre></td>
<td># Controlling the effect parameters within the block<br>
 <br>
# here we set the reverb level quite low to start with (0.1)<br>
# and we can change it later by using the 'fx' reference we've set up<br>
# plays note 60 with a little bit of reverb<br>
 <br>
# change the parameters of the effect to add more reverb<br>
# again note 60 but with more reverb<br>
 <br>
# change the parameters of the effect to add more reverb<br>
# plays note 60 with loads of reverb</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>with_fx :reverb, reps: 16 do
  play (scale :e3, :minor_pentatonic), release: 0.1
  sleep 0.125
end

with_fx :reverb do
  16.times do
    play (scale :e3, :minor_pentatonic), release: 0.1
    sleep 0.125
  end
end</code></pre></td>
<td># Repeat the block 16 times internally<br>
 <br>
 <br>
 <br>
 <br>
# The above is a shorthand for this:</td>
</tr>
</table>
