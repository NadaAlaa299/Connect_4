from const import *
import random
class Board:
    def __init__(self):
        self.board = [['-' for j in range(COLS)] for i in range(ROWS)]
        self.empty_pos = []

    def print_board(self):
        for rows in self.board:
            print(' | '.join(rows))

    def is_empty(self, player, cols):
        # Loop to check if the tile is empty
        for i in range(5, -1, -1):
            if self.board[i][cols] == '-':
                self.board[i][cols] = player
                return True

        return False

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
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != '-':
                    return self.board[i][j]
                elif self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] != '-':
                    return self.board[i][j]
        return 0

    def player_turn(self, player):
        if player == '#':
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

    def get_empty_pos(self):
        pass


    def is_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == '-':
                   return False
        return True



Board().print_board()