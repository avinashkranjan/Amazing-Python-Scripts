# -*- coding: utf-8 -*-


import random

from tkinter import *

#variables and Dictionary
# These are total events that could occur if/else can also be used but they are pain to implement
schema = {
    "rock": {"rock": 1, "paper": 0, "scissors": 2},
    "paper": {"rock": 2, "paper": 1, "scissors": 0},
    "scissors": {"rock": 0, "paper": 2, "scissors": 1}
}

comp_score = 0

player_score = 0

# functions


def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["rock", "paper", "scissors"]
    num = random.randint(0, 2)
    computer_choice = outcomes[num]
    result = schema[user_choice][computer_choice]

    # now config the labes acc to the choices
    Player_Choice_Label.config(
        fg="green", text="Player choice : "+str(user_choice))

    Computer_Choice_Label.config(
        fg="red", text="Computer choice : "+str(computer_choice))

    if result == 2:
        player_score += 2
        Player_Score_Label.config(text="Player : "+str(player_score))
        Outcome_Label.config(fg="blue", bg="skyblue", text="Player-Won")
    elif result == 1:
        player_score += 1
        comp_score += 1
        Player_Score_Label.config(text="Player : "+str(player_score))
        Outcome_Label.config(fg="blue", bg="skyblue", text="Draw")
        Computer_Score_Label.config(text="Computer : "+str(comp_score))
    elif result == 0:
        comp_score += 2
        Outcome_Label.config(fg="blue", bg="skyblue", text="Computer-Won")
        Computer_Score_Label.config(text="Computer : "+str(comp_score))


# main Screen
master = Tk()
master.title("RPS")
# labels
Label(master, text="Rock , Paper , Scissors", font=(
    "Calibri", 15)).grid(row=0, sticky=N, pady=10, padx=200)

Label(master, text="Please Select an option",
      font=("Calibri", 12)).grid(row=2, sticky=N)

Player_Score_Label = Label(master, text="Player : 0", font=(
    "Calibri", 12))  # label for player Score
Player_Score_Label.grid(row=3, sticky=W)

Computer_Score_Label = Label(master, text="Computer : 0", font=(
    "Calibri", 12))  # label for computer score
Computer_Score_Label.grid(row=3, sticky=E)
# player and computer choice labels
Player_Choice_Label = Label(master, font=("Calibri", 12))
Player_Choice_Label.grid(row=5, sticky=W)

Computer_Choice_Label = Label(master, font=("Calibri", 12))
Computer_Choice_Label.grid(row=5, sticky=E)
# outcome Labels
Outcome_Label = Label(master, font=("Calibri", 12))
Outcome_Label.grid(row=5, sticky=N, pady=10)


# buttons
Button(master, text="Rock", width=17, command=lambda: outcome_handler(
    "rock")).grid(row=6, sticky=W, padx=10, pady=10)
Button(master, text="Paper", width=17, command=lambda: outcome_handler(
    "paper")).grid(row=6, sticky=N, pady=10)
Button(master, text="Scissors", width=17, command=lambda: outcome_handler(
    "scissors")).grid(row=6, sticky=E, padx=10, pady=10)

# dummy label to create space at the end of master screen
Label(master).grid(row=5)
master.mainloop()
