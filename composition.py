from music21 import *
import random


# CONFIGURATION

length = 24
pitch_set = [0, 0, 1, 4, 8]
inverse_pitch_set = [0, 0, 11, 7, 3]
octave_offsets = [47, 59, 71]
durations = [0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]
duration_mod = 0.5
smallest_subdivision = 16
bass_cutoff = 60
treble_cutoff = 83

timeNumerator = 7
timeDenominator = 8

seed = 'anvers'


kicks = [0, 16]
kick_note = 36
snares = [8, 22]
snare_note = 38
hi_hats = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27]
hi_hat_note = 42

# SETUP

random.seed(seed)

timeSignatureDivision = str(timeNumerator) + '/' + str(timeDenominator)
timeSignature = meter.TimeSignature(timeSignatureDivision)

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

    # print(f"absolute pitch {absolute_pitch}, bass cuttoff {bass_cutoff},")

    random_duration = random.choice(durations) * duration_mod
    duration_to_add = duration.Duration(random_duration)
    note_to_add.duration = duration_to_add

    is_bass = absolute_pitch < bass_cutoff

    add_bass_or_treble(note_to_add, is_bass)
    # add_drum_from_melody(note_to_add)

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

        # print(f"add: {part_note_to_add.pitch}, duration {part_note_to_add.duration}")

        if is_bass:
            last_bass_pitch = added_note.pitch
        else:
            last_treble_pitch = added_note.pitch


def add_drum_from_melody(added_note):
    drum_duration = part1.duration.quarterLength * timeDenominator / (timeNumerator / 2)

    drum_duration_remainder = drum_duration % timeNumerator
    # print(f"remainder: {drum_duration_remainder}, integer:{drum_duration_remainder.is_integer()}")

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


def add_drum_from_beat(quarter_length):
    # drum_duration = part1.duration.quarterLength * timeDenominator / (timeNumerator / 2)

    drum_duration_remainder = quarter_length % (timeNumerator * smallest_subdivision / 4)
    print(f"remainder: {drum_duration_remainder} for {quarter_length}")

    drum_pitch = -1

    if drum_duration_remainder in kicks:
        print(f"set to {kick_note}")
        drum_pitch = kick_note
    if drum_duration_remainder in hi_hats:
        print(f"set to {hi_hat_note}")
        drum_pitch = hi_hat_note
    if drum_duration_remainder in snares:
        print(f"set to {snare_note}")
        drum_pitch = snare_note

    if drum_pitch != -1:
        drum_note = note.Note(drum_pitch)
        print(f"created note with pitch {drum_note.pitch}")
        drum_note.duration = duration.Duration(0.125)

        part4.append(drum_note)
    else:
        drum_note = note.Rest()
        print(f"created default note with pitch {'C-1'}")
        drum_note.duration = duration.Duration(0.125)

        part4.append(drum_note)


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

scaled_length = int(part1.quarterLength * smallest_subdivision)

print('total length:' + str(part1.quarterLength) + ', scaled length:' + str(scaled_length))

for i in range(scaled_length):
    add_drum_from_beat(i)

result = stream.Score()

result.append(part1)
result.append(part2)
result.append(part3)
result.append(part4)

result.show()
