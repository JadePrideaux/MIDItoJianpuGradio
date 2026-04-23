from code.protocols.protocols import MidiFile, MidiMessage
from typing import Iterator


class DummyMessage:
  def __init__(
      self,
      note : int,
      channel : int,
      velocity: int = 64,
      type: str = "note_on",
      time: int = 0
  ) -> None:
    self.note = note
    self.channel = channel
    self.velocity = velocity
    self.type = type
    self.time = time

class DummyMIDI:
  def __init__(
      self,
      tracks: list[list[MidiMessage]],
      ticks_per_beat: int = 100
    ) -> None:
    self.tracks = tracks
    self.ticks_per_beat = ticks_per_beat

  def __iter__(self) -> Iterator[MidiMessage]:
    return iter(self.tracks[0])

def make_dummy_midi() -> MidiFile:
  return DummyMIDI([[
    DummyMessage(62, 0),
    DummyMessage(64, 1),
    DummyMessage(66, 0)
  ]])

def make_dummy_message(
    note=62,
    channel=0,
    velocity=64,
    type="note_on",
    time: int = 10
    ) -> MidiMessage:
  return DummyMessage(
    note = note,
    channel = channel,
    velocity=velocity,
    type=type,
    time=time
  )