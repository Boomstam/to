import music21
from music21 import stream, note, chord

# Create a list of pitch classes (notes)
pitch_classes = ['C', 'E', 'G', 'A', 'C', 'D', 'F', 'G']
note1 = note.Note("C4")
note2 = note.Note("F#4")

aStream = stream.Stream()
src = list(range(12)) # create a list of integers 0 through 11
src = src[2:4] + src[0:2] + src[8:9] + src[4:8] + src[9:12] # recombine
for i in range(0, 12, 3):
    print(src[i:i + 3])
    aStream.append(chord.Chord(src[i:i + 3]))

#aStream.show()

for ch in aStream:
    print(ch.primeFormString)

pitches = [1, 5, 3, 6]
test_chord = chord.Chord(pitches)

print(test_chord.primeForm)
print(test_chord.intervalVector)
print(test_chord.root().__str__() + test_chord.quality)
print(test_chord.fullName)
print(test_chord.commonName)
print(test_chord.chordTablesAddress)


