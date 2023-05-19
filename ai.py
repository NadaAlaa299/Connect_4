import random

from board import Board

ROW_COUNT = 6
COLUMN_COUNT = 7
AI_PIECE = 'x'
PLAYER_PIECE = 'o'
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
        if case == 'o':
            return -1, None

        # draw
        if board.is_full():
            return 0, None

        if (depth == 0):
            return score_position(board.board, self.player), None

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


def score_position(board, piece):
    score = 0

    # Evaluate rows
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            window = board[row][col:col + 4]
            score += evaluate_window(window, piece)

    # Evaluate columns
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            window = [board[i][col] for i in range(row, row + 4)]
            score += evaluate_window(window, piece)

    # Evaluate diagonals (positive slope)
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Evaluate diagonals (negative slope)
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            window = [board[row + 3 - i][col + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score
