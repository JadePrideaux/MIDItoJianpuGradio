import unittest
from code.midi_to_string import midi_to_jianpu_str
from test.dummy_objects import make_dummy_midi


class MidiToJianpuTest(unittest.TestCase):
  
  def setUp(self):
    self.test_midi = make_dummy_midi()

  def test_midi_to_jianpu_str(self):
    # using a fake midi file so types dont need to match
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 0), "[1] [3]")
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 1), "[2]")

  def test_invalid_channel(self):
    result = midi_to_jianpu_str(self.test_midi, 12)
    self.assertEqual(result, "Channel 12 does not exist in this MIDI file.")

  def test_channel_filtering(self):
    result = midi_to_jianpu_str(self.test_midi, 0)
    self.assertNotIn("2", result)
