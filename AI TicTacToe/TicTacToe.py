import random


def display_board(board):
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]  # diagonals
    ]
    return any(all(board[i] == mark for i in combination) for combination in winning_combinations)


def choose_first():
    return random.choice(['Player 1', 'Player 2'])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
    return position


def replay():
    choice = input('Do you want to play again? Enter Yes or No: ')
    return choice.lower() == 'yes'


def play_tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    while True:
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input('Are you ready to play? Enter y or n: ')
        if play_game.lower() == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Player 1 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            if play_game.lower() == 'n':
                print('BYE! Have a good day.')
            else:
                print('Thank you for playing.')
            break


# Start the game
play_tic_tac_toe()
