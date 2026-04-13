from code.constants import SCALE_MAP, TONIC


def midi_note_to_jianpu(note: int) -> str:
  '''Given a MIDI note value, return its jianpu representation.'''
  relative = (note - TONIC) % 12
  octave = (note - TONIC) // 12

  degree = SCALE_MAP.get(relative, "?")

  if octave > 0:
    degree = "·" * octave + degree
  elif octave < 0:
    degree = degree + "·" * (-octave)

  return degree

def transpose(value: int, offset: int) -> int:
  '''Given a MIDI value, transpose it by the given number of semitones and return the resulting value.'''
  return value + offset

def calculate_offset(semitones: int, octaves: int) -> int:
  '''Calculate the offset in semitones by adding the octaves and semitone offsets.'''
  return (octaves * 12) + semitones