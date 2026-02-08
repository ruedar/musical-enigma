# Store information in the Time State

## Uso

```ruby
set  time_state_key (default), value (anything)
```

Store information in the Time State for the current time for either the current or any other thread. If called multiple times without an intervening call to `sleep`, `sync`, `set` or `cue`, the last value set will prevail. The value will remain in the Time State until overwritten by another call to `set`, or until Sonic Pi quits.

May be used within a `time_warp` to set past/future events. Does not affect time.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set :foo, 1</code></pre></td>
<td>#=&gt; Stores the value 1 with key :foo</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>set :foo, 3 
get[:foo]</code></pre></td>
<td># Set :foo to 3<br>
#=&gt; returns 3</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>in_thread do
  set :foo, 3 
end
in_thread do
  puts get[:foo] 
end</code></pre></td>
<td># Set :foo to 3<br>
 <br>
 <br>
#=&gt; always returns 3 (no race conditions here!)</td>
</tr>
</table>
