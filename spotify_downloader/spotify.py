import spotdl
import sys,os
def spotify():
    if(len(sys.argv) <= 1): 
        print("try 'python3 spotify.py -h' for help")
        return 1
    elif(sys.argv[1] == '-h'):
        print("To download a song run,\n   python3 spotify.py $trackUrl\n\nTo download an album run,\n   python3 spotify.py $albumUrl\n\nTo download a playlist run,\n   python3 spotify.py $playlistUrl")
        return 1
    url = sys.argv[1]
    if (url.find('track') > -1): 
        os.system(f'spotdl --song {url}')
    else:
        # Playlist
        if (url.find('playlist') > -1):
            os.system(f"spotdl -p {url} --write-to playlist.txt")
            os.system(f"spotdl --list playlist.txt")
        # Artist
        if (url.find('artist') > -1):
            os.system(f"spotdl --all {url} --write-to artist.txt")
            os.system(f"spotdl --list artist.txt")
        # album
        if (url.find('album') > -1):
            os.system(f"spotdl -a {url} --write-to album.txt")
            os.system(f"spotdl --list album.txt")
            

if __name__ == "__main__":
    spotify()
