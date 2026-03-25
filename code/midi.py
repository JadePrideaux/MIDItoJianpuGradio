from code.logic import calculate_offset, midi_note_to_jianpu, transpose
from tempfile import _TemporaryFileWrapper

import mido


def load_midi_file(file: _TemporaryFileWrapper) -> mido.MidiFile:
  '''Loads a MIDI file'''
  return mido.MidiFile(file.name)

def check_channel(midi: mido.MidiFile, channel: int) -> bool:
  '''Returns true if the channel exists in the midi file'''
  return channel in get_midi_channels(midi)

def midi_to_jianpu_str(midi: mido.MidiFile, channel: int = 0, semitone_offset: int = 0, octave_offset: int = 0) -> str:
  '''Get notes in jianpu notation as a string from a given channel in a MIDI file.'''

  if not check_channel(midi, channel):
    return f"Channel {channel} does not exist in this MIDI file."

  offset = calculate_offset(semitone_offset, octave_offset)

  notes = extract_notes(midi, channel, offset)
  return " ".join(notes)

def extract_notes(midi: mido.MidiFile, channel: int, offset: int) -> list[str]:
  '''Gets a list of notes from the given midi file from the selected channel with an offset.'''
  notes = []
  for message in midi:
    if message.type == "note_on" and message.velocity > 0 and message.channel == channel:
      note = transpose(message.note, offset)
      notes.append(midi_note_to_jianpu(note))
  return notes

def get_midi_channels(midi: mido.MidiFile) -> set[int]:
  """Return a set of all channels used in the MIDI file."""
  return {
    msg.channel
    for track in midi.tracks
    for msg in track
    if hasattr(msg, "channel")
  }