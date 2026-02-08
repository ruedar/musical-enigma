# Set the bit depth for recording wav files

## Uso

```ruby
set_recording_bit_depth!  bit_depth (number)
```

When you hit the record button, Sonic Pi saves all the audio you can hear into a wav file. By default, this file uses a resolution of 16 bits which is the same as CD audio and good enough for most use cases. However, when working with professional equipment, it is common to want to work with even higher quality files such as 24 bits and even 32 bits. This function allows you to switch the default from 16 to one of 8, 16, 24 or 32.

## Introduced in v2.11

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>set_recording_bit_depth! 24</code></pre></td>
<td># Set recording bit depth to 24</td>
</tr>
</table>
