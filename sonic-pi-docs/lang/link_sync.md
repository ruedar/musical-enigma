# Use Ableton Link network metronome with automatic session and phase syncing

## Uso

```ruby
link_sync  quantum (number), phase (number)
```

Similar to link except it also waits for the link session to be playing. If it is, then it behaves identially to link. If the session is not playing, then link_sync will first wait until the session has started before then continuing as if just link had been called.

See link for further details and usage.

## Introduced in v4.0

## Example

See link for usage examples; link_sync works the same way but also waits for the Link session to be playing.
