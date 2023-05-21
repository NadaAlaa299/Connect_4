# Connect Four Game

This is a Python implementation of the Connect Four game. The game allows two players to take turns dropping colored discs into a grid, with the goal of connecting four discs of the same color in a row, column, or diagonal.
 
 ## Dependencies

- Python 3.x
- Pygame library

## How to Run the Game

1. Install Python 3.x on your system if it is not already installed.
2. Install the Pygame library by running the following command:
   ```
   pip install pygame
   ```
3. Download or clone the project source code from the repository.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the following command to start the game:
   ```
   python main.py
   ```

## How to Play

1. The game starts with an empty grid.
2. Two players take turns dropping their discs into the grid by selecting a column.
3. The goal is to connect four discs of the same color in a row, column, or diagonal.
4. The first player to connect four discs wins the game.
5. If the grid is completely filled without a winner, the game is a draw.

## Game Controls

- Mouse: Click on a column to drop a disc into that column.
- Keyboard:
  - Left/Right Arrow Keys: Move the cursor left or right.
  - Enter/Return Key: Drop a disc into the selected column.
  - Escape Key: Quit the game.

## AI Player

The game includes an AI player that can be enabled to play against the human player. The AI player uses the minimax algorithm with alpha-beta pruning to make intelligent moves. The AI player has three difficulty levels (1, 2, and 3), with level 1 being the easiest and level 3 being the most challenging.

To enable the AI player, modify the `AI_PLAYER_ENABLED` constant in the `const.py` file. Set it to `True` to enable the AI player or `False` to play against another human player.

## Credits

| Name | ID |  Section  |GitHub
| --- | --- | --- | --- |
| Mohamed Sayed Ali | 20200450 | CS S6-S7 |@moGaara
| Mohamed Yasser Shehta | 20200484 | CS S5 |@newYasser
| Nada Alaa | 20200589 | CS S6-S7 |@NadaAlaa299
| Mohamed Samy Abdelsalam  | 20200445 | CS S6-S7 |@muhammedelsepa3y





