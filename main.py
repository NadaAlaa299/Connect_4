from board import Board
from ai import AI




def main():
    print("Hello, let's start the game\n")
    game_board = Board()
    ai = AI()
    current_player = 0
    while True:
        if current_player == 0:
            game_board.play('x')
        elif current_player == 1:
            pos, temp_board = ai.evaluate(game_board)
            game_board.board = temp_board
            game_board.mark_pos(pos[0], pos[1], 'o')
        game_board.print_board()
        if game_board.is_winning():
            print("Player " + game_board.is_winning() + " wins!")
            break
        current_player = (current_player + 1) % 2

main()
