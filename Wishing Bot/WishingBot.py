import time
from random import randint
import pygame
import threading
import sys
import os

pygame.init()
emojis = ['😃', '🐻‍❄️', '🐏', '🌲', '🎆', '❤️', '⛄', '🎮', '🔊', '⚙️', '😍', '😴', '🤑', '💀', '👻', '👽', '🐭', '🐸',
          '🐢', '🐬', '🧟', '🥷', '🎈', '🎉', '😷', '🕸️', '🎯', '🔒', '🔑', '🧲', '☎️', '🏧', '⏰', '🧭', '🏚️', '☢️', '📵', '🚓']

# Fetching songs from the given directory
musicDir = './Wishing Bot/musics'
songs = os.listdir(musicDir)


def wishingBot():
    for i in range(len(songs)):
        print(f"[{i}] - {songs[i][:-4]}")
    id = int(input("\nEnter your occasion number - "))

    # emojis printing function
    def playEmojis():
        for i in range(1, 85):
            print('')
        space = ''

        l = len(emojis)

        i = 0
        while pygame.mixer.music.get_busy():
            count = randint(1, 100)
            while count > 0:
                space += ' '
                count -= 1

            if i % 10 == 0:
                print(space + songs[id][:-4] + emojis[0])
            else:
                print(space + emojis[i % l])

            space = ''
            i = i+1
            time.sleep(0.2)

    def playSong():
        pygame.mixer.music.load(os.path.join(musicDir, songs[id]))
        pygame.mixer.music.play()

        # Wait for the song to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        # Song has finished playing, stop the printing function
        thread1.join()

    thread1 = threading.Thread(target=playEmojis)
    thread2 = threading.Thread(target=playSong)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for the song to finish playing
    thread2.join()

    # Exit the program
    sys.exit()


# Start the bot
wishingBot()
