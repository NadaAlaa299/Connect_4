import random
from const import *
from board import Board

AI_PIECE = 'o'
PLAYER_PIECE = 'x'
EMPTY = '-'


class AI:

    def __init__(self, level=1, player='o'):
        self.level = level
        self.player = player
        self.node_count = 0

    # The minimax algorithm
    def minimax(self, board, maximizing, depth):
        self.node_count += 1
        # Base case

        # print("board")
        # board.print_board()
        case = board.is_winning()
        # print(case)
        #   player 1 wins
        if case == 'x':
            return 1, None  # eval, move

        # player 2 wins
        if case == 'o':
            return -1, None

        # draw
        elif board.is_full() or depth == 6:
            return 0, None

        if maximizing:
            temp_board = Board()
            max_eval = -2
            best_move = None
            empty_pos = board.get_empty_pos()

            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                temp_board.mark_pos(row, col, 'x')
                evaluation = self.minimax(temp_board, False, depth + 1)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            temp_board = Board()
            min_eval = 2
            best_move = None
            empty_pos = board.get_empty_pos()
            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                # print(col)
                # print(row)
                temp_board.mark_pos(row, col, 'o')
                evaluation = self.minimax(temp_board, True, depth + 1)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = (row, col)

                # print(min_eval)
                # print(best_move)

            return min_eval, best_move

    # The Alpha-Beta pruning
    def alpha_beta(self, board, maximizing, depth, alpha, beta):
        self.node_count += 1

        # Base case
        case = board.is_winning()

        #   player 1 wins
        if case == 'x':
            return 1, None  # eval, move

        # player 2 wins
        if case == 'o':
            return -1, None

        # draw
        elif board.is_full() or depth == 6:
            return 0, None

        if maximizing:
            temp_board = Board()
            max_eval = -2
            best_move = None
            empty_pos = board.get_empty_pos()

            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                temp_board.mark_pos(row, col, 'x')
                evaluation = self.alpha_beta(temp_board, False, depth + 1, alpha, beta)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = (row, col)

                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break  # Beta cutoff

            return max_eval, best_move

        elif not maximizing:
            temp_board = Board()
            min_eval = 2
            best_move = None
            empty_pos = board.get_empty_pos()
            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                # print(col)
                # print(row)
                temp_board.mark_pos(row, col, 'o')
                evaluation = self.alpha_beta(temp_board, True, depth + 1, alpha, beta)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = (row, col)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break  # Alpha cutoff


            return min_eval, best_move

    # This is minimax alpha beta with one additional factor to make it more realistic
    def minimax_alpha_beta(self, board, maximizing, depth, alpha, beta):
        self.node_count += 1
        # Base case
        #print("board")
        #board.print_board()
        case = board.is_winning()
        #print(case)
      #   player 1 wins
        if case == 'x':
            return 1, None  # eval, move

        # player 2 wins
        elif case == 'o':
            return -1, None


        # draw
        if board.is_full():
            return 0, None

        if (depth == 0):
            return self.scoreCalc(board.board, self.player), None

        if maximizing:
            temp_board = Board()
            max_eval = -2
            empty_pos = board.get_empty_pos()
            best_move = random.choice(empty_pos)
            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                temp_board.mark_pos(row, col, 'x')
                evaluation = self.minimax_alpha_beta(temp_board, False, depth - 1, alpha- 1, beta)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = (row, col)

                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break  # Beta cutoff

            return max_eval, best_move

        elif not maximizing:
            temp_board = Board()
            min_eval = 2
            empty_pos = board.get_empty_pos()
            best_move = random.choice(empty_pos)
            for (row, col) in empty_pos:
                temp_board.board = board.copy_val()
                #print(col)
                #print(row)
                temp_board.mark_pos(row, col, 'o')
                evaluation = self.minimax_alpha_beta(temp_board, True, depth - 1, alpha, beta)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = (row, col)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break  # Alpha cutoff

                # print(min_eval)
                # print(best_move)

            return min_eval, best_move

    def evaluate(self, main_board, depth):
        temp_board = main_board.copy_val()
        evaluation, move = self.minimax_alpha_beta(main_board, False, depth, -100, 100)
        print(f'move: {move} and the evaluation: {evaluation}')
        return move, temp_board

    def evaluateForX(self, main_board, depth, first_move):

        temp_board = main_board.copy_val()
        if first_move:
            return self.randAi(main_board), temp_board
        evaluation, move = self.minimax_alpha_beta(main_board, True, depth, -100, 100)
        print(f'move: {move} and the evaluation: {evaluation}')
        return move, temp_board

    def randAi(self, board):
        emptyPositions = board.get_empty_pos()
        row, col = random.choice(emptyPositions)

        return [row, col]
    def reset_node_count(self):
        self.node_count = 0

    def scoreCalc(self, board, player):
        totalScore = 0
        # vertical
        for col in range(COLS):
            for row in range(ROWS - 3):
                collection = [board[row][col], board[row + 1][col], board[row + 2][col], board[row + 3][col]]
                totalScore += self.getCollectionScore(collection, player)
        # horizontal
        for row in range(ROWS):
            for col in range(COLS - 3):
                collection = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
                totalScore += self.getCollectionScore(collection, player)
        # negative diagonal
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                collection = [board[row+3][col], board[row+2][col+1], board[row+1][col+2], board[row][col+3]]
                totalScore += self.getCollectionScore(collection, player)
        # positive diagonal
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                collection = [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]]
                totalScore += self.getCollectionScore(collection, player)
        return totalScore

    def getCollectionScore(self, collection, player):
        totalScore = 0
        if player == 'x':
            player2 = 'o'
        else:
            player2 = 'x'
        if collection.count(player) == 4:
            totalScore += 100
        elif collection.count(player) == 3 and collection.count('-') == 1:
            totalScore += 10
        elif collection.count(player) == 2 and collection.count('-') == 2:
            totalScore += 5
        if collection.count(player2) == 3 and collection.count('-') == 1:
            totalScore -= 5
        elif collection.count(player2) == 2 and collection.count('-') == 2:
            totalScore -= 2
        elif collection.count(player2) == 1 and collection.count('-') == 3:
            totalScore -= 1
        return totalScore



