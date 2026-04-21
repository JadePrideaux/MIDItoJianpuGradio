from code.protocols.protocols import MidiFile


def get_time_in_beats(midi: MidiFile, ticks: int) -> float:
  return ticks / midi.ticks_per_beat