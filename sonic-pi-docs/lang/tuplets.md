# Run block with tuplet timing and optional swing

## Uso

```ruby
tuplets  tuplet_list (list)
```

Runs the block with tuplet timing and optional swing. Each element in the list is considered a tuplet. If the element is a list, each element in the list is considered a tuplet. The duration between each tuplet is specified by the duration opt. The swing opt specifies the amount of swing to apply to the timing. The swing_pulse opt specifies the number of beats between each swing. The swing_offset opt specifies the offset from the start of the list to apply the swing.

## Introduced in v4.6

## Options

### duration:

The duration between each tuplet in beats. Defaults to 1.

### swing:

The amount of swing to apply to the timing. Defaults to 0. Note, only affects tuplets that are multiples of the swing_pulse.

### swing_pulse:

The number of beats between each swing. Defaults to 2.

### swing_offset:

The offset from the start of the list to apply the swing. Defaults to 0.

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>tuplets [70, [72, 72], 70, [82, 82, 82]] do |n|
  play n
end</code></pre></td>
<td># plays 70,<br>
# then at double speed, 72, 72,<br>
# followed by another 70,<br>
# then 82, 82, 82 as triplets</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>tuplets [70, [72, 72], 70, [82, 82, 82]], swing: 0.2 do |n|
  play n
end</code></pre></td>
<td># plays 70,<br>
# then at double speed, 72, 72 with a swing of 0.2<br>
# followed by another 70,<br>
# then 82, 82, 82 as triplets without swing as 3 is not a multiple of 2</td>
</tr>
</table>
