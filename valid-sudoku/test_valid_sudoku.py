import unittest

from valid_sudoku import Solution


def valid_board():
    return [["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isValidSudoku(valid_board()))

    def test_example_2(self):
        board = valid_board()
        board[0][0] = "8"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_empty_board(self):
        self.assertTrue(self.solution.isValidSudoku([["."] * 9 for _ in range(9)]))

    def test_duplicate_in_row(self):
        board = [["."] * 9 for _ in range(9)]
        board[4][0] = board[4][8] = "3"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_duplicate_in_column(self):
        board = [["."] * 9 for _ in range(9)]
        board[0][5] = board[8][5] = "7"
        self.assertFalse(self.solution.isValidSudoku(board))


if __name__ == "__main__":
    unittest.main()
