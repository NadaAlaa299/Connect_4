import numpy as np
import random
import pygame
import sys
import math

rows = 6
cols = 7

def make_board():
    board = [['-' for j in range(cols)] for i in range(rows)]
    return board

def print_board(board):
    for rows in board:
        print(' | '.join(rows))


def insert(board, player, colms):
    # Loop to check if the tile is empty
    for i in range(5, -1, -1):
        if board[i][colms] == '-':
            board[i][colms] = player
            return True

    return False

def player_turn(board, player):
    if player == 'x':
        colms = random.randint(0, 6)
        print("Computer chooses column:", colms)
    else:
        colms = int(input("Player " + player + ", choose a column (0-6): "))
    if colms < 0 or colms >= cols:
        print("Invalid column. Try again.")
        return player_turn(board, player)
    elif not insert(board, player, colms):
        print("Column is full. Try again.")
        return player_turn(board, player)

    return board


def is_winning(board):
    # search in rows
    pl1 = 'x'
    pl2 = 'o'
    for i in range(3):
        for j in range(7):
            # condition to check if there are 4 same chars in a row
            # by doing a change in row but column stays the same
            if board[i][j] == 'x' and board[i + 1][j] == 'x' and board[i + 2][j] == 'x' and board[i + 3][j] == 'x':
                return pl1
            elif board[i][j] == 'o' and board[i + 1][j] == 'o' and board[i + 2][j] == 'o' and board[i + 3][j] == 'o':
                return pl2

    # search in columns
    for j in range(4):
        for i in range(6):
            # condition to check if there are 4 same chars in a column
            # by doing a change in column but row stays the same
            if board[i][j] == 'x' and board[i][j + 1] == 'x' and board[i][j + 2] == 'x' and board[i][j + 3] == 'x':
                return pl1
            elif board[i][j] == 'o' and board[i][j + 1] == 'o' and board[i][j + 2] == 'o' and board[i][j + 3] == 'o':
                return pl2

    # search in diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] == 'x' and board[i + 1][j + 1] == 'x' and board[i + 2][j + 2] == 'x' and board[i + 3][
                j + 3] == 'x':
                return pl1
            elif board[i][j] == 'o' and board[i + 1][j + 1] == 'o' and board[i + 2][j + 2] == 'o' and board[i + 3][
                j + 3] == 'o':
                return pl2
            elif board[i][j] == 'x' and board[i + 1][j - 1] == 'x' and board[i + 2][j - 2] == 'x' and board[i + 3][
                j - 3] == 'x':
                return pl1
            elif board[i][j] == 'o' and board[i + 1][j - 1] == 'o' and board[i + 2][j - 2] == 'o' and board[i + 3][
                j - 3] == 'o':
                return pl2
    return 0



def play_game():
    print("Hello, let's start the game\n")
    board = make_board()
    print_board(board)
    players = ['x', 'o']
    current_player = 0
    while True:
        player = players[current_player]
        board = player_turn(board, player)
        print_board(board)
        winner = is_winning(board)
        if winner:
            print("Player " + winner + " wins!")
            break
        current_player = (current_player + 1) % 2

play_game()