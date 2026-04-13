import math
from code.logic import calculate_offset, midi_note_to_jianpu, transpose
from tempfile import _TemporaryFileWrapper
from typing import Any, cast

import mido


def load_midi_file(file: _TemporaryFileWrapper) -> mido.MidiFile:
  '''Loads a MIDI file'''
  return mido.MidiFile(file.name)

def check_channel_exists(midi: mido.MidiFile, channel: int) -> bool:
  '''Returns true if the channel exists in the midi file'''
  return channel in get_midi_channels(midi)

def midi_to_jianpu_str(
    midi: mido.MidiFile,
    channel: int = 0,
    offset: int = 0,
  ) -> str:
  '''Get notes in jianpu notation as a string from a given channel in a MIDI file.'''

  if not check_channel_exists(midi, channel):
    return f"Channel {channel} does not exist in this MIDI file."

  notes = extract_notes(midi, channel, offset)
  return " ".join(notes)

def get_time_in_beats(midi: mido.MidiFile, ticks: int) -> float:
  return ticks / midi.ticks_per_beat

def extract_notes(midi: mido.MidiFile, channel: int, offset: int) -> list[str]:
  '''Gets a list of notes from the given midi file from the selected channel with an offset.'''
  notes = []
  for message in midi:
    # if the message is not in the elected channel, skip it
    if not is_correct_channel(message, channel):
      continue
    # if it is a note:
    if is_note(message):
      beats = 1
      notes.append(get_note_string(message, offset, beats))
    # if it is a rest
    elif is_rest(message):
      beats = 1
      notes.append(get_rest_string(message, beats))
  return notes

def is_note(message: mido.Message) -> bool:
  return getattr(message, "type") == "note_on" and getattr(message, "velocity") > 0
    
def is_rest(message: mido.Message) -> bool:
  return getattr(message, "type") == "note_off" or (getattr(message, "type") == "note_on" and getattr(message, "velocity") == 0)

def is_correct_channel(message: mido.Message, channel: int) -> bool:
  '''Check if the message is in the selected channel'''
  if not hasattr(message, "channel"):
    return False
  return cast(Any, message).channel == channel

def get_note_string(message: mido.Message, offset: int, beats: int) -> str:
  note = transpose(getattr(message, "note"), offset)
  value = str(midi_note_to_jianpu(note))
  return wrap_value(value, get_time_space(beats))

def get_rest_string(message: mido.Message, beats: int) -> str:
  return wrap_value("", get_time_space(beats))

def get_time_space(beats: float) -> str:
  time_string = ""
  for _ in range(math.ceil(beats) - 1):
    time_string += "-"
  return time_string

def wrap_value(note: str, time_space: str) -> str:
  '''Wraps the note and time_space values'''
  if not time_space:
    return "[" + note + "]"
  if not note:
    return "[" + time_space + "]"
  else:
    return "[" + note + "|" + time_space + "]"

def get_midi_channels(midi: mido.MidiFile) -> set[int]:
  """Return a set of all channels used in the MIDI file."""
  return {
    msg.channel
    for track in midi.tracks
    for msg in track
    if hasattr(msg, "channel")
  }
