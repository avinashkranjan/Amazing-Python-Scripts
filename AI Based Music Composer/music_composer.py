import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator

# Set the directory to save the generated MIDI files
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)

# Initialize the Melody RNN model
model_name = 'attention_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model_name=model_name)

# Set the temperature for music generation (higher values lead to more randomness)
temperature = 1.0

# Set the number of music pieces to generate
num_music_pieces = 3

# Set the number of steps per music piece
steps_per_music_piece = 128

# User input for preferred genre and tempo
preferred_genre = input(
    "Enter your preferred genre (e.g., classical, jazz, rock): ")
preferred_tempo = int(input("Enter your preferred tempo (BPM): "))

# Chord progression for the chosen genre (you can add more genres and progressions)
chord_progressions = {
    "classical": ["C", "Am", "F", "G"],
    "jazz": ["Cmaj7", "Dm7", "Em7", "A7"],
    "rock": ["C", "G", "Am", "F"],
}

# Basic drum pattern for accompaniment
drum_pattern = mm.DrumTrack(
    # Kick drum and Hi-hat pattern (adjust as needed)
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=steps_per_music_piece // 4,
    steps_per_quarter=4,
)

# Generate music pieces
for i in range(num_music_pieces):
    # Generate a melody sequence
    melody_sequence = melody_rnn.generate(
        temperature=temperature,
        steps=steps_per_music_piece,
        primer_sequence=None
    )

    # Add chords to the melody sequence based on the preferred genre
    chords = [chord_progressions.get(preferred_genre, ["C"])[i % len(
        chord_progressions.get(preferred_genre, ["C"]))] for i in range(steps_per_music_piece)]
    chord_sequence = mm.ChordSequence(chords)
    melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(
        melody_sequence, chord_sequence)

    # Create a MIDI file from the melody with chords sequence and drum pattern
    music_sequence = mm.sequences_lib.concatenate_sequences(
        melody_with_chords_sequence, drum_pattern)
    music_sequence.tempos[0].qpm = preferred_tempo

    midi_file = os.path.join(output_dir, f'music_piece_{i + 1}.mid')
    mm.sequence_proto_to_midi_file(music_sequence, midi_file)
    print(f'Music piece {i + 1} generated and saved as {midi_file}')

print('Music generation complete!')
