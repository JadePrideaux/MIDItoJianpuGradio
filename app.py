from code.midi_loading import load_midi_file
from code.midi_to_midi import get_new_midi
from code.midi_to_string import midi_to_jianpu_str
from code.transposition import calculate_offset
from tempfile import _TemporaryFileWrapper

import gradio as gr
import mido


def midi_file_to_jianpu_str(
        file: _TemporaryFileWrapper,
        channel: int, semitone_offset: int,
        octave_offset: int
    ) -> tuple[str, tuple[str, int, int]]:
    '''Given a midi file, return the notes in jianpu notation'''
    offset = calculate_offset(semitone_offset, octave_offset)
    try:
        midi = load_midi_file(file)
    except:
        return f"Error processing file, make sure to upload a MIDI file.", ("", channel, offset)
    result = midi_to_jianpu_str(midi, channel, offset)
    return result, (file.name, channel, offset)

def get_midi(state) -> tuple[str, str | None]:
    if state is None:
        return "No data yet. Upload and Convert a MIDI file first", None

    file_path, channel, offset = state

    try:
        midi = mido.MidiFile(file_path)
    except Exception as e:
        return f"Failed to load MIDI file: {e}", None

    try:
        output_path = get_new_midi(midi, channel, offset)
    except Exception as e:
        return f"Failed to generate MIDI: {e}", None

    return "MIDI generated successfully!", output_path

with gr.Blocks() as ui:
    state = gr.State()
    with gr.Row():
        with gr.Column():
            gr.Markdown("# MIDI to Jianpu")
            gr.Markdown("## How to use:")
            gr.Markdown("Upload a MIDI file then click convert to see it in Jianpu notation. " \
                        "Select options to select the channel and alter the output. " \
                        "Once converted you can download the edited MIDI file with just the selected track to check how the notes should sound.")
            gr.Markdown("### Options:")
            gr.Markdown("**MIDI Channel** - Select which channel to convert.")
            gr.Markdown("**Semitone Offset** - Offset the song by a semitone")
            gr.Markdown("**Octave Offset** - Offset the song by an octave")
            gr.Markdown("### Key:")
            gr.Markdown("[n] - note")
            gr.Markdown("[n|----] - longer note")
            gr.Markdown("[-----] - rest")
            gr.Markdown("[·n] - octave above")
            gr.Markdown("[n·] - octave below")

        with gr.Column():
            midi_input = gr.File(label="Upload MIDI file")

            channel_slider = gr.Slider(
                minimum=0, maximum=15, step=1, value=0,
                label="MIDI Channel"
            )

            semitone_slider = gr.Slider(
                minimum=-11, maximum=11, step=1, value=0,
                label="Semitone Offset"
            )

            octave_slider = gr.Slider(
                minimum=-8, maximum=8, step=1, value=0,
                label="Octave Offset"
            )

            run_button = gr.Button("Convert")

        with gr.Column():
            output_text = gr.Textbox(label="Jianpu Output")
            download_button = gr.Button("Prepare MIDI for Download")
            midi_output = gr.File(label="Playable MIDI")
            status_text = gr.Textbox(label="Status")

    run_button.click(
        fn=midi_file_to_jianpu_str,
        inputs=[
            midi_input,
            channel_slider,
            semitone_slider,
            octave_slider
        ],
        outputs=[output_text, state]
    )

    download_button.click(
        fn=get_midi,
        inputs=state,
        outputs=[status_text, midi_output]
    )


if __name__ == "__main__":
    ui.launch()
