import unittest
from code.midi_channels import get_midi_channels
from test.dummy_objects import make_dummy_midi


class MidiChannelsTest(unittest.TestCase):

  def setUp(self):
    self.test_midi = make_dummy_midi()

  def test_get_midi_channels(self):
    self.assertEqual(get_midi_channels(self.test_midi), {0, 1})