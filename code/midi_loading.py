from tempfile import _TemporaryFileWrapper

import mido


def load_midi_file(file: _TemporaryFileWrapper) -> mido.MidiFile:
  '''Loads a MIDI file'''
  return mido.MidiFile(file.name)