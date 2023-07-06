# TIC TAC TOE Minmax algorithm
'''
1. Backtracking algorithm
2. Max wiil try to maximize it utility 
3. Min will try to minimize user or human utility to win
4. Time complexity : O(b^d)

b : branching factor (choices, number of possible move)
d : depth 
'''

# Format colour
import random
bright_cyan = "\033[0;96m"

# import package

board = [' ' for i in range(10)]


def insertLetter(letter, pos):
    '''
    insert either 'O' or 'X' at perticular position
    '''
    board[pos] = letter


def spaceIsFree(pos):
    '''
    Boolean : Check whether their is any empty position is present or not in the board
    '''
    return board[pos] == ' '


def printBoard(board):
    '''
    Display the board 
    '''
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, letter):
    '''
    Boolean : check whether winning criteria met or not
    '''
    # condition of horizontal, vertical, diagonal
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
        (board[4] == letter and board[5] == letter and board[6] == letter) or \
        (board[7] == letter and board[8] == letter and board[9] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[3] == letter and board[6] == letter and board[9] == letter) or \
        (board[1] == letter and board[5] == letter and board[9] == letter) or \
        (board[3] == letter and board[5] == letter and board[7] == letter)


def playerMove():
    '''
    Take the input from user and validate user's input
    '''
    run = True
    while run:
        try:

            move = int(input("Select a position to place \'X\' (1-9) : "))
            if isinstance(move, str):
                print("Please enter the valid number 😏")
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Position is already occupied 😳")
            else:
                print("Please enter valid position within the valid range 😏")
        except:
            print("Please enter the valid number 😏")


def compMove():
    '''
    Function decide computer's moves i.e where to place 'O' , so that it win
    '''
    # 1. winning move
    # 2. Block move ,if human gets benefited
    # 3. move at corner
    # 4. move at center
    # 5. move at any edge
    possibleMove = [
        x for x, letter in enumerate(board) if letter == ' ' and x != 0
    ]
    move = 0

    # 1st way -> To check whether computer can win or not , if not then
    # computer now tries to block opponent move, so that he could not win
    for let in ['O', 'X']:
        for i in possibleMove:
            # replica of board
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    if board[1] == 'X' or board[3] == 'X' or board[7] == 'X' or board[9] == 'X':
        if 5 in possibleMove:
            move = 5
            return move

    edgesOpen = []

    if (board[1] == 'X' and board[9] == 'X') or (board[3] == 'X'
                                                 and board[7] == 'X'):
        for i in possibleMove:
            if i in [2, 4, 6, 8]:
                edgesOpen.append(i)

    # randomly select a corner to move Into
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    # Same code repeat for edges also
    cornersOpen = []

    # Check whether there is any corner is empty if find empty then we place
    # letter in that corner position

    for i in possibleMove:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # randomly select a corner to move Into
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Place letter at center pow
    if 5 in possibleMove:
        move = 5
        return move

    # Check whether there is any edge is empty if find empty then we place
    # letter in that edge position

    for i in possibleMove:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    # randomly select a corner to move Into
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    return random.choice(li)


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# Human = 'X'
# Bot = 'O'


def main():
    '''
    Main function 
    '''
    print(bright_cyan +
          "# -----------  Welcome to TIC TAC TOE ------------- #")
    name = input("Enter your name : ")
    print("👲  {} : \'X\' and 🤖  Computer : \'O\' ".format(name.capitalize()))
    print()

    printBoard(board)

    while not (isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()  # Ask player for next move
            printBoard(board)  # print board
        else:
            print("\nOOPS O\'s won the game 😞  !!")
            break

        if not isWinner(board, 'X'):
            move = compMove()  # Ask computer for next move
            if move == 0:
                print('Tie game !!')
            else:
                insertLetter('O', move)
                print("Computer enter \'O\' at Position : {}".format(move))
                printBoard(board)  # print board
        else:
            print("\nYeah X\'s won the game 😎  !!")
            break

    if isBoardFull(board):
        print("Game over !!")


main()

while True:
    print()
    ans = input("Do want to play again 😀  ... ? (Y|N) : ")
    print()  # next line
    if ans.lower() == 'y' and ans.upper() == 'Y':
        board = [' ' for i in range(10)]
        main()
    else:
        break
