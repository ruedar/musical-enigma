# Global Cent tuning

## Uso

```ruby
set_cent_tuning!  cent_shift (number)
```

Globally tune Sonic Pi to play with another external instrument.

Uniformly tunes your music by shifting all notes played by the specified number of cents. To shift up by a cent use a cent tuning of 1. To shift down use negative numbers. One semitone consists of 100 cents.

See `use_cent_tuning` for setting the cent tuning value locally for a specific thread or `live_loop`. This is a global value and will shift the tuning for *all* notes. It will also persist for the entire session.

Important note: the cent tuning set by `set_cent_tuning!` is independent of any thread-local cent tuning values set by `use_cent_tuning` or `with_cent_tuning`.

## Introduced in v2.10

## Example

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>play 50
set_cent_tuning! 1
play 50</code></pre></td>
<td># Plays note 50<br>
 <br>
# Plays note 50.01</td>
</tr>
</table>
