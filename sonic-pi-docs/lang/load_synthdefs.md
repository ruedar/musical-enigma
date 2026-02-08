# Load external synthdefs

## Uso

```ruby
load_synthdefs  path (string)
```

Load all pre-compiled synth designs in the specified directory. The binary files containing synth designs need to have the extension `.scsyndef`. This is useful if you wish to use your own SuperCollider synthesiser designs within Sonic Pi.

## Important notes

You may not trigger external synthdefs unless you enable the following GUI preference:

`Studio -> Synths and FX -> Enable external synths and FX`

Also, if you wish your synth to work with Sonic Pi’s automatic stereo sound infrastructure *you need to ensure your synth outputs a stereo signal* to an audio bus with an index specified by a synth arg named `out_bus`. For example, the following synth would work nicely:

```ruby
(
SynthDef(\piTest,
         {|freq = 200, amp = 1, out_bus = 0 |
           Out.ar(out_bus,
                  SinOsc.ar([freq,freq],0,0.5)* Line.kr(1, 0, 5, amp, doneAction: 2))}
).writeDefFile("/Users/sam/Desktop/")
)
```

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>load_synthdefs "~/Desktop/my_noises"</code></pre></td>
<td># Load all synthdefs in my_noises folder</td>
</tr>
</table>
