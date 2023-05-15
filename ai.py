import copy
from board import Board


class AI:

    def __init__(self, level=1, player='o'):
        self.level = level
        self.player = player

    def minimax(self, board, maximizing, depth):
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
                #print(col)
                #print(row)
                temp_board.mark_pos(row, col, 'o')
                evaluation = self.minimax(temp_board, True, depth + 1)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = (row, col)

                   #print(min_eval)
                    #print(best_move)

            return min_eval, best_move

    def evaluate(self, main_board):
        temp_board = main_board.copy_val()
        evaluation, move = self.minimax(main_board, False, 0)
        print(f'move: {move} and the evaluation: {evaluation}')

        return move, temp_board
