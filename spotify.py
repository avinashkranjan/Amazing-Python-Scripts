import sys
## we use spotify_dl to fetch the url here
from spotify_dl.scaffold import log ##logging into account with credentials
from spotify_dl.utils import sanitize


def fetching(client ,type, url):
    """
    Fetches tracks from the  URL.
    :param client: Spotify client
    :param type: item type  requested for: album/playlist/track
    :param url: URL of the item
    :return Dictionary {song :artist}
    """
    list_of_songs = [] ## an empty list to be filled(appended) with list of songs
    offset = 0

    if type == 'playlist':
        while 1:
            items = client.playlist_items(playlist_id=url,

                                      fields='items.track.name,items.track.artists(name, uri),'
                                             'items.track.album(name, release_date, total_tracks, images),'

                                             'items.track.track_number,total, next,offset',
                                      additional_types=['track'], offset=offset)
            """takes the url from the request library and returns response which is a json file.
            we extract the fields from the json file in the form of key-value pairs(dicitonaries)"""

            total_no_of_songs = items.get('total')
            for item in items['items']:
                track_name = item['track']['name']
                track_artist = ", ".join([artist['name'] for artist in item['track']['artists']])
                track_album = item['track']['album']['name']
                track_year = item['track']['album']['release_date'][:4]
                album_total = item['track']['album']['total_tracks']
                track_num = item['track']['track_number']
                if len(item['track']['album']['images']) > 0:
                    cover = item['track']['album']['images'][0]['url']
                else:
                    cover = None

                if len(client.artist(artist_id=item['track']['artists'][0]['uri'])['genres']) > 0:
                    genre = client.artist(artist_id=item['track']['artists'][0]['uri'])['genres'][0]
                else:
                    genre = ""
                list_of_songs.append({"name": track_name, "artist": track_artist, "album": track_album,
                                   "year": track_year,
                                   "num_tracks": album_total, "num": track_num,
                                   "playlist_num": offset + 1,
                                   "cover": cover, "genre": genre})
                offset += 1

            log.info(f"Fetched {offset}/{total_no_of_songs} songs in the playlist")
            if total_no_of_songs == offset:
                log.info('All pages fetched. Added %s songs in total', offset)
                break

    elif type == 'album':
        while 1:
            album_info = client.album(album_id=url)
            items = client.album_tracks(album_id=url)
            total_songs = items.get('total')
            track_album = album_info['name']
            track_year = album_info['release_date'][:4]
            album_total = album_info['total_tracks']
            if len(album_info['images']) > 0:
                cover = album_info['images'][0]['url']
            else:
                cover = None
            if len(client.artist(artist_id=album_info['artists'][0]['uri'])['genres']) > 0:
                genre = client.artist(artist_id=album_info['artists'][0]['uri'])['genres'][0]
            else:
                genre = ""
            for item in items['items']:
                track_name = item['name']
                track_artist = ", ".join([artist['name'] for artist in item['artists']])
                track_num = item['track_number']
                list_of_songs.append({"name": track_name, "artist": track_artist, "album": track_album,
                                   "year": track_year,
                                   "num_tracks": album_total, "num": track_num,
                                   "playlist_num": offset + 1,
                                   "cover": cover, "genre": genre})
                offset += 1

            log.info(f"Fetched {offset}/{total_songs} songs in the album")
            if total_songs == offset:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif type == 'track':
        items = client.track(track_id=url)
        track_name = items['name']
        track_artist = ", ".join([artist['name'] for artist in items['artists']])
        track_album = items['album']['name']
        track_year = items['album']['release_date'][:4]
        album_total = items['album']['total_tracks']
        track_num = items['track_number']
        if len(items['album']['images']) > 0:
            cover = items['album']['images'][0]['url']
        else:
            cover = None
        if len(client.artist(artist_id=items['artists'][0]['uri'])['genres']) > 0:
            genre = client.artist(artist_id=items['artists'][0]['uri'])['genres'][0]
        else:
            genre = ""
        list_of_songs.append(
            {"name": track_name, "artist": track_artist, "album": track_album, "year": track_year,
             "num_tracks": album_total, "num": track_num, "playlist_num": offset + 1,
             "cover": cover, "genre": genre})

    return list_of_songs


def parse_spotify_url(url):
    """
    Parse the provided Spotify playlist URL and determine if it is a playlist, track or album.
    :param url: URL to be parsed
    :return tuple indicating the type and id of the item
    """
    if url.startswith("spotify:"):
        log.error("Spotify URI was provided instead of a playlist/album/track URL.")
        sys.exit(1)
    parsed_url = url.replace("https://open.spotify.com/", "")
    item_type = parsed_url.split("/")[0]
    item_id = parsed_url.split("/")[1]
    return item_type, item_id


def get_item_name(client, type, id):
    """
    Fetch the name of the item.
    :param client: Spotify Client
    :param type: Type of the item
    :param id: id of the item
    :return String indicating the name of the item
    """
    if type == 'playlist':
        name = client.playlist(playlist_id=id, fields='name').get('name')
    elif type == 'album':
        name = client.album(album_id=id).get('name')
    elif type == 'track':
        name = client.track(track_id=id).get('name')
    return sanitize(name)


def validate_spotify_url(url):
    """
    Validate the URL to determine if the item type is supported.
    :return Boolean .
    """
    type, id = parse_spotify_url(url)
    log.debug(f" item type :{type} ; item_id: {id}")
    if type not in ['album', 'track', 'playlist']:
        log.error("Only albums/tracks/playlists are supported")
        return False
    if id is None:
        log.error("Couldn't get a valid id")
        return False
    return True
