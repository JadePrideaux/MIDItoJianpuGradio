from code.logic import midi_note_to_jianpu, transpose
from tempfile import _TemporaryFileWrapper

import mido


def load_midi_file(file: _TemporaryFileWrapper) -> mido.MidiFile:
  '''Loads a MIDI file'''
  return mido.MidiFile(file.name)


def midi_to_jianpu_str(midi: mido.MidiFile, channel: int = 0, offset: int = 0) -> str:
  '''Get notes in jianpu notation as a string from a given channel in a MIDI file.'''

  if channel not in get_midi_channels(midi):
    return f"Channel {channel} does not exist in this MIDI file."

  output = []
  for message in midi:
    if message.type == "note_on" and message.velocity > 0:
      if message.channel == channel:
        note = transpose(message.note, offset)
        output.append(midi_note_to_jianpu(note))
  return " ".join(output)

def get_midi_channels(midi: mido.MidiFile) -> set[int]:
  """Return a set of all channels used in the MIDI file."""
  return {
    msg.channel
    for track in midi.tracks
    for msg in track
    if hasattr(msg, "channel")
  }