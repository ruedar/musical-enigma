# Load a single external synthdef

## Uso

```ruby
load_synthdef  path (string)
```

Load a pre-compiled synth design from the specified file. This is useful if you wish to use your own SuperCollider synthesiser designs within Sonic Pi.

**Important notes**

- The binary file containing the synth design must have the extension .scsyndef.
- You may not trigger external synthdefs unless you enable the following GUI preference: Studio -&gt; Synths and FX -&gt; Enable external synths and FX
- If you wish your synth to work with Sonic Pi's automatic stereo sound infrastructure you need to ensure your synth outputs a stereo signal to an audio bus with an index specified by a synth arg named out_bus. Also, Sonic Pi makes no automatic attempt to free a synth once triggered, so to behave like the built-in synths, your synth needs to automatically free itself. For example, the following synth would work nicely:

```supercollider
(
SynthDef(\piTest,
         {|freq = 200, amp = 1, out_bus = 0 |
           Out.ar(out_bus,
                  SinOsc.ar([freq,freq],0,0.5)* Line.kr(1, 0, 5, amp, doneAction: 2))}
).writeDefFile("/Users/sam/Desktop/")
)
```

## Introduced in v4.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>load_synthdef "~/Desktop/my_noises/whoosh.scsyndef"</code></pre></td>
<td># Load whoosh synthdef design.</td>
</tr>
</table>
