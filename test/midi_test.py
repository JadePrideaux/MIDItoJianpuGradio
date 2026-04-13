import unittest
from code.midi_channels import get_midi_channels
from code.midi_to_string import midi_to_jianpu_str


class DummyMessage:
    def __init__(self, note, channel, velocity=64, type="note_on", time=0):
        self.note = note
        self.channel = channel
        self.velocity = velocity
        self.type = type
        self.time = time

class DummyMIDI:
    def __init__(self, messages):
        self.tracks = [messages]

    def __iter__(self):
        return iter(self.tracks[0])

class TestMIDI(unittest.TestCase):
  
  test_midi = DummyMIDI([
      DummyMessage(62, 0),
      DummyMessage(64, 1),
      DummyMessage(66, 0)
    ])

  def test_midi_to_jianpu_str(self):
    # using a fake midi file so types dont need to match
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 0), "[1] [3]") # type: ignore
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 1), "[2]") # type: ignore

  def test_get_midi_channels(self):
    self.assertEqual(get_midi_channels(self.test_midi), {0, 1})  # type: ignore

  def test_invalid_channel(self):
    result = midi_to_jianpu_str(self.test_midi, 12)  # type: ignore
    self.assertEqual(result, "Channel 12 does not exist in this MIDI file.")

  def test_channel_filtering(self):
    result = midi_to_jianpu_str(self.test_midi, 0)  # type: ignore
    self.assertNotIn("2", result)