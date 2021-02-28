import lyricsgenius as lg

# File for writing the Lyrics
filename = input('Enter a filename: ') or 'Lyrics.txt'
file = open(filename, "w+")

# Acquire a Access Token to connect with Genius API
genius = lg.Genius(
    'Client_Access_Token_Goes_Here',
    # Skip song listing
    skip_non_songs=True,
    # Terms that are redundant song names with same lyrics, e.g. Old Town Raod and Old Town Road Remix
    # have same lyrics
    excluded_terms=["(Remix)", "(Live)"],
    # In order to keep headers like [Chorus], [Bridge] etc.
    remove_section_headers=True)

# List of Artist and Maximum Songs
input_string = input("Enter name of Artists separated by spaces: ")
artists = input_string.split(" ")


def get_lyrics(arr, max_song):
    """
    Returns: Number of songs grabbed by Function
    Saves : Text File with Lyrics
    Parameters :
        arr : Artist
        max_song : Number of maximum songs to be grabbed
    """
    # Write lyrics of k songs by each artist in arr
    c = 0
    # A counter
    for name in arr:
        try:
            songs = (genius.search_artist(name,
                                          max_songs=max_song,
                                          sort='popularity')).songs
            s = [song.lyrics for song in songs]
            # A custom delimiter
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")


# Function Call
get_lyrics(artists, 3)
