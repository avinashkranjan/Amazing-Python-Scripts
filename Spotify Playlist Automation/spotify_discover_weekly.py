import config
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'spotify cookie'
app.secret_key = '10)293@han2%^s*hka02zkls'
TOKEN_INFO = 'token_info'


@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly', external=True))


@app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect('/')
    sp = spotipy.Spotify(auth=token_info['access_token'])
    # to get user's playlists which are public
    current_playlists = sp.current_user_playlists()['items']
    discover_weekly_playlist_id = None
    saved_weekly_playlist_id = None
    user_id = sp.current_user()['id']
    playlist_names = []
    playlist_id = []
    k = 0
    # find the Discover Weekly and Saved Weekly playlists
    for playlist in current_playlists:
        playlist_names.append(playlist['name'])
        playlist_id.append(playlist['id'])
    for playlist in playlist_names:
        if playlist == 'Discover Weekly':
            discover_weekly_playlist_id = playlist_id[k]
        if playlist == 'Saved Weekly':
            saved_weekly_playlist_id = playlist_id[k]
        k += 1
    if discover_weekly_playlist_id == None:
        return 'Discover Weekly not found.'
    if saved_weekly_playlist_id == None:
        new_playlist = sp.user_playlist_create(user_id, 'Saved Weekly', True)
        saved_weekly_playlist_id = new_playlist['id']

    # get the tracks from the Discover Weekly playlist
    discover_weekly_playlist = sp.playlist_items(discover_weekly_playlist_id)
    song_uris = []
    for song in discover_weekly_playlist['items']:
        song_uri = song['track']['uri']
        song_uris.append(song_uri)
    # we need uris because when we want to add songs to the playlist, we need uris parameter
    sp.user_playlist_add_tracks(
        user_id, saved_weekly_playlist_id, song_uris, None)
    return ("Playlist Update Success")


def get_token():
    # checking two edge cases, 1. If the token is expired, 2. Token doesn't exist
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect_page(url_for('login', external=False))
    current_time = int(time.time())
    is_expired = token_info['expires_at'] - current_time < 60
    if (is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(
            token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(client_id=config.client_id, client_secret=config.secret_key, redirect_uri=url_for('redirect_page', _external=True), scope='user-library-read playlist-modify-public playlist-modify-private')


app.run(debug=True)
