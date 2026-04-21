from code.protocols.protocols import MidiFile

import mido


def check_channel_exists(midi: MidiFile, channel: int) -> bool:
  '''Returns true if the channel exists in the midi file'''
  return channel in get_midi_channels(midi)

def get_midi_channels(midi: MidiFile) -> set[int]:
  """Return a set of all channels used in the MIDI file."""
  return {
    msg.channel
    for track in midi.tracks
    for msg in track
    if hasattr(msg, "channel")
  }