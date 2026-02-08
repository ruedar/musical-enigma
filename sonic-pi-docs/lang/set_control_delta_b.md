# Set control delta globally

## Uso

```ruby
set_control_delta!  time (number)
```

Specify how many seconds between successive modifications (i.e. trigger then controls) of a specific node on a specific thread. Set larger if you are missing control messages sent extremely close together in time.

## Introduced in v2.1

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_control_delta! 0.1                
s = play 70, release: 8, note_slide: 8
control s, note: 82</code></pre></td>
<td># Set control delta to 0.1<br>
# Play a note and set the slide time<br>
# immediately start sliding note.<br>
# This control message might not be<br>
# correctly handled as it is sent at the<br>
# same virtual time as the trigger.<br>
# If you don't hear a slide, try increasing the<br>
# control delta until you do.</td>
</tr>
</table>
