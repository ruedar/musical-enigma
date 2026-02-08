# Get current beat

## Uso

```ruby
beat
```

Returns the beat value for the current thread/live_loop. Beats are advanced only by calls to `sleep` and `sync`. Beats are distinct from virtual time (the value obtained by calling `vt` ) in that it has no notion of rate. It is just essentially a counter for sleeps. After a `sync`, the beat is overridden with the beat value from the thread which called `cue`.

## Introduced in v2.10

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>use_bpm 120 
  puts beat   
  sleep 1
  puts beat   
  use_bpm 2000
  sleep 2
  puts beat</code></pre></td>
<td># The current BPM makes no difference<br>
#=&gt; 0<br>
 <br>
#=&gt; 1<br>
 <br>
 <br>
#=&gt; 3</td>
</tr>
</table>
