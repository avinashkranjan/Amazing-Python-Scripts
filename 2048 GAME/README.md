# Project Name

This is a simple implementation of the classic game 2048 in Python. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. The game ends when the grid is full, and no more moves can be made, or when the player successfully creates the 2048 tile.

## How to Play (For Games/Apps)

Initialization: At the start of the game, an empty 4x4 grid is displayed with two randomly placed tiles, each having a value of 2.

Controls: Use the following keys to control the game:

'W' or 'w': Move Up
'S' or 's': Move Down
'A' or 'a': Move Left
'D' or 'd': Move Right
Gameplay: The game progresses with each move in the direction specified by the player. All tiles slide in the specified direction until they reach the grid's edge or collide with another tile of the same value. If two tiles of the same value collide, they merge into a single tile with double the value. After each move, a new tile with a value of 2 is added to the grid at a random empty cell.

Winning Condition: The game is won when a tile with the value of 2048 is created.

Losing Condition: The game is lost when the grid is full, and no more valid moves can be made.

## Features

Basic 2048 gameplay with grid and tile manipulation.
Random tile generation after each move.
Game over and win conditions detection.
Simple console-based interface.

## Technologies Used

Python programming language.
