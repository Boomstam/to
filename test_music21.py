from music21 import converter, chord, scale, pitch

littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
#littleMelody.show('midi')

score = converter.parse('/Users/mennobuggenhout/Documents/Ableton/Trumpet Eppers C.mid')

print(score)
print(score.chordify())
print(score.pitches)

ch = chord.Chord(score.pitches)

print(ch.commonName)
print(ch.chordTablesAddress)
print(ch.scaleDegrees)
print(ch.root())
print(ch.primeFormString)
print(ch.primeForm)

littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
#littleMelody.show('midi')

sc = scale.ConcreteScale(pitches= score.pitches)
print(sc.name)
print(sc.tonic)
print(sc.style)
print(sc.isConcrete)

