import os
from os import walk
import os.path
import sys
import pygame
from pygame import mixer


#init mixer process
mixer.init()

#get files
songs = []

os.chdir(os.getcwd() + '/songs')

for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    songs.extend(filenames)
    break


        

it = 0

#player
while True:
    song = songs[it]

    mixer.music.load(song) #load song
    mixer.music.set_volume(0.5) #set volume
    mixer.music.play() #play

    playing = 1

    while True:
        os.system('cls')

        print("-----------------------------------------")
        print("----------  ZABE MUSIC PLAYER  ----------")
        print("------------------------------------------")
        print("    Current song: " + song + "")
        print("    A(<<) (>>)D")
        print("    Volume: " + str(int(100*mixer.music.get_volume())) + "%· W(++) (--)S")
        print("    P: play/pause")
        print("    E: exit")
        print("-----------------------------------------")
        print("    Current song: " + song)
        print("    Songs queued: " + str(len(songs)))

        action = input(">>> ")

        if action == 'P' or action == 'p': #play,pause
            if playing:
                mixer.music.pause()
                playing = 0
            else:
                mixer.music.unpause()
                playing = 1
        elif action == 'W' or action == 'w': #volume up
            v = mixer.music.get_volume()
            mixer.music.set_volume(v + 0.1)
        elif action == 'S' or action == 's': #volume down
            v = mixer.music.get_volume()
            mixer.music.set_volume(v- 0.1)
        elif action == 'A' or action == 'a': #previous song
            it = (it - 1)%len(songs)
            break
        elif action == 'D' or action == 'd': #next song
            it = (it + 1)%len(songs)
            break
        elif action == 'E' or action == 'e': #stop
            mixer.music.stop()
            print("Closing...")
            sys.exit(0)