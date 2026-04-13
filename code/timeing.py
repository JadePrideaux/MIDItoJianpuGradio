import mido


def get_time_in_beats(midi: mido.MidiFile, ticks: int) -> float:
  return ticks / midi.ticks_per_beat