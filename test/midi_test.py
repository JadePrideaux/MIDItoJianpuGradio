import unittest
from code.midi import get_midi_channels, midi_to_jianpu_str


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

  def test_velocity_zero_as_note_off(self):
    midi = DummyMIDI([
        DummyMessage(62, 0, velocity=64, time=0),
        DummyMessage(62, 0, velocity=0, type="note_on", time=1),
    ])
    result = midi_to_jianpu_str(midi, 0)  # type: ignore
    self.assertIn("-", result)

  def test_zero_time_note_off_ignored(self):
    midi = DummyMIDI([
        DummyMessage(62, 0, time=0),
        DummyMessage(62, 0, type="note_off", time=0),
    ])
    result = midi_to_jianpu_str(midi, 0)  # type: ignore
    self.assertNotIn("-", result)

  def test_timing_affects_output(self):
    midi = DummyMIDI([
        DummyMessage(62, 0, time=0),
        DummyMessage(62, 0, type="note_off", time=3),
        DummyMessage(0, 0, velocity=0, time=1)
    ])
    result = midi_to_jianpu_str(midi, 0, time_interval=1)  # type: ignore
    self.assertEqual(result, "[1] [---] [-]")

  def test_channel_filtering(self):
    result = midi_to_jianpu_str(self.test_midi, 0)  # type: ignore
    self.assertNotIn("2", result)