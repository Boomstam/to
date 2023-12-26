from music21 import *
import random

length = 100
pitch_set = [0, 0, 1, 4, 8]
inverse_pitch_set = [0, 0, 11, 7, 3]
octave_offsets = [47, 59, 71]
#offsets = [0, ]
durations = [0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]
bass_cutoff = 60

timeSignature = meter.TimeSignature('7/8')

part1 = stream.Part()
part1.append(timeSignature)

part2 = stream.Part()
part2.append(timeSignature)

part3 = stream.Part()
part3.append(timeSignature)

current_time = 0.
last_bass_pitch = -1

def add_first_part_note(set_to_choose_from, stream_to_add_to):

    random_pitch = random.choice(set_to_choose_from)
    random_octave_offset = random.choice(octave_offsets)
    absolute_pitch = random_pitch + random_octave_offset
    note_to_add = note.Note(absolute_pitch)

    print(f"absolute pitch {absolute_pitch}, bass cuttoff {bass_cutoff},")
    if absolute_pitch < bass_cutoff:
        add_bass(note_to_add)

    random_duration = random.choice(durations)
    duration_to_add = duration.Duration(random_duration)

    global current_time
    current_time += random_duration

    note_to_add.duration = duration_to_add

    stream_to_add_to.append(note_to_add)

def add_bass(added_note):
    global last_bass_pitch

    if last_bass_pitch == -1:
        last_bass_pitch = added_note.pitch
        print(f"first last bass pitch set: {last_bass_pitch}")
    else:
        #print(part1.duration)
        #print(part2.duration)

        bass_note_to_add = note.Note(last_bass_pitch)
        delta_duration = part1.duration.quarterLength - part2.duration.quarterLength
        bass_note_duration = duration.Duration(delta_duration)
        bass_note_to_add.duration = bass_note_duration
        part2.append(bass_note_to_add)
        print(f"add: {bass_note_to_add.pitch}, duration {bass_note_to_add.duration}")

        last_bass_pitch = added_note.pitch
        print(f"new last bass pitch set: {last_bass_pitch}")

for i in range(length):
    add_first_part_note(pitch_set, part1)

#for i in range(length):
    #add_first_part_note(inverse_pitch_set, part2)

result = stream.Score()
result.append(part1)
result.append(part2)

result.show()
