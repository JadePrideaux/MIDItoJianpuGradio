from typing import Iterator, Protocol


class MidiMessage(Protocol):
  note: int
  channel: int
  velocity: int
  type: str
  time: int

class MidiFile(Protocol):
  tracks: list[list[MidiMessage]]
  ticks_per_beat: int

  def __iter__(self) -> Iterator[MidiMessage]: ...