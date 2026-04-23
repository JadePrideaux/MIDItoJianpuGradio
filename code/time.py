from code.protocols.protocols import MidiMessage


def ticks_to_beats(ticks: int, ticks_per_beat: int) -> float:
  return round(ticks / ticks_per_beat)

def get_time(message: MidiMessage) -> float:
  return message.time

# time = ticks since previous message
# accumulated time = sum of all previous time values
# note duration: note_off current time - note_on current time (store note values that have started playing in a set)
# rest duration: note_on current time - note_off current time (regardless of note value)