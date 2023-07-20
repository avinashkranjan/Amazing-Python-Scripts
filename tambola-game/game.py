from tkinter import *
import random
import tkinter.messagebox

parent = Tk()
numbers_generated = NONE

parent.geometry("950x500")
parent.configure(bg="#B0E2FF")
array1 = []
array2 = []
label = Label(parent, text="", font=("Arial", 24, "bold"))
unique_nums_generated = []
unique_nums_tickets = []
label.pack(pady=200)
buttons1 = {}
buttons2 = {}
button_font = ("Arial", 10)
TAMBOLA = Label(parent, text="TAMBOLA",
                font="Times 20 italic bold underline", bg="#B0E2FF").place(x=400, y=30)


def print_number():
    random_number = random.randint(0, 100)
    if random_number in unique_nums_generated:
        while (random_number in unique_nums_generated):
            random_number = random.randint(0, 100)
    unique_nums_generated.append(random_number)
    label.config(text=str(random_number), bg="#B0E2FF")
    global numbers_generated
    numbers_generated = random_number


def winner():
    x = 0
    if len(array1) == 0:
        x = 1
    elif len(array2) == 0:
        x = 2
    else:
        pass
    if (x != 0):
        popup(x)


def popup(x):
    x = str(x)
    tkinter.messagebox.showinfo("GAME OVER", "player "+x+" won")
    parent.after(5, lambda: parent.destroy())


def pressed(number):
    # print("entered", number,numbers_generated)
    if number == 1:
        if numbers_generated in buttons1.keys():
            buttons1[numbers_generated].configure(bg="pale violet red")
            array1.remove(numbers_generated)
    elif number == 2:
        if numbers_generated in buttons2.keys():
            buttons2[numbers_generated].configure(bg="pale violet red")
            array2.remove(numbers_generated)
    else:
        pass

    winner()


def generate_buttons():

    for numb in range(3):
        buttons1[array1[numb]] = Button(parent, text=array1[numb], width=10, height=5,
                                        font=button_font, bg='LightYellow2', command=lambda: pressed(1))
        buttons1[array1[numb]].place(x=40+(100*numb), y=100)

        buttons2[array2[numb]] = Button(parent, text=array2[numb], width=10,
                                        height=5, font=button_font, bg='LightPink1', command=lambda: pressed(2))
        buttons2[array2[numb]].place(x=600+(100*numb), y=100)
    space = 0
    for numb in range(3, 6):
        buttons1[array1[numb]] = Button(parent, text=array1[numb], width=10, height=5,
                                        font=button_font, bg='LightYellow2', command=lambda: pressed(1))
        buttons1[array1[numb]].place(x=40+(100*space), y=200)

        buttons2[array2[numb]] = Button(parent, text=array2[numb], width=10,
                                        height=5, font=button_font, bg='LightPink1', command=lambda: pressed(2))
        buttons2[array2[numb]].place(x=600+(100*space), y=200)
        space = space+1

    space = 0
    for numb in range(6, 9):
        buttons1[array1[numb]] = Button(parent, text=array1[numb], width=10, height=5,
                                        font=button_font, bg='LightYellow2', command=lambda: pressed(1))
        buttons1[array1[numb]].place(x=40+(100*space), y=300)

        buttons2[array2[numb]] = Button(parent, text=array2[numb], width=10,
                                        height=5, font=button_font, bg='LightPink1', command=lambda: pressed(2))
        buttons2[array2[numb]].place(x=600+(100*space), y=300)
        space = space+1

    number_button = Button(parent, text="CLICK TO GENERATE A NUMBER",
                           command=print_number, width=35, height=4, bg='PaleGreen1')
    number_button.place(x=338, y=260)
    # button1=Button(parent,text=array1[1],width=10,height=5)
    # button1.place(x=150,y=100)


def generate_number():
    x = 0

    while (x < 9):
        number = random.randint(0, 100)
        if number in array1:
            while (number in array1):
                number = random.randint(0, 100)
        array1.append(number)
        x = x+1
    y = 0
    while (y < 9):
        number = random.randint(0, 100)
        if number in array2:
            while (number in array2):
                number = random.randint(0, 100)
        array2.append(number)
        y = y+1

    generate_buttons()


button_start = Button(parent, text="START GAME",
                      command=generate_number, fg="green",)
button_start.pack(side=TOP)
button_end = Button(parent, text="END GAME", fg="red", command=parent.destroy)
button_end.pack(side=BOTTOM)

parent.mainloop()
