from music21 import *
import random

length = 17
pitch_set = [0, 0, 1, 4, 8]
inverse_pitch_set = [0, 0, 11, 7, 3]
octave_offsets = [47, 59, 71]
#offsets = [0, ]
durations = [0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]
bass_cutoff = 60
treble_cutoff = 71

timeSignature = meter.TimeSignature('7/8')

last_bass_pitch = -1
last_treble_pitch = -1

part1 = stream.Part()
part1.append(timeSignature)

part2 = stream.Part()
part2.append(timeSignature)

part3 = stream.Part()
part3.append(timeSignature)

part4 = stream.Part()
part4.append(timeSignature)


def add_first_part_note(set_to_choose_from, stream_to_add_to):

    random_pitch = random.choice(set_to_choose_from)
    random_octave_offset = random.choice(octave_offsets)
    absolute_pitch = random_pitch + random_octave_offset
    note_to_add = note.Note(absolute_pitch)

    print(f"absolute pitch {absolute_pitch}, bass cuttoff {bass_cutoff},")

    random_duration = random.choice(durations)
    duration_to_add = duration.Duration(random_duration)
    note_to_add.duration = duration_to_add

    is_bass = absolute_pitch < bass_cutoff

    add_bass_or_treble(note_to_add, is_bass)
    add_drum(note_to_add, is_bass)

    stream_to_add_to.append(note_to_add)


def add_bass_or_treble(added_note, is_bass):
    global last_bass_pitch
    global last_treble_pitch

    if is_bass and last_bass_pitch == -1:
        last_bass_pitch = added_note.pitch
    elif is_bass is False and last_treble_pitch == -1:
        last_treble_pitch = added_note.pitch
    else:
        part_last_pitch = last_bass_pitch if is_bass else last_treble_pitch
        part_note_to_add = note.Note(part_last_pitch)

        part_duration = part3.duration.quarterLength if is_bass else part2.duration.quarterLength
        delta_duration = part1.duration.quarterLength - part_duration
        part_note_duration = duration.Duration(delta_duration)
        part_note_to_add.duration = part_note_duration

        part3.append(part_note_to_add) if is_bass else part2.append(part_note_to_add)

        print(f"add: {part_note_to_add.pitch}, duration {part_note_to_add.duration}")

        if is_bass:
            last_bass_pitch = added_note.pitch
        else:
            last_treble_pitch = added_note.pitch


def add_drum(added_note, is_bass):
    drum_duration = part1.duration.quarterLength * 2

    drum_duration_remainder = drum_duration % 7
    print(f"remainder: {drum_duration_remainder}, integer:{drum_duration_remainder.is_integer()}")

    if drum_duration_remainder == 0 or drum_duration_remainder == 5:
        print("set to 36")
        drum_pitch = 36
    elif drum_duration_remainder.is_integer():
        print("set to 38")
        drum_pitch = 38
    else:
        print("set to 42")
        drum_pitch = 42

    drum_note = note.Note(drum_pitch)
    print(f"created note with pitch {drum_note.pitch}")
    drum_note.duration = added_note.duration

    part4.append(drum_note)

    pass


for i in range(length):
    add_first_part_note(inverse_pitch_set, part1)
for i in range(length):
    add_first_part_note(pitch_set, part1)
for i in range(length):
    add_first_part_note(inverse_pitch_set, part1)
for i in range(length):
    add_first_part_note(pitch_set, part1)
for i in range(length):
    add_first_part_note(inverse_pitch_set, part1)

result = stream.Score()

result.append(part1)
result.append(part2)
result.append(part3)
result.append(part4)

result.show()
