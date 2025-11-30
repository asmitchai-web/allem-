from lyricals import generate_full_lyrics
from musicpy_generator_musical import generate_song_instrumental, save_midi

def generate_song(genre="pop", mood="happy"):
    # Step 1: Generate lyrics
    lyrics = generate_full_lyrics(genre=genre, mood=mood)

    # Step 2: Generate music (MusicPy)
    instrumental = generate_song_instrumental(genre=genre, mood=mood)
    midi_path = save_midi(instrumental, f"{genre}_{mood}.mid")

    return {
        "lyrics": lyrics,
        "midi_file": midi_path
    }

