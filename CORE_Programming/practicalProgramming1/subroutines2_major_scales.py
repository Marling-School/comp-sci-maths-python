from typing import List

# Declare all the note names in a list that we can rotate through
NOTE_NAMES: List[str] = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

# Do, Ra, Mi, Fah, So, Lah, Ti, Do
MAJOR_SCALE_OFFSET: List[int] = [0, 2, 4, 5, 7, 9, 11, 12]


def get_major_scale_notes(starting_note: str) -> List[str]:
    notes: List[str] = []
    # Find the starting note, defaults to C if the given note is invalid
    starting_index: int = 0
    try:
        starting_index: int = NOTE_NAMES.index(starting_note)
    except ValueError:
        print("Invalid note given {}".format(starting_note))

    for relative_offset in MAJOR_SCALE_OFFSET:
        offset_index: int = (starting_index + relative_offset) % len(NOTE_NAMES)
        notes.append(NOTE_NAMES[offset_index])

    return notes


c_major = get_major_scale_notes("C")
e_major = get_major_scale_notes("E")
a_flat_major = get_major_scale_notes("G#/Ab")
fish_major = get_major_scale_notes("fish")

print("C Major is {}".format(c_major))
print("E Major is {}".format(e_major))
print("Ab Major is {}".format(a_flat_major))
print("fish Major is (should effectively default to C) {}".format(fish_major))

