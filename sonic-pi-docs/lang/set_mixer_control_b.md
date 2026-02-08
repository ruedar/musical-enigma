# Control main mixer

## Uso

```ruby
set_mixer_control!
```

The main mixer is the final mixer that all sound passes through. This fn gives you control over the main mixer allowing you to manipulate all the sound playing through Sonic Pi at once. For example, you can sweep a lpf or hpf over the entire sound. You can reset the controls back to their defaults with `reset_mixer!`.

## Introduced in v2.7

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_mixer_control! lpf: 30, lpf_slide: 16</code></pre></td>
<td># slide the global lpf to 30 over 16 beats.</td>
</tr>
</table>
