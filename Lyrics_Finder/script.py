import requests


def find_lyrics(artist, title):
    base_url = 'https://api.lyrics.ovh/v1/{}/{}'.format(artist, title)
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data.get('lyrics', 'Lyrics not found for this song.')
        return lyrics
    else:
        return 'Error fetching lyrics. Please check the artist and title and try again.'


if __name__ == '__main__':
    artist_name = input('Enter the artist name: ')
    song_title = input('Enter the song title: ')

    lyrics = find_lyrics(artist_name, song_title)
    print('\nLyrics:\n')
    print(lyrics)

# Make sure you have the requests library installed in your Python environment before running this script. You can install it using pip install requests.

# To use the script, simply run it, and it will prompt you to enter the artist name and song title. After entering the details, it will fetch and display the lyrics for the specified song.
