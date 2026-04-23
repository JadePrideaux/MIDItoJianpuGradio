class Message():
  def __init__(
    self,
    note: int,
    time: float,
    type: str
  ) -> None:
    self.note = note
    self.time = time
    self.type = type

def make_midi() -> list[Message]:
  return [
    Message(60, 0, "on"),
    Message(60, 100, "off"),

    Message(62, 0, "on"),
    Message(64, 10, "on"),
    Message(62, 70, "off"),
    Message(64, 0, "off"),

    Message(60, 40, "on"),
    Message(60, 100, "off")
  ]
  
def extract_notes(messages: list[Message]) -> tuple[list, bool]:

  playing_notes = dict()
  current_ticks = 0
  last_note_off_tick = 0
  has_overlap = False
  notes = []

  for msg in messages:
    current_ticks+= msg.time
    if msg.type == "on":
      if len(playing_notes) == 0:
        rest_duration = current_ticks - last_note_off_tick
        if rest_duration > 0:
          notes.append(("rest", rest_duration))
      if playing_notes:
        has_overlap = True
      playing_notes[msg.note] = current_ticks
    elif msg.type == "off":
      if msg.note in playing_notes:
        duration = current_ticks - playing_notes.pop(msg.note)
        notes.append((msg.note, duration))
        if not playing_notes:
            last_note_off_tick = current_ticks
  return (notes, has_overlap)

if __name__ == "__main__":
  messages = make_midi()
  output = extract_notes(messages)
  print(output[0])
  if output[1]:
    print("MIDI Contains overlapping notes")