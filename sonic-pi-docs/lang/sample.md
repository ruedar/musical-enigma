# Trigger sample

## Uso

```ruby
sample  name_or_path (symbol_or_string)
```

Play back a recorded sound file (sample). Sonic Pi comes with lots of great samples included (see the section under help) but you can also load and play `.wav`, `.wave`, `.aif`, `.aiff`, `.ogg`, `.oga` or `.flac` files from anywhere on your computer too. To play a built-in sample use the corresponding keyword such as `sample :bd_haus`. To play any file on your computer use a full path such as `sample "/path/to/sample.wav"`.

There are many opts for manipulating the playback. For example, the `rate:` opt affects both the speed and the pitch of the playback. To control the rate of the sample in a pitch-meaningful way take a look at the `rpitch:` opt.

The sampler synth has three separate envelopes - one for amplitude, one for a low pass filter and another for a high pass filter. These work very similar to the standard synth envelopes except for two major differences. Firstly, the envelope times do not stretch or shrink to match the BPM. Secondly, the sustain time by default stretches to make the envelope fit the length of the sample. This is explained in detail in the tutorial.

Samples are loaded on-the-fly when first requested (and subsequently remembered). If the sample loading process takes longer than the schedule ahead time, the sample trigger will be skipped rather than be played late and out of time. To avoid this you may preload any samples you wish to work with using `load_sample` or `load_samples`.

It is possible to set the `start:` and `finish:` positions within the sample to play only a sub-section of it. These values can be automatically chosen based on an onset detection algorithm which will essentially isolate each individual drum or synth hit in the sample and let you access each one by an integer index (floats will be rounded to the nearest integer value). See the `onset:` docstring and examples for more information.

Finally, the sampler supports a powerful filtering system to make it easier to work with large folders of samples. The filter commands must be used before the first standard opt. There are six kinds of filter parameters you may use:

By combining commands which add to the candidates and then filtering those candidates it is possible to work with folders full of samples in very powerful ways. Note that the specific ordering of filter parameters is irrelevant with the exception of the numbers - in which case the last number is the index. All the candidates will be gathered first before the filters are applied.

## Introduced in v2.0

## Examples

<table>
<tr>
<th colspan="2"># Example 1</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen</code></pre></td>
<td># Play a built-in sample<br>
# Plays the Amen break</td>
</tr>
<tr>
<th colspan="2"># Example 2</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen
sample :ambi_lunar_land</code></pre></td>
<td># Play two samples at the same time<br>
# with incredible timing accuracy<br>
 <br>
# Note, for timing guarantees select the pref:<br>
#   Studio -&gt; Synths and FX -&gt; Enforce timing guarantees</td>
</tr>
<tr>
<th colspan="2"># Example 3</th>
</tr>
<tr>
<td><pre><code>live_loop :bass do
  sample :bd_haus
  sleep 0.5
end</code></pre></td>
<td># Create a simple repeating bass drum</td>
</tr>
<tr>
<th colspan="2"># Example 4</th>
</tr>
<tr>
<td><pre><code>live_loop :rhythm do
  sample :tabla_ghe3 if (spread 5, 7).tick
  sleep 0.125
end
live_loop :bd, sync: :rhythm do
  sample :bd_haus, lpf: 90, amp: 2
  sleep 0.5
end</code></pre></td>
<td># Create a more complex rhythm with multiple live loops:</td>
</tr>
<tr>
<th colspan="2"># Example 5</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, rate: 0.5</code></pre></td>
<td># Change the playback speed of the sample using rate:<br>
# Play the Amen break at half speed<br>
# for old school hip-hop</td>
</tr>
<tr>
<th colspan="2"># Example 6</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, rate: 1.5</code></pre></td>
<td># Speed things up<br>
# Play the Amen break at 1.5x speed<br>
# for a jungle/gabba sound</td>
</tr>
<tr>
<th colspan="2"># Example 7</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, rate: -1</code></pre></td>
<td># Go backwards<br>
# Negative rates play the sample backwards</td>
</tr>
<tr>
<th colspan="2"># Example 8</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, rate: -3</code></pre></td>
<td># Fast rewind<br>
# Play backwards at 3x speed for a fast rewind effect</td>
</tr>
<tr>
<th colspan="2"># Example 9</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, start: 0.5</code></pre></td>
<td># Start mid sample<br>
# Start playback half way through</td>
</tr>
<tr>
<th colspan="2"># Example 10</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, finish: 0.5</code></pre></td>
<td># Finish mid sample<br>
# Finish playback half way through</td>
</tr>
<tr>
<th colspan="2"># Example 11</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, start: 0.125, finish: 0.25</code></pre></td>
<td># Play part of a sample<br>
# Play the second eighth of the sample</td>
</tr>
<tr>
<th colspan="2"># Example 12</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, start: 0.25, finish: 0.125</code></pre></td>
<td># Finishing before the start plays backwards<br>
# Play the second eighth of the sample backwards</td>
</tr>
<tr>
<th colspan="2"># Example 13</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, start: 0.125, finish: 0.25, rate: -0.25</code></pre></td>
<td># Play a section of a sample at quarter speed backwards<br>
# Play the second eighth of the<br>
# amen break backwards at a<br>
# quarter speed</td>
</tr>
<tr>
<th colspan="2"># Example 14</th>
</tr>
<tr>
<td><pre><code>s = sample :loop_amen, lpf: 70
sleep 0.5
control s, lpf: 130
sleep 0.5
synth :dsaw, note: :e3</code></pre></td>
<td># Control a sample synchronously<br>
 <br>
 <br>
 <br>
 <br>
# This is triggered 1s from start</td>
</tr>
<tr>
<th colspan="2"># Example 15</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, lpf: 70 do |s|
  sleep 1                               
  control s, lpf: 130                   
end
sleep 0.5
synth :dsaw, note: :e3</code></pre></td>
<td># Controlling a sample asynchronously<br>
 <br>
# This block is run in an implicit in_thread<br>
# and therefore is asynchronous<br>
 <br>
 <br>
# This is triggered 0.5s from start</td>
</tr>
<tr>
<th colspan="2"># Example 16</th>
</tr>
<tr>
<td><pre><code>sample :loop_garzul, slice: 0     
sleep 0.5
4.times do
  sample :loop_garzul, slice: 1   
  sleep 0.125
end
sample :loop_garzul, slice: 4, num_slices: 4, rate: -1</code></pre></td>
<td># Play with slices<br>
# =&gt; play the first 16th of the sample<br>
 <br>
 <br>
# =&gt; play the second 16th of the sample 4 times<br>
 <br>
 <br>
# =&gt; play the final quarter backwards</td>
</tr>
<tr>
<th colspan="2"># Example 17</th>
</tr>
<tr>
<td><pre><code>use_sample_bpm :loop_amen                   
live_loop :beat_slicer do
  n = 8                                     
                                            
  s = rand_i n                              
  sample :loop_amen, slice: s, num_slices: n
  sleep 1.0/n                               
end</code></pre></td>
<td># Build a simple beat slicer<br>
# Set the BPM to match the amen break sample<br>
 <br>
# Specify number of slices<br>
# (try changing to 2, 4, 6, 16 or 32)<br>
# Choose a random slice within range<br>
# Play the specific part of the sample<br>
# Sleep for the duration of the slice</td>
</tr>
<tr>
<th colspan="2"># Example 18</th>
</tr>
<tr>
<td><pre><code>sample :loop_amen, lpf: 80, hpf: 70, compress: 1, pre_amp: 10</code></pre></td>
<td># Play with the built-in low pass filter, high pass filter and compressor<br>
# Make the amen break sound punchy.</td>
</tr>
<tr>
<th colspan="2"># Example 19</th>
</tr>
<tr>
<td><pre><code>sample :loop_garzul, lpf_attack: 8
sleep 8
sample :loop_garzul, hpf_attack: 8</code></pre></td>
<td># Use the cutoff filter envelopes<br>
# Sweep the low pass filter up over 8 beats<br>
 <br>
# Sweep the high pass filter down over 8 beats</td>
</tr>
<tr>
<th colspan="2"># Example 20</th>
</tr>
<tr>
<td><pre><code>puts sample_duration :loop_industrial                  
puts sample_duration :loop_industrial, beat_stretch: 1 
live_loop :industrial do
  sample :loop_industrial, beat_stretch: 1             
  sleep 1                                              
                                                       
                                                       
end</code></pre></td>
<td># Sample stretching<br>
# =&gt; 0.88347<br>
# =&gt; 1<br>
 <br>
# Stretch the sample to make it 1 beat long<br>
# This now loops perfectly.<br>
# However, note that stretching/shrinking<br>
# also modifies the pitch.</td>
</tr>
<tr>
<th colspan="2"># Example 21</th>
</tr>
<tr>
<td><pre><code>puts sample_duration :loop_garzul                      
puts sample_duration :loop_garzul, beat_stretch: 6     
live_loop :garzul do
  sample :loop_garzul, beat_stretch: 6                 
                                                       
                                                       
  sleep 6
end</code></pre></td>
<td># Sample shrinking<br>
# =&gt; 8<br>
# =&gt; 6<br>
 <br>
# As :loop_garzul is longer than 6 beats<br>
# it is shrunk to fit. This increases the<br>
# pitch.</td>
</tr>
<tr>
<th colspan="2"># Example 22</th>
</tr>
<tr>
<td><pre><code>use_bpm 30                                             
puts sample_duration :loop_garzul                      
puts sample_duration :loop_garzul, beat_stretch: 6     
live_loop :garzul do
  sample :loop_garzul, beat_stretch: 6                 
  sleep 6
end</code></pre></td>
<td># Sample stretching matches the BPM<br>
# Set the BPM to 30<br>
# =&gt; 4.0 (at 30 BPM the sample lasts for 4 beats)<br>
# =&gt; 6.0<br>
 <br>
# The sample is stretched to match 6 beats at 30 BPM</td>
</tr>
<tr>
<th colspan="2"># Example 23</th>
</tr>
<tr>
<td><pre><code>sample "/path/to/sample.wav"</code></pre></td>
<td># External samples<br>
# Play any Wav, Aif, Ogg, Oga, or FLAC sample on your computer<br>
# by simply passing a string representing the full<br>
# path</td>
</tr>
<tr>
<th colspan="2"># Example 24</th>
</tr>
<tr>
<td><pre><code>dir = "/path/to/dir/of/samples"                      
sample dir                                             
                                                       
sample dir, 1                                          
sample dir, 99                                         
                                                       
                                                       
                                                       
                                                       
sample dir, "120"                                    
                                                       
                                                       
sample dir, "120", 1                                 
                                                       
                                                       
sample dir, /beat[0-9]/                                
                                                       
                                                       
                                                       
                                                       
sample dir, /beat[0-9]0/, "100"</code></pre></td>
<td># Sample pack filtering<br>
# You can easily work with a directory of samples<br>
# Play the first sample in the directory<br>
# (it is sorted alphabetically)<br>
# Play the second sample in the directory<br>
# Play the 100th sample in the directory, or if there<br>
# are fewer, treat the directory like a ring and keep<br>
# wrapping the index round until a sample is found.<br>
# For example, if there are 90 samples, the 10th sample<br>
# is played (index 9).<br>
# Play the first sample in the directory that contains<br>
# the substring "120".<br>
# For example, this may be "beat1_120_rave.wav"<br>
# Play the second sample in the directory that contains<br>
# the substring "120".<br>
# For example, this may be "beat2_120_rave.wav"<br>
# Play the first sample in the directory that matches<br>
# the regular expression /beat[0-9]/.<br>
# For example, this may be "beat0_100_trance.wav"<br>
# You may use the full power of Ruby's regular expression<br>
# system here: http://ruby-doc.org/core-2.1.1/Regexp.html<br>
# Play the first sample in the directory that both matches<br>
# the regular expression /beat[0-9]0/ and contains the<br>
# the substring "100".<br>
# For example, this may be "beat10_100_rave.wav"</td>
</tr>
<tr>
<th colspan="2"># Example 25</th>
</tr>
<tr>
<td><pre><code>sample "tabla_"                                      
                                                       
sample "tabla_", 2</code></pre></td>
<td># Filtering built-in samples<br>
# If you don't pass a directory source, you can filter over<br>
# the built-in samples.<br>
# Play the first built-in sample that contains the substring<br>
# "tabla"<br>
# Play the third built-in sample that contains the substring<br>
# "tabla"</td>
</tr>
<tr>
<th colspan="2"># Example 26</th>
</tr>
<tr>
<td><pre><code>load_samples "tabla_"                                
                                                       
                                                       
live_loop :tabla do
  sample "tabla_", tick                              
  sleep 0.125
end</code></pre></td>
<td># Play with whole directories of samples<br>
# You may pass any of the source/filter options to load_samples<br>
# to load all matching samples. This will load all the built-in<br>
# samples containing the substring "tabla_"<br>
 <br>
# Treat the matching samples as a ring and tick through them</td>
</tr>
<tr>
<th colspan="2"># Example 27</th>
</tr>
<tr>
<td><pre><code>dir1 = "/path/to/sample/directory"
dir2 = "/path/to/other/sample/directory"
sample dir1, dir2, "foo"</code></pre></td>
<td># Specify multiple sources<br>
 <br>
 <br>
# Match the first sample that contains the string "foo" out of<br>
# all the samples in dir1 and dir2 combined.<br>
# Note that the sources must be listed before any filters.</td>
</tr>
<tr>
<th colspan="2"># Example 28</th>
</tr>
<tr>
<td><pre><code>dir = "/path/to/sample/directory"                    
                                                       
dir_recursive = "/path/to/sample/directory/**"       
                                                       
                                                       
sample dir, 0                                          
sample dir_recursive, 0</code></pre></td>
<td># List contents recursively<br>
# By default the list of all top-level samples within the directory<br>
# is considered.<br>
# However, if you finish your directory string with ** then if that<br>
# directory contains other directories then the samples within the<br>
# subdirectories and their subsubdirectories in turn are considered.<br>
# Play the first top-level sample in the directory<br>
# Play the first sample found after combining all samples found in<br>
# the directory and all directories within it recursively.<br>
# Note that if there are many sub directories this may take some time<br>
# to execute. However, the result is cached so subsequent calls will<br>
# be fast.</td>
</tr>
<tr>
<th colspan="2"># Example 29</th>
</tr>
<tr>
<td><pre><code>filter = lambda do |candidates|                        
  [candidates.choose]                                  
end                                                    
                                                       
8.times do
  sample "drum_", filter                             
  sleep 0.25                                           
end</code></pre></td>
<td># Bespoke filters<br>
# If the built-in String, Regexp and index filters are not sufficient<br>
# you may write your own. They need to be a function which takes a list<br>
# of paths to samples and return a list of samples. This one returns a<br>
# list of a single randomly selected sample.<br>
 <br>
# Play 8 randomly selected samples from the built-in sample set that also<br>
# contain the substring "drum_"</td>
</tr>
<tr>
<th colspan="2"># Example 30</th>
</tr>
<tr>
<td><pre><code>sample :loop_tabla, start: 0, finish: 0.00763          
                                                       
                                                       
sleep 1
                                                       
                                                       
sample :loop_tabla, onset: 0                           
                                                       
                                                       
sleep 1
sample :loop_tabla, onset: 1</code></pre></td>
<td># Basic Onset Detection<br>
# If you know the right start: and finish: values, you can extract a<br>
# single drum hit from a longer sample. However, finding these values<br>
# can be very time consuming.<br>
 <br>
# Instead of specifying the start: and finish: values manually you can<br>
# use the onset: option to find them for you using an integer index.<br>
# onset: 0 will set the start: and finish: values so that the first<br>
# percussive sound (something that shifts from quiet to loud quickly)<br>
# is picked out.<br>
 <br>
# We can easily find the second percussive sound in the sample with<br>
# onset: 1</td>
</tr>
<tr>
<th colspan="2"># Example 31</th>
</tr>
<tr>
<td><pre><code>live_loop :tabla do
  use_bpm 50                                           
  sample :loop_tabla, onset: tick                      
  sleep [0.125, 0.25].choose                           
end</code></pre></td>
<td># Ticking through onsets<br>
# The onsets are actually a ring so the index will wrap around. This<br>
# means that if there are only 8 onsets in a sample, specifying an<br>
# onset of 100 will still return one of the 8 onsets. This means we<br>
# can use tick to work through each onset in sequence. This allows us<br>
# to redefine the rhythm and tempo of a sample<br>
 <br>
# We can choose our own BPM here - it doesn't need to match the sample<br>
# tick through each onset in sequence<br>
# randomly choose a delay between onset triggers</td>
</tr>
<tr>
<th colspan="2"># Example 32</th>
</tr>
<tr>
<td><pre><code>use_bpm 50
live_loop :tabla do
  sample :loop_tabla, onset: pick                      
  sleep [0.125, 0.25].choose                           
end</code></pre></td>
<td># Random Onset Triggering<br>
# We can easily pick a random onset using the pick fn<br>
 <br>
 <br>
# Each time round the live loop we now trigger a random onset<br>
# creating an infinite stream of randomly selected drums</td>
</tr>
<tr>
<th colspan="2"># Example 33</th>
</tr>
<tr>
<td><pre><code>live_loop :tabla do
  use_random_seed 30000                                
  8.times do
    sample :loop_tabla, onset: pick
    sleep [0.125, 0.25].choose
  end
end</code></pre></td>
<td># Repeatable Random Onsets<br>
# Instead of an infinite stream of choices, we can combine iteration<br>
# and use_random_seed to create repeatable riffs:<br>
 <br>
# every 8 times, reset the random seed, this resets the riff</td>
</tr>
<tr>
<th colspan="2"># Example 34</th>
</tr>
<tr>
<td><pre><code>live_loop :tabla do
  sample :loop_tabla, onset: pick, sustain: 0, release: 0.1
                                                           
                                                           
                                                           
  sleep [0.125, 0.25].choose
end</code></pre></td>
<td>#  Random Onset Duration<br>
# Each onset has a variable length (determined by the sample contents).<br>
# Therefore, if you wish to ensure each onset has a specific length it<br>
# is necessary to use the sample's amplitude envelope.<br>
# As the sample's envelope automatically changes the sustain: value to<br>
# match the duration - you also need to override this with a value of 0.<br>
 <br>
# Each drum onset will now be no longer than 0.1. Note that the envelope<br>
# for a sample only determines the maximum duration of a sample trigger.<br>
# If the actual audible duration of the onset is smaller than 0.1 then<br>
# it will *not* be extended.</td>
</tr>
<tr>
<th colspan="2"># Example 35</th>
</tr>
<tr>
<td><pre><code>l = lambda {|c| puts c ; c[0]}                         
                                                       
                                                       
                                                       
sample :loop_tabla, onset: l</code></pre></td>
<td># Onset lambdas<br>
# The onset index can be a lambda as well as an integer. If a lambda is<br>
# given, it will be passed a ring of all of the onsets as an argument.<br>
# This will be a ring of maps:<br>
# define a lambda which accepts a single argument, prints it and<br>
# returns the first value. This particular example is essentially<br>
# the same as using onset: 0 with the side effect of also printing out<br>
# the full ring of onsets:<br>
# (ring {:start=&gt;0.0, :finish=&gt;0.0076}, {:start=&gt;0.0076, :finish 0.015}...)<br>
# We are therefore free to define this lambda to do anything we want.<br>
# This gives us very powerful control over the choice of onset. It is<br>
# unlikely you will use this frequently, but it is a powerful tool<br>
# that's there when you need it.</td>
</tr>
<tr>
<th colspan="2"># Example 36</th>
</tr>
<tr>
<td><pre><code>sample :loop_tabla, onset: 1</code></pre></td>
<td># Plays the 2nd onset (the first onset would have index 0)<br>
# Will override opts with: {start: 0.0151, finish: 0.0304}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)</td>
</tr>
<tr>
<th colspan="2"># Example 37</th>
</tr>
<tr>
<td><pre><code>sample :loop_tabla, onset: 1, slice: 0, num_slices: 1</code></pre></td>
<td># Plays the 2nd onset. This behaves the same as not specifying<br>
# a slice as we select the first of one slices.<br>
# Will override opts with: {start: 0.0151, finish: 0.0304}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)</td>
</tr>
<tr>
<th colspan="2"># Example 38</th>
</tr>
<tr>
<td><pre><code>sample :loop_tabla, onset: 1, slice: 0, num_slices: 2</code></pre></td>
<td># This plays the first half of the 2nd onset.<br>
# This is because  we split that onset into two slices and<br>
# play just the first slice (with index 0).<br>
# Will override opts with: {start: 0.0151, finish: 0.0227}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)</td>
</tr>
<tr>
<th colspan="2"># Example 39</th>
</tr>
<tr>
<td><pre><code>sample :loop_tabla, onset: 1, slice: 0, num_slices: 4               
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
sample :loop_tabla, onset: 1, slice: 0, num_slices: 4, finish: 0.5  
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
sample :loop_tabla, onset: 1, slice: 0, num_slices: 4, finish: 0.0, start: 0.5</code></pre></td>
<td># This plays the first quarter of the 2nd onset.<br>
# This is because we split that onset into four slices and<br>
# play just the first slice (with index 0).<br>
# Will override opts with: {start: 0.0151, finish: 0.0189}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)<br>
# Will play the first 1/8th of the 2nd onset.<br>
# This is because we split that specific onset into 4 slices<br>
# and then only play the first half of the first slice.<br>
# Will override opts with: {start: 0.0151, finish: 0.017}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)<br>
# Will play the first 1/8th of the 2nd onset backwards..<br>
# This is because we split that specific onset into 4 slices<br>
# and then only play from the first half of the first slice<br>
# back to the beginning.<br>
# Will override opts with: {start: 0.017, finish: 0.0151}<br>
# (these values are specific to the :loop_tabla sample and<br>
# will vary for different samples)</td>
</tr>
</table>
