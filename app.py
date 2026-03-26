from code.logic import calculate_offset
from code.midi import load_midi_file, midi_to_jianpu_str
from tempfile import _TemporaryFileWrapper

import gradio as gr


def midi_file_to_jianpu_str(
        file: _TemporaryFileWrapper,
        channel: int, semitone_offset: int,
        octave_offset: int,
        time_interval: int
    ) -> str:
    '''Given a midi file, return the notes in jianpu notation'''
    try:
        midi = load_midi_file(file)
    except:
        return f"Error processing file, make sure to upload a MIDI file."
    return midi_to_jianpu_str(midi, channel, semitone_offset, octave_offset, time_interval)

def play_midi():
    pass

with gr.Blocks() as ui:

    with gr.Row():
        with gr.Column():
            gr.Markdown("# MIDI to Jianpu")
            gr.Markdown("## How to use:")
            gr.Markdown("## Key:")

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

            interval_slider = gr.Slider(
                minimum=1, maximum=16, step=1, value=8,
                label="Time Interval"
            )

            run_button = gr.Button("Convert")

        with gr.Column():
            output_text = gr.Textbox(label="Jianpu Output")
            play_button = gr.Button("Play")

    run_button.click(
        fn=midi_file_to_jianpu_str,
        inputs=[
            midi_input,
            channel_slider,
            semitone_slider,
            octave_slider,
            interval_slider
        ],
        outputs=output_text
    )

    play_button.click(
        fn=play_midi
    )


if __name__ == "__main__":
    ui.launch()
