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
        self.fg_board = ['*' for _ in range(self.columns * self.rows)]
        self.bg_board = [string.ascii_uppercase[i] for i in range(int(self.columns * self.rows / 2))]
        self.bg_board = self.bg_board + self.bg_board
        shuffle(self.bg_board)

    def coordinates_to_index(self, col, row):
        return self.columns * row + col

    def is_game_over(self):
        return False if '*' in self.fg_board else True

    def is_unknown(self, cell):
        return True if '*' == self.fg_board[cell] else False

    def is_match(self, cell1, cell2):
        return True if self.bg_board[cell1] == self.bg_board[cell2] else False

    def reveal(self, cell):
        self.fg_board[cell] = self.bg_board[cell]
        self.display()

    def unreveal(self, cell1, cell2):
        self.fg_board[cell1] = '*'
        self.fg_board[cell2] = '*'
        self.display()

    def display(self):
        """Printout the bored with the current squares shapes and coordinates.

        :return: None
        """
        print('  ' + '   '.join([str(i) for i in range(self.columns)]))
        for y in range(self.rows):
            print(str(y) + ' ' + ' | '.join(self.fg_board[y * self.columns:y * self.columns + self.columns]) + ' ')
            if self.rows != y + 1:
                print(' ---' + '+---' * (self.columns - 1))
        print()

    def add_game_to_history(self, moves):
        self.games_history['games'] += 1
        number_of_shapes = int(self.columns * self.rows / 2)
        if number_of_shapes not in self.games_history or self.games_history[number_of_shapes] > moves:
            self.games_history[number_of_shapes] = moves

    def print_games_history(self):
        print(f"You have played {self.games_history['games']} game{'' if 1 == self.games_history['games'] else 's'}.")
        print('Best moves:')
        for shapes in self.games_history:
            if 'games' == shapes:
                continue
            print(f'\t{shapes} shapes board: {self.games_history[shapes]} moves.')



if __name__ == "__main__":
    b = Board()
    b.set_board_size(4, 4)
    b.new_board()
    # print(b.fg_board)
    print(b.bg_board)
    b.display()
