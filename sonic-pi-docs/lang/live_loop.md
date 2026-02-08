# A loop for live coding

## Uso

```ruby
live_loop  name (symbol)
```

Loop the do/end block forever. However, unlike a basic loop, a live_loop has two special properties. Firstly it runs in a thread - so you can have any number of live loops running at the same time (concurrently). Secondly, you can change the behaviour of a live loop whilst it is still running without needing to stop it. Live loops are therefore the secret to live coding with Sonic Pi.

As live loops are excecuted within a named in_thread, they behave similarly. See the in_thread documentation for all the details. However, it’s worth mentioning a few important points here. Firstly, only one live loop with a given name can run at any one time. Therefore, if you define two or more `live_loop` s called `:foo` only one will be running. Another important aspect of `live_loop` s is that they manage their own thread locals set with the `use_*` and `with_*` fns. This means that each `live_loop` can have its own separate default synth, BPM and sample defaults. When a `live_loop` is *first* created, it inherits the thread locals from the parent thread, but once it has started, the only way to change them is by re-defining the do/end body of the `live_loop`. See the examples below for details. Finally, as mentioned above, provided their names are different, you may have many `live_loop` s executing at once.

A typical way of live coding with live loops is to define a number of them in a buffer, hit Run to start them and then to modify their do/end blocks and then hit Run again. This will not create any more thread, but instead just modify the behaviour of the existing threads. The changes will *not* happen immediately. Instead, they will only happen the next time round the loop. This is because the behaviour of each live loop is implemented with a standard function. When a live loop is updated, the function definition is also updated. Each time round the live loop, the function is called, so the new behviour is only observed next time round the loop.

Also sends a `cue` with the same name each time the `live_loop` repeats. This may be used to `sync` with other threads and `live_loop` s.

If the `live_loop` block is given a parameter, this is given the result of the last run of the loop (with initial value either being `0` or an init arg). This allows you to ‘thread’ values across loops.

Finally, it is possible to delay the initial trigger of the live_loop on creation with both the `delay:` and `sync:` opts. See their respective docstrings. If both `delay:` and `sync:` are specified, on initial live_loop creation first the delay will be honoured and then the sync.

## Introduced in v2.1

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>live_loop :ping do 
  sample :elec_ping
  sleep 1          
end</code></pre></td>
<td># Define and start a simple live loop<br>
# Create a live loop called :ping<br>
# This live loops plays the :elec_ping sample<br>
# Then sleeps for 1 beat before repeating</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>live_loop :ping do 
  sample :elec_ping
                   
                   
                   
end</code></pre></td>
<td># Every live loop must sleep or sync<br>
# Create a live loop called :ping<br>
# This live loops plays the :elec_ping sample<br>
# However, because the do/end lock of the live loop does not<br>
# contain any calls to sleep or sync, the live loop stops at<br>
# the end of the first loop with a 'Did not sleep' error.</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do 
  play 70
  sleep 1
end
live_loop :bar do 
  sample :bd_haus 
  sleep 0.5       
end</code></pre></td>
<td># Multiple live loops will play at the same time<br>
# Start a live loop called :foo<br>
 <br>
 <br>
 <br>
# Start another live loop called :bar<br>
# Both :foo and :bar will be playing<br>
# at the same time.</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>use_bpm 30
live_loop :foo do
  play 70          
  sleep 1          
end</code></pre></td>
<td># Live loops inherit external use_* thread locals<br>
 <br>
 <br>
# live loop :foo now has a BPM of 30<br>
# This sleep will be for 2 seconds</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do
  use_bpm 30      
  play 70
  sleep 1         
end
live_loop :bar do
  use_bpm 120     
  play 82
  sleep 1         
end</code></pre></td>
<td># Live loops can have their own thread locals<br>
 <br>
# Set the BPM of live loop :foo to 30<br>
 <br>
# This sleep will be for 2 seconds<br>
 <br>
 <br>
# Set the BPM of live loop :bar to 120<br>
 <br>
# This sleep will be for 0.5 seconds</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do |a| 
  puts a              
  sleep 1
  a += 1              
end</code></pre></td>
<td># Live loops can pass values between iterations<br>
# pass a param (a) to the block (inits to 0)<br>
# prints out all the integers<br>
 <br>
# increment a by 1 (last value is passed back into the loop)</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>live_loop :foo do 
  play 70
  sleep 1
end
live_loop :foo do 
  sample :bd_haus 
  sleep 0.5       
                  
end</code></pre></td>
<td># Live loop names must be unique<br>
# Start a live loop called :foo<br>
 <br>
 <br>
 <br>
# Attempt to start another also called :foo<br>
# With a different do/end block<br>
# This will not start another live loop<br>
# but instead replace the behaviour of the first.<br>
# There will only be one live loop running playing<br>
# The bass drum</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>live_loop :foo, sync: :bar do
 play 70                     
 sleep 1                     
end
sleep 4                      
live_loop :bar do            
  sample :bd_haus            
  sleep 0.5                  
end</code></pre></td>
<td># You can sync multiple live loops together<br>
# Wait for a :bar cue event before starting :foo<br>
# Live loop :foo is therefore blocked and does<br>
# not make a sound initially<br>
 <br>
# Wait for 4 beats<br>
# Start a live loop called :foo which will emit a :bar<br>
# cue message therefore releasing the :foo live loop.<br>
# Live loop :foo therefore starts and also inherits the<br>
# logical time of live loop :bar.<br>
# This pattern is also useful to re-sync live loops after<br>
# errors are made. For example, when modifying live loop :foo<br>
# it is possible to introduce a runtime error which will stop<br>
# :foo but not :bar (as they are separate, isolated threads).<br>
# Once the error has been fixed and the code is re-run, :foo<br>
# will automatically wait for :bar to loop round and restart<br>
# in sync with the correct virtual clock.</td>
</tr>
</table>
