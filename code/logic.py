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