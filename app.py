from code.midi import load_midi_file, midi_to_jianpu_str
from tempfile import _TemporaryFileWrapper

import gradio as gr


def midi_file_to_jianpu_str(file: _TemporaryFileWrapper, channel: int) -> str:
    '''Given a midi file, return the notes in jianpu notation'''
    try:
        midi = load_midi_file(file)
    except:
        return f"Error processing file, make sure to upload a MIDI file."
    return midi_to_jianpu_str(midi, channel)
    

interface = gr.Interface(
    fn = midi_file_to_jianpu_str,
    inputs = [
        gr.File(label="Upload MIDI file"),
        gr.Slider(minimum=0, maximum=15, step=1, value=0, label="MIDI Channel")
    ],
    outputs = "text",
    title = "MIDI to Jianpu"
)

if __name__ == "__main__":
    interface.launch()
