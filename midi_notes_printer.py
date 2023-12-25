import mido


def print_midi_notes(midi_file_path):
    try:
        midi_file = mido.MidiFile(midi_file_path)

        for i, track in enumerate(midi_file.tracks):
            print(f"Track {i + 1}:")

            for msg in track:
                if msg.type == 'note_on':
                    print(f"Note: {msg.note}, Velocity: {msg.velocity}, Time: {msg.time}")

    except mido.exceptions.MidiFileNotFoundError:
        print(f"MIDI file not found: {midi_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    file_path = '/Users/mennobuggenhout/Documents/Ableton/Trumpet Eppers C.mid'  # Replace with the path to your MIDI file
    print_midi_notes(file_path)

