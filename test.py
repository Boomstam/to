from music21 import stream, note, meter
import random

# Create a measure
measure = stream.Measure()

# Set the time signature (commonly 4/4)
measure.timeSignature = meter.TimeSignature('4/4')

# List of notes in C major scale
c_major_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Generate and add random notes from C major to the measure
for _ in range(4):  # Assuming quarter notes
    random_note_name = random.choice(c_major_scale)
    random_note = note.Note(random_note_name)
    measure.append(random_note)

# Display the measure
measure.show()
