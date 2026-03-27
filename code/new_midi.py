import tempfile

import mido


def get_new_midi(
  midi: mido.MidiFile,
  channel: int = 0,
  offset: int = 0
  ) -> str:
  '''Converts the original MIDI file into a new MIDI file with the selected channel and offset'''
  new_midi = generate_new_midi(midi, channel, offset)
  tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
  tmp_file.close()
  new_midi.save(tmp_file.name)
  return tmp_file.name

def generate_new_midi(
  midi: mido.MidiFile,
  channel: int = 0,
  offset: int = 0
)-> mido.MidiFile:
  '''Generates a midi file based on an original midi file and given parameters (channel and offset)'''
  new_midi = mido.MidiFile(ticks_per_beat=midi.ticks_per_beat)

  for track in midi.tracks:
    new_track = mido.MidiTrack()
    for msg in track:
      if msg.type in ['note_on', 'note_off']:
        if msg.channel == channel:
          new_msg = msg.copy(note=msg.note + offset, channel=channel)
          new_track.append(new_msg)
      else:
        new_track.append(msg.copy())
    if len(new_track) > 0:
      new_midi.tracks.append(new_track)

  return new_midi