# memory-game
A python cli memory game.

## :mahjong: Game Description

A player guesses where are pairs fo shapes (letters) on the board.


### :1234: Game Setup

At game start, the player can configure the game board size by setting its number of rows and columns - board size
should be with an even number of cells that is between 4-52 (rows X columns = cells).


### :repeat: Game Turns

Each turn the player choose 2 cells to reveal. After he enters his first choice, that cell is revealed on the board,
and he can see it before choosing the 2nd cell to reveal.

:white_check_mark: If these 2 cells holds a pair of identical shapes (letters), they stay revealed and next turn will
start.

:hourglass_flowing_sand: If it isn't a matching pair, player will get 5 seconds to memorize them before they are
covered again and next turn will start.



A cell to reveal is chosen by entering its column and row separated by a comma - :dart: 0,0 for the top left cell.
A 4 by 4 board will look like this:
```
  0   1   2   3
0 * | * | * | *
 ---+---+---+---
1 * | * | * | *
 ---+---+---+---
2 * | * | * | *
 ---+---+---+---
3 * | * | * | *
```


### :checkered_flag: Game End

Game is won when all pairs are revealed.
After a game is ended, player can choose to play again, if he doesn't, a summery will be printed:

- :8ball: Number of games played.

- :trophy: Best game for each board played (minimum number of moves).
