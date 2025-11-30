from musicpy import *
import random

def generate_chord_progression(key="C", scale_type="major"):
    s = scale(key, scale_type)
    chords = s.chords()  # automatically generated triads
    progression = [random.choice(chords) for _ in range(4)]
    return progression

def generate_melody(key="C", scale_type="major", bars=4, tempo=120):
    s = scale(key, scale_type)
    notes_list = []
    for _ in range(bars * 4):
        note = random.choice(s)
        notes_list.append(note)
    melody = chord(notes_list, interval=1/4, bpm=tempo)
    return melody

def generate_song_instrumental(genre="pop", mood="happy"):
    if genre == "pop":
        key = "C"
        scale_type = "major"
    elif genre == "sad":
        key = "A"
        scale_type = "minor"
    else:
        key = "C"
        scale_type = "major"

    chords = generate_chord_progression(key, scale_type)
    melody = generate_melody(key, scale_type)

    full_song = chords + melody
    return full_song

def save_midi(song, filename="generated_song.mid"):
    song.write(filename)
    return filename
