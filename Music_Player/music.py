import pygame


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def main():
    print("Simple Music Player")
    print("-------------------")

    while True:
        print("1. Play Music")
        print("2. Stop Music")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = r"./Otnicka_-_Peaky_Blinder_(lyrics)___i_am_not_outsider_i'm_a_peaky_blinder(256k).mp3"
            play_music(file_path)
        elif choice == "2":
            stop_music()
        elif choice == "3":
            stop_music()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
