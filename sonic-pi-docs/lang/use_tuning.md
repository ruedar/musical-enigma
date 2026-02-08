# Use alternative tuning systems

## Uso

```ruby
use_tuning  tuning (symbol), fundamental_note (symbol_or_number)
```

In most music we make semitones by dividing the octave into 12 equal parts, which is known as equal temperament. However there are lots of other ways to tune the 12 notes. This method adjusts each midi note into the specified tuning system. Because the ratios between notes aren’t always equal, be careful to pick a centre note that is in the key of the music you’re making for the best sound. Currently available tunings are `:just`, `:pythagorean`, `:meantone` and the default of `:equal`

## Introduced in v2.6

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play :e4
use_tuning :just, :c
play :e4

play 64</code></pre></td>
<td># Plays note 64<br>
 <br>
# Plays note 63.8631<br>
# transparently changes midi notes too<br>
# Plays note 63.8631</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>play 64
use_tuning :just
play 64
use_tuning :equal
play 64</code></pre></td>
<td># You may change the tuning multiple times:<br>
# Plays note 64<br>
 <br>
# Plays note 63.8631<br>
 <br>
# Plays note 64</td>
</tr>
</table>
