# Use new synth defaults

## Uso

```ruby
use_synth_defaults
```

Specify new default values to be used by all subsequent calls to `play`. Will remove and override any previous defaults.

## Introduced in v2.0

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
use_synth_defaults amp: 0.5, cutoff: 70
play 50
use_synth_defaults cutoff: 90
play 50</code></pre></td>
<td># plays note 50 with default arguments<br>
 <br>
# plays note 50 with an amp of 0.5, cutoff of 70 and defaults for rest of args<br>
 <br>
# plays note 50 with a cutoff of 90 and defaults for rest of args - note that amp is no longer 0.5</td>
</tr>
</table>
