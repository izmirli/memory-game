import unittest
import sys
sys.path.append("memory_game")

from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_init_defaults(self):
        self.assertIsInstance(self.b, Board)
        self.assertEqual(self.b.rows, 4)
        self.assertEqual(self.b.columns, 4)

    def test_set_board_size(self):
        with self.subTest(columns=2, rows=3):
            self.b.set_board_size(2, 3)
            self.assertEqual(self.b.columns, 2)
            self.assertEqual(self.b.rows, 3)

        with self.subTest('exceptions'):
            cases = [
                {'columns': 1, 'rows': 2, 'exception': UserWarning},
                {'columns': 8, 'rows': 8, 'exception': UserWarning},
                {'columns': 3, 'rows': 3, 'exception': UserWarning},
            ]
            for c in cases:
                self.assertRaises(c['exception'], self.b.set_board_size, c['columns'], c['rows'])

    def test_new_board(self):
        self.b.set_board_size(2, 2)
        self.b.new_board()
        self.assertListEqual(self.b.fg_board, ['*', '*', '*', '*'])
        self.assertListEqual(sorted(self.b.bg_board), ['A', 'A', 'B', 'B'])

    def test_coordinates_to_index(self):
        self.assertEqual(self.b.coordinates_to_index(0, 0), 0)
        self.assertEqual(self.b.coordinates_to_index(1, 0), 1)
        self.assertEqual(self.b.coordinates_to_index(0, 1), 4)
        self.assertEqual(self.b.coordinates_to_index(2, 2), 10)

    def test_is_game_over(self):
        self.b.set_board_size(2, 2)
        with self.subTest('game over'):
            self.b.fg_board = ['A', 'A', 'B', 'B']
            self.assertTrue(self.b.is_game_over())

        with self.subTest('game not over'):
            for board in (['*', '*', '*', '*'], ['*', '*', 'A', 'A'], ['A', '*', 'A', '*'], ['*', 'A', '*', '*']):
                self.b.fg_board = board
                self.assertFalse(self.b.is_game_over())

    def test_is_unknown(self):
        self.b.fg_board = ['A', 'A', '*', '*']
        self.assertFalse(self.b.is_unknown(0))
        self.assertTrue(self.b.is_unknown(2))

    def test_is_match(self):
        self.b.bg_board = ['A', 'A', 'B', 'B']
        self.assertFalse(self.b.is_match(0, 2))
        self.assertTrue(self.b.is_match(0, 1))

    @unittest.skip("TO DO")
    def test_display(self):
        pass

    @unittest.skip("TO DO")
    def test_reveal(self):
        pass

    @unittest.skip("TO DO")
    def test_unreveal(self):
        pass

    def test_add_game_to_history(self):
        with self.subTest('initial'):
            self.assertEqual(self.b.games_history['games'], 0)
        with self.subTest('1st'):
            self.b.add_game_to_history(12)
            self.assertEqual(self.b.games_history['games'], 1)
            self.assertEqual(self.b.games_history['8'], 12)
        with self.subTest('better game'):
            self.b.add_game_to_history(10)
            self.assertEqual(self.b.games_history['games'], 2)
            self.assertEqual(self.b.games_history['8'], 10)
        with self.subTest('not better game'):
            self.b.add_game_to_history(13)
            self.assertEqual(self.b.games_history['games'], 3)
            self.assertEqual(self.b.games_history['8'], 10)

    @unittest.skip("TO DO")
    def test_print_games_history(self):
        pass
