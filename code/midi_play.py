import mido


def midi_to_audio(
  midi: mido.MidiFile,
  channel: int = 0,
  semitone_offset: int = 0,
  octave_offset: int = 0
  ):
  '''Converts the original midi file into a playable audio file based on the users settings.'''
  pass

def generate_midi(
  midi: mido.MidiFile,
  channel: int = 0,
  offset: int = 0
): # -> mido.MidiFile
  '''Generates a midi file based on an original midi file and given parameters (channel and offset)'''
  pass

def generate_audio(
  midi: mido.MidiFile
):
  '''Generates and audio file based on a given midi file'''
  pass