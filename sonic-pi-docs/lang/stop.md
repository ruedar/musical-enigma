# Stop current thread or run

## Uso

```ruby
stop
```

Stops the current thread or if not in a thread, stops the current run. Does not stop any running synths triggered previously in the run/thread or kill any existing sub-threads.

## Introduced in v2.5

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen
  sleep 0.5
  stop               
  sample :loop_garzul</code></pre></td>
<td>#=&gt; this sample is played until completion<br>
 <br>
#=&gt; signal to stop executing this run<br>
#=&gt; this never executes</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>in_thread do
    play 60     
    stop
    sleep 0.5   
    play 72     
  end
  play 80</code></pre></td>
<td>#=&gt; this note plays<br>
 <br>
#=&gt; this sleep never happens<br>
#=&gt; this play never happens<br>
 <br>
#=&gt; this plays as the stop only affected the above thread</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :foo
    sample :bd_haus
    sleep 1
    stop              
  end
  live_loop :bar      
    sample :elec_blip
    sleep 0.25
  end</code></pre></td>
<td># Stopping live loops<br>
 <br>
 <br>
 <br>
# live loop :foo will now stop and no longer loop<br>
 <br>
# live loop :bar will continue looping</td>
</tr>
</table>
