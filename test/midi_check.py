import mido

# Load the MIDI file
midi_file = mido.MidiFile("data/Daft-Punk-Harder-Better-Faster-Stronger.mid")

# Iterate over all notes
for track in midi_file.tracks:
    for msg in track:
        if msg.type == 'note_on' and msg.velocity > 0:
            print(f"Note: {msg.note}")