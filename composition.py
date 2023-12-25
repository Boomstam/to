from music21 import *
import random

length = 100
pitch_set = [0, 0, 1, 4, 8]
inverse_pitch_set = [0, 0, 11, 7, 3]
octave_offsets = [47, 59, 71]
#offsets = [0, ]
durations = [0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]

composition = stream.Stream()

timeSignature = meter.TimeSignature('7/8')
composition.append(timeSignature)


def add_note(set_to_choose_from):
    random_pitch = random.choice(set_to_choose_from)
    random_octave_offset = random.choice(octave_offsets)
    note_to_add = note.Note(random_pitch + random_octave_offset)

    random_duration = random.choice(durations)
    duration_to_add = duration.Duration(random_duration)

    note_to_add.duration = duration_to_add

    composition.append(note_to_add)


for i in range(length):
    add_note(pitch_set)

for i in range(length):
    add_note(inverse_pitch_set)

composition.show()
