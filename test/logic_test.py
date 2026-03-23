import unittest
from code.logic import midi_note_to_jianpu


class TestLogic(unittest.TestCase):

  def test_tonic(self):
    '''Test that the tonic is mapped correctly'''
    self.assertEqual(midi_note_to_jianpu(62), "1")

  def test_octaves(self):
    '''Test the octaves are mapped correctly'''
    self.assertEqual(midi_note_to_jianpu(74), "·1")
    self.assertEqual(midi_note_to_jianpu(50), "1·")