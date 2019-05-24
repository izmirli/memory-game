import os
from time import sleep
from board import Board


def play_game(board):
    clear()
    board.new_board()
    board.display()
    moves = 0
    while not board.is_game_over():
        moves += 1
        next_move(board)
    print(f'Success! you solved the game after {moves} moves.')
    board.add_game_to_history(moves)


def next_move(board):
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
            print(f'Invalid coordinates given - please stay withing the game board (0-{board.columns - 1},0-{board.rows - 1}).')
            continue
        return cell_index


def board_size_by_user(board):
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
    return True if 'y' == input('Do you want to play again (N/y)? ').casefold() else False


def clear():
    print('bla')
    os.system('clear' if 'posix' == os.name else 'cls')


def main():
    b = Board()
    while True:
        board_size_by_user(b)
        play_game(b)
        if not play_again():
            break
    b.print_games_history()


if __name__ == "__main__":
    main()
