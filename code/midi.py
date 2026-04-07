from code.logic import calculate_offset, midi_note_to_jianpu, transpose
from math import floor
from tempfile import _TemporaryFileWrapper

import mido


def load_midi_file(file: _TemporaryFileWrapper) -> mido.MidiFile:
  '''Loads a MIDI file'''
  return mido.MidiFile(file.name)

def check_channel(midi: mido.MidiFile, channel: int) -> bool:
  '''Returns true if the channel exists in the midi file'''
  return channel in get_midi_channels(midi)

def midi_to_jianpu_str(
    midi: mido.MidiFile,
    channel: int = 0,
    offset: int = 0,
    time_interval: int = 64
  ) -> str:
  '''Get notes in jianpu notation as a string from a given channel in a MIDI file.'''

  if not check_channel(midi, channel):
    return f"Channel {channel} does not exist in this MIDI file."

  notes = extract_notes(midi, channel, offset, time_interval)
  return " ".join(notes)

def extract_notes(midi: mido.MidiFile, channel: int, offset: int, time_interval: int) -> list[str]:
  '''Gets a list of notes from the given midi file from the selected channel with an offset.'''
  notes = []
  for message in midi:
    if not hasattr(message, "channel") or message.channel != channel:
      continue
    if message.type == "note_on" and message.velocity > 0:
      note = transpose(message.note, offset)
      time = message.time * time_interval
      value = wrap_value(str(midi_note_to_jianpu(note)), get_time_space(time, time_interval))
      notes.append(value)
    if (message.type == "note_off" or (message.type == "note_on" and message.velocity == 0)) and message.time != 0:
      time = message.time * time_interval
      value = wrap_value("", get_time_space(time, time_interval))
      notes.append(value)
  return notes

def wrap_value(note: str, time_space: str) -> str:
  '''Wraps the note and time_space values'''
  if not time_space:
    return "[" + note + "]"
  if not note:
    return "[" + time_space + "]"
  else:
    return "[" + note + "|" + time_space + "]"

def get_time_space(time: float, time_interval: int) -> str:
  time_string = ""
  for i in range(floor(time * time_interval)):
    time_string += "-"
  return time_string

def get_midi_channels(midi: mido.MidiFile) -> set[int]:
  """Return a set of all channels used in the MIDI file."""
  return {
    msg.channel
    for track in midi.tracks
    for msg in track
    if hasattr(msg, "channel")
  }