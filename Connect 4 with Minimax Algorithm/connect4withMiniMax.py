import numpy as np
import random
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2


def createBoard():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def dropPiece(board, row, col, piece):
    board[row][col] = piece


def isPlaceValid(board, col):
    return board[ROW_COUNT-1][col] == 0


def GetNextRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def printBoard(board):
    print(np.flip(board, 0))


def winningMove(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def scoringScorePosition(selectedGroup, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if selectedGroup.count(piece) == 4:
        score += 100
    elif selectedGroup.count(piece) == 3 and selectedGroup.count(0) == 1:
        score += 5
    elif selectedGroup.count(piece) == 2 and selectedGroup.count(0) == 2:
        score += 2

    if selectedGroup.count(opp_piece) == 3 and selectedGroup.count(0) == 1:
        score -= 4

    return score


def scorePosition(board, piece):
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT-3):
            selectedGroup = row_array[c:c+4]
            score += scoringScorePosition(selectedGroup, piece)

    # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT-3):
            selectedGroup = col_array[r:r+4]
            score += scoringScorePosition(selectedGroup, piece)

    # Score posiive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            selectedGroup = [board[r+i][c+i] for i in range(4)]
            score += scoringScorePosition(selectedGroup, piece)

    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            selectedGroup = [board[r+3-i][c+i] for i in range(4)]
            score += scoringScorePosition(selectedGroup, piece)

    return score


def isTerminalNode(board):
    return winningMove(board, PLAYER_PIECE) or winningMove(board, AI_PIECE) or len(getValidLocations(board)) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    validLocations = getValidLocations(board)
    isTerminal = isTerminalNode(board)
    if depth == 0 or isTerminal:
        if isTerminal:
            if winningMove(board, AI_PIECE):
                return (None, 100000000000000)
            elif winningMove(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, scorePosition(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = GetNextRow(board, col)
            b_copy = board.copy()
            dropPiece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = GetNextRow(board, col)
            b_copy = board.copy()
            dropPiece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def getValidLocations(board):
    validLocations = []
    for col in range(COLUMN_COUNT):
        if isPlaceValid(board, col):
            validLocations.append(col)
    return validLocations


def bestMoveForAI(board, piece):

    validLocations = getValidLocations(board)
    bestScore = -10000
    bestMove = random.choice(validLocations)
    for col in validLocations:
        row = GetNextRow(board, col)
        temp_board = board.copy()
        dropPiece(temp_board, row, col, piece)
        score = scorePosition(temp_board, piece)
        if score > bestScore:
            bestScore = score
            bestMove = col

    return bestMove


def drawBoard(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r *
                             SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(
                c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = createBoard()
printBoard(board)
isGameOver = False

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()
pygame.display.set_caption('Connect 4')
myfont = pygame.font.SysFont("monospace", 75)

turn = random.randint(PLAYER, AI)

while not isGameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(
                    screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if isPlaceValid(board, col):
                    row = GetNextRow(board, col)
                    dropPiece(board, row, col, PLAYER_PIECE)

                    if winningMove(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 win!!", 1, RED)
                        screen.blit(label, (40, 10))
                        isGameOver = True

                    turn += 1
                    turn = turn % 2

                    printBoard(board)
                    drawBoard(board)

    # # Ask for Player 2 Input
    if turn == AI and not isGameOver:

        # col = random.randint(0, COLUMN_COUNT-1)
        # col = bestMoveForAI(board, AI_PIECE)
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

        if isPlaceValid(board, col):
            # pygame.time.wait(500)
            row = GetNextRow(board, col)
            dropPiece(board, row, col, AI_PIECE)

            if winningMove(board, AI_PIECE):
                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                isGameOver = True

            printBoard(board)
            drawBoard(board)

            turn += 1
            turn = turn % 2

    if isGameOver:
        pygame.time.wait(5000)
