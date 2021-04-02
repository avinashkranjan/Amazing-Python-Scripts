import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# variable to decide the turn of which player
turn = 0
# Creates an empty board
board = [[" " for x in range(3)] for y in range(3)]


# function to give the global variables to default
def clear():
    global board, turn
    board = [[" " for x in range(3)] for y in range(3)]
    turn = 0


# To check if the game has a winner or not according to the logic
def winner(brd, mark):
    return ((brd[0][0] == brd[0][1] == brd[0][2] == mark) or (brd[1][0] == brd[1][1] == brd[1][2] == mark) or
            (brd[2][0] == brd[2][1] == brd[2][2] == mark) or (brd[0][0] == brd[1][0] == brd[2][0] == mark) or
            (brd[0][1] == brd[1][1] == brd[2][1] == mark) or (brd[0][2] == brd[1][2] == brd[2][2] == mark) or
            (brd[0][0] == brd[1][1] == brd[2][2] == mark) or (brd[0][2] == brd[1][1] == brd[2][0] == mark))


# To declare the result of the game in multiplayer
def get_text_mp(i, j, gb, plyr1, plyr2):
    global button
    global turn
    if board[i][j] == ' ':
        if turn % 2 == 0:
            plyr1.config(state=DISABLED)
            plyr2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            plyr2.config(state=DISABLED)
            plyr1.config(state=ACTIVE)
            board[i][j] = "O"
        turn += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        messagebox.showinfo("Winner", "Player 1 won the match!")
        clear()
    elif winner(board, "O"):
        gb.destroy()
        messagebox.showinfo("Winner", "Player 2 won the match!")
        clear()
    elif is_board_full():
        gb.destroy()
        messagebox.showinfo("Winner?", "Game has been tied!")
        clear()


# Check the board is full or not
def is_board_full():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


def gameboard_mp(game_board, plyr1, plyr2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_mp, i, j, game_board, plyr1, plyr2)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Function to decide the move for the computer
def comp_move():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if not possiblemove:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]


# To declare the result of the game in single player
def get_text_sp(i, j, gb, plyr, comp):
    global turn
    if board[i][j] == ' ':
        if turn % 2 == 0:
            plyr.config(state=DISABLED)
            comp.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            comp.config(state=DISABLED)
            plyr.config(state=ACTIVE)
            board[i][j] = "O"
        turn += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        messagebox.showinfo("Winner", "You won the match!")
        clear()
    elif winner(board, "O"):
        gb.destroy()
        x = False
        messagebox.showinfo("Winner", "Computer won the match!")
        clear()
    elif is_board_full():
        gb.destroy()
        x = False
        messagebox.showinfo("Winner?", "Game has been tied!")
        clear()
    if x:
        if turn % 2 != 0:
            move = comp_move()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_sp(move[0], move[1], gb, plyr, comp)


def gameboard_sp(game_board, plyr, comp):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_sp, i, j, game_board, plyr, comp)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Creation of single player mode window
def single_player():
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    plyr = Button(game_board, text="Player : X", width=10)
    plyr.grid(row=1, column=1)
    comp = Button(game_board, text="Computer : O", width=10, state=DISABLED)
    comp.grid(row=2, column=1)
    gameboard_sp(game_board, plyr, comp)


# Creation of multiplayer mode window
def multi_player():
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    plyr1 = Button(game_board, text="Player 1 : X", width=10)
    plyr1.grid(row=1, column=1)
    plyr2 = Button(game_board, text="Player 2 : O", width=10, state=DISABLED)
    plyr2.grid(row=2, column=1)
    gameboard_mp(game_board, plyr1, plyr2)


# Defines the Game main menu GUI
def main():
    menu = Tk()
    # set new geometry of the window
    menu.geometry('350x400')
    menu.title("GAME MENU")

    head = Button(menu, text="---Welcome to tic-tac-toe---", activeforeground='#fad744', activebackground="#2b3252"
                  , bg="#fad744", fg="#2b3252", width=500, font='summer', bd=10, padx=10, pady=20)

    b1 = Button(menu, text="Single Player Mode", command=single_player, activeforeground='#fad744', activebackground="#2b3252"
                , bg="#fad744", fg="#2b3252", width=500, font='summer', bd=5)

    b2 = Button(menu, text="Multi Player Mode", activeforeground='#fad744', command=multi_player, activebackground="#2b3252",
                bg="#fad744", fg="#2b3252", width=500, font='summer', bd=5)

    b3 = Button(menu, text="Exit Game", command=menu.destroy, activeforeground='#fad744', activebackground="#2b3252",
                bg="#fad744", fg="#2b3252", width=500, font='summer', bd=5)
    
    head.pack(pady=20)
    b1.pack(padx=20, pady=20)
    b2.pack(padx=20, pady=20)
    b3.pack(padx=20, pady=20)
    menu.configure(bg="#ef5455")
    menu.mainloop()


main()
