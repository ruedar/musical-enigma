# Get information from the Time State

## Uso

```ruby
get  time_state_key (default)
```

Retrieve information from Time State set prior to the current time from either the current or any other thread. If called multiple times will always return the same value unless a call to `sleep`, `sync`, `set` or `cue` is interleaved. Also, calls to `get` will always return the same value across Runs for deterministic behaviour - which means you may safely use it in your compositions for repeatable music. If no value is stored with the relevant key, will return `nil`.

May be used within a `time_warp` to retrieve past events. If in a time warp, `get` can not be called from a future position. Does not advance time.

## Introduced in v3.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>get :foo</code></pre></td>
<td>#=&gt; returns the last value set as :foo, or nil</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>set :foo, 3
get[:foo]</code></pre></td>
<td>#=&gt; returns 3</td>
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
<td>#=&gt; always returns 3 (no race conditions here!)</td>
</tr>
</table>
