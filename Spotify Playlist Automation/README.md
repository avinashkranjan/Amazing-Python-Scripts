# Spotify Playlist Automation

# Description
Its an application which allows the user to automate saving the "Discover Weekly" Playlist into a new playlist called as- "Saved Weekly". Since new songs are added every week, the user wont have to add songs everytime.

# Prerequisite tasks:
1. Make sure you have made the "Discover Weekly" Playlist public by selecting the playlist to be displayed on       profile.

2. Browse to https://developer.spotify.com/dashboard/applications.

3. Log in with your Spotify account.

4. Click on ‘Create an app’.

5. Pick an ‘App name’ and ‘App description’ of your choice and mark the checkboxes.

6. After creation, you see your ‘Client Id’ and you can click on ‘Show client secret` to unhide your ’Client secret’

# Getting Started

1. Install the dependencies via the requirements txt file:
 
$ pip install -r requirements.txt

2. After installation, Update the client_id and secret_key in the configuration file to authenticate the spotipy api

3. After updation run the file spotify_discover_weekly.py in the terminal

4. Click on the link which is generated. It is basically running the app on the port locally.