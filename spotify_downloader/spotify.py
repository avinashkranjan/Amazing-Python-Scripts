import spotdl
import sys,os
def console_entry_point():
    '''
    This is where all the console processing magic happens.
    Its super simple, rudimentary even but, it's dead simple & it works.
    '''
    arguments = parse_arguments()

    spotifyClient.initialize(
        clientId='4fe3fecfe5334023a1472516cc99d805',
        clientSecret='0f02b7c483c04257984695007a4a8d5c'
    )

    if arguments.path:
        if not os.path.isdir(arguments.path):
            sys.exit("The output directory doesn't exist.")
        print(f"Will download to: {os.path.abspath(arguments.path)}")
        os.chdir(arguments.path)

    downloader = DownloadManager()

    for request in arguments.url:
        if 'open.spotify.com' in request and 'track' in request:
            print('Fetching Song...')
            song = SongObj.from_url(request)

            if song.get_youtube_link() is not None:
                downloader.download_single_song(song)
            else:
                print('Skipping %s (%s) as no match could be found on youtube' % (
                    song.get_song_name(), request
                ))

        elif 'open.spotify.com' in request and 'album' in request:
            print('Fetching Album...')
            songObjList = get_album_tracks(request)

            downloader.download_multiple_songs(songObjList)

        elif 'open.spotify.com' in request and 'playlist' in request:
            print('Fetching Playlist...')
            songObjList = get_playlist_tracks(request)

            downloader.download_multiple_songs(songObjList)

        elif 'open.spotify.com' in request and 'artist' in request:
            print('Fetching artist...')
            artistObjList = get_artist_tracks(request)

            downloader.download_multiple_songs(artistObjList)

        elif request.endswith('.spotdlTrackingFile'):
            print('Preparing to resume download...')
            downloader.resume_download_from_tracking_file(request)

        else:
            print('Searching for song "%s"...' % request)
            try:
                song = search_for_song(request)
                downloader.download_single_song(song)

            except Exception:
                print('No song named "%s" could be found on spotify' % request)

    downloader.close()


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="spotdl",
        description=help_notice,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("url", type=str, nargs="+", help="URL to a song/album/playlist")
    parser.add_argument("-o", "--output", help="Output directory path", dest="path")

    return parser.parse_args()


if __name__ == '__main__':
    console_entry_point()
