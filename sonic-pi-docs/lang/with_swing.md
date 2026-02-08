# Add swing to successive calls to do/end block

## Uso

```ruby
with_swing  shift (beats), pulse (number), tick (symbol)
```

Runs block within a `time_warp` except for once every `pulse` consecutive runs (defaulting to 4). When used for rhythmical purposes this results in one in every `pulse` calls of the block being ‘on beat’ and the rest shifted forward or backwards in time by `shift` beats.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  with_swing 0.1 do
    sample :elec_beep     
  end
  sleep 0.25
end</code></pre></td>
<td># plays the :elec_beep sample late except for every 4th time</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  with_swing -0.1 do
    sample :elec_beep     
  end                     
  sleep 0.25
end</code></pre></td>
<td># plays the :elec_beep sample slightly early<br>
# except for every 4th time</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  with_swing -0.1, pulse: 8 do
    sample :elec_beep     
  end                     
  sleep 0.25
end</code></pre></td>
<td># plays the :elec_beep sample slightly early<br>
# except for every 8th time</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  with_swing 0.14, tick: :a do
    sample :elec_beep     
  end                     
  with_swing -0.1, tick: :b do
    sample :elec_beep, rate: 2 
  end                          
  sleep 0.25
end</code></pre></td>
<td># Use unique tick names if you plan on using with_swing<br>
# more than once in any given live_loop or thread.<br>
 <br>
 <br>
# plays the :elec_beep sample slightly late<br>
# except for every 4th time<br>
 <br>
# plays the :elec_beep sample at double rate<br>
#  slightly early except for every 4th time</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  with_swing 0.1 do
    cue :tick             
  end
  sleep 0.25
end
live_loop :bar do
  sync :tick
  sample :elec_beep      
                         
                         
end</code></pre></td>
<td># send out cue messages with swing timing<br>
 <br>
 <br>
 <br>
 <br>
 <br>
# sync on the swing cue messages to bring the swing into<br>
# another live loop (sync will match the timing and clock of<br>
# the sending live loop)</td>
</tr>
</table>
