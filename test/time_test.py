import unittest
from code.time import get_time, ticks_to_beats
from test.dummy_objects import make_dummy_message, make_dummy_midi


class TimeTest(unittest.TestCase):
  def setUp(self):
    self.test_midi = make_dummy_midi()
    self.test_message = make_dummy_message()

  def test_get_time(self):
    self.assertEqual(get_time(self.test_message), 10)

  def test_ticks_to_beats(self):
    self.assertEqual(ticks_to_beats(ticks = 100, ticks_per_beat = 100), 1)
    self.assertEqual(ticks_to_beats(ticks = 200, ticks_per_beat = 100), 2)
    self.assertEqual(ticks_to_beats(ticks = 400, ticks_per_beat = 100), 4)
    self.assertEqual(ticks_to_beats(ticks = 0, ticks_per_beat = 100), 0)
    self.assertEqual(ticks_to_beats(ticks = 140, ticks_per_beat = 100), 1)
    self.assertEqual(ticks_to_beats(ticks = 160, ticks_per_beat = 100), 2)
    