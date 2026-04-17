class DummyMessage:
  def __init__(self, note, channel, velocity=64, type="note_on", time=0):
    self.note = note
    self.channel = channel
    self.velocity = velocity
    self.type = type
    self.time = time

class DummyMIDI:
  def __init__(self, messages):
    self.tracks = [messages]

  def __iter__(self):
    return iter(self.tracks[0])
    
def make_dummy_midi(): # type: ignore
  return DummyMIDI([
    DummyMessage(62, 0),
    DummyMessage(64, 1),
    DummyMessage(66, 0)
  ])