from typing import Any, cast

import mido


def is_note(message: mido.Message) -> bool:
  return getattr(message, "type") == "note_on" and getattr(message, "velocity") > 0
    
def is_rest(message: mido.Message) -> bool:
  return getattr(message, "type") == "note_off" or (getattr(message, "type") == "note_on" and getattr(message, "velocity") == 0)

def is_correct_channel(message: mido.Message, channel: int) -> bool:
  '''Check if the message is in the selected channel'''
  if not hasattr(message, "channel"):
    return False
  return cast(Any, message).channel == channel