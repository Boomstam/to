from music21 import converter, stream, note, meter, midi
import random

file_path = '/Users/mennobuggenhout/PycharmProjects/to/untitled.mid'
score = converter.parse(file_path)

midi_file = midi.MidiFile()
midi_file.open(file_path)
midi_file.read()
print(f'midi file format: {midi_file.format}')
tracks = midi_file.tracks
print(f'number of tracks: {len(tracks)}')

track1 = tracks[0]
track2 = tracks[1]

print(f'track1: {track1}')
print(f'track2: {track2}')

for event in track1.events:
    print(f'{event}')
for event in track2.events:
    print(f'{event}')

# score.show()
