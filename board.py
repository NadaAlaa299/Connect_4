from const import *
import random


class Board:
    def __init__(self):
        self.board = [['-' for _ in range(COLS)] for _ in range(ROWS)]
        self.empty_pos = []
        self.winPos = []


    def is_empty(self, player, cols):
        # Loop to check if the tile is empty
        if self.board[5][cols] != '-':
            return False
        for i in range(0, 6, 1):
            if self.board[i][cols] == '-':
                self.board[i][cols] = player
                return True

        return False


    def copy_val(self):
        copy_board = [['-' for _ in range(COLS)] for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                copy_board[row][col] = self.board[row][col]
        return copy_board

    def is_winning(self):
        # search in rows
        for i in range(3):
            for j in range(7):
                # condition to check if there are 4 same chars in a row
                # by doing a change in row but column stays the same
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != '-':
                    return self.board[i][j]

        # search in columns
        for j in range(4):
            for i in range(6):
                # condition to check if there are 4 same chars in a column
                # by doing a change in column but row stays the same
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != '-':
                    return self.board[i][j]

        # search in diagonals
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][
                    j + 3] != '-':
                    return self.board[i][j]
        for i in range(COLS-3):
            for j in range(3, ROWS):
                if self.board[j][i] == self.board[j - 1][i + 1] == self.board[j - 2][i + 2] == self.board[j - 3][
                    i + 3] != '-':
                    return self.board[j][i]


        return 0

    def player_turn(self, player):
        if player == 'x':
            colms = random.randint(0, 6)
            print("Computer chooses column:", colms)
        else:
            colms = int(input("Player " + player + ", choose a column (0-6): "))
        if colms < 0 or colms >= COLS:
            print("Invalid column. Try again.")
            return self.player_turn(player)
        elif not self.is_empty(player, colms):
            print("Column is full. Try again.")
            return self.player_turn(player)

    def play(self, player):
        col = int(input("Player " + player + ", choose a column (0-6): "))
        if col < 0 or col >= COLS:
            print("Invalid column. Try again.")
            return self.play(player)
        elif not self.is_empty(player, col):
            print("Column is full. Try again.")
            return self.play(player)

    def get_empty_pos(self):
        self.empty_pos.clear()
        for col in range(COLS):
            for row in range(0, 6, 1):
                if self.board[row][col] == '-':
                    self.empty_pos.append((row, col))
                    break
        return self.empty_pos

    def mark_pos(self, row, col, player):
        self.board[row][col] = player

    def is_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == '-':
                    return False
        return True

    def print_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                print(self.board[row][col], end=' ')
            print()
        print()

