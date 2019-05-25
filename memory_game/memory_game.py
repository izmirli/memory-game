"""A python cli memory game.

A player guesses where are pairs fo shapes (letters) on the board.

At game start, the player can configure the game board size by
setting its number of rows and columns - board size should be with
an even number of cells that is between 4-52 (rows X columns = cells).

Each turn the player choose 2 cells to reveal. After he enters his
first choice, that cell is revealed on the board, and he can see it
before choosing the 2nd cell to reveal. If these 2 cells holds a pair
of identical shapes (letters), they stay revealed and next turn will
start. If it isn't a matching pair, player will get 5 seconds to
memorize them before they are covered again and next turn will start.

A cell to reveal is chosen by entering its column and row separated
by a comma - 0,0 for the top left cell. A 4 by 4 board will look like
this:

  0   1   2   3
0 * | * | * | *
 ---+---+---+---
1 * | * | * | *
 ---+---+---+---
2 * | * | * | *
 ---+---+---+---
3 * | * | * | *

After a game is ended, he can choose to play again, if he doesn't,
a summery will be printed:
* Number of games played.
* Best game for each board played (minimum number of moves).
"""

import os
from time import sleep
from board import Board


def play_game(board):
    """Play a single game, from resetting board and till finding all pairs.

    Set (or reset) game board, clear screen and display starting board.
    Loop for each turn move and count them till game has ended.
    Print end game message and add game to board history.

    :param board: Board object.
    :return: None
    """
    clear()
    board.new_board()
    board.display()
    turns = 0
    while not board.is_game_over():
        turns += 1
        next_move(board)
    print(f'Success! you solved the game after {turns} turns.')
    board.add_game_to_history(turns)


def next_move(board):
    """Get and make player's next move (cells to reveal this turn).

    Get cells coordinates from user one by one, revealing them on the board.
    If it isn't a matching pair, pause for 5 seconds and "cover" them.

    :param board: Board object.
    :return: None
    """
    print('What is your next move? Enter the 2 cells to reveal (give coordinates for each of them).')
    cell1 = get_cell(board)
    clear()
    board.reveal(cell1)
    cell2 = get_cell(board, cell1)
    clear()
    board.reveal(cell2)
    if not board.is_match(cell1, cell2):
        for countdown in range(5, 0, -1):
            print(countdown)
            sleep(1)
        board.unreveal(cell1, cell2)
        clear()
        board.display()


def get_cell(board, prev_cell=None):
    """Get next cell to reveal from user.

    Prompt user for next cell to reveal coordinates.
    If no valid input is given, user warning will be printed, and user will
    be proped again.

    :param board: Board object.
    :param prev_cell: int index of previous cell revealed in this turn.
    Optional param to be used if this is 2nd cell in the current turn.
    :return: int index of the cell to reveal.
    """
    while True:
        cell = input(f"{'1st' if prev_cell is None else '2nd'} cell coordinates (column,row): ")
        try:
            col, row = cell.split(',')
            col = int(col)
            row = int(row)
        except TypeError as e:
            print(e)
            continue
        except ValueError:
            print('No valid coordinates given. Please use column,row format (e.g. 2,1).')
            continue
        cell_index = board.coordinates_to_index(col, row)
        try:
            if not board.is_unknown(cell_index):
                print(f'The cell at {col},{row} is already revealed. Please choose a different one.')
                continue
            elif prev_cell is not None and prev_cell == cell_index:
                print('These are same coordinates of previous cell. Please choose a different one.')
                continue
        except IndexError:
            print(f'Invalid coordinates given - please stay withing the game board \
(0-{board.columns - 1},0-{board.rows - 1}).')
            continue
        return cell_index


def board_size_by_user(board):
    """Get and set board size by user input.

    Prompt user to enter number of rows and columns for the board. Default are
    the currant board settings (used in user enter nothing).
    If no valid inputs are given, user warning will be printed and he will be
    prompted for input again.

    :param board: Board object.
    :return: None
    """
    while True:
        print('Please set game board size (need to have even number of cells, that is between 4-52).')
        try:
            rows = input(f'Number of rows ({board.rows}):')
            rows = board.rows if '' == rows else int(rows)
            cols = input(f'Number of rows ({board.columns}):')
            cols = board.columns if '' == cols else int(cols)
        except (TypeError, ValueError):
            print(f'Invalid input. Please use numbers only.')
            continue
        try:
            board.set_board_size(cols, rows)
        except UserWarning as e:
            print(e)
            continue
        break


def play_again():
    """Ask user if he wants to play again.

    I user enters 'y' or 'Y' this means he wants to play again. Anything else,
    including entering nothing, is considered as a refusal to play again.

    :return: True if user if he wants to play again, False othrwise.
    """
    return True if 'y' == input('Do you want to play again (N/y)? ').casefold() else False


def clear():
    """Clear cli screen

    :return: None
    """
    os.system('clear' if 'posix' == os.name else 'cls')


def main():
    """Main function called at start to initialize and run games.

    After board initialization starts a loop of games, for each:
    1. get and set board size by user's input.
    2. play a single game.
    3. loop again if players wants to.
    Before exiting, print games summery (number of games and best scores).

    :return: None
    """
    b = Board()
    while True:
        board_size_by_user(b)
        play_game(b)
        if not play_again():
            break
    b.print_games_history()


if __name__ == "__main__":
    main()
