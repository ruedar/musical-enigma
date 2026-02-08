# Euclidean distribution for beats

## Uso

```ruby
spread  num_accents (number), size (number)
```

Creates a new ring of boolean values which space a given number of accents as evenly as possible throughout a bar. This is an implementation of the process described in ‘The Euclidean Algorithm Generates Traditional Musical Rhythms’ (Toussaint 2005).

## Introduced in v2.4

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>(spread 3, 8)</code></pre></td>
<td>#=&gt; (ring true, false, false, true, false, false, true, false) a spacing of 332</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>(spread 3, 8, rotate: 1)</code></pre></td>
<td>#=&gt; (ring true, false, false, true, false, true, false, false) a spacing of 323</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :euclid_beat do
    sample :elec_bong, amp: 1.5 if (spread 3, 8).tick
    sample :perc_snap, amp: 0.8 if (spread 7, 11).look
    sample :bd_haus, amp: 2 if (spread 1, 4).look
    sleep 0.125
  end</code></pre></td>
<td># Easily create interesting polyrhythmic beats<br>
 <br>
# Spread 3 bongs over 8<br>
# Spread 7 snaps over 11<br>
# Spread 1 bd over 4</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>(spread 2, 5) 
  (spread 3, 4) 
                
  (spread 3, 5) 
                
                
  (spread 3, 7) 
  (spread 3, 8) 
  (spread 4, 7) 
  (spread 4, 9) 
  (spread 4, 11)
  (spread 5, 6) 
                
  (spread 5, 7) 
  (spread 5, 8) 
  (spread 5, 9) 
  (spread 5, 11)
                
  (spread 5, 12)
                
  (spread 5, 16)
  (spread 7, 8) 
  (spread 7, 12)
  (spread 7, 16)
  (spread 9, 16)
  (spread 11, 24)
  (spread 13, 24)</code></pre></td>
<td># Spread descriptions from<br>
# 'The Euclidean Algorithm Generates Traditional Musical Rhythms' (Toussaint 2005).<br>
# A thirteenth century Persian rhythm called Khafif-e-ramal.<br>
# The archetypal pattern of the Cumbria from Columbia, as well<br>
# as a Calypso rhythm from Trinidad<br>
# When started on the second onset, is another thirteenth<br>
# century Persian rhythm by the name of Khafif-e-ramal, as well<br>
# as a Romanian folk-dance rhythm.<br>
# A ruchenitza rhythm used in a Bulgarian folk-dance.<br>
# The Cuban tresillo pattern<br>
# Another Ruchenitza Bulgarian folk-dance rhythm<br>
# The Aksak rhythm of Turkey.<br>
# The metric pattern used by Frank Zappa in his piece Outside Now<br>
# Yields the York-Samai pattern, a popular Arab rhythm, when<br>
# started on the second onset.<br>
# The Nawakhat pattern, another popular Arab rhythm.<br>
# The Cuban cinquillo pattern.<br>
# A popular Arab rhythm called Agsag-Samai.<br>
# The metric pattern used by Moussorgsky in Pictures at an<br>
# Exhibition<br>
# The Venda clapping pattern of a South African children's<br>
# song.<br>
# The Bossa-Nova rhythm necklace of Brazil.<br>
# A typical rhythm played on the Bendir (frame drum)<br>
# A common West African bell pattern.<br>
# A Samba rhythm necklace from Brazil.<br>
# A rhythm necklace used in the Central African Republic.<br>
# A rhythm necklace of the Aka Pygmies of Central Africa.<br>
# Another rhythm necklace of the Aka Pygmies of the upper<br>
# Sangha.</td>
</tr>
</table>
