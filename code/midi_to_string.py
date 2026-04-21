from code.jianpu_string_formatter import get_note_string, get_rest_string
from code.message_checks import is_correct_channel, is_note, is_rest
from code.midi_channels import check_channel_exists
from code.protocols.protocols import MidiFile

import mido


def midi_to_jianpu_str(
    midi: MidiFile,
    channel: int = 0,
    offset: int = 0,
  ) -> str:
  '''Get notes in jianpu notation as a string from a given channel in a MIDI file.'''

  if not check_channel_exists(midi, channel):
    return f"Channel {channel} does not exist in this MIDI file."

  notes = extract_notes(midi, channel, offset)
  return " ".join(notes)

def extract_notes(midi: MidiFile, channel: int, offset: int) -> list[str]:
  '''Gets a list of notes from the given midi file from the selected channel with an offset.'''
  notes = []
  for track in midi.tracks:
    for message in track:
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
        notes.append(get_rest_string(beats))
  return notes