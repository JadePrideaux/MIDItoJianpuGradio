import math
from code.note_conversion import midi_note_to_jianpu, transpose
from code.protocols.protocols import MidiMessage

import mido


def get_note_string(message: MidiMessage, offset: int, beats: int) -> str:
  note = transpose(getattr(message, "note"), offset)
  value = str(midi_note_to_jianpu(note))
  return wrap_value(value, get_time_space(beats))

def get_rest_string(beats: int) -> str:
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