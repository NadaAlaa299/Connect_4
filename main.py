from board import Board
from ai import AI


game_board = Board()
ai = AI()


def main():
    print("Hello, let's start the game\n")
    game_board.print_board()
    players = ['x', 'o']
    current_player = 0
    while True:
        player = players[current_player]
        game_board.player_turn(player)
        if player == 'x':
            game_board.player_turn(player)

        if game_board.is_winning():
            print("Player " + game_board.is_winning() + " wins!")
            break
        current_player = (current_player + 1) % 2

main()
