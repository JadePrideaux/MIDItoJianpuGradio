import unittest
from code.midi import get_midi_channels, midi_to_jianpu_str


class DummyMessage:
    def __init__(self, note, channel, velocity=64, type="note_on"):
        self.note = note
        self.channel = channel
        self.velocity = velocity
        self.type = type

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
    ''''''
    # using a fake midi file so types dont need to match
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 0), "1 3") # type: ignore
    self.assertEqual(midi_to_jianpu_str(self.test_midi, 1), "2") # type: ignore

  def test_get_midi_channels(self):
    self.assertEqual(get_midi_channels(self.test_midi), {0, 1})  # type: ignore