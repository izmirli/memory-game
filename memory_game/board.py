"""A cli memory game board.

A representation of a memory game board and functions to interact with it.
"""

import string
from random import shuffle


class Board:
    """A memory game board."""

    def __init__(self):
        self.rows = 4
        self.columns = 4
        self.bg_board = []
        self.fg_board = []
        self.games_history = {'games': 0}

    def set_board_size(self, columns, rows):
        """Set the game board's number of columns and rows.

        Will raise UserWarning in input params are invalid - not even number
        of cells or not between 4-52 cells.

        :param columns: int number of columns.
        :param rows:  int number of rows.
        :return: None.
        """
        if rows * columns < 4:
            raise UserWarning(f'Game bored mast have at least 4 cells ({rows} X {columns} = {rows * columns}).')
        if rows * columns % 2 != 0:
            raise UserWarning(f'Game bored mast have an even number of cells ({rows} X {columns} = {rows * columns}).')
        if rows * columns / 2 > len(string.ascii_uppercase):
            raise UserWarning(f'Game bored mast not have more then {len(string.ascii_uppercase) * 2} cells \
({rows} X {columns} = {rows * columns}).')
        self.rows = rows
        self.columns = columns

    def new_board(self):
        """Set (or reset) game bored representation to starting position.

        Set foreground and background boards - foreground with asterisks,
        background with randomise placed pairs of letters.

        :return: None
        """
        self.fg_board = ['*' for _ in range(self.columns * self.rows)]
        self.bg_board = [string.ascii_uppercase[i] for i in range(int(self.columns * self.rows / 2))]
        self.bg_board = self.bg_board + self.bg_board
        shuffle(self.bg_board)

    def coordinates_to_index(self, col, row):
        """Convert from 2d coordinates to the 1d index on game's board.

        :param col: int column coordinate.
        :param row: int row coordinate.
        :return: int cell 1D index.
        """
        return self.columns * row + col

    def is_game_over(self):
        """Check if game is over (all pairs are revealed - no more moves).

        :return: True if game is over. False otherwise.
        """
        return False if '*' in self.fg_board else True

    def is_unknown(self, cell):
        """Check if given cell index is unknown - no revealed yet.

        :param cell: int cell index.
        :return: True if unknown. False otherwise.
        """
        return True if '*' == self.fg_board[cell] else False

    def is_match(self, cell1, cell2):
        """Check if the 2 given cell indexes are holding a matching pair.

        :param cell1: int cell index.
        :param cell2: int cell index.
        :return: True if matching pair. False otherwise.
        """
        return True if self.bg_board[cell1] == self.bg_board[cell2] else False

    def reveal(self, cell):
        """Reveal a cell on the foreground boeard and display (print) it.

        :param cell: int cell index.
        :return: None.
        """
        self.fg_board[cell] = self.bg_board[cell]
        self.display()

    def unreveal(self, cell1, cell2):
        """Cover given cells on the foreground boeard and display (print) it.

        :param cell1: int cell index.
        :param cell2: int cell index.
        :return: None.
        """
        self.fg_board[cell1] = '*'
        self.fg_board[cell2] = '*'
        self.display()

    def display(self):
        """Printout the bored with the current cells shapes and coordinates.

        :return: None
        """
        print('  ' + '   '.join([str(i) for i in range(self.columns)]))
        for y in range(self.rows):
            print(str(y) + ' ' + ' | '.join(self.fg_board[y * self.columns:y * self.columns + self.columns]) + ' ')
            if self.rows != y + 1:
                print(' ---' + '+---' * (self.columns - 1))
        print()

    def add_game_to_history(self, turns):
        """Add this game to the board's game history.

        1. Increment number of games.
        2. For current game's number of shapes, add/update numbers of turns to
           win if previously nonexistent or bigger than current one.

        :param turns: int number of turns to win current board.
        :return: None.
        """
        self.games_history['games'] += 1
        number_of_shapes = int(self.columns * self.rows / 2)
        if number_of_shapes not in self.games_history or self.games_history[str(number_of_shapes)] > turns:
            self.games_history[str(number_of_shapes)] = turns

    def print_games_history(self):
        """Display board's games history.

        print a summery of all games played on this board:
        * Number of games played.
        * Best game for each number of shapes played (minimum number of turns).

        :return: None.
        """
        print(f"You have played {self.games_history['games']} game{'' if 1 == self.games_history['games'] else 's'}.")
        print('Best games:')
        for shapes in self.games_history:
            if 'games' == shapes:
                continue
            print(f'\t{shapes} shapes board: {self.games_history[shapes]} turns.')
