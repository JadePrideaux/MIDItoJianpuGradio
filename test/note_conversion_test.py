import unittest
from code.note_conversion import (calculate_offset, midi_note_to_jianpu,
                                  transpose)


class NoteConversionTest(unittest.TestCase):

  def test_tonic(self):
    '''Test that the tonic is mapped correctly'''
    self.assertEqual(midi_note_to_jianpu(62), "1")

  def test_octaves(self):
    '''Test the octaves are mapped correctly'''
    self.assertEqual(midi_note_to_jianpu(74), "·1")
    self.assertEqual(midi_note_to_jianpu(50), "1·")

  def test_transpose(self):
    '''Test the value transposition'''
    self.assertEqual(transpose(60, 7), 67)
    self.assertEqual(transpose(60, -4), 56)

  def test_calculate_offset(self):
    '''Test the offset calculations'''
    self.assertEqual(calculate_offset(5, 0), 5)
    self.assertEqual(calculate_offset(4, -2), -20)
    self.assertEqual(calculate_offset(4, 3), 40)