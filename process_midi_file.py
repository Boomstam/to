import mido
import csv


def process_midi_file(midi_file_path):
    notes = {}
    try:
        midi_file = mido.MidiFile(midi_file_path)

        for track in midi_file.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    note = msg.note
                    velocity = msg.velocity
                    time = msg.time

                    if note not in notes:
                        notes[note] = {
                            'count': 1,
                            'total_velocity': velocity,
                            'total_duration': time
                        }
                    else:
                        notes[note]['count'] += 1
                        notes[note]['total_velocity'] += velocity
                        notes[note]['total_duration'] += time

        # Sort notes by their MIDI values (ascending order)
        sorted_notes = sorted(notes.items())

        with open('midi_notes.csv', 'w', newline='') as csvfile:
            fieldnames = ['Note', 'Count', 'Average Velocity', 'Average Duration']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for note, data in sorted_notes:
                count = data['count']
                average_velocity = data['total_velocity'] / count
                average_duration = data['total_duration'] / count

                writer.writerow({
                    'Note': note,
                    'Count': count,
                    'Average Velocity': average_velocity,
                    'Average Duration': average_duration
                })

        print("CSV file 'midi_notes.csv' has been created.")

    except mido.exceptions.MidiFileNotFoundError:
        print(f"MIDI file not found: {midi_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    file_path = '/Users/mennobuggenhout/Documents/Ableton/Trumpet Eppers C.mid'
    process_midi_file(file_path)
