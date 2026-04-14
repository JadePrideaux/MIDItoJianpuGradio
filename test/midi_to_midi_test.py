import os
import unittest
from code.midi_to_midi import generate_new_midi, get_new_midi

import mido


class MidiToMidiTest(unittest.TestCase):
  def setUp(self):
      # Create a simple MIDI file with one track and a few messages
      self.midi = mido.MidiFile()
      track = mido.MidiTrack()
      self.midi.tracks.append(track)

      # Add messages on two channels
      track.append(mido.Message('note_on', note=60, velocity=64, time=0, channel=0))
      track.append(mido.Message('note_off', note=60, velocity=64, time=10, channel=0))
      track.append(mido.Message('note_on', note=62, velocity=64, time=0, channel=1))
      track.append(mido.Message('note_off', note=62, velocity=64, time=10, channel=1))

  def test_generate_new_midi_filters_channel(self):
    new_midi = generate_new_midi(self.midi, channel=0, offset=0)

    for track in new_midi.tracks:
      for msg in track:
        if msg.type in ['note_on', 'note_off']:
          self.assertEqual(msg.channel, 0)

  def test_generate_new_midi_applies_offset(self):
    offset = 2
    new_midi = generate_new_midi(self.midi, channel=0, offset=offset)

    notes = [
      msg.note
      for track in new_midi.tracks
      for msg in track
      if msg.type == 'note_on'
    ]

    self.assertIn(62, notes)

  def test_generate_new_midi_removes_other_channels(self):
    new_midi = generate_new_midi(self.midi, channel=0, offset=0)

    notes = [
      msg.note
      for track in new_midi.tracks
      for msg in track
      if msg.type == 'note_on'
    ]

    self.assertNotIn(62, notes)

  def test_get_new_midi_creates_file(self):
    file_path = get_new_midi(self.midi, channel=0, offset=0)

    self.assertTrue(os.path.exists(file_path))

    os.remove(file_path)